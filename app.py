import requests
import json
import pickle
import csv
from flask import Flask
from flask import Flask, render_template

app = Flask(__name__)

res = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = res.json()
data_as_dict = data[0]
# data_rates = data_as_dict.get('rates')
data_rates_as_json = json.dumps(data_as_dict)
data_from_json = json.loads(data_rates_as_json)

data_rates = data_from_json.get('rates')


def get_rates(data): 
    for i in data:
        for j in i:
            print(j, end=';')   
        break
    print(end='\n')
   
    for item in data:
        for value in item.values():
            print(value, end=';')
        print(end='\n') 

    
rates = get_rates(data_rates)

@app.route('/', methods=['GET','POST'])
def getrates():
    return render_template('index1.html')

if __name__ == '__main__':
    app.run(debug=True)


# data_for_csv += data_for_csv.append(data)
# print(type(data_for_csv))


# with open('rates.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(rates)

# with open('countries.csv', 'w', encoding='UTF8') as f:
#     writer = csv.writer(f)

#     # write the header
#     writer.writerow(header)

#     # write the data
#     writer.writerow(data)


