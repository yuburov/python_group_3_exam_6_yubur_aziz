from django.db import models

CHOICE = 'active'
STATUS_CHOICES = (
    (CHOICE, 'Активно'),
    ('blocked', 'Заблокировано'),
)

class G_book(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    email = models.EmailField(verbose_name='Почта')
    text = models.TextField(max_length=2000, verbose_name='Текст')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=CHOICE, verbose_name='Статус')

    def __str__(self):
        return self.name