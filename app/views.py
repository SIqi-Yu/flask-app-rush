
from flask import render_template, request, redirect, url_for, flash, json, session
from jinja2  import TemplateNotFound
from sqlalchemy import func
from datetime import datetime

# App modules
from app import app, db
from app.models import Member, Challenge, Tmatch, membership

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')

#####-------q1------------
#q1--register
@app.route('/q1register')
def q1register():
    return render_template('q1register.html')

@app.route('/q1registersubmit', methods=['GET','POST'])
def registersubmit():
    # get user input as string (same with input name)
    meid=request.form.get('meid')
    email=request.form.get('email')
    password=request.form.get('password')
    firstname=request.form.get('firstname')
    lastname=request.form.get('lastname')
    phone=request.form.get('phone')
    age=request.form.get('age')
    gender=request.form.get('gender')
    utr=request.form.get('utr')
    
    error=False
    if not meid or not email or not password or not firstname or not lastname or not phone or not age or not gender or not utr:
        flash('The information but lastname is required')
        error=True
    else:
        age=int(age)
        if age < 0:
            flash('age need >=0')
            error=True
    
    if not error:
        member=Member.query.get(meid)  
        if member is None:
            meid=request.form.get('meid')
            meid=int(meid)
            date=datetime.now()
            membership=Member(MEID = meid, FirstName=firstname,LastName=lastname,Email=email, Age=age,UTR=utr,Gender=gender,Phone=phone, MPassword=password, DateOfCreation=date)
            db.session.add(membership)
            db.session.commit()
            db.session.refresh(membership)
            flash('A new member with MEID='+str(membership.MEID)+'has been added')
            return render_template('q1afterregister.html', membership=membership)
        else:
            meid=int(meid)
            membership=Member.query.get(meid)
            membership.FirstName = firstname
            membership.LastName = lastname
            membership.Email = email
            membership.Age = age
            membership.Gender=gender
            membership.UTR=utr
            membership.Phone=phone
            membership.Mpassword=password
            membership.verified=True
            db.session.commit()
            flash("The MEID: "+str(meid)+'has been updated.')
            return render_template('q1afterregister.html', membership=membership)
    else:
        return render_template('q1register.html',meid=meid, firstname=firstname,lastname=lastname,email=email,age=age, gender=gender, utr=utr,phone=phone,password=password )

@app.route('/q1log')
def q1login():
    return render_template('q1login.html')

@app.route('/afterlogin', methods=['GET','POST'])
def afterLogin():
    meid = request.form.get('meid')
    password = request.form.get('password')

    if not meid or not password:
        flash('The MEID and Password are required')
        return render_template('q1login.html',meid=meid,password=password)
        
    else:
        member = Member.query.get(meid)
        if member is None:
            flash('Incorrect MEID or Password')
            return render_template('q1login.html',meid=meid,password=password)
        
        elif password==member.MPassword:
            session['meid'] = meid
            session['password'] = password
            currentHour = datetime.now().hour
            greeting = "morning" if currentHour < 12 else "afternoon"
            return render_template('q1afterlogin.html', greeting=greeting)
        
        else:
            flash('Incorrect MEID or Password')
            return render_template('q1login.html',meid=meid,password=password)
@app.route('/q1modify')
def q1modify():
    return render_template('q1modify.html')

@app.route('/aftermodify', methods=['GET','POST'])
def aftermodify():
    meid=request.form.get('meid')
    email=request.form.get('email')
    password1=request.form.get('password1')
    password2=request.form.get('password2')
    firstname=request.form.get('firstname')
    lastname=request.form.get('lastname')
    phone=request.form.get('phone')
    age=request.form.get('age')
    gender=request.form.get('gender')
    
    if not meid or not email or not password1 or not password2 or not firstname or not lastname or not phone or not age or not gender:
        flash('The information but lastname is required')
        return render_template('q1modify.html')
    
    elif int(age) < 0:
        flash('age need >=0')
        return render_template('q1modify.html')
    
    else:
        meid=int(meid)
        membership=Member.query.get(meid)
        
        if membership is None:
            flash('MEID is not exist')
            return render_template('q1modify.html')
        
        elif password1==membership.MPassword:
            membership.FirstName = firstname
            membership.LastName = lastname
            membership.Email = email
            membership.Age = age
            membership.Gender=gender
            membership.Phone=phone
            membership.Mpassword=password2
            membership.verified=True
            db.session.commit()
            flash("The Information of MEID: "+str(meid)+'has been updated.')
            return render_template('q1aftermodify.html', membership=membership)
        
        else:
            flash('Incorrect MEID or Password')
            return render_template('q1modify.html', meid=meid, password1=password1, password2=password2, age=age, email=email, firstname=firstname, lastname=lastname,gender=gender)
