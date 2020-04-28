from django.db import models

"""
python manage.py migrate   # 创建表结构

python manage.py makemigrations zhdb   # 让 Django 知道我们在我们的模型有一些变更
python manage.py migrate  
"""


# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    pswd = models.CharField(max_length=20)
    account = models.CharField(max_length=20)
    create_time = models.IntegerField()

    def _toJSON(self):
        return {
            'id': self.id,
            'name': self.name,
            'pswd': '',
            'account': self.account,
            'create_time': self.create_time
        }


class BaseInfo(models.Model):
    id = models.AutoField(primary_key=True)
    web_side_name = models.CharField(max_length=50)  # 网站名字
    logo_url = models.CharField(max_length=255)  # logo的url
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    record_number = models.CharField(max_length=20)

    def _toJSON(self):
        return {
            'id': self.id,
            'web_side_name': self.web_side_name,
            'logo_url': self.logo_url,
            'phone': self.phone,
            'email': self.email,
            'record_number': self.record_number
        }


class News(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, verbose_name='title')  # 标题
    content = models.TextField()  # 内容
    author = models.CharField(max_length=50)  # 作者
    create_time = models.IntegerField()  # 创建时间
    shot_time = models.IntegerField(null=True)  # 中标时间
    img_url = models.CharField(max_length=255)  # 图片路径
    n_type = models.CharField(max_length=1)  # 类型 0 新闻 1公告 2中标信息
    is_show = models.CharField(max_length=1, null=True, verbose_name='1')  # 是否显示 0不显示 1显示
    is_del = models.CharField(max_length=1, null=True)  # 是否删除， 0 正常 1删除

    def _toJSON(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'author': self.author,
            'create_time': self.create_time,
            'shot_time': self.shot_time,
            'img_url': self.img_url,
            'n_type': self.n_type,
            'is_show': self.is_show
        }


class Job(models.Model):
    id = models.AutoField(primary_key=True)
    job_name = models.CharField(max_length=20)  # 职位
    job_desc = models.CharField(max_length=255)  # 岗位描述
    professional = models.CharField(max_length=255)  # 专业要求
    education_level = models.CharField(max_length=255)  # 学历要求
    work_address = models.CharField(max_length=255)  # 工作地点
    people_number = models.CharField(max_length=255)  # 人数
    work_age = models.CharField(max_length=20)  # 工作年限
    gender = models.CharField(max_length=1)  # 性别
    people_age = models.CharField(max_length=20)  # 年龄要求
    salary = models.CharField(max_length=10)  # 薪资待遇
    work_range = models.CharField(max_length=255)  # 工作范围
    contact = models.CharField(max_length=100)  # 联系人
    phone = models.CharField(max_length=50)  # 联系电话
    email = models.CharField(max_length=50)  # 邮箱
    address = models.CharField(max_length=255)  # 公司地址
    create_time = models.IntegerField(null=True)  # 创建时间
    update_time = models.IntegerField(null=True)  # 更新时间
    valid_time = models.IntegerField(null=True, )  # 有效时间
    is_show = models.CharField(max_length=1, null=True)  # 是否显示 0不显示 1 显示

    def _toJSON(self):
        return {
            'id': self.id,
            'job_name': self.job_name,
            'job_desc': self.job_desc,
            'professional': self.professional,
            'education_level': self.education_level,
            'work_address': self.work_address,
            'people_number': self.people_number,
            'work_age': self.work_age,
            'gender': self.gender,
            'people_age': self.people_age,
            'salary': self.salary,
            'work_range': self.work_range,
            'contact': self.contact,
            'phone': self.phone,
            'email': self.email,
            'address': self.address,
            'create_time': self.create_time,
            'valid_time': self.valid_time,
            'is_show': self.is_show,
            'update_time': self.update_time
        }


class Aptitudes(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    create_time = models.IntegerField()

    def _toJSON(self):
        return {
            'id': self.id,
            'name': self.name,
            'create_time': self.create_time
        }


class Banner(models.Model):  # 轮播图
    id = models.AutoField(primary_key=True)
    urls = models.CharField(max_length=255)
    name = models.CharField(max_length=255, null=True)
    create_time = models.IntegerField()

    def _toJSON(self):
        return {
            'id': self.id,
            'urls': self.urls,
            'name': self.name,
            'create_time': self.create_time
        }


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    pro_type = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    img_urls = models.CharField(max_length=255)
    create_time = models.IntegerField()
    aptitudes_id = models.IntegerField()

    def _toJSON(self):
        return {
            'id': self.id,
            'name': self.name,
            'address': self.address,
            'company': self.company,
            'pro_type': self.pro_type,
            'img_urls': self.img_urls,
            'create_time': self.create_time,
            'aptitudes_id': self.aptitudes_id,
        }
