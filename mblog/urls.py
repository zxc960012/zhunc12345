from django.contrib import admin
from django.urls import path
from mainsite.views import homepage, lotto, showpost, mychart, mychart2, mychart3, chart
 


urlpatterns = [
	path('post/<str:slug>/', showpost),
    path('admin/', admin.site.urls),
    path('lotto/', lotto),
    path('mychart/', mychart),
    path('mychart2/', mychart2),
    path('mychart3/', mychart3),
    path('mychart/<int:bid>/', mychart),
    path('mychart2/<int:bid>/', mychart2),
    path('mychart3/<int:bid>/', mychart3),
    path('chartbydate/<int:year>/<int:month>/', chart),
    path('chartbydate/<int:year>/', chart),
    path('', homepage),
]