@app.route('/q1delete')
def q1delete():
    return render_template('q1delete.html')

@app.route('/afterdelete', methods=['GET','POST'])
def afterdelete():
    meid = request.form.get('meid')
    password = request.form.get('password')

    if not meid or not password:
        flash('The MEID and Password are required')
        return render_template('q1delete.html',meid=meid,password=password)
        
    else:
        member = Member.query.get(meid)
        if member is None:
            flash('Incorrect MEID or Password')
            return render_template('q1delete.html',meid=meid,password=password)
        
        elif password==member.MPassword:
            meid = request.form.get('meid')
            meid=int(meid)
            member=Member.query.get(meid)
            db.session.delete(member)
            db.session.commit()
            flash('Your Information has been deleted')
            return render_template('base.html')
        else:
            flash('Incorrect MEID or Password')
            return render_template('q1delete.html',meid=meid,password=password)     

@app.route('/q1chart1')
def q1chart1():
    result=db.session.query(Member.Gender.label('label'), func.count(Member.MEID).label('value')).group_by('Gender')
    chartData1 = [row._asdict() for row in result]
    chartData1 = json.dumps(chartData1)
    return render_template('q1chart1.html', chartData = chartData1)

@app.route('/q1chart2')
def q1chart2():
    result=db.session.query(func.count(Member.MEID).label('value')).group_by('Age')
    chartData2 = [row._asdict() for row in result]
    chartData2 = json.dumps(chartData2)
     
    return render_template('q1chart2.html', chartData = chartData2)

@app.route('/q1chart3')
def q1chart3():
    result=db.session.query(Member.UTR.label('label'), func.count(Member.MEID).label('value')).group_by('UTR')
    chartData3 = [row._asdict() for row in result]
    chartData3 = json.dumps(chartData3)
     
    return render_template('q1chart3.html', chartData = chartData3)




# ---------q2----------
@app.route('/q2log')
def q2log():
    return render_template('challenge_log.html')
    
#after log
@app.route('/q2logsubmit', methods=['GET', 'POST'])
def q2logSubmit():
    # Get the user input values
    c_meid = request.form.get('cmeid')
    c_pass = request.form.get('cpass')   
    #check error
    if not c_meid or not c_pass:
        flash('You need to input your MEID and password')
    else:
        c_member = Member.query.get(c_meid)
        if c_pass==c_member.MPassword:
        #save the supplierID and company name into session, 
            session['c_meid'] = c_meid
            currentHour = datetime.now().hour
            greeting = "morning" if currentHour < 12 else "afternoon"
            filtered_challenges = Challenge.query.filter(Challenge.ChallengerMEID==int(session['c_meid'])).all()
            return render_template('challenge_afterlog.html', greeting=greeting, filtered_challenges = filtered_challenges)
        else:
            flash('Invalid MEID or Passwords')
            return render_template('challenge_log.html',cmeid=c_meid, cpass=c_pass)

                
# afterlog -- create a new challenge
@app.route('/q2create')
def create():
    return render_template('create_challenge.html')

## afterlog -- address challenge request
@app.route('/q2address')
def address():
    filtered_challenges = Challenge.query.filter(Challenge.ChallengerMEID==int(session['c_meid'])).all()
    return render_template('address_challenge.html', filtered_challenges = filtered_challenges)

## afterlog -- show chart
@app.route('/q2graph', methods=['GET', 'POST'])
def graph():
    c_meid = session.get('c_meid')
    result_win = db.session.query(Tmatch.WinnerMEID.label('Wins'), 
                                  func.count(Tmatch.WinnerMEID).label('value')).filter(Tmatch.WinnerMEID==c_meid)
    result_lose = db.session.query(Tmatch.LoserMEID.label('Loses'), 
                                   func.count(Tmatch.LoserMEID).label('value')).filter(Tmatch.LoserMEID==c_meid)
    
    chartData1 = [row._asdict() for row in result_win]
    chartData2 = [row._asdict() for row in result_lose]
    chartData = chartData1 + chartData2
    chartData = json.dumps(chartData)
    return render_template('challenge_graph.html', chartData=chartData)


## address request -- delete row in database
@app.route('/delete', methods=['GET', 'POST'])
def requestSubmit():
    delete_cid = request.form.get('cid')
    if not delete_cid:
        flash("if you want to delete a challenge, please input a CID")
    else:
        delete_challenge = Challenge.query.get(delete_cid)
        if not delete_challenge:
            flash('You input wrong CID')
        else:
            db.session.delete(delete_challenge)
            db.session.commit()
            filtered_challenges = Challenge.query.filter(Challenge.ChallengerMEID==int(session['c_meid'])).all()
            return render_template('address_challenge.html',filtered_challenges=filtered_challenges)

