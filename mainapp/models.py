from django.db import models
from django.conf import settings

NULLABLE = {'blank': True, 'null': True}


class BaseModel(models.Model):
    created_at = models.DateTimeField(verbose_name='Дата создания',
                                      auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(verbose_name='Дата модификации',
                                      auto_now=True, editable=False)
    deleted = models.BooleanField(verbose_name='Запись удалена', default=False)

    def delete(self, *args, **kwargs):
        self.deleted = True
        self.save()

    class Meta:
        # '-' говорит об обратной сортировке
        ordering = ('-created_at',)
        # важный флаг для исключения дублирования
        abstract = True


class ObjectsManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().all()


class News(BaseModel):
    objects = ObjectsManager()

    title = models.CharField(verbose_name='Заголовок', max_length=255)
    preview = models.CharField(verbose_name='Описание', max_length=1000)
    body = models.TextField(verbose_name='Содержание')

    body_as_markdown = models.BooleanField(verbose_name='Тип MD',
                                           default=False)

    def __str__(self) -> str:
        return f'{self.pk} {self.title}'

    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'новости'
        ordering = BaseModel.Meta.ordering


class Course(BaseModel):
    objects = ObjectsManager()

    name = models.CharField(verbose_name='Название', max_length=256)
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    description_as_markdown = models.BooleanField(verbose_name='Тип MD',
                                                  default=False)
    cost = models.DecimalField(verbose_name='Стоимость',
                               max_digits=8, decimal_places=2, default=0)
    cover = models.FileField(verbose_name='Обложка',
                             max_length=25, default='no_image.svg')

    def __str__(self) -> str:
        return f'{self.pk} {self.name}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(BaseModel):
    objects = ObjectsManager()

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    num = models.PositiveIntegerField(verbose_name='Номер')
    title = models.CharField(verbose_name='Тема', max_length=256)
    description = models.TextField(verbose_name='Описание', **NULLABLE)
    description_as_markdown = models.BooleanField(
        verbose_name='Тип MD', default=False)

    def __str__(self) -> str:
        return f'{self.course.name} | {self.num} | {self.title}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'

        ordering = ('course', 'num')


class CoursesTeacher(BaseModel):

    courses = models.ManyToManyField(Course)
    name_first = models.CharField(verbose_name='Имя', max_length=128)
    name_second = models.CharField(verbose_name='Фамилия', max_length=128)
    day_birth = models.DateField(verbose_name='Дата рождения')

    def __str__(self) -> str:
        return f'{self.pk} | {self.name_second} {self.name_first}'


class CourseFeedback(BaseModel):
    RATING_FIVE = 5

    RATINGS = (
        (RATING_FIVE, '⭐⭐⭐⭐⭐'),
        (4, '⭐⭐⭐⭐'),
        (3, '⭐⭐⭐'),
        (2, '⭐⭐'),
        (1, '⭐'),
    )

    course = models.ForeignKey(
        Course, 
        verbose_name='Курс', 
        on_delete=models.CASCADE
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        verbose_name='Пользователь',
        on_delete=models.CASCADE, 
    )

    rating = models.SmallIntegerField(
        verbose_name='Рейтинг',
        choices=RATINGS,
        default=RATING_FIVE,
    )

    feedback = models.TextField(
        verbose_name='Отзыв', 
        default='Без отзыва',
    )

    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзовы'

    def __str__(self) -> str:
        return f'Отзыв на {self.course} от {self.user}'