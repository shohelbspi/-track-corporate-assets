from django.shortcuts import render
from assetTrackerApp.models import Company,Asset,Employee,AssetLog
from assetTrackerApp.serializer import CompanySerializer,AssetSerializer,EmployeeSerializer,AssetLogSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.response import Response


# Create your views here.

class CompanyListCreateView(ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class CompanyRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class AssetListCreateView(ListCreateAPIView):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer

class AssetRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Asset.objects.all()
    serializer_class = AssetSerializer

class EmployeeListCreateView(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class AssetLogListCreateView(ListCreateAPIView):
    queryset = AssetLog.objects.all()
    serializer_class = AssetLogSerializer

class AssetLogRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = AssetLog.objects.all()
    serializer_class = AssetLogSerializer