@app.route('/allcha', methods=['GET', 'POST'])
def challengerinfo():
    filtered_challenges = Challenge.query.filter(Challenge.ChallengerMEID==int(session['c_meid'])).all()
    return render_template('challenge_info.html', filtered_challenges = filtered_challenges)

#create new challenge information
@app.route('/createchallenge', methods=['GET', 'POST'])
def challengeFormSubmit():
    # get user input values
    c_id = request.form.get('cid')
    challenger_meid = request.form.get('challengerID')
    challenged_meid = request.form.get('challengedID')
    c_date = request.form.get('date')
    c_note = request.form.get('note')
    
    
    #check error
    error = False
    if not c_id:
        flash('The CID is required')
        error = True
    else:
        c_id=int(c_id)
    
    if not challenger_meid:
        flash('The challenger id is required')
        error = True
    else:
        challenger_member = Member.query.get(challenger_meid)
        if not challenger_member:
            flash('The Challenger MEID does not exist')
            error = True
        
    if not challenged_meid:
        flash('The challenged id is required')
        error = True
    else:
        challenged_member = Member.query.get(challenged_meid)
        if not challenged_member:
            flash('The Challenger MEID does not exist')
            error = True
            
    if not c_date:
        flash('The challenge date is required')
        error = True
        
    challenge = Challenge.query.get(c_id)
    if not error:
        if not challenge:
            challenge=Challenge(CID = c_id, ChallengerMEID=challenger_meid, ChallengedMEID=challenged_meid, DateOfChallenge=c_date, Notes=c_note)
            db.session.add(challenge)
            db.session.commit()
            db.session.refresh(challenge)
            flash('A new challenge with CID = '+str(challenge.CID)+' has been added')
            return render_template('challenge_info.html', challenge=challenge)
        else:
            challenge=Challenge.query.get(c_id)
            challenge.CID = c_id
            challenge.ChallenderMEID=challenger_meid
            challenge.ChallendedMEID=challenged_meid
            challenge.DateOfChallenge=c_date
            challenge.Notes=c_note
            challenge.verified=True
            db.session.commit()
            flash("You update Challenging information.The challenge with CID = "+str(c_id)+' has been modified and updated.')
            return render_template('create_info.html', challenge=challenge)
    else:
        return render_template('create_challenge.html',error=error, cid=c_id, challengerID=challenger_meid, challengedID=challenged_meid, date=c_date, note=c_note)



#---------q4---------------
@app.route("/MSbase")
def MSbase():
    return render_template('MSbase.html')

@app.route("/q4.1")
def MScreate():
    
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
            new_membership = membership(MEID=meid,StartDate=startdate,EndDate=enddate,InvoiceDate=indate
                                        ,DueDate=duedate,Amount=amount,PaidDate=paiddate)
            db.session.add(new_membership)
            db.session.commit()
            db.session.refresh(new_membership)#get new pid
            session['meid']=new_membership.MEID
            flash("A new Membership=" +str(new_membership.MSID) + " has been added.")
            return render_template('success.html')
            
        else:
            #save a session var

            #modify an existing product
            new_membership = membership.query.get(msid)
            new_membership.MEID = meid
            new_membership.StartDate = startdate
            new_membership.EndDate = enddate
            new_membership.InvoiceDate = indate
            new_membership.DueDate = duedate
            new_membership.PaidDate = paiddate
            new_membership.Amount = amount
            new_membership.verified=True
            db.session.commit()
            flash("The Membership " +str(new_membership.MSID) + " information has been modified.")
            return render_template('success.html')
    else:
        return render_template('MScreate.html',error=error,MEID=meid,MSID=msid,STARTDATE=startdate,ENDDATE=enddate,INDATE=indate,DUEDATE=duedate,PAIDDATE=paiddate,AMOUNT=amount)
    

@app.route("/q4.2")
def MSsearch():
    
    return render_template('MSsearch.html')

@app.route("/MembershipSearch",methods=['GET','POST'])
def MembershipSearch():

    msid = request.form.get('msid')
    session['msid']=msid
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
    


@app.route("/membership_chart/<year>")
def membership_chart(year):
    # Get the membership records for the given year
    memberships = membership.query.filter(db.func.extract('year', membership.PaidDate) == year).all()

    # Count the number of members who have paid and who have not paid
    members_paid = sum(1 for membership in memberships if membership.DueDate)
    members_not_paid = sum(1 for membership in memberships if not membership.DueDate)

    # Prepare the chart data
    chart_data = {
        "chart": {
            "caption": f"Membership Dues Payment for Year {year}",
            "theme": "fusion"
        },
        "data": [
            {"label": "Paid", "value": members_paid},
            {"label": "Not Paid", "value": members_not_paid}
        ]
    }
    chart_data = json.dumps(chart_data)

    return render_template("MSgraph.html", chart_data=chart_data)