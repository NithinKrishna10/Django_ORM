from django import views
from django.http import HttpRequest,HttpResponse
from django.shortcuts import render

from django.db import models
from faker import Faker
import random
from myapp.models import Author, Post


from django.db.models import Q
from django.db.models import Count, Sum
from django.db.models import F

from django.db import connection
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.db.models import Avg


# Create an instance of the Faker class
fake = Faker()
def api(request):
    # # Generate and insert random authors
    # for _ in range(10):
    #     name = fake.name()
    #     email = fake.email()
    #     bio = fake.text()
    #     age = random.randint(18, 65) 
    #     Author.objects.create(name=name, email=email, bio=bio,age=age)

    # Retrieve all authors
    # authors = Author.objects.all()

    # # Generate and insert random posts
    # for _ in range(20):
    #     title = fake.sentence()
    #     content = fake.paragraphs(random.randint(1, 10))
    #     author = random.choice(authors)
    #     is_published = random.choice([True, False])
    #     Post.objects.create(title=title, content=content, author=author, is_published=is_published)
    return HttpResponse('Hallo World')


def orm_querys(request):
        # Get
    authors1 = Author.objects.all()  # Retrieve all authors

    # Filter
    authors2 = Author.objects.filter(age__gt=30)  # Retrieve authors with age greater than 30

    # Q object
    authors3 = Author.objects.filter(Q(age__gt=30) | Q(email__contains="example"))  # Retrieve authors with age greater than 30 or email contains "example"

    # Annotate vs Aggregate
    authors4 = Author.objects.annotate(num_posts=Count('post'))  # Annotate the number of posts for each author
    total_posts = Post.objects.aggregate(total=Sum('id'))  # Aggregate the total number of posts

    # Values and ValuesList
    authors5 = Author.objects.values('name', 'email')  # Retrieve authors' names and emails as a list of dictionaries
    authors = Author.objects.values_list('name', 'email')  # Retrieve authors' names and emails as a list of tuples

    # Aggregate functions
    average_age = Author.objects.aggregate(avg_age=Avg('age'))  # Calculate the average age of all authors

    # F and F expressions
    author = Author.objects.get(id=1)
    author.age = F('age') + 1  # Increment the age of an author by 1
    author.save()

    # Managers
    authors8 = Author.objects.custom_manager_method()  # Retrieve authors using a custom manager method

    return 

def related():
    # Prefetch related and Select related
    authors6 = Author.objects.prefetch_related('post')  # Retrieve authors with their related posts
    authors7 = Author.objects.select_related('post__title')  # Retrieve authors with their related posts limited to specific fields


def my_custom_query():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM my_table")
        results = cursor.fetchall()
    return results

    # Cursor
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM my_table")
        for row in cursor.fetchall():
            # Process each row
            print(row)

# Redirect and Reverse lazy
def my_view(request):
    x = 0
    return redirect('api')  # Redirect to a specific URL

class MyView():
    success_url = reverse_lazy('my_view_name')  # Reverse a URL lazily

