# Importing flask functions to be used 
from flask import Flask, render_template, redirect, url_for, flash, request, session

#This will allow us to load the csv data in the myLines down below
import read_csv as pr

# We are importing functions to checkrequirements
# And to get programs using certain criteria
from get_results import *


# Instantiating the flask Object
# Nothing to see here
app = Flask(__name__)

# Config to hold global variables
config= {}

@app.route('/')
def start():
    """Render the main page where the user profile is captured"""
    return render_template("index.html")


@app.route('/create_student', methods=['GET', 'POST'])
def create_student():
    """
    Using the form input from the POST request, 
    create the user profile and get the userIndexList;
    Make them both accessible globally
    """
    
    # Creating the user profile from the form input
    user_profile_01={"full_name":request.form['student_name'], 
                    "year":request.form['year'], 
                    "bschool":request.form['bschool'], 
                    "primary_major":request.form['major'], 
                    "secondary_major":request.form['minor'], 
                    "gpa":float(request.form['gpa'])}
    
    
    # Adding the userprofile to the global config so we have access to it elsewhere
    config['userprofile'] = user_profile_01
    
    #Using the userprofile to build a userList
    config['userList'] = check_requirements(myLines, user_profile_01)
    
    #get_price(myLines, userList, 1)
    return redirect(url_for('get_goal'))


@app.route('/get_goal', methods=['GET', 'POST'])
def get_goal():
    """Render the goal selection page"""
    return render_template("goal.html",
                          user = config['userprofile'])


@app.route('/process_goal', methods=['GET', 'POST'])
def process_goal():
    """
    Use the selected goal to direct 
    the user to the proper page
    """
    goal = int(request.form['goal'])
    
    if (goal==1):
        return redirect(url_for('check_price')) 
    elif (goal==2):
        return redirect(url_for('check_location')) 
    elif (goal==3):
        return redirect(url_for('check_duration')) 
    elif (goal==4):
        return redirect(url_for('check_topic')) 
    elif (goal==5):
        return redirect(url_for('check_language')) 
    else:
        return "Error"

    
@app.route('/check_price', methods=['GET', 'POST'])
def check_price():
    """Choose price point"""
    return render_template("check_price.html",
                          user = config['userprofile'])    


@app.route('/process_price', methods=['GET', 'POST'])
def process_price():
    """Get result based on price point and render them"""
    selection = int(request.form['decision'])
    programs = get_by_price(myLines, 
                       config['userList'], 
                       selection)
    return render_template("results.html",
                           user = config['userprofile'],
                            programs = programs)
    
    
@app.route('/check_location', methods=['GET', 'POST'])
def check_location():
    """Choose preferred location"""
    return render_template("check_location.html",
                          user = config['userprofile'])    
    
    
@app.route('/process_location', methods=['GET', 'POST'])
def process_location():
    """
    Get results based on chosen duration 
    and render them 
    """
    selection = int(request.form['decision'])
    programs = get_by_location(myLines, 
                       config['userList'], 
                       selection)
    return render_template("results.html",
                           user = config['userprofile'],
                            programs = programs)
    
    
@app.route('/check_duration', methods=['GET', 'POST'])
def check_duration():
    """Choose preferred duration"""
    return render_template("check_duration.html",
                          user = config['userprofile'])  


@app.route('/process_duration', methods=['GET', 'POST'])
def process_duration():
    """
    Get results based on duration and redner them
    """
    selection = int(request.form['decision'])
    programs = get_by_duration(myLines, 
                       config['userList'], 
                       selection)
    return render_template("results.html",
                           user = config['userprofile'],
                           programs = programs)
    
    
@app.route('/check_topic', methods=['GET', 'POST'])
def check_topic():
    """Choose preferred topic """
    return render_template("check_topic.html",
                          user = config['userprofile'],)    


@app.route('/process_topic', methods=['GET', 'POST'])
def process_topic():
    """
    Get results based on topic and render them
    """
    selection = int(request.form['decision'])
    programs = get_by_topic(myLines, 
                       config['userList'], 
                       selection)
    return render_template("results.html",
                            user = config['userprofile'],
                            programs = programs)
    
    
@app.route('/check_language', methods=['GET', 'POST'])
def check_language():
    "Choose preferred language"
    return render_template("check_language.html",
                          user = config['userprofile'])   


@app.route('/process_language', methods=['GET', 'POST'])
def process_language():
    """
    Get results based on language and render them
    """
    selection = int(request.form['decision'])
    programs = get_by_language(myLines, 
                       config['userList'], 
                       selection)
    return render_template("results.html",
                            user = config['userprofile'],
                            programs = programs)


if __name__ == "__main__":   
    myLines = pr.read_project_csv("Project_Master_SheetV3.csv")
    app.run(debug=True)