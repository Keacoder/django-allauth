from django.urls import path

from . import views

urlpatterns = [
    path("metamask/login/", views.metamask_login, name="metamask_login"),
    path("metamask/nonce/", views.metamask_nonce, name="metamask_nonce"),
    path("metamask/login_api/", views.login_api, name="login_api"),

]