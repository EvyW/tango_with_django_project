
from django.shortcuts import render
from django.http import HttpResponse

# Each view exists within the views.py file as a series of individual functions. In this instance,
# we only created one view - called index
# Note:
# Each view must return a HttpResponse object!!
# With the view created, you’re only part of the way to allowing a user to access it. For a user to see your view,
# you must map a URL (Uniform Resource Locator) to the view (in the url file!).

#def index(request):

#    return HttpResponse('Rango says hey there partner! <br/> <a href="/rango/about/">About</a>')

# new index function to show our html template: templates/rango/index.html
def index(request):
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    # When a template file is loaded with the Django templating system, a template context is created.
    # In simple terms, a template context is a Python dictionary that maps template variable names with Python variables
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake!"} # the string Crunchy, creamy, cookie, candy, cupcake! is mapped to template variable boldmessage. The string Crunchy, creamy, cookie, candy, cupcake! therefore replaces any instance of {{ boldmessage }} within the template.
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render(request, 'rango/index.html', context=context_dict) # render takes as input the user's request, the template and the context dictionary and mash it together to produce a complete HTML and return a HttpResponse



def about(request):
    context_dict = {'boldmessage': "This tutorial has been put together by Ewwy"}

    #return HttpResponse(' Rango says here is the about page <a href="/rango/">Index</a>')

    return render(request, 'rango/about.html',context=context_dict)
