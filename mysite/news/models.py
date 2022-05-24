from django.db import models

class News(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d')
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']

class Category(models.Model):
    title = models.CharField(max_length= 150, db_index=True, verbose_name = 'Наименование категории')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']

class Users(models.Model):
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    Fiction = models.BooleanField(default=False)
    Romance = models.BooleanField(default=False)
    Fantasy = models.BooleanField(default=False)
    Young_Adult = models.BooleanField(default=False)
    Contemporary = models.BooleanField(default=False)
    Nonfiction = models.BooleanField(default=False)
    Adult = models.BooleanField(default=False)
    Novels = models.BooleanField(default=False)
    Mystery = models.BooleanField(default=False)
    Historical_Fiction = models.BooleanField(default=False)
    Classics = models.BooleanField(default=False)
    Adventure = models.BooleanField(default=False)
    Historical = models.BooleanField(default=False)
    Paranormal = models.BooleanField(default=False)
    Literature = models.BooleanField(default=False)
    Science_Fiction = models.BooleanField(default=False)
    Childrens = models.BooleanField(default=False)
    Thriller = models.BooleanField(default=False)
    Magic = models.BooleanField(default=False)
    Humor = models.BooleanField(default=False)
    History = models.BooleanField(default=False)
    Crime = models.BooleanField(default=False)
    Contemporary_Romance = models.BooleanField(default=False)
    Suspense = models.BooleanField(default=False)
    Urban_Fantasy = models.BooleanField(default=False)
    Middle_Grade = models.BooleanField(default=False)
    Chick_Lit = models.BooleanField(default=False)
    Science_Fiction_Fantasy = models.BooleanField(default=False)
    Supernatural = models.BooleanField(default=False)
    Biography = models.BooleanField(default=False)
    Mystery_Thriller = models.BooleanField(default=False)
    Paranormal_Romance = models.BooleanField(default=False)
    Horror = models.BooleanField(default=False)
    Teen = models.BooleanField(default=False)
    Philosophy = models.BooleanField(default=False)
    Adult_Fiction = models.BooleanField(default=False)
    Short_Stories = models.BooleanField(default=False)
    Literary_Fiction = models.BooleanField(default=False)
    British_Literature = models.BooleanField(default=False)
    Realistic_Fiction = models.BooleanField(default=False)
    Drama = models.BooleanField(default=False)
    Religion = models.BooleanField(default=False)
    New_Adult = models.BooleanField(default=False)
    Memoir = models.BooleanField(default=False)
    War = models.BooleanField(default=False)
    twentyth_Century = models.BooleanField(default=False)
    Vampires = models.BooleanField(default=False)
    Christian = models.BooleanField(default=False)
    Graphic_Novels = models.BooleanField(default=False)
    American = models.BooleanField(default=False)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']