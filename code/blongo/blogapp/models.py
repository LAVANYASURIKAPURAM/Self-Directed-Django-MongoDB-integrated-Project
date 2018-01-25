from mongoengine import *
from blongo.settings import DBNAME
from gpk import *


connect(DBNAME)

class Post(Document):
    title = StringField(max_length=120, required=True)
    content = StringField(max_length=500, required=True)
    last_update = DateTimeField(required=True)
    tags = ListField(StringField(max_length=30))

class Requirement(Document):
    requirement_true = StringField(required=True)
    creator = StringField(max_length=50)
    requirement_id = StringField(required=True)
    created_on = StringField(required=True)
    last_modified_by = StringField(required=True)
    last_modified_on = StringField(required=True)
    description = StringField(max_length=500, required=True)


##for i in range(0,3):
##    requirement = Requirement(requirement_true=data['IsRequirement'][i])
##    requirement.creator = data['Created By'][i]
##    requirement.requirement_id = data['\xef\xbb\xbf"Requirement_ID"'][i]
##    requirement.created_on = data['Created On'][i]
##    requirement.last_modified_by = data['Last Modified By'][i]
##    requirement.last_modified_on = data['Last Modified On'][i]
##    requirement.description = data['Object Text'][i]
##    print i
##    requirement.save()    



