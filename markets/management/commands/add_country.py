import csv
from django.core.management.base import BaseCommand
from markets.models import Location 

class Command(BaseCommand):
    
    def add_arguments(self, parser):
        parser.add_argument('-p', '--path', type=str, help='path to csv file',)
        
    def handle(self, *args, **kwargs):
        path = kwargs['path']
        file = open(path)
        csvreader = csv.reader(file)
        countries = []
        for row in csvreader:
            countries.append(Location(name=row[0]))
            Location.objects.bulk_create(countries)
            

       

