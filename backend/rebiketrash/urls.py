from django.urls import path, re_path
from . import views

from django.contrib import admin
from django.urls import include, path, re_path



urlpatterns =[
    #path('mainpage/users/<user_id>/<upload_img>',views.UploadImage.as_view()),
    #path('mainpage/users/<user_id>',views.post_image),
    path('mainpage/images/<uploaded_trash_image_id>/result',views.ImageResultPage),
    path('mainpage/search-words/<search_word>/result',views.SearchResultPage),

    path('mainpage/users/<user_id>',views.UploadImage.as_view()),

    path('mypage/users/<user_id>/images',views.UploadedtrashimageListAPI.as_view()),
    path('mypage/users/<user_id>/images/<uploaded_trash_image_id>',views.UploadedtrashimageDetailListAPI.as_view()),
    path('mypage/users/<user_id>/statistics',views.statistics),
    path('mypage/users/<user_id>/statistics/period/<from_date>/<to_date>',views.statistics_by_date),
]

### 자주 쓰이는 코드 유틸화 trashUtils.py