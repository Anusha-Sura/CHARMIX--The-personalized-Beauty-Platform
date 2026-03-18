from db_config import get_connection

# ---------------- ADD TO CART ----------------
def add_to_cart_db(user_id, img, title, price):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO cart_items (user_id, product_img, product_title, price, qty)
        VALUES (%s, %s, %s, %s, 1)
    """, (user_id, img, title, price))

    conn.commit()
    cursor.close()
    conn.close()


# ---------------- GET CART FOR USER ----------------
def get_cart_db(user_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT * FROM cart_items
        WHERE user_id = %s
    """, (user_id,))

    items = cursor.fetchall()
    cursor.close()
    conn.close()
    return items


# ---------------- UPDATE QUANTITY ----------------
def update_qty_db(item_id, qty):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE cart_items
        SET qty = %s
        WHERE id = %s
    """, (qty, item_id))

    conn.commit()
    cursor.close()
    conn.close()


# ---------------- REMOVE ITEM ----------------
def remove_cart_item_db(item_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM cart_items WHERE id = %s", (item_id,))

    conn.commit()
    cursor.close()
    conn.close()


# ---------------- CLEAR USER CART ----------------
def clear_cart_db(user_id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM cart_items WHERE user_id = %s", (user_id,))

    conn.commit()
    cursor.close()
    conn.close()
