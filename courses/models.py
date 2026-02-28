from django.db import models

# Create your models here.


# جدول لتصنيف الدورات
class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="اسم التصنيف")

    def __str__(self):
        return self.name

# جدول الدورات التدريبية 
class Course(models.Model):
    title = models.CharField(max_length=100, verbose_name="اسم الدورة")
    instructor = models.CharField(max_length=100, verbose_name="اسم المدرب")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="سعر الدورة")
    description = models.TextField(verbose_name="وصف الدورة")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="التصنيف")

    def __str__(self):
        return self.title

# جدول رسائل تواصل معنا
class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name="الاسم")
    email = models.EmailField(verbose_name="البريد الإلكتروني")
    subject = models.CharField(max_length=255, verbose_name="الموضوع")
    message = models.TextField(verbose_name="الرسالة")

    def __str__(self):
        return self.name