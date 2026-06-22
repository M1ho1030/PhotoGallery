from django.urls import path
# views モジュールをインポート
from . import views
# URLパターンを逆引きできるように名前を付ける
app_name = 'accounts'

# URLパターンを登録するための変数
urlpatterns = [
    # サインアップページのビュー呼び出し
    # [https(s)://<ホスト名>/signup/]へのアクセスに対し、
    # viewsモジュールのSignUpViweをインスタンス化する
    path('signup/',
         views.SignUpView.as_view(),
         name='signup'),

    # サインアップ完了ページのビューの呼び出し
    # [http(s)://<ホスト名>/signup_success/]へのアクセスに対して、
    # viewsモジュールのSignUpSuccessViewをインスタンス化する
    path('signup_success/',
         views.SignUpSuccessView.as_view(),
         name='signup_success')
]