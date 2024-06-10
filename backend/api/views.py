from django.shortcuts import render
from api.serializers import JobSerializer, CompanySerializer
from rest_framework import viewsets, views
from jobs.models import *
from rest_framework.response import Response

# Create your views here.

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

    # def update(self, request, pk=None):
    #     """
    #     Update an existing job instance.
    #     """
    #     try:
    #         job = Job.objects.get(pk=pk)
    #         serializer = JobSerializer(job, data=request.data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return JsonResponse(serializer.data)
    #         return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #     except Job.DoesNotExist:
    #         return JsonResponse(status=status.HTTP_404_NOT_FOUND)

class CompanyListAPIView(views.APIView):
    def get(self, request):
        queryset = Company.objects.all()
        serializer = CompanySerializer(queryset, many=True)
        return Response(serializer.data)