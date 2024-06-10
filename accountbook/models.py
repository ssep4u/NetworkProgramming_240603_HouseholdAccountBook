from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=20)
    bgcolor = models.CharField(max_length=7)  # '#ff007f'
    #accoountbook_set: 해당 category와 연결되어있는 accountbook 여러개를 가져온다

    class Meta:
        verbose_name_plural = 'categories'  #복수형 단어 설정

    def __str__(self):
        return f'{self.name}: {self.bgcolor}'


class AccountBook(models.Model):
    TYPE_CHOICES = [
        (0, '지출'),
        (1, '소비'),
    ]
    type = models.PositiveSmallIntegerField(choices=TYPE_CHOICES, default=0)  # 0:지출, 1:소비
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # models.CASCADE() 에서 () 삭제!!!    1:n관계
    time = models.DateTimeField()
    contents = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):  # get_type_display(): 0 -> 지출
        return f'{self.get_type_display()} {self.price} {self.contents} {self.category} {self.time}'
