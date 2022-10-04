from django.urls import path

from .views import create_student
# from .views import delete_student
# from .views import detail_student
from .views import get_students
# from .views import update_student


app_name = 'student'

urlpatterns = [
    path('create/', create_student, name='create'),                   # Create
    path('', get_students, name='list'),
    # path('detail/<int:student_id>/', detail_student, name='detail'),  # Read
    # path('update/<int:student_id>/', update_student, name='update'),  # Update
    # path('delete/<int:student_id>/', delete_student, name='delete'),  # Delete
]

# https://docs.djangoproject.com:8000/              en/4?te=3