from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)  # 책 이름
    author = models.CharField(max_length=100)  # 저자
    is_complete = models.BooleanField(default=False)  # 완결 여부
    shelf_number = models.IntegerField()  # 책장 번호 (정수 값)

    def __str__(self):
        return f"{self.title} by {self.author}"
