from django.urls import path
from . import views
urlpatterns=[

    path('auth-check',views.teacher_auth),
    path('view-teachers',views.view_teachers),
    path('add-student',views.add_student),
    path('load-students',views.load_students),
    path('delete-student/<int:id>',views.delete_student),
    path('update-student/<int:id>',views.update_student),
    path('student/<int:id>',views.loadSingleStudent)

]