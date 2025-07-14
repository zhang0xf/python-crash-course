"""定义learning_log_app的URL模式"""
from django.urls import path
from . import views

app_name = 'learning_log_app'

urlpatterns = [
    # 主页
    # views.index:指定要调用的视图函数，
    # name='index':将这个URL模式的名称指定为index，让我们能够在代码的其他地方引用它。每当需要提供到这个主页的链接时，我们都将使用这个名称，而不编写URL。
    path('',views.index,name='index'), 
    path('topics/',views.topics,name='topics'), 
    # 特定主题的详细页面(使用主题的id属性来指出请求的是哪个主题)
    path('topics/<int:topic_id>/',views.topic,name='topic'),
    path('new_topic/',views.new_topic,name='new_topic'), 
    path('new_entry/<int:topic_id>/',views.new_entry,name='new_entry'), 
    path('edit_entry/<int:entry_id>/',views.edit_entry,name='edit_entry'), 
]