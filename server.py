from flask import Flask, render_template, current_app
import os
import csv
from config import keys

app = Flask(__name__)

def extract_data(path1, path2):
    data1 = csv.reader(open(path1))
    data2 = csv.reader(open(path2))
    for item in data1:
        pos1 = item[0]
        nue1 = item[1]
        neg1 = item[2] 
    for item in data2:
        pos2 = item[0]
        nue2 = item[1]
        neg2 = item[2]
    return [int(pos1),int(nue1),int(neg1), int(pos2),int(nue2),int(neg2)]

@app.route("/")
def home():
    data = extract_data( os.path.join(app.root_path, 'data', 'data1.csv'), os.path.join(app.root_path, 'data', 'data2.csv') )
    titles = [ keys['input1'], keys['input2'] ]
    return render_template('index.html', data = data, titles = titles)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ.get('PORT', 3000), debug=True)

