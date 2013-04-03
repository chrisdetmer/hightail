from django.db import models
from django.contrib.auth.models import User

COLORS = (
    ('red', 'Red'),
    ('orange', 'Orange'),
    ('yellow', 'Yellow'),
    ('white', 'White'),
    ('blue', 'Blue'),
    ('brown', 'Brown'),
    ('green', 'Green'),
    ('pink', 'Pink'),
    ('purple', 'Purple'),
    ('grey', 'Grey')
)

SPRINT_STATUS = (
    ('draft', 'Draft'),
    ('open', 'Open'),
    ('closed', 'Closed'),
    ('backlog', 'Backlog'),
    ('suspended', 'Suspended'),
    ('archived', 'Archived')
)

CARD_STATUS = (
    ('tbp', 'To be pointed'),
    ('ready', 'Ready'),
    ('started', 'Started'),
    ('suspended', 'Suspended'),
    ('complete', 'Complete'),
    ('backlog', 'Backlog')
)

class Team(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    members = models.TextField(help_text='Comma separated list of user IDs.', blank=True, null=True)
    
    def __unicode__(self):
        return '%s Team' % self.name

class Sprint(models.Model):
    pub_date = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    author_id = models.IntegerField(help_text='ID of author')
    team_id = models.IntegerField()
    description = models.TextField(help_text='Overview of sprint', blank=True, null=True)
    notes = models.TextField(help_text='Notes from sprint', blank=True, null=True)
    status = models.CharField(max_length=25, choices=SPRINT_STATUS)

    def __unicode__(self):
        return 'Sprint from %s to %s' % (self.start_date, self.end_date)
    
    @property
    def author(self):
        return User.objects.get(id=self.author_id)
    
class SprintProject(models.Model):
    title = models.CharField(max_length=100)
    color = models.CharField(max_length=25, choices=COLORS)
    status = models.CharField(max_length=25, choices=SPRINT_STATUS)
    pub_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(help_text='Overview of project', blank=True, null=True)
    notes = models.TextField(help_text='Notes from sprint', blank=True, null=True)
    author_id = models.IntegerField(help_text='ID of author')
    sprint_id = models.IntegerField()
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    
    def __unicode__(self):
        return 'Sprint project "%s"' % self.title
    
    @property
    def author(self):
        return User.objects.get(id=self.author_id)
    
class SprintCard(models.Model):
    pub_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=25, choices=CARD_STATUS)
    content = models.TextField(help_text='Task to be performed', blank=True, null=True)
    notes = models.TextField(help_text='Notes from card', blank=True, null=True)
    color = models.CharField(max_length=25, choices=COLORS)
    points = models.IntegerField(null=True, blank=True)
    author_id = models.IntegerField(help_text='ID of author')
    sprint_id = models.IntegerField()
    project_id = models.IntegerField(null=True, blank=True)
    
    def __unicode__(self):
        return 'Sprint card ""' % self.id
    
    @property
    def author(self):
        return User.objects.get(id=self.author_id)
    