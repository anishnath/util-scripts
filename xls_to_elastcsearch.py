import json
import sys
import requests

import xlrd
from elasticsearch import Elasticsearch


workbook = xlrd.open_workbook(sys.argv[1])
worksheet = workbook.sheet_by_name(sys.argv[2])
res = requests.get('http://0.0.0.0:9200')
print(res.content)
es = Elasticsearch([{'host': '0.0.0.0', 'port': 9200}])

data = []
keys = [v.value for v in worksheet.row(0)]
i = 1
for row_number in range(worksheet.nrows):
    if row_number == 0:
        continue
    row_data = {}
    for col_number, cell in enumerate(worksheet.row(row_number)):
        row_data[keys[col_number]] = cell.value
    es.index(index='test', doc_type='default', id=i, body=row_data)
    i=i+1
    data.append(row_data)
