# scraper/management/commands/scrape_properties.py
from django.core.management.base import BaseCommand
from scraper.scraping import scrape_property_data

class Command(BaseCommand):
    help = 'Scrape property data'

    def handle(self, *args, **kwargs):
        scrape_property_data()
