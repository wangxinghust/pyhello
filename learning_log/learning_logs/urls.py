"""
定义learning_logs的URL模式
"""

# from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # 主页
    path('', views.index, name='index'),
    # Page that show all topics
    path('topics/', views.topics, name='topics'),
    # Detail page for a single topic.
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    # 用于添加新主题的网页
    path('new_topic/', views.new_topic, name='new_topic'),
    # Page for adding a new entry
    path('new_entry/<int:topic_id>', views.new_entry, name='new_entry'),
    # Page for editting an entry
    path('edit_entry/<int:entry_id>', views.edit_entry, name='edit_entry'),
]
