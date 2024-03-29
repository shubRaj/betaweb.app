from django.urls import path, include
from django.views.decorators.cache import cache_page
from django.contrib.sitemaps.views import sitemap
from .sitemaps import sitemaps
# from webapp.views import
from . import views
app_name = "app_webapp"
sub_urlpatterns = [
    path("dp-downloader/", views.DPDownloaderView.as_view(),
         name="dp_downloader_index"),
    path("stories-downloader/", views.StoriesDownloaderView.as_view(),
         name="stories_downloader_index"),
    path("reels-downloader/", views.ReelsDownloaderView.as_view(),
         name="reels_downloader_index"),
    path("photos-videos-downloader/", views.PhotoVideoDownloaderView.as_view(),
         name="photo_video_downloader_index"),
    path("who-unfollowed-me-on-instagram/",
         views.WhoUnfollowedView.as_view(), name="who_unfollowed_index"),
]
urlpatterns = [
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
    path("robots.txt", views.robots_txt, name="robots_txt"),
    path("instatools/", include(sub_urlpatterns),),
    path("<slug:slug>/", views.PageView.as_view(), name="page"),
    path("", views.HomeView.as_view(), name="home"),
]
