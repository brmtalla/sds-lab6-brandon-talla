# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
# from flask import render_template
from flask import request
from flask import redirect
from model import ansDict

state_capitals = {"MD": "Annapolis", "NC": "Raleigh", "FL": "Tallahassee", "GA": "Atlanta", "TX": "Austin"}

# -- Initialization section --
app = Flask(__name__)


# -- Routes section --
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/results', methods=['GET', 'POST'])
def results():
    if request.method == 'GET':
        return redirect('/index')

    answers = {"MD": request.form['Maryland'], 
                "NC": request.form['North Carolina'], 
                "FL": request.form['Florida'], 
                "TX": request.form['Texas'], 
                "GA": request.form['Georgia']}
    
    return render_template('results.html', answers=ansDict(answers), states = state_capitals)