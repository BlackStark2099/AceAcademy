from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models.person import Person
from .serializers import PeopleSerialzers    


@api_view(['GET'])
def first_api(request):
    if request.method == 'GET':
        courses = {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "publication_year": 1925,
        "genres": ["Fiction", "Classic", "Drama"],
        "available_formats": {
            "hardcover": True,
            "paperback": True,
            "ebook": True,
            "audiobook": False
        },
        "ratings": {
            "goodreads": 4.1,
            "amazon": 4.3
        },
        "price": 10.99,
        "in_stock": True
        }
    if request.method == 'POST':
        courses = {
            'name' : 'HELLO WORLD'
        }
    
    return Response(courses)


@api_view(['GET'])
def get_persons(request): 
    persons = Person.objects.all()
    serializer = PeopleSerialzers(persons,many = True)
    return Response(serializer.data)

@api_view(['POST'])
def add_person(request):
    data = request.data

    
    serializer = PeopleSerialzers(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
    return Response(serializer.errors)

    
# Create your views here.
