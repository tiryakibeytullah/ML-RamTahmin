from flask import Flask, render_template, request
import json
from ramTahmin import tahmin

app = Flask(__name__, template_folder="templates")

@app.route('/', methods=['GET', 'POST'])
def RamHomePage():
    data = ""
    if request.method == "POST":
        print(request.form)
        ramTahmin = {}
        for x in request.form:
            ramTahmin[x] = [int(request.form[x])]
        print(ramTahmin)
        data = tahmin(ramTahmin)
        data = round(data, 2)
        print(data)

        return render_template('RamHomePage.html', data=data)
    return render_template('RamHomePage.html')

#Servisim
@app.route('/api/ram', methods=['POST'])
def forapi():
    if request.method == "POST":
        data = tahmin(request.json)
        data = round(data, 2)
        return str(data)
    return "ERROR DETECTED"

app.run(debug=True)
