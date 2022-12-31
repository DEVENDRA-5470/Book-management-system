from django.db import models

# Create your models here.

BOOKS=(
    ('READER','READER'),
    ('STORY','STORY'),
    ('POETRY','POETRY')
)

class Mybook(models.Model):
    # book_image=models.ImageField(upload_to='bookimages')
    writer_name=models.CharField(max_length=150)
    book_name=models.CharField(max_length=150)
    book_category=models.CharField(max_length=6,choices=BOOKS)
    book_content=models.TextField()
    published_by=models.CharField(max_length=150)
    published_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Writer :{self.writer_name} and Book:{self.book_name}'