from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext, Context, loader
from models import Post, Requirement
import datetime
from gpk import *

def index(request):
    if request.method == 'POST':
       # save new post
       title = request.POST['title']
       content = request.POST['content']

       post = Post(title=title)
       post.last_update = datetime.datetime.now() 
       post.content = content
       post.save()

    # Get all posts from DB
    posts = Post.objects 
    return render_to_response('index.html', {'Posts': posts},
                              context_instance=RequestContext(request))


def update(request):
    id = eval("request." + request.method + "['id']")
    post = Post.objects(id=id)[0]
    
    if request.method == 'POST':
        # update field values and save to mongo
        post.title = request.POST['title']
        post.last_update = datetime.datetime.now() 
        post.content = request.POST['content']
        post.save()
        template = 'index.html'
        params = {'Posts': Post.objects} 

    elif request.method == 'GET':
        template = 'update.html'
        params = {'post':post}
   
    return render_to_response(template, params, context_instance=RequestContext(request))
                              

def delete(request):
    id = eval("request." + request.method + "['id']")

    if request.method == 'POST':
        post = Post.objects(id=id)[0]
        post.delete() 
        template = 'index.html'
        params = {'Posts': Post.objects} 
    elif request.method == 'GET':
        template = 'delete.html'
        params = { 'id': id } 

    return render_to_response(template, params, context_instance=RequestContext(request))

def user_details(request):
    for i in range(0,79):
        requirement = Requirement(requirement_true=data['IsRequirement'][i])
        requirement.creator = data['Created By'][i]
        requirement.requirement_id = data['\xef\xbb\xbf"Requirement_ID"'][i]
        requirement.created_on = data['Created On'][i]
        requirement.last_modified_by = data['Last Modified By'][i]
        requirement.last_modified_on = data['Last Modified On'][i]
        requirement.description = data['Object Text'][i]
        print i
        requirement.save()
    template = loader.get_template('Requirement.html')
    requirements = Requirement.objects
    context =Context( {'Requirements': requirements})
    return HttpResponse(template.render(context))
    
#if request.method == 'POST':

##        requirement = Requirement(requirement_true=data['IsRequirement'][1])
##        requirement.creator = data['Created By'][1]
##        requirement.requirement_id = data['\xef\xbb\xbf"Requirement_ID"'][1]
##        requirement.created_on = data['Created On'][1]
##        requirement.save()
        
    # Get all posts from DB
    #requirements = Requirement.objects
##    print 'hello'
##    print requirements
##    return render_to_response('Requirement.html', {'Requirements': Requirement.objects})



