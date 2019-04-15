import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Django_Demo_1.settings')

import django
django.setup()

#FAKE SCRIPT
import random
from Django_Demo_App_1.models import AccessRecord,Topic,Webpage
from faker import Faker

fakegen=Faker()
topic=['Search','Social','Market','News','Games']

def add_topic():
    t=Topic.objects.get_or_create(top_name=random.choice(topic))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        #Get topic for entry
        top=add_topic()

        #Create fake data for entry
        fake_url=fakegen.url()
        fake_date=fakegen.date()
        fake_name=fakegen.company()

        #Create Webpage entry
        webpg=Webpage.objects.get_or_create(topic=top,urls=fake_url,name=fake_name)[0]

        #Create fake access AccessRecord
        acc_rec=AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]

if __name__ == '__main__':
    print("Populating Script")
    populate(20)
    print("Populating Complete")
