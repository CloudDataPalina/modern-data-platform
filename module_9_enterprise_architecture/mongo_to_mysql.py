from pymongo import MongoClient
import mysql.connector

mongo = MongoClient(
    "<MONGODB_CONNECTION_STRING>"
)

collection = mongo["product_returns"]["details"]

mysql_conn = mysql.connector.connect(
    host="<MYSQL_HOST>",
    user="root",
    password="<MYSQL_PASSWORD>",
    database="product_returns"
)

cursor = mysql_conn.cursor()

for doc in collection.find():

    sql = """
    INSERT INTO details
    (mongo_id, product_id, variant_sku, reason, return_date)
    VALUES (%s,%s,%s,%s,%s)
    """

    values = (
        str(doc.get("_id")),
        doc.get("order_id"),
        doc.get("sku"),
        doc.get("return_reason"),
        doc.get("return_date")
    )

    cursor.execute(sql, values)

mysql_conn.commit()

print("Migration completed successfully.")

cursor.close()
mysql_conn.close()
mongo.close()
