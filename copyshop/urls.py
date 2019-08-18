"""copyshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,include
from django.views.static import serve
from copyshop.settings import MEDIA_ROOT
import xadmin
from rest_framework import routers
from users import views as uviews
from goods import views as gviews

router = routers.DefaultRouter()
router.register(r"users", uviews.UserProfileViewSet)
router.register(r"groups", uviews.GroupViewSet)
router.register(r"categorys", gviews.CategoryView)
router.register(r"banners", gviews.BannerView)

urlpatterns = [
    path("", include(router.urls)),
    path('admin/', xadmin.site.urls),
    path("media/<path:path>", serve, {"document_root": MEDIA_ROOT})

]
