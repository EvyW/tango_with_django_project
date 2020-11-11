import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','tango_with_django_project.settings')
import django
django.setup()
from rango.models import Category, Page

def populate():
    # First, we will create lists of dictionaries containing the pages
    # we want to add into each category.
    # Then we will create a dictionary of dictionaries for our categories.
    # This might seem a little bit confusing, but it allows us to iterate # through each data structure, and add the data to our models.
    python_pages = [
        {"title": "Official Python Tutorial",
         "url":"http://docs.python.org/2/tutorial/"},
        {"title":"How to Think like a Computer Scientist",
         "url":"http://www.greenteapress.com/thinkpython/"},
        {"title":"Learn Python in 10 Minutes",
         "url":"http://www.korokithakis.net/tutorials/python/"} ]
    django_pages = [
        {"title":"Official Django Tutorial",
         "url":"https://docs.djangoproject.com/en/1.9/intro/tutorial01/"},
        {"title":"Django Rocks",
         "url":"http://www.djangorocks.com/"},
        {"title":"How to Tango with Django",
         "url":"http://www.tangowithdjango.com/"} ]
    other_pages = [
        {"title":"Bottle",
         "url":"http://bottlepy.org/docs/dev/"},
        {"title":"Flask",
         "url":"http://flask.pocoo.org"} ]
    #cats = {"Python": {"pages": python_pages},
    #        "Django": {"pages": django_pages},
    #        "OtherFrameworks": {"pages": other_pages} }
    cats = {"Python": {"pages": python_pages, "views": 128, "likes": 64},
            "Django": {"pages": django_pages, "views": 64, "likes": 32},
            "OtherFrameworks": {"pages": other_pages, "views": 32, "likes": 16} }

    # If you want to add more catergories or pages,
    # add them to the dictionaries above.
    # The code below goes through the cats dictionary, then adds each category,
    # and then adds all the associated pages for that category.
    # if you are using Python 2.x then use cats.iteritems() see
    # http://docs.quantifiedcode.com/python-anti-patterns/readability/
    # for more information about how to iterate over a dictionary properly.

    for cat, cat_data in cats.items(): # al parecer cat es el 1er item del dicionario y cat_data is all the item, e.g. "Python": {"pages": python_pages, "views": 128, "likes": 64}
        c = add_cat(cat, cat_data["views"], cat_data["likes"])
        #c = add_cat(cat, cat_data)
        for p in cat_data["pages"]:
            add_page(c, p["title"], p["url"])

    # Print out the categories we have added.
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(p)))

    def add_page(cat, title, url, views=0):
        p = Page.objects.get_or_create(category=cat, title=title)[0] # We make use of the convenience get_or_create() method for creating model instances
        # As we don’t want to create duplicates of the same entry, we can use get_or_create(), If it doesn’t exist, the method creates it
        # The get_or_create() method returns a tuple of (object, created)
        p.url = url
        p.views = views
        p.save()
        return p

    #def add_cat(name):
    def add_cat(name, views=0, likes=0):
    #def add_cat(name, cat_data):
        c = Category.objects.get_or_create(name=name)[0]
        #c = Category.objects.get_or_create(name=name, views=views, likes=likes)[0]
        c.views = views
        #c.views = cat_data["views"]
        c.likes = likes
        #c.likes = cat_data["likes"]
        c.save()
        return c

    # Start execution here!
    # This is because above this point, we define functions; these are not executed unless we call them. When the
    # interpreter hits if __name__ == '__main__', we call the populate() function.
    # trick is a useful one that allows a Python module to act as either a reusable module or a standalone Python script.
    # Consider a reusable module as one that can be imported into other modules (e.g. through an import statement), while a standalone Python script would be executed from a terminal/Command Prompt by entering python module.py.
    if __name__ == '__main__':
        print("Starting Rango population script...")
        populate()