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

def data(tabel):
    query = "SELECT * FROM " + str(tabel)
    cursor_db = db.cursor()
    cursor_db.execute(query)
    result = cursor_db.fetchall()
    cursor_db.close()

    heder   = header(tabel)
    allData = []
    for i in range(len(result)):
        itemData    = [[heder[j]] + [result[i][j]] for j in range(len(heder))]
        dicItemData = dict((x, y) for x, y in itemData)
        allData.append(dicItemData)
    return allData

def searchProductById(id):
    for product in data("products"):
        print(product.get('product_id'))
        if product.get('product_id') == (int(id)):
            return product
    return {"result" :"Tidak Ditemukan"}

@app.get('/products')
async def products():
    return data("products")


