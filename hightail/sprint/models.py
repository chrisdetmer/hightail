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
    ('archived', 'Archived')
)

STORY_STATUS = (
    ('tbp', 'To be pointed'),
    ('ready', 'Ready'),
    ('inprogress', 'In Progress'),
    ('testing', 'Testing'),
    ('complete', 'Complete'),
    ('backlog', 'Backlog'),
    ('archived', 'Archived')
)

STORY_TYPE = (
    ('product', 'Product'),
    ('feature', 'Feature'),
    ('story', 'Story')
)

class Team(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    members = models.TextField(help_text='Comma separated list of user IDs.', blank=True, null=True)
    
    def __unicode__(self):
        return '%s Team' % self.name
    
    @property
    def get_sprints(self):
        return Sprint.objects.filter(team_id=self.id)

class BoardSection(models.Model):
    pub_date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    description = models.TextField(help_text='Overview of project', blank=True, null=True)
    team_id = models.IntegerField()
    url = models.CharField(max_length=100, blank=True, null=True)
	sort_order = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return '%s board section' % self.name

class Sprint(models.Model):
    pub_date = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    author_id = models.IntegerField(help_text='ID of author')
    team_id = models.IntegerField()
	points = models.IntegerField(blank=True, null=True)
    description = models.TextField(help_text='Overview of sprint', blank=True, null=True)
    notes = models.TextField(help_text='Notes from sprint', blank=True, null=True)
    status = models.CharField(max_length=25, choices=SPRINT_STATUS)
    history = models.TextField(help_text='History of changes for this sprint', blank=True, null=True)

    def __unicode__(self):
        return 'Sprint from %s to %s' % (self.start_date, self.end_date)
    
    @property
    def author(self):
        if self.author_id:
            return User.objects.get(id=self.author_id)
        else:
            return None
    
    @property
    def get_projects(self):
        return SprintProject.objects.filter(sprint_id=self.id)
    
    @property
    def get_stories(self):
        return SprintStory.objects.filter(sprint_id=self.id)
    
class SprintProject(models.Model):
    title = models.CharField(max_length=100)
    color = models.CharField(max_length=25, choices=COLORS)
    status = models.CharField(max_length=25, choices=SPRINT_STATUS)
	start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    type = models.CharField(max_length=25, choices=STORY_TYPE)
	points = models.IntegerField(blank=True, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(help_text='Overview of project', blank=True, null=True)
    notes = models.TextField(help_text='Notes from sprint', blank=True, null=True)
    author_id = models.IntegerField(help_text='ID of author')
    sprint_id = models.IntegerField()
    history = models.TextField(help_text='History of changes for this project', blank=True, null=True)
    
    def __unicode__(self):
        return 'Sprint project "%s"' % self.title
    
    @property
    def author(self):
        if self.author_id:
            return User.objects.get(id=self.author_id)
        else:
            return None
    
    @property
    def get_sprint(self):
        if self.sprint_id:
            return Sprint.objects.get(id=self.sprint_id)
        else:
            return None
    
    @property
    def get_stories(self):
        return SprintStory.objects.filter(project_id=self.id)
    
class SprintStory(models.Model):
    pub_date = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=25, choices=STORY_TYPE)
    status = models.CharField(max_length=25, choices=STORY_STATUS)
    content = models.TextField(help_text='Task to be performed', blank=True, null=True)
    notes = models.TextField(help_text='Notes from card', blank=True, null=True)
    color = models.CharField(max_length=25, choices=COLORS)
    points = models.IntegerField(null=True, blank=True)
    author_id = models.IntegerField(help_text='ID of author')
    sprint_id = models.IntegerField()
    project_id = models.IntegerField(null=True, blank=True)
    section_id = models.IntegerField(null=True, blank=True)
    history = models.TextField(help_text='History of changes for this card', blank=True, null=True)
	sort_order = models.IntegerField(blank=True, null=True)
    
    def __unicode__(self):
        return 'Sprint card "%s"' % self.id
    
    @property
    def author(self):
        if self.author_id:
            return User.objects.get(id=self.author_id)
        else:
            return None
    
    @property
    def get_sprint(self):
        if self.sprint_id:
            return Sprint.objects.get(id=self.sprint_id)
        else:
            return None
        
    @property
    def get_project(self):
        if self.project_id:
            return SprintProject.objects.get(id=self.project_id)
        else:
            return None
