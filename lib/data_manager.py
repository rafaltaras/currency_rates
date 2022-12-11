import requests
import csv

class DataManager:
    def __init__(self, csv_file_name):
        self.csv_file_name = csv_file_name

    def get_rates(self):
        res = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
        data = res.json()
        data_rates = data[0].get('rates')
        rates=[]
        for data in data_rates:
            rates.append(list(data.values()))
        return rates

    def save_to_csv(self, rates):
        headers = ["currency", "code", "bid", "ask"]
        with open('data.csv','w', newline='') as f:
            writer = csv.writer(f, delimiter=';')
            writer.writerow(headers)
            for i in rates:
                writer.writerow(i)

    def get_from_csv(self):
        with open('data.csv', mode ='r')as file: 
            csvFile = csv.reader(file, delimiter=';') 
            rates = [] 
            for lines in csvFile: 
                    rates.append(lines)
            return rates

data_manager = DataManager(csv_file_name="data.csv")

