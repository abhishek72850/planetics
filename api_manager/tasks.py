from datetime import datetime, timedelta

from celery import shared_task
from app_perf.models import UpcomingPlanModel, Subscribers

from helpers.db import get_all_users, get_all_upcoming_user_plans, update_user_plan, update_upcoming_plan_status
from helpers.utils import get_local_datetime

import pytz

import requests


@shared_task
def ready():
    requests.get(url="https://text-summary.herokuapp.com/app")
    print('Ready...')


@shared_task
def hourly_service_plan_update():
    upcoming_plan_set = get_all_upcoming_user_plans()

    for user in get_all_users():
        if user.plan_subscribed:
            if get_local_datetime(user.timezone_offset, (user.plan_subscribed_at + timedelta(days=user.plan_subscribed.plan_duration))) <= get_local_datetime(user.timezone_offset):
                Subscribers.objects.filter(id=user.id).update(
                    plan_status='EXPIRED'
                )

    for upcoming in upcoming_plan_set:
        if get_local_datetime(upcoming.user.timezone_offset, upcoming.plan_starts_from) <= get_local_datetime(upcoming.user.timezone_offset):
            if upcoming.status == 'IN_QUEUE':
                update_user_plan(upcoming.user, upcoming.plan)
                update_upcoming_plan_status(upcoming)




