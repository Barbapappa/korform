from django.contrib.sites.models import Site
from django.db import models
from annoying.fields import AutoOneToOneField

class SiteConfig(models.Model):
    site = AutoOneToOneField(Site, related_name='config')
    
    term_member = models.CharField(max_length=20, blank=False, default=u"member")
    term_members = models.CharField(max_length=20, blank=False, default=u"members")
    term_contact = models.CharField(max_length=20, blank=False, default=u"contact")
    term_contacts = models.CharField(max_length=20, blank=False, default=u"contacts")
