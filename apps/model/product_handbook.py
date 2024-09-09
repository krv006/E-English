from django.db.models import Model, CharField, SlugField, IntegerChoices, ForeignKey, TextField, CASCADE, \
    BooleanField
from django.utils.text import slugify
from django_resized import ResizedImageField

from apps.model.base import BaseModel


class Category(Model):
    title = CharField(max_length=255)
    image = ResizedImageField(upload_to='category/')
    slug = SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            while Category.objects.filter(slug=self.slug).exists():
                slug = Category.objects.filter(slug=self.slug).first().slug
                if '-' in slug:
                    try:
                        if slug.split('-')[-1] in self.title:
                            self.slug += '-1'
                        else:
                            self.slug = '-'.join(slug.split('-')[:-1]) + '-' + str(int(slug.split('-')[-1]) + 1)
                    except:
                        self.slug = slug + '-1'
                else:
                    self.slug += '-1'
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    @property
    def product_count(self):
        return self.product_set.count()


class Comment(BaseModel):
    class Rate(IntegerChoices):
        GREAT = 1, 'Ajoyib'
        GOOD = 2, 'Yaxshi'
        SATISFACTORY = 3, 'Qoniqarli'
        BAD = 4, 'Yomon'
        TOO_BAD = 5, 'Judayomon'

    name = CharField(max_length=255)
    content = TextField()
    status = BooleanField(default=False)
    rate = CharField(max_length=25, choices=Rate.choices, default=Rate.SATISFACTORY)
    product = ForeignKey('apps.Product', CASCADE)

    def __str__(self):
        return self.name
