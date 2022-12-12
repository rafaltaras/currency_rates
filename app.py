from flask import Flask
from flask import Flask, render_template, request
from lib.data_manager import data_manager

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def getrates():
    rates = data_manager.get_rates()
    data_manager.save_to_csv(rates)
    if request.method == 'GET':
        return render_template('index1.html')
    if request.method == 'POST':
        currency = request.form['code']
        number = request.form['number']
        cost = get_cost(currency, number)
        return render_template ('index2.html', cost = cost)

def get_cost(currency, number):
    rates_from_csv = data_manager.get_from_csv()
    for rate in rates_from_csv:
        if rate[1] == currency:
            bid = rate[2]
    cost = round((number * float(bid)),2)
    return cost
    
if __name__ == '__main__':
    app.run(debug=True)


