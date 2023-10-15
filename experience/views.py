from datetime import datetime, timedelta
from django.shortcuts import render
from .models import Job

DAYS_YEAR = 365


# Create your views here.


def experience(request):
    jobs = Job.objects.all()
    experiences = []
    for job in jobs:
        experiences.append(ExperienceView(job))

    return render(request, "experience/experience.html", {'experiences': experiences})


class ExperienceView:

    def __init__(self, job):
        self.job = job
        duration = job.to_date - job.from_date if job.to_date else datetime(datetime.utcnow().year,
                                                                            datetime.utcnow().month,
                                                                            datetime.utcnow().day).date() - job.from_date
        self.years = int(duration.days / DAYS_YEAR)
        self.months = int(((duration.days / DAYS_YEAR) * 12) -
                          (int(duration.days / DAYS_YEAR) * 12))
