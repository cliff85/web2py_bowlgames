# -*- coding: utf-8 -*-
import operator
def index():
	bowls=db(db.bowls).select()
	return locals()
def bowls():
	bowlgame=request.args(0)
	#Title = Bowl game
	#Subtitle = Results
	#Table two columns, headers are of each team. Contents below are who picked them. 
	bowls=db(db.bowls.id==bowlgame).select()
	picks1=db((db.picks.bowl==bowlgame)&(db.picks.pick==bowls[0].team1)).select()
	picks2=db((db.picks.bowl==bowlgame)&(db.picks.pick==bowls[0].team2)).select()
	results=[]
	return locals()
def stats():
	bowls=db(db.bowls).select()
	results=[]
	for bowl in bowls:
		team1_pick=db(db.picks.pick==bowl.team1).count()
		team2_pick=db(db.picks.pick==bowl.team2).count()
		if team1_pick > team2_pick:
			percent=100*float(float(team1_pick-team2_pick)/team1_pick)
		else:
			percent=100*float(float(team2_pick-team1_pick)/team2_pick)
		results.append((bowl.name, bowl.team1.teamname, team1_pick, bowl.team2.teamname, team2_pick, percent,bowl.id))
	print_results = sorted(results, key=operator.itemgetter(5),reverse=True)
	return locals()
def statscat():
	if request.args(0)=='most':
		most={}
		most['Rutgers']=0
		picks=db(db.picks).select()
		for pick in picks:
			try:
				most[pick.pick.teamname]+=1
			except:
				most[pick.pick.teamname]=1
		results = sorted(most.iteritems(), key=operator.itemgetter(1), reverse=True)
	if request.args(0)=='least':
		most={}
		most['Rutgers']=0
		picks=db(db.picks).select()
		for pick in picks:
			try:
				most[pick.pick.teamname]+=1
			except:
				most[pick.pick.teamname]=1
		results = sorted(most.iteritems(), key=operator.itemgetter(1))
def picks():
	user = request.args(0)
	person = db(db.persons.id==user).select()
	points = db(db.picks.person==user).select()
	wins=0
	for point in points:
		if point.pick.winner==True:
			wins+=1
	bowls = db(db.bowls).select()
	listbowls=[]
	for bowl in bowls:
		teampick=db((db.picks.bowl==bowl.id)&(db.picks.person==user)).select()
		if teampick[0].pick.winner==True:
			game_result="W"
		else:
			game_result=" "
		listbowls.append([bowl.name,teampick[0].pick.teamname, game_result, bowl.final_result, bowl.id])
	return locals()
def results():
	picks = db(db.picks).select()
	persons = db(db.persons).select()
	remaining_bowls=db(db.bowls.final_result==None).count()
	results={}
	for row in persons:
		points=0
		for pick in picks:
			if (row.id == pick.person.id) and (pick.pick.winner == True):
				points +=1
				results[row.person] = (int(points), pick.person.id, row.tie1, row.tie2, row.tie3)
	desc_results = sorted(results.iteritems(), key=operator.itemgetter(1), reverse=True)
	print desc_results
	return dict(desc_results=desc_results, remaining_bowls=remaining_bowls)
def addbets():
	user = request.args(0)
	personheader = db(db.persons.id==user).select()
	rows = db(db.bowls).select()
	listpicks = db.picks
	if request.post_vars:
			listpicks.insert(person=user,bowl=4, pick=request.post_vars.pick4)
			listpicks.insert(person=user,bowl=5, pick=request.post_vars.pick5)
			listpicks.insert(person=user,bowl=6, pick=request.post_vars.pick6)
			listpicks.insert(person=user,bowl=7, pick=request.post_vars.pick7)
			listpicks.insert(person=user,bowl=8, pick=request.post_vars.pick8)
			listpicks.insert(person=user,bowl=9, pick=request.post_vars.pick9)
			listpicks.insert(person=user,bowl=10, pick=request.post_vars.pick10)
			listpicks.insert(person=user,bowl=11, pick=request.post_vars.pick11)
			listpicks.insert(person=user,bowl=12, pick=request.post_vars.pick12)
			listpicks.insert(person=user,bowl=13, pick=request.post_vars.pick13)
			listpicks.insert(person=user,bowl=14, pick=request.post_vars.pick14)
			listpicks.insert(person=user,bowl=15, pick=request.post_vars.pick15)
			listpicks.insert(person=user,bowl=16, pick=request.post_vars.pick16)
			listpicks.insert(person=user,bowl=17, pick=request.post_vars.pick17)
			listpicks.insert(person=user,bowl=18, pick=request.post_vars.pick18)
			listpicks.insert(person=user,bowl=19, pick=request.post_vars.pick19)
			listpicks.insert(person=user,bowl=20, pick=request.post_vars.pick20)
			listpicks.insert(person=user,bowl=21, pick=request.post_vars.pick21)
			listpicks.insert(person=user,bowl=22, pick=request.post_vars.pick22)
			listpicks.insert(person=user,bowl=23, pick=request.post_vars.pick23)
			listpicks.insert(person=user,bowl=24, pick=request.post_vars.pick24)
			listpicks.insert(person=user,bowl=25, pick=request.post_vars.pick25)
			listpicks.insert(person=user,bowl=26, pick=request.post_vars.pick26)
			listpicks.insert(person=user,bowl=27, pick=request.post_vars.pick27)
			listpicks.insert(person=user,bowl=28, pick=request.post_vars.pick28)
			listpicks.insert(person=user,bowl=29, pick=request.post_vars.pick29)
			listpicks.insert(person=user,bowl=30, pick=request.post_vars.pick30)
			listpicks.insert(person=user,bowl=31, pick=request.post_vars.pick31)
			listpicks.insert(person=user,bowl=32, pick=request.post_vars.pick32)
			listpicks.insert(person=user,bowl=33, pick=request.post_vars.pick33)
			listpicks.insert(person=user,bowl=34, pick=request.post_vars.pick34)
			listpicks.insert(person=user,bowl=35, pick=request.post_vars.pick35)
			listpicks.insert(person=user,bowl=36, pick=request.post_vars.pick36)
			listpicks.insert(person=user,bowl=37, pick=request.post_vars.pick37)
			listpicks.insert(person=user,bowl=38, pick=request.post_vars.pick38)
	return dict(user=user,rows=rows, personheader=personheader)
def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())

@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_signature()
def data():
    """
    http://..../[app]/default/data/tables
    http://..../[app]/default/data/create/[table]
    http://..../[app]/default/data/read/[table]/[id]
    http://..../[app]/default/data/update/[table]/[id]
    http://..../[app]/default/data/delete/[table]/[id]
    http://..../[app]/default/data/select/[table]
    http://..../[app]/default/data/search/[table]
    but URLs must be signed, i.e. linked with
      A('table',_href=URL('data/tables',user_signature=True))
    or with the signed load operator
      LOAD('default','data.load',args='tables',ajax=True,user_signature=True)
    """
    return dict(form=crud())
