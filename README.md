# Python Crash Course
[随书资源地址](https://www.ituring.com.cn/book/1861)

### 创建虚拟环境
* 参考: [Blender Development Environment](https://github.com/zhang0xf/collection/blob/main/readme/blender_development.md)

### 项目《外星人入侵》
* 切换到Python虚拟环境:`workon python_crash_course_env`
* 安装**pygame**:`pip install pygame`
* 查看虚拟环境包信息:`pip list`

### 项目《数据可视化》
* 切换到Python虚拟环境:`workon python_crash_course_env`
* 安装**matplotlib**:`pip install matplotlib`
* 安装**Pygal**:`pip install pygal`
* 安装**Requests**:`pip install requests`

### 项目《学习笔记》（Web应用程序）
* 切换到Python虚拟环境:`workon python_crash_course_env`
* 安装**Django**:`pip install Django`
* 使用`Django`命令创建`learning_log`项目:`django-admin startproject learning_log ./project/web_application`
* 创建数据库(manage.py是一个简单的程序，它接受命令并将其交给Django的相关部分去运行):
  * `cd project/web_application/`
  * `python manage.py migrate`
* 核实`Django`是否正确地创建了项目:
  * `python manage.py runserver`
  * 浏览器访问:`http://127.0.0.1:8000/`
* 创建应用程序:`python manage.py startapp learning_log_app`
* 自定义模型:`[modify]learning_log_app/models.py`
* 生成迁移文件(`0001_initial.py`,这个文件将在数据库中为自定义模型创建一个表):`python manage.py makemigrations learning_log_app`
* 应用迁移，让`Django`修改数据库:`python manage.py migrate`
* 创建超级用户(密码:123456):
  * `python manage.py createsuperuser --username zhangfei`
  * 浏览器访问(管理员账号):`http://127.0.0.1:8000/admin`
* 向管理网站注册模型:`[modify]learning_log_app/admin.py`
* **【只阅读到19.1章结束】**