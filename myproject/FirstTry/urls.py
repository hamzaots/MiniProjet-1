
from django.urls import path
from . import views

urlpatterns =[
    path("Home", views.home, name ="home"),
    path("index", views.Index , name = "index"),
    path("viewhtml",views.form , name='form'),
    path('vulnerability_data', views.vulnerability_data, name='vulnerability_data'),
    path("Dashboard" , views.dashboard, name = 'dashboard'),
    path("results",views.your_view, name ="results"),
    path("NewTask",views.AddTask,name = "NewTask"),
    path('login/', views.user_login, name='login'),
    path('', views.user_signup, name='signup'),
    path("ResultsTCP", views.ShowResultsTCP , name = 'TCPResults'),
    path("VulnResults", views.ShowResults , name = 'VulnResults'),
    path("NewSchedule", views.AddSchedule , name ='NewSchedule'),
    path("NewTarget", views.AddTarget , name ='NewTarget'),
    path("NewScanConf", views.AddScan , name ='NewScanConf'),
    path("NewCustomScanConf", views.AddCustomScan , name ='NewCustomScanConf'),
    path('create-task/', views.create_task, name='create_task'),
    path('Scans', views.ShowScans, name='Scans'),
    path('editScan', views.edit_rowScan, name='edit_Scanrow'),
    path('deleteScan?<int:row_id>', views.delete_row, name='delete_row'),

    # Other URL patterns
    #path('download_report?<string:format>', views.download_report, name='download_report'),
]
