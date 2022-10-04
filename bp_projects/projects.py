from flask import Blueprint, render_template

app_projects = Blueprint('projects', __name__,
                url_prefix='/projects',
                template_folder='templates/bp_projects/')

# connects /Gene path to render Gene.html
@app_projects.route('/Nathan/')
def Nathan():
    return render_template("Nathan.html")

# connects /Gene path to render Gene.html
@app_projects.route('/Gene/')
def Gene():
    return render_template("Gene.html")

@app_projects.route('/Toby/')
def Toby():
    return render_template("Toby.html")

@app_projects.route('/Caleb/')
def Caleb():
    return render_template("Caleb.html")