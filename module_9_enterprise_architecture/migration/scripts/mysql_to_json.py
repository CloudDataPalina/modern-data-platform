import json
import mysql.connector

conn = mysql.connector.connect(
    host="<MYSQL_HOST>",
    user="root",
    password="<MYSQL_PASSWORD>",
    database="product_catalog"
)

cursor = conn.cursor(dictionary=True)
cursor.execute("SELECT * FROM Products;")
rows = cursor.fetchall()

with open("products.json", "w") as f:
    json.dump(rows, f, default=str, indent=2)

cursor.close()
conn.close()

print(f"Exported {len(rows)} products to products.json")
