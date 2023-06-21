# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

# Flask modules
from flask   import render_template,json,request, redirect, url_for, flash, session
from jinja2  import TemplateNotFound
from datetime import datetime
# App modules
from app import app, db
from app.models import membership
# from app.models import Profiles

# App main route + generic routing
@app.route('/')
def index():
    return render_template('index.html')


@app.route("/MSbase")
def about3():
    return render_template('MSbase.html')

@app.route("/q4.1")
def about1():
    
    return render_template('MScreate.html')

@app.route("/membershipCreate",methods=['GET','POST'])
def membershipCreate():
    msid = request.form.get('msid')
    meid = request.form.get('meid')
    startdate = request.form.get('startdate')
    enddate = request.form.get('enddate')
    indate = request.form.get('indate')
    duedate = request.form.get('duedate')
    paiddate = request.form.get('paiddate')
    amount = request.form.get('amount')

    
    error =False
    if not meid:
        flash("The Member ID is required")
        error=True
    if not startdate:
        flash("The startdate is required")
        error=True
    if not enddate:
        flash("The enddate is required")
        error=True    
    if not indate:
        flash("The indate is required")
        error=True
    if not duedate:
        flash("The duedate is required")
        error=True
    if not amount:
        flash("The amount is required")
        error=True
    if not paiddate:
        flash("The paiddate is required")
        error=True
        

    if not error:
        if not msid:
            # create a new membership in database
            new_membership = membership(MSID=msid, MEID=meid,StartDate=startdate,EndDate=enddate)
            db.session.add(new_membership)
            db.session.commit()
            db.session.refresh(new_membership)#get new pid
            session['meid']=new_membership.MEID
            flash("A new supplier with SupplierID=" +str(new_membership.ProductID) + " has been added.")
        else:
            #save a session var
            session['msid']=msid
            #modify an existing product
            new_membership = membership.query.get('msid')
            new_membership.MEID = meid
            new_membership.StartDate = startdate
            new_membership.EndDate = enddate
            new_membership.InvoiceDate = indate
            new_membership.DueDate = duedate
            new_membership.PaidDate = paiddate
            new_membership.Amount = amount
            new_membership.verified=True
            db.session.commit()
            flash("updated")
        return render_template('MScreate.html')
    else:
        return render_template('MScreate.html',error=error,MEID=meid,MSID=msid,STARTDATE=startdate,ENDDATE=enddate,INDATE=indate,DUEDATE=duedate,PAIDDATE=paiddate,AMOUNT=amount)
    

@app.route("/q4.2")
def about2():
    
    return render_template('MSsearch.html')

@app.route("/MembershipSearch",methods=['GET','POST'])
def MembershipSearch():

    msid = request.form.get('msid')
    session['msid']=msid
    meid = request.form.get('meid')
    MEMbership = membership.query.get(msid)
    error =False
    if not msid :
        flash("The Membership ID is required")
        error=True
    else:
        if not MEMbership:
            flash("The Membership ID is not existed")
            error=True
    
    if not error:
        gridData = MEMbership
        #gridData = json.dumps(gridData)
        return render_template("MSgraph1.html",gridData = gridData)
    
    else:
        return render_template('MSsearch.html',error=error)

@app.route("/MembershipDelete",methods=['GET','POST'])
def MembershipDelete():
    del_msid=session.get("msid")
    db.session.delete(membership.query.get(del_msid))
    db.session.commit()
    flash('Record deleted successfully.')
    
    return render_template("success.html")
    


@app.route("/MembershipOverdue")
def MembershipOverdue():
    current_time = datetime.now()
    flash(current_time)
    mem_overdue = membership.query.filter(membership.DueDate<=current_time).all()
    gridData = mem_overdue
    return render_template("MSgraph.html",gridData=gridData)