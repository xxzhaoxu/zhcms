"""zhCMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from . import view


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', view.hello),
    url(r'^login$', view.login),
    url(r'^find_all_user$', view.find_all_user),
    url(r'^find_base_info$', view.find_base_info),
    url(r'^update_base_info$', view.update_base_info),
    url(r'^save_update_news$', view.save_update_news),
    url(r'^find_news$', view.find_news),
    url(r'^find_news_by_id$', view.find_news_by_id),
    url(r'^delete_news$', view.delete_news),
    url(r'^add_job$', view.add_job),
    url(r'^update_job$', view.update_job),
    url(r'^find_jobs$', view.find_jobs),
    url(r'^find_jobs_id$', view.find_jobs_by_id),
    url(r'^save_aptitudes$', view.save_aptitudes),
    url(r'^find_aptitudes$', view.find_aptitudes),
    url(r'^save_update_banner$', view.save_update_banner),
    url(r'^find_banner$', view.find_banner),
    url(r'^find_all_banner$', view.find_all_banner),
    url(r'^del_banner$', view.del_banner),
    url(r'^save_product$', view.save_product),
    url(r'^del_product$', view.del_product),
    url(r'^find_product$', view.find_product),
    url(r'^find_product_by_id$', view.find_product_by_id),
    url(r'^upload_file_access$', view.upload_file_access),
]
