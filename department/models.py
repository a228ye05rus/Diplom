from django.db import models


class Cathedra(models.Model):
    """Кафедра"""
    name = models.CharField('Название кафедры', max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Кафедра'
        verbose_name_plural = 'Кафедры'


class Employee(models.Model):
    """Сотрудник кафедры"""
    cathedra = models.ManyToManyField(Cathedra)
    post = models.CharField('Должность', max_length=30)
    picture = models.ImageField('Фотография', upload_to='employee/', blank=True)
    name = models.CharField('Имя', max_length=30)
    surname = models.CharField('Фамилия', max_length=30)
    midname = models.CharField('Отчество', max_length=30)
    degree = models.CharField('Научная степень', max_length=100)
    disciplines = models.TextField('Преподаваемые дисцпилины')
    honorary_titles = models.CharField('Почетные звания', max_length=700)
    education = models.CharField('Образование', max_length=450)
    scientific_specialty = models.CharField('Научная специальность', max_length=500)
    Professional_development = models.CharField('Данные о повышении квалификации', max_length=700)
    scientific_interests = models.CharField('Область научных интересов', max_length=900)
    work_experience = models.PositiveSmallIntegerField('Трудовой стаж')
    projects = models.TextField('Проекты')
    publications = models.TextField('Публикации')
    contacts = models.CharField('Контакты', max_length=20)
    mail = models.EmailField('Почта')

    def __str__(self):
        return f'{self.name} - {self.surname} - {self.midname}'

    class Meta:
        verbose_name = 'Сотрудник кафедры'
        verbose_name_plural = 'Сотрудники кафедры'


class Section(models.Model):
    """Разделы бокового меню"""
    name = models.CharField('Имя раздела', max_length=250)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Раздел бокового меню'
        verbose_name_plural = 'Разделы бокового меню'


class Article(models.Model):
    """Статьи внутри разделов"""
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    date = models.DateTimeField('Дата')
    name = models.CharField('Название статьи', max_length=50)
    full_text = models.TextField('Содержимое статьи')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class TagNews(models.Model):
    """Тэги для новостей"""
    name = models.CharField('Название тега', max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Теги'


class News(models.Model):
    """Новости сайта"""
    tag = models.ManyToManyField(TagNews)
    date = models.DateTimeField('Дата')
    headline = models.CharField('Заголовок', max_length=250)
    full_text = models.TextField('Содержимое новости')

    def __str__(self):
        return self.headline

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

