from django.shortcuts import render, get_object_or_404
from .models import State, District, City
from django.http import JsonResponse
from django.conf import settings
import requests  # Import settings


def home1(request):
    # Fetch all states to display in the dropdown
    states = State.objects.all()
    return render(request, 'gymlocator/index1.html', {'states': states})


def get_districts(request):
    state_id = request.GET.get('state_id')
    if state_id:
        try:
            state = get_object_or_404(State, id=state_id)  # Use get_object_or_404 for better error handling
            districts = list(state.districts.values('id', 'name'))  # Fetch all districts for the state
            return JsonResponse({'districts': districts})
        except Exception as e:
            return JsonResponse({'error': 'An error occurred while fetching districts.'}, status=500)
    else:
        return JsonResponse({'error': 'State ID is required.'}, status=400)


def get_cities(request):
    district_id = request.GET.get('district_id')
    if district_id:
        try:
            district = get_object_or_404(District, id=district_id)  # Use get_object_or_404 for better error handling
            cities = list(district.cities.values('id', 'name'))  # Fetch all cities for the district
            return JsonResponse({'cities': cities})
        except Exception as e:
            return JsonResponse({'error': 'An error occurred while fetching cities.'}, status=500)
    else:
        return JsonResponse({'error': 'District ID is required.'}, status=400)





def get_gyms(request):
    city_name = request.GET.get('city_name')  # Fetch the city name from the request
    if city_name:
        try:
            # Define Google Places API request parameters
            GOOGLE_API_KEY = 'YOUR_GOOGLE_API_KEY'
            url = f"https://maps.googleapis.com/maps/api/place/textsearch/json?query=gyms+in+{city_name}&key={GOOGLE_API_KEY}"

            # Make a request to the Google Places API
            response = requests.get(url)
            if response.status_code == 200:
                places_data = response.json()
                gyms = [
                    {
                        'name': place['name'],
                        'address': place['formatted_address'],
                        'location': place['geometry']['location'],
                    }
                    for place in places_data.get('results', [])
                ]
                return JsonResponse({'gyms': gyms})
            else:
                return JsonResponse({'error': 'Failed to fetch gym data from Google Maps API.'}, status=500)
        except Exception as e:
            return JsonResponse({'error': 'An error occurred while fetching gyms.'}, status=500)
    else:
        return JsonResponse({'error': 'City name is required.'}, status=400)
