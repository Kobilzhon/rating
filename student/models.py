from django.db import models

class Students(models.Model):
    class Meta:
        verbose_name = "Студент"
        verbose_name_plural = "Студенты"

    fio = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)

    def __str__(self):
        return self.fio

class Rating(models.Model):
    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"
    students = models.ForeignKey(Students, on_delete=models.CASCADE)
    ball = models.PositiveIntegerField(default=0)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.students.fio} - {self.ball}'


class House(models.Model):
    class Meta:
        verbose_name = "Дом"
        verbose_name_plural = "Дома"
    count_room = models.PositiveIntegerField()
    address = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.address