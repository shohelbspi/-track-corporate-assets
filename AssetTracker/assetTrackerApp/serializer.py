from rest_framework import serializers
from assetTrackerApp.models import Company,Employee,Asset,AssetLog
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError


# create serializers for  Company
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

# Create serializers for employee
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

# Create serializers for Asset
class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = ['id','name','model','brand','purchased_date','condition']

# Create serializers for AssetLog
class AssetLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetLog
        fields = '__all__'

    def create(self, validated_data):
        asset_data = validated_data.pop('asset')
        asset_id = asset_data.id

        asset = get_object_or_404(Asset, id=asset_id)

        if asset.issued:
            raise ValidationError("Asset is already issued")  
        
        asset.issued = True
        asset.save()

        validated_data['asset'] = asset


        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        asset_data = validated_data.pop('asset')
        asset_id = asset_data.id

        asset = get_object_or_404(Asset, id=asset_id)

        if asset.issued:
            raise ValidationError("Asset is already issued")  
        
        asset.issued = True
        asset.save()

        instance.asset = asset

        return super().update(instance, validated_data)