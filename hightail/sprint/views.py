from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext, Context
from django.utils import simplejson
from django.contrib.auth.decorators import login_required

from sprint.models import Sprint, SprintProject, SprintCard, Team

def dashboard(request, team_id):
    
    team = Team.objects.get(id=team_id)
    sprints = Sprint.objects.filter(team_id=team_id)
    projects = SprintProject.objects.filter(team_id=team_id)
    
    return render_to_response('dashboard.html', {
        'team': team,
        'sprints': sprints,
        'projects': projects
    })
    