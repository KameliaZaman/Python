import csv


def read_data():
    data = []
    with open('sales.csv', 'r') as sales_csv:
        spreadsheet = csv.DictReader(sales_csv)
        for row in spreadsheet:
            data.append(row)
    return data


def run():
    data = read_data()
    sales = []
    for row in data:
        sale = int(row['sales'])
        sales.append(sale)
    total = sum(sales)
    print('Total sales: {}'.format(total))
    high = max(sales)
    low = min(sales)
    monhi = []
    monlo = []
    for value in data:
        if int(value['sales']) == high:
            monhi.append(value['month'])
        if int(value['sales']) == low:
            monlo.append(value['month'])
    print('Max sales: {}'.format(monhi))
    print('Min sales: {}'.format(monlo))


run()
