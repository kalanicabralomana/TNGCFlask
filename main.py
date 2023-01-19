# import "packages" from flask
from flask import render_template  # import render_template from "public" flask libraries
# import "packages" from "this" project
from __init__ import app  # Definitions initialization
from chess import app_api2 # Blueprint import api definition
from users import user_api
from superCoolFile import chess_user_api
from bp_projects.projects import app_projects # Blueprint directory import projects definition

app.register_blueprint(app_api2) # register api routes
app.register_blueprint(user_api)
app.register_blueprint(chess_user_api)
app.register_blueprint(app_projects) # register api routes

@app.errorhandler(404)  # catch for URL not found
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

@app.route('/')  # connects default URL to index() function
def index():
    return render_template("index.html")

@app.route('/stub/')  # connects /stub/ URL to stub() function
def stub():
    return render_template("stub.html")

@app.route('/team/')  # connects /team/ URL to team() function
def team():
    return render_template("team.html")

@app.route('/chess/')  # connects /team/ URL to chess() function
def chess():
    return render_template("chess.html")

# this runs the application on the development server
if __name__ == "__main__":
    app.run(debug=True)
