from flask import Flask, request, render_template
from modules import get_track
import os, sys
currDir = os.path.dirname(os.path.realpath(__file__))
rootDir = os.path.abspath(os.path.join(currDir, '..'))
if rootDir not in sys.path: # add parent dir to paths
    sys.path.append(rootDir)
app = Flask(__name__, template_folder='templates')
 
@app.route("/")
def index():
    return render_template('index.html', title='Home')
 
@app.route("/", methods = ['POST'])
def tracked():
    try:
        result = []
        get_track.config()
        t_id = str(request.form['tracking_number'])
        t_id = t_id.split(',')
        for tracking_id in t_id:
            result.append(get_track.get_tracking_info(tracking_id))
        if result is None:
            return "ERROR 404"
        else:
            return render_template("Tracking.html", result=result)
    except:
        return "ERROR"
 
if __name__ == '__main__':
    app.run(debug=True)