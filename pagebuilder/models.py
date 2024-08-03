from django.db import models
from django_grapesjs.models import GrapesJsHtmlField
from django.template.loader import render_to_string
from bs4 import BeautifulSoup
import os
import polib
import subprocess
import sys

TEMPLATE_CHOICES = [
    ("frontend/index.html", "home"),
]


class Pages(models.Model):
    title = models.CharField(max_length=100)
    title_ar = models.CharField(max_length=100, verbose_name="Arabic Title")
    meta_description = models.TextField()
    meta_description_ar = models.TextField(verbose_name="Arabic Meta Description")
    favicon = models.ImageField(upload_to='favicons/', blank=True, null=True)
    meta_keywords = models.TextField(blank=True, null=True)
    meta_keywords_ar = models.TextField(blank=True, null=True, verbose_name="Arabic Meta Keywords")
    slug = models.SlugField(unique=True)
    seo_title = models.CharField(max_length=70, blank=True, null=True)
    seo_title_ar = models.CharField(max_length=70, blank=True, null=True, verbose_name="Arabic SEO Title")
    canonical_url = models.URLField(blank=True, null=True)
    canonical_url_ar = models.URLField(blank=True, null=True)
    og_title = models.CharField(max_length=100, blank=True, null=True)
    og_title_ar = models.CharField(max_length=100, blank=True, null=True, verbose_name="Arabic OG Title")
    og_description = models.TextField(blank=True, null=True)
    og_description_ar = models.TextField(blank=True, null=True, verbose_name="Arabic OG Description")
    og_image = models.ImageField(upload_to='og_images/', blank=True, null=True)
    twitter_card = models.CharField(max_length=100, blank=True, null=True)
    twitter_card_ar = models.CharField(max_length=100, blank=True, null=True, verbose_name="Arabic Twitter Card")
    
    
    
    content = GrapesJsHtmlField(
        default_html='frontend/index.html',
        apply_django_tag=True,
        redactor_config='base',
    )
    content_ar=GrapesJsHtmlField(
        default_html='frontend/index_ar.html',
        apply_django_tag=True,
        redactor_config='min',
        verbose_name="Arabic Content"
        
    )

    def save(self, *args, **kwargs):
        # Load default template content if content is empty
        if not self.content :
            self.content = render_to_string(self.template_choice)
            
        if not self.content_ar :
            self.content_ar = render_to_string(self.template_choice)

        super().save(*args, **kwargs)

    def __str__(self):
        return str(self.title)

