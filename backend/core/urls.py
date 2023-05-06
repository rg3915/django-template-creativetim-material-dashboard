from django.urls import path

from backend.core import views as v

app_name = 'core'


urlpatterns = [
    path('', v.index, name='index'),  # noqa E501
    path('dashboard/', v.dashboard, name='dashboard'),  # noqa E501
    path('table/', v.table, name='table'),  # noqa E501
    path('billing/', v.billing, name='billing'),  # noqa E501
    path('notification/', v.notification, name='notification'),  # noqa E501
    path('profile/', v.profile, name='profile'),  # noqa E501
    path('signin/', v.signin, name='signin'),  # noqa E501
    path('signup/', v.signup, name='signup'),  # noqa E501
]
