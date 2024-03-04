from django.urls import path
from assetTrackerApp import views

urlpatterns = [
    path('company-list-create/',views.CompanyListCreateView.as_view(),name='company_list_create'),
    path('company-rud/<int:pk>/',views.CompanyRetrieveUpdateDeleteView.as_view(),name='company_rud'),

    path('asset-list-create/',views.AssetListCreateView.as_view(),name='asset_list_create'),
    path('asset-rud/<int:pk>/',views.AssetRetrieveUpdateDeleteView.as_view(),name='asset_rud'),

    path('employee-list-create/',views.EmployeeListCreateView.as_view(),name='employee_list_create'),
    path('employee-rud/<int:pk>/',views.EmployeeRetrieveUpdateDeleteView.as_view(),name='employee_rud'),

    path('assetlog-list-create/',views.AssetLogListCreateView.as_view(),name='assetlog_list_create'),
    path('assetlog-rud/<int:pk>/',views.AssetLogRetrieveUpdateDeleteView.as_view(),name='assetlog_rud'),
]
