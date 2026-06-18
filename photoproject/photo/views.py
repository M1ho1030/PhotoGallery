from django.shortcuts import render
# django.views.genericからTemplateViewをインポート
from django.views.generic import TemplateView

class IndexView(TemplateView):
    '''トップページのビュー
    '''

    # index.htmlをレンダリングする
    template_name = 'index.html'
