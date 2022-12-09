import requests
import json
import pickle
import csv
from flask import Flask
from flask import Flask, render_template, request

app = Flask(__name__)

res = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = res.json()
data_rates = data[0].get('rates')


headers = ["currency", "code", "bid", "ask"]
data_value=[]
for data in data_rates:
    data_value.append(list(data.values()))

with open('data.csv','w', newline='') as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerow(headers)
    for i in data_value:
        writer.writerow(i)

@app.route('/', methods=['GET','POST'])
def getrates():
    if request.method == 'GET':
        return render_template('index1.html')
    if request.method == 'POST':
        currency = request.form['code']
        number = request.form['number']

        for i in data_value:
            if i[1] == currency:
               bid = i[2]
              
        cost = int(number) * bid

        return render_template ('index2.html', cost = cost)


if __name__ == '__main__':
    app.run(debug=True)


