from django.contrib import admin

# Register your models here.
from learning_log_app.models import Topic,Entry
admin.site.register(Topic) # 让Django可以通过管理网站管理我们的模型
admin.site.register(Entry) 