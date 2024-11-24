from django.db import models

# Create your models here.

class BoardPost(models.Model):
    CATEGORY_CHOICES = [
        ('sell', 'Sell'),
        ('buy', 'Buy'),
        ('trans_bank', 'Bank Transfer'),
        ('other', 'Other'),
    ]


    id = models.AutoField(primary_key=True)
    sanho = models.CharField(max_length=200)
    user_selected_date = models.DateField()  # User-selected date
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='sell')  # Category of the post
    amount = models.DecimalField(max_digits=15, decimal_places=0)
    memo = models.TextField()  # Content of the post
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set on creation
    updated_at = models.DateTimeField(auto_now=True)  # Automatically updated when saved

    def __str__(self):
        return f"{self.sanho} - {self.user_selected_date}"
    
    class Meta:
        ordering = ("-user_selected_date",)   # 開発者が作った中で選べること
