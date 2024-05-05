from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, NoteSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note


class NoteListCreate(generics.ListCreateAPIView): #list all of the notes users has created, or create a new notes, thats why using lsit create api view
        serializer_class = NoteSerializer
        permission_classes = [IsAuthenticated] # You cannot call this route unless your authenticated .

        def get_queryset(self):
                user = self.request.user #give user object, who is only authenticated. 
                return Note.objects.filter(author=user)
        
        def perform_create(self, serializer):
                if serializer.is_valid():
                    serializer.save(author=self.request.user)
                else:
                    print(serializer.errors)
                       
    

class NoteDelete(generics.DestroyAPIView):
       serializer_class = NoteSerializer
       permission_classes = [IsAuthenticated]

       def get_queryset(self):
              user = self.request.user
              return Note.objects.filter(author=user)

class CreateUserView(generics.CreateAPIView):
        queryset = User.objects.all()
        serializer_class = UserSerializer
        permission_classes = [AllowAny]

