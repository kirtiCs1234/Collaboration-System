"""CollaborationSystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from BasicArticle import viewsets
from BasicArticle import views as articleview
from rest_framework import routers
from UserRolesPermission import views as user_views
from Community import views as communityview
from Community import viewsets as communityviewsets
from Group import views as group_views
from machina.app import board
from UserRolesPermission import viewsets as user_viewsets
from django.conf import settings
from django.conf.urls.static import static


router = routers.DefaultRouter()
router.register(r'articleapi', viewsets.ArticleViewSet)
router.register(r'communityapi', communityviewsets.CommunityViewSet)

urlpatterns = [
    url(r'^$', user_views.home, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^signup/$', user_views.signup, name ='signup' ),
    url(r'^', include(router.urls)),
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^forgot_password/$', user_views.forgot_password,name='forgot_password'),
    #url(r'^reset_password/$',  user_views.reset_password,name='reset_password'),


    url(r'^auth/', include('social_django.urls', namespace='social')),

    url(r'^communities/$', communityview.display_communities, name ='display_communities'),
    url(r'^community-view/(?P<pk>\d+)/$', communityview.community_view, name='community_view'),
    url(r'^community-subscribe/$', communityview.community_subscribe, name='community_subscribe'),
    url(r'^community-unsubscribe/$', communityview.community_unsubscribe, name='community_unsubscribe'),
    url(r'^community-article-create/$', communityview.community_article_create, name='community_article_create'),

    url(r'^comments/', include('django_comments_xtd.urls')),

    url(r'^articles/$', articleview.display_articles, name='display_articles'),
    url(r'^article-view/(?P<pk>\d*)/$', articleview.view_article, name='article_view'),
    url(r'^article-edit/(?P<pk>\d*)/$', articleview.edit_article, name='article_edit'),
    url(r'^article-delete/(?P<pk>\d*)/$', articleview.delete_article, name='article_delete'),
    url(r'^article-revision/(?P<pk>\d*)/$', articleview.SimpleModelHistoryCompareView.as_view(template_name='revision_article.html'), name='article_revision' ),

    url(r'^mydashboard/$', user_views.user_dashboard, name='user_dashboard'),
    url(r'^community-group-create/$', communityview.community_group, name='community_group'),

    url(r'^group-view/(?P<pk>\d+)/$', group_views.group_view, name='group_view'),
    url(r'^group-subscribe/$', group_views.group_subscribe, name='group_subscribe'),
    url(r'^group-unsubscribe/$', group_views.group_unsubscribe, name='group_unsubscribe'),
    url(r'^group-article-create/$', group_views.group_article_create, name='group_article_create'),

    url(r'^forum/', include(board.urls)),
    url(r'^registrationapi/$', user_viewsets.RegistrationViewsets.as_view(), name='account-create'),

    url(r'^request_community_creation/$', communityview.request_community_creation, name='request_community_creation'),
    url(r'^handle_community_creation_requests/$', communityview.handle_community_creation_requests, name='handle_community_creation_requests'),

    url(r'^updateprofile/$', user_views.update_profile, name='update_profile'),

    url(r'^manage_community/(?P<pk>\d+)/$', communityview.manage_community, name='manage_community'),

    url(r'^manage_group/(?P<pk>\d+)/$', group_views.manage_group, name='manage_group'),

    url(r'^myprofile/$', user_views.view_profile, name='view_profile'),

    url(r'^userprofile/(?P<username>[\w.@+-]+)/$', user_views.display_user_profile, name='display_user_profile'),

    url(r'^update_group_info/(?P<pk>\d+)/$', group_views.update_group_info, name='update_group_info'),
    url(r'^update_community_info/(?P<pk>\d+)/$', communityview.update_community_info, name='update_community_info'),

    url(r'^create_community/$', communityview.create_community, name='create_community'),

    url(r'^community_content/(?P<pk>\d+)/$', communityview.community_content, name='community_content'),

    url(r'^password_reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        user_views.change_password,
        name='change_password'),
    url(r'^change_password/$', user_views.change_password, name='change_password'),
    url(r'^change_password_success/$', user_views.change_password_success, name='change_password_success'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
