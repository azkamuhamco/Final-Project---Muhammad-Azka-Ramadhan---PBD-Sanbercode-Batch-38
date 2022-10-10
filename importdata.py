from models import Products, Users
from constant import engine
from sqlalchemy.orm import Session
import csv

with open('productsRepair.csv', newline='') as fp: 
    reader   = csv.reader(fp)
    raw_data = list(reader)
    isi_data = raw_data[1:]

    products = []
    for i in range(len(isi_data)):
        if len(isi_data[i]) == 1:
            products.append(isi_data[i][0].split(";"))
        else:
            products.append((''.join(isi_data[i])).split(";"))

with open('users.csv', newline='') as fu: 
    readerP = csv.reader(fu)
    u_data  = list(readerP)
    users   = u_data[1:]

# function insertData
def insertData():
    # Insert Products
    p_data3 = [] 
    obj = [] 

    for i in range(len(products)): 
        p_data3.append(products[i]) 
        p_data3[i][0] = int(p_data3[i][0]) 

        objProduct = Products( 
            product_id = p_data3[i][0], 
            product_name = p_data3[i][1], 
            category = p_data3[i][2], 
            sub_category = p_data3[i][3]
        ) 
        
        obj.append(objProduct)

    # Insert Users
    u_data3 = [] 

    for i in range(len(users)): 
        u_data3.append(users[i]) 
        u_data3[i][0] = int(u_data3[i][0]) 

        objUsers = Users( 
            customer_id = u_data3[i][0], 
            name = u_data3[i][1], 
            city = u_data3[i][2], 
            state = u_data3[i][3],
            postal = u_data3[i][4] 
        ) 
        
        obj.append(objUsers)

    with Session(engine) as s: 
        s.add_all(obj) 
        s.commit()

if __name__ == "__main__":
    insertData()
