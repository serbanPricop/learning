import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','datacamp.settings')


import django
django.setup()

import random
from datacamp_app.models import AccessRecord, Topic, WebPage
from faker import Faker

fake = Faker()
topics = ['Search','Social','Marketplace']

def add_topic():
    t = Topic.objects.get_or_create(top_name = random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):

    for entry in range(N):
        top = add_topic()

        fake_url = fake.domain_name()
        fake_date = fake.date()
        fake_name = fake.company()

        webpg = WebPage.objects.get_or_create(topic = top,url = fake_url,name = fake_name)[0]
        acc_rec = AccessRecord.objects.get_or_create(name = webpg,date = fake_date)[0]


if __name__ == '__main__':
    print('populating script')
    populate(20)
    print('population complete')