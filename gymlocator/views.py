from django.shortcuts import render, get_object_or_404
from .models import State, District, City
from django.http import JsonResponse
from django.conf import settings  # Import settings


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
    city_id = request.GET.get('city_id')
    if city_id:
        try:
            city = get_object_or_404(City, id=city_id)  # Use get_object_or_404 for better error handling
            gyms = city.gyms.values('name', 'phone_number', 'google_maps_link', 'image')  # Fetch gyms for the city
            gyms_with_image_url = [
                {**gym, 'image': request.build_absolute_uri(settings.MEDIA_URL + gym['image'])} if gym['image'] else {**gym, 'image': None}
                for gym in gyms
            ]
            return JsonResponse({'gyms': gyms_with_image_url})
        except Exception as e:
            return JsonResponse({'error': 'An error occurred while fetching gyms.'}, status=500)
    else:
        return JsonResponse({'error': 'City ID is required.'}, status=400)
