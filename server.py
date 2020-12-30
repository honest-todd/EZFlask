from flask import Flask, render_template, current_app
import os
import csv
from config import keys

app = Flask(__name__)

def extract_data(path1, path2):
    '''
    Extract current data from the files - Iterate through files and 
    compile both into a dicionary to be rendered to to the webpage.
    
    PARAMETERS
    ----------
        path1 : str
            filepath of first dataset

        path2 : str
            filepath of second dataset
    
    RETURNS
    -------
        dictionary : dicionary of sentiment scores
    '''
    res = {}
    for item in csv.reader(open(path1)):
        res["data1"] = [item[0],item[1],item[2]] 
    for item in csv.reader(open(path2)):
        res["data2"] = [item[0],item[1],item[2]]
    return res

@app.route("/")
def home():
    '''
    This is the routing for the home page of the website(only page).
    Extract current data and render the HTML template. 
    
    RETURNS
    -------
        rendered HTML template containing home screen.
    '''
    data = extract_data( os.path.join(app.root_path, 'data', 'data1.csv'), os.path.join(app.root_path, 'data', 'data2.csv') )
    return render_template('index.html', data1 = data["data1"], data2 = data["data2"], titles = [ keys['input1'], keys['input2'] ])
    
if __name__ == '__main__':
    app.run(host='127.0.0.1', port=os.environ.get('PORT', 5500), debug=True)
