from django.db import models

# Notes:
# By default, all models have an auto-increment integer field called id which is automatically assigned and acts a primary key
# For each field, you can specify the unique attribute. If set to True, the given field’s value must be unique throughout the underlying database table
# You can also specify additional attributes for each field, such as stating a default value with the syntax default='value', and whether the value for a field can be blank (or NULL) (null=True) or not (null=False).
# Django provides three types of fields for forging relationships between models in your database. These are:
# • ForeignKey, a field type that allows us to create a one-to-many relationship;
# • OneToOneField, a field type that allows us to define a strict one-to-one relationship; and
# • ManyToManyField, a field type which allows us to define a many-to-many relationship.
# Without this method implemented when you go to print the object, it will show as <Category: Category object>. This isn’t very useful when debugging or accessing the object - instead the code above will print, for example, <Category: Python>
# All apps that are installed in your Django project (check INSTALLED_APPS in settings.py) will update their database representations with this command
# After this command is issued, you should then see a db.sqlite3 file in your Django project’s root.


# Create your models here.
class Category(models.Model):
    # note how it inherits from the Model base class:
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)

    class Meta: # para que en el ADMIN interface el plural de category salga correcto (categories y no categorys)
        verbose_name_plural = 'Categories'

    def __str__(self): # _str_() generates a string representation of the class.
        # For Python 2, use __unicode__ too instead of _str_(). In Python 3.x, strings are Unicode by default - so you only need to implement the __str__()
        return self.name


class Page(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self): # For Python 2, use __unicode__ too
        return self.title

