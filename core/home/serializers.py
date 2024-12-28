from rest_framework import serializers 
# from .models.person import Person
# from models.person import Person
from .models.person import Person


class PeopleSerialzers(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'   ## this lets you add all the feilds 
        # exclude = ['age']    ## this lets you exclude the feilds
        # fields = ['name','age']  ## this lets you add selected feilds 

