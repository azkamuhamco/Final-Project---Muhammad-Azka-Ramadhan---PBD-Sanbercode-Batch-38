from fastapi import FastAPI
from constant import db
from re import search

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
        if product.get('product_id') == (int(id)):
            return product
    return {"result" :"Tidak Ditemukan"}

@app.get('/products')
async def show_all_products():
    return data("products")

@app.get("/product/{id}")
async def get_product_by_id(id):
    return searchProductById(id)

@app.get("/product_search")
async def search_country_by_name(name):
    for product in data("products"):
        if search(str(name), product.get('product_name')):
            return product
    return {"result" :"Tidak Ditemukan"}

def searchUserById(id):
    for user in data("users"):
        if user.get('customer_id') == (int(id)):
            return user
    return {"result" :"Tidak Ditemukan"}

@app.get('/users')
async def show_all_users():
    return data("users")

@app.get("/user/{id}")
async def get_user_by_id(id):
    return searchUserById(id)