import os
import random

from faker import Faker

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_pro.settings')
import django

django.setup()

from first_app.models import Topic, WebPage, AccessRecord
from accounts.models import CustomUser

fakegen = Faker()

# Create topics
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic():
    t,_ = Topic.objects.get_or_create(top_name=random.choice(topics))
    t.save()
    return t

def create_fake_users(num_users):
    users = []
    for _ in range(num_users):
        username = fakegen.user_name()
        # Directly create CustomUser instances
        user = CustomUser.objects.create_user(username=username)
        users.append(user)
    return users

def get_random_user(users):
    return random.choice(users)

def populate(N=5):
    users = create_fake_users(N)  # Create fake users using CustomUser model

    for _ in range(N):
        top = add_topic()

        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.webpg()

        webpg, _ = WebPage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)

        user = get_random_user(users)
        AccessRecord.objects.create(name=webpg, date=fake_date, user=user)

if __name__ == '__main__':
    print("Populating script!")
    populate(N=20)  # Adjust N for desired number of users
    print("Populating complete")

