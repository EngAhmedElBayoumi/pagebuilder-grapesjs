from django.shortcuts import render
from .models import Pages
from django.shortcuts import redirect
from django.utils.translation import check_for_language
from django.conf import settings
from django.utils import translation
from django.template import engines
from django.utils.safestring import mark_safe

from django.shortcuts import get_object_or_404


def render_template_string(value, context=None):
    """
    Utility function to render a template string with the given context.
    Ensures that required libraries are loaded.
    """
    # Ensure the i18n library is loaded
    value = '{% load i18n %}\n' + value
    django_engine = engines['django']
    template = django_engine.from_string(value)
    return template.render(context or {})




def index(request, slug):
    page = get_object_or_404(Pages, slug=slug)
    # Prepare context for rendering template strings
    if not page:
        return render(request, 'no_pages.html')
    context = {
        'page': page,
    }
    # Render the template strings from the database
    rendered_page_content = render_template_string(page.content_ar, context)
    return render(request, 'index_ar.html', {
        'page': page,
        'page_content': mark_safe(rendered_page_content),
    })


def index_en(request, slug):
    #get object or 404
    page = get_object_or_404(Pages, slug=slug)
    # Prepare context for rendering template strings
    if not page:
        return render(request, 'no_pages.html')
    context = {
        'page': page,
    }
    # Render the template strings from the database
    rendered_page_content = render_template_string(page.content, context)
    return render(request, 'index.html', {
        'page': page,
        'page_content': mark_safe(rendered_page_content),
    })


def home(request):
    # Get the first page slug
    page = Pages.objects.first()
    if page:
        slug = page.slug
        # Redirect to the index page with the slug
        return redirect('pages:pages', slug=slug)
    else:
        # Handle the case where there are no pages in the database
        return render(request, 'no_pages.html')
    
    