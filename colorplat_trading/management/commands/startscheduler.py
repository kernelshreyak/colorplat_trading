import random

from django.conf import settings

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.management.base import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
from django_apscheduler import util

from colorplat_trading.models import ColorPrice

def update_color_prices():
    
    newprice = ColorPrice()
    newprice.priceRed = round(random.uniform(0.1,1.0),2)
    newprice.priceGreen = round(random.uniform(0.1,1.0),2)
    newprice.priceBlue = round(random.uniform(0.1,1.0),2)
    newprice.save()

    print("Color prices updated")
    pass


class Command(BaseCommand):
    help = "Runs APScheduler."

    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")

        # update the color prices every 30 seconds
        scheduler.add_job(
            update_color_prices,
            trigger=CronTrigger(second="*/20"),  # Every 20 seconds
            id="update_color_prices",  # The `id` assigned to each job MUST be unique
            max_instances=1,
            replace_existing=True,
        )
        print("Added job 'update_color_prices'.")


        try:
            print("Starting scheduler...")
            scheduler.start()
        except KeyboardInterrupt:
            print("Stopping scheduler...")
            scheduler.shutdown()
            print("Scheduler shut down successfully!")