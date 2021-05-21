import os
from flask import Flask, render_template, url_for, json, send_file,send_from_directory

app = Flask(__name__,
            static_url_path='', 
            static_folder='web/static',
            template_folder='web/templates')
app.config['JSON_SORT_KEYS'] = False



@app.route('/')
def home():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT,  "web/static/resultados",  "PA.json")
    DatosPIE = json.load(open(json_url))
    return render_template('index.html', DatosPIE=DatosPIE)
@app.route('/tables.html')
def tablas():
    return render_template('tables.html')



    
@app.route('/charts.html', methods=["GET"])
def charts():
    return render_template('charts.html')

if __name__ == '__main__':
    app.run(port=3000,debug=True)



