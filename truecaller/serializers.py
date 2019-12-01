from rest_framework import serializers
from . import models


class UserProfileSerializer(serializers.ModelSerializer):
        

        class Meta:
            model= models.UserProfile
            fields= ('id','name','contact','email','password')
            extra_kwargs= {
                'password':{
                    'write_only':True,
                    'style':{'input_type':'password'}                    
                }
                
            }
        
        def create(self,validated_data):
            user= models.UserProfile.objects.create_user(
                name= validated_data['name'],
                password= validated_data['password'],
                email=validated_data['email'],
                contact=validated_data['contact']
            )

            return user
            