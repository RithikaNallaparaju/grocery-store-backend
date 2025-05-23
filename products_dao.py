from sql_connection import get_sql_connection

def get_all_products(connection):
    cursor = connection.cursor()
    query = ("select products.product_id, products.name, products.uom_id, products.price_per_unit, uom.uom_name from products inner join uom on products.uom_id=uom.uom_id")
    cursor.execute(query)
    response = []
    for (product_id, name, uom_id, price_per_unit, uom_name) in cursor:
        response.append({
            'product_id': product_id,
            'name': name,
            'uom_id': uom_id,
            'price_per_unit': price_per_unit,
            'uom_name': uom_name
        })
    return response

def insert_new_product(connection, product):
    cursor = connection.cursor()
    query = ("INSERT INTO products "
             "(name, uom_id, price_per_unit)"
             "VALUES (%s, %s, %s)")
    data = (product['product_name'], product['uom_id'], product['price_per_unit'])

    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid

def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = ("DELETE FROM products where product_id=" + str(product_id))
    cursor.execute(query)
    connection.commit()

    return cursor.lastrowid

def update_product(connection,product_id,name,price_per_unit):
    cursor = connection.cursor()
    query = ("Update grocery_store.products "
             "set name= %s , price_per_unit = %s "
            "where product_id = %s")
    cursor.execute(query, (name, price_per_unit, product_id))
    connection.commit()
    return product_id
    # # Fetch and return the updated product
    # cursor.execute("SELECT * FROM products WHERE product_id=%s", (product_id,))
    # return cursor.fetchone()

if __name__ == '__main__':
    connection = get_sql_connection()
    # comment=Ctrl 0/
    # # print(get_all_products(connection))
    # print(insert_new_product(connection, {
    #     'product_name': 'potatoes',
    #     'uom_id': '1',
    #     'price_per_unit': 10
    # }))
    print(update_product(connection,12,'LED',1250))

