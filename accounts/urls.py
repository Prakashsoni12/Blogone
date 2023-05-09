from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blogs/', views.blogs, name="blogs"),
    path('viewblog/<int:pk>', views.viewblog, name='viewblog'),
    path('add-blog', views.addblog, name='addblog'),
    path('editblog/<int:pk>', views.editBlog, name='editblog'),
    path('deleteblog/<int:pk>', views.deleteBlog, name='delete'),
    path('ragister', views.ragisterPage, name='ragister'),
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutPage, name='logout'),
    path('myblog', views.myblog, name='myblog'),
]
