from django import http
from django.shortcuts import render, HttpResponse

html_base = """
<h1>Mi Web Personal</h1>
<ul>
    <li><a href="/">Portada</a></li>
    <li><a href="/about-me/">Acerca de</a></li>
    <li><a href="/portfolio/">Portfolio</a></li>
    <li><a href="/contact/">Contacto</a></li>

</ul>    

"""

# Create your views here.

def home(request):
    return HttpResponse (html_base + """
    <h2>Portadas</h2>
    <p>Esto es la portada</p>
    
    """)

def about (request):
    return HttpResponse (html_base + """
    <h2>Acerca de</h2>
    <p>Me llamo Marcelo y soy programador</p>
    
    """)   

def portfolio (request):
    return HttpResponse (html_base + """
    <h2>Portafolio</h2>
    <p>Algunos de mis trabajos</p>
    
    """)

def contact (request):
    return HttpResponse (html_base + """
    <h2>Contacto</h2>
    <a href = "mailto:marcelo@mail.com">marcelo@mail.com</a>
    
    """)      