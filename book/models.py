from django.db import models


# Create your models here.

class AuthorInfo(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True, unique=True, verbose_name='作者id')
    name = models.CharField(max_length=32, verbose_name='标题')
    age = models.IntegerField(verbose_name='年龄', default=18)
    create_time = models.DateTimeField(auto_now_add=True, null=True, verbose_name='创建时间')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        db_table = 'author_info'
        verbose_name_plural = verbose_name = "作者表"

    def __str__(self):
        return self.name


class CategoryInfo(models.Model):
    name = models.CharField(max_length=32, verbose_name='类别名称')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        db_table = 'category_info'
        verbose_name_plural = verbose_name = "类别"

    def __str__(self):
        return self.name


class BookInfo(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True, unique=True, verbose_name='码流id')
    title = models.CharField(max_length=32, verbose_name='标题', db_index=False)
    price = models.IntegerField(verbose_name='价格')
    pub_date = models.DateField(verbose_name='日期')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')
    readcount = models.IntegerField(default=0, verbose_name='阅读量')
    commentcount = models.IntegerField(default=0, verbose_name='评论量')
    auth = models.ForeignKey(AuthorInfo, null=True, to_field='id', on_delete=models.CASCADE, verbose_name='作者')
    category = models.ForeignKey(CategoryInfo, null=True, to_field='id', on_delete=models.CASCADE, verbose_name='图书')

    class Meta:
        db_table = 'book_info'
        verbose_name_plural = verbose_name = "图书表"

    def __str__(self):
        return self.title


class PublishInfo(models.Model):
    name = models.CharField(max_length=32, verbose_name='出版社名称')
    city = models.CharField(max_length=32, verbose_name='出版社城市')

    class Meta:
        db_table = 'publish_info'
        verbose_name_plural = verbose_name = "出版社表"

        # 终端操作
        # python manage.py makemigrations book
        # python manage.py migrate
        # python manage.py shell
        # from book.models import BookInfo
        # BookInfo.objects.create(title="python3核心编程",price="68",pub_date="2015-10-10")
        # BookInfo.objects.create(title="流畅的python",price="98",pub_date="2017-07-15")
        # BookInfo.objects.create(title="笨方法学python",price="87",pub_date="2019-03-20")
