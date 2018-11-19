from django.conf.urls import url,include
from .views import HomePageView,AboutPageView

urlpatterns = [
    url(r'home', HomePageView.as_view(), name="Home_Page"),
    url(r'about/', AboutPageView.as_view(), name="About_Page"),
    
    
]