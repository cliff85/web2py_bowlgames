# -*- coding: utf-8 -*-

if request.env.web2py_runtime_gae:
    db = DAL('gae')
    session.connect(request,response,db)
else:
    db = DAL('sqlite://storage.sqlite',pool_size=1,check_reserved=['all'],adapter_args=dict(foreign_keys=False))

## by default give a view/generic.extension to all actions from localhost
## none otherwise. a pattern can be 'controller/function.extension'
response.generic_patterns = ['*'] if request.is_local else []

from gluon.tools import Auth, Crud, Service, PluginManager, prettydate
auth = Auth(db)
crud, service, plugins = Crud(db), Service(), PluginManager()

## create all tables needed by auth if not custom tables
auth.define_tables(username=False, signature=False)

## configure email
mail = auth.settings.mailer
mail.settings.server = 'logging' or 'smtp.gmail.com:587'
mail.settings.sender = 'you@gmail.com'
mail.settings.login = 'username:password'

## configure auth policy
auth.settings.registration_requires_verification = False
auth.settings.registration_requires_approval = False
auth.settings.reset_password_requires_verification = True

## if you need to use OpenID, Facebook, MySpace, Twitter, Linkedin, etc.
## register with janrain.com, write your domain:api_key in private/janrain.key
from gluon.contrib.login_methods.rpx_account import use_janrain
use_janrain(auth, filename='private/janrain.key')
db.define_table('persons', Field('person'), Field('email'), Field('tie1'), Field('tie2'), Field('tie3'))
db.define_table('teams', Field('teamname'), Field('winner', 'boolean', default=False))
db.define_table('bowls', Field('name'), Field('team1', 'reference teams'),Field('team2', 'reference teams'), Field('gametime', 'date'), Field('final_result', default='TBD'))
db.define_table('picks', Field('person', 'reference persons'),Field('bowl', 'reference bowls'), Field('pick', 'reference teams'))
db.picks.person.requires = IS_IN_DB(db, db.persons.id, '%(person)s')
db.bowls.team1.requires = IS_IN_DB(db, db.teams.id, '%(teamname)s')
db.bowls.team2.requires = IS_IN_DB(db, db.teams.id, '%(teamname)s')

