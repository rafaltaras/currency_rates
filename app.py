import requests
import json
import pickle
import csv
from flask import Flask
from flask import Flask, render_template

# app = Flask(__name__)

res = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = res.json()
data_rates = data[0].get('rates')


headers = ["currency", "code", "bid", "ask"]
data_value=[]
for data in data_rates:
    data_value.append(list(data.values()))

print(headers)
for i in data_value:
    print(i)

with open('data.csv','w', newline='') as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerow(headers)
    for i in data_value:
        writer.writerow(i)



# @app.route('/', methods=['GET','POST'])
# def getrates():
#     return render_template('index1.html')

# if __name__ == '__main__':
#     app.run(debug=True)




