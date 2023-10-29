from flask import Flask, render_template, url_for
import json



app = Flask(__name__)


def load_anime():
    with open('materials\\animelist.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data
    
@app.route('/')
def index():
    anime = load_anime()
    return render_template('index.html', serials=anime)
    
        
        
        
        
if __name__ == "__main__":
    app.run(debug=True)