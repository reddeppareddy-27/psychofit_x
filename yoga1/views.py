from yoga1.models import YogaPlan
from django.shortcuts import render
from django.db import DatabaseError

def yoga_plan_view(request):
    try:
        # Fetch all YogaPlan objects
        yoga_plans = YogaPlan.objects.all()
        # Render the template with the fetched data
        return render(request, 'yoga/yoga.html', {'yoga1': yoga_plans})
    except DatabaseError as db_error:
        # Handle database-related issues
        return render(request, 'yoga/yoga.html', {'error': "Database error occurred. Please try again later."})
    except Exception as e:
        # Catch other potential errors
        return render(request, 'yoga/yoga.html', {'error': f"An unexpected error occurred: {str(e)}"})