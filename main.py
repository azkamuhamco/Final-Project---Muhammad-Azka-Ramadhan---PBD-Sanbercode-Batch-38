from fastapi import FastAPI
from constant import db

app = FastAPI()

def header(tabel):
    query = "DESCRIBE " + str(tabel)
    cursor_db = db.cursor()
    cursor_db.execute(query)
    result = cursor_db.fetchall()
    cursor_db.close()
    return [i[0] for i in result]

@app.get('/products')
async def products():
    query = "SELECT * FROM products"
    cursor_db = db.cursor()
    cursor_db.execute(query)
    result = cursor_db.fetchall()
    cursor_db.close()

    heder   = header("products")
    allData = []
    for i in range(len(result)):
        itemData    = [[heder[j]] + [result[i][j]] for j in range(len(heder))]
        dicItemData = dict((x, y) for x, y in itemData)
        allData.append(dicItemData)
    return allData
