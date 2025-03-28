from django.shortcuts import render
from meditation1.models import MeditationPlan

import logging
logger = logging.getLogger(__name__)

def meditation_view(request):
    try:
        meditation_plans = MeditationPlan.objects.all()
        return render(request, 'meditation/meditation.html', {'meditation': meditation_plans})
    except Exception as e:
        logger.error(f"Error fetching meditation plans: {str(e)}")
        return render(request, 'meditation/meditation.html', {'error': "Something went wrong! Please try again later."})