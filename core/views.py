from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Note , User
from .serializers import NoteSerializer , UserSerializer


class getnotes(APIView):

	def get(self,request,uid,format=None):
		note_list = Note.objects.filter(uid=uid)
		serializer = NoteSerializer(note_list,many=True)
		return Response(serializer.data,status=status.HTTP_201_CREATED)


class addnote(APIView):
	def post(self,request,format=None):
		serializer = NoteSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,status=status.HTTP_201_CREATED)
		return Response(serializer.errors,status=status.HTTP_404_BAD_REQUEST)


class adduser(APIView):
	def post(self,request,format=None):
		serializer = UserSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,status=status.HTTP_201_CREATED)
		return Response(serializer.errors,status=status.HTTP_404_BAD_REQUEST)


class updatenote(APIView):
	def put(self,request,pk,format=None):
		note = Note.objects.get(pk=pk)
		serializer = NoteSerializer(note,data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data,status=status.HTTP_201_CREATED)
		return Response(serializer.errors,status=status.HTTP_404_BAD_REQUEST)
