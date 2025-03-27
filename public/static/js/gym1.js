$(document).ready(function () {
    // Handle state dropdown change
    $('#state').change(function () {
        const stateId = $(this).val();
        if (stateId) {
            $.get('/get-districts/', { state_id: stateId }, function (data) {
                let districtOptions = '<option value="">--Select District--</option>';
                data.districts.forEach(d => {
                    districtOptions += `<option value="${d.id}">${d.name}</option>`;
                });
                $('#district').html(districtOptions).prop('disabled', false);
                resetCityAndGyms();
            }).fail(function () {
                alert("Error fetching districts. Please try again.");
                resetDropdowns();
            });
        } else {
            resetDropdowns();
        }
    });

    // Handle district dropdown change
    $('#district').change(function () {
        const districtId = $(this).val();
        if (districtId) {
            $.get('/get-cities/', { district_id: districtId }, function (data) {
                let cityOptions = '<option value="">--Select City--</option>';
                data.cities.forEach(c => {
                    cityOptions += `<option value="${c.id}">${c.name}</option>`;
                });
                $('#city').html(cityOptions).prop('disabled', false);
                resetGyms();
            }).fail(function () {
                alert("Error fetching cities. Please try again.");
                resetCityAndGyms();
            });
        } else {
            resetCityAndGyms();
        }
    });

    // Show the Find Gym button when a city is selected
    $('#city').change(function () {
        if ($(this).val()) {
            $('#find-gym-btn').fadeIn();
        } else {
            $('#find-gym-btn').fadeOut();
            resetGyms();
        }
    });

    // Handle Find Gym button click
    $('#find-gym-btn').click(function () {
        const cityName = $('#city option:selected').text();
        if (cityName) {
            initMap(cityName);
        }
    });
});

// Utility functions
function resetDropdowns() {
    $('#district, #city').prop('disabled', true).html('<option value="">--Select--</option>');
    resetGyms();
}

function resetCityAndGyms() {
    $('#city').prop('disabled', true).html('<option value="">--Select City--</option>');
    resetGyms();
}

function resetGyms() {
    $('#gyms-list').empty();
    $('#find-gym-btn').fadeOut();
}

// Initialize Google Map and fetch gyms
function initMap(cityName) {
    const map = new google.maps.Map(document.getElementById("map"), {
        zoom: 12,
        center: { lat: 0, lng: 0 }, // Default center
    });

    const geocoder = new google.maps.Geocoder();
    geocoder.geocode({ address: cityName }, (results, status) => {
        if (status === "OK") {
            const cityCenter = results[0].geometry.location;
            map.setCenter(cityCenter);

            const service = new google.maps.places.PlacesService(map);
            service.nearbySearch(
                {
                    location: cityCenter,
                    radius: 5000, // 5 km radius
                    keyword: "gym",
                },
                (results, status) => {
                    $('#gyms-list').empty();
                    if (status === google.maps.places.PlacesServiceStatus.OK) {
                        results.forEach(place => {
                            const marker = new google.maps.Marker({
                                position: place.geometry.location,
                                map: map,
                                title: place.name,
                            });

                            const infoWindow = new google.maps.InfoWindow({
                                content: `<h3>${place.name}</h3><p>${place.vicinity}</p>`,
                            });

                            marker.addListener('click', () => {
                                infoWindow.open(map, marker);
                            });

                            // Append gym details to the list
                            $('#gyms-list').append(`
                                <li>
                                    <h3>${place.name}</h3>
                                    <p>${place.vicinity}</p>
                                </li>
                            `);
                        });
                    } else if (status === google.maps.places.PlacesServiceStatus.ZERO_RESULTS) {
                        $('#gyms-list').append('<li>No gyms found in this city.</li>');
                    } else {
                        alert("Places API error. Status: " + status);
                    }
                }
            );
        } else {
            alert(`Geocoding failed for ${cityName}: ${status}`);
            console.error("Geocoding failed:", status);
        }
    });
}
