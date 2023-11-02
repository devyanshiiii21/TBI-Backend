from django.urls import path
from .views import NidhiEirAPIView, NidhiPrayasAPIView,TideEirAPIView, TideGrantAPIView

urlpatterns = [
    path('nidhieir/',NidhiEirAPIView.as_view(), name = 'nidhieir'),
    path('nidhiprayas/',NidhiPrayasAPIView.as_view(), name = 'nidhiprayas'),
    path('tideeir/', TideEirAPIView.as_view(), name = 'tide-eir'),
    path('tidegrant/', TideGrantAPIView.as_view(), name = 'tide-grant'),
]