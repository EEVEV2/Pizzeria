from fastapi import FastAPI, HTTPException
from database import Database
from builder import PizzaBuilder
from utils import get_distance_between_addresses

app = FastAPI()

db = Database()

@app.get("/menu")
def get_menu():
    menu_items = db.query("SELECT nazwa_dodatku, cena_na_mala, cena_na_duza FROM menu").fetchall()
    return [{"ingredient": item[0], "small_price": item[1], "large_price": item[2]} for item in menu_items]

@app.put("/order")
def place_order(size: str, ingredients: list, delivery_address: str = None):
    builder = PizzaBuilder().set_size(size)
    for ingredient in ingredients:
        builder.add_ingredient(ingredient)
    pizza = builder.build()

    ingredient_prices = db.query(
        "SELECT cena_na_mala, cena_na_duza FROM menu WHERE nazwa_dodatku IN ({})".format(
            ",".join(["?"] * len(ingredients))
        ),
        tuple(ingredients),
    ).fetchall()

    if not ingredient_prices:
        raise HTTPException(status_code=400, detail="Invalid ingredients")

    cost = sum(price[1] if size.lower() == "duza" else price[0] for price in ingredient_prices)
    delivery_cost, delivery_time = 0, 0

    if delivery_address:
        distance = get_distance_between_addresses("Pizzeria Address", delivery_address)
        if distance is None or distance > 8.5:
            raise HTTPException(status_code=400, detail="Delivery unavailable")
        delivery_cost = 5 if distance < 2 else 10 if distance < 5 else 15
        delivery_time = 5 + int(2 * distance)

    total_time = 15 + delivery_time
    total_cost = cost + delivery_cost

    db.query(
        """
        INSERT INTO zamowienia (imie, nazwisko, telefon_kontaktowy, adres_zamawiajacego,
        dystans_dostawy, kwota_do_zaplaty, status_zamowienia, opis_zamowienia)
        VALUES ('Test', 'User', '123456789', ?, ?, ?, 'NOWE', ?)
        """,
        (delivery_address, distance or 0.0, total_cost, str(pizza)),
    )

    return {"cost": total_cost, "estimated_time": total_time, "status": "NOWE"}

@app.get("/orders")
def get_orders():
    orders = db.query("SELECT id_zamowienia, imie, nazwisko, kwota_do_zaplaty, status_zamowienia FROM zamowienia").fetchall()
    return [{"id": order[0], "customer": f"{order[1]} {order[2]}", "total_cost": order[3], "status": order[4]} for order in orders]

@app.post("/order_status")
def update_order_status(order_id: int, status: str):
    valid_statuses = ["NOWE", "W_REALIZACJI", "ZREALIZOWANE", "ANULOWANE"]
    if status not in valid_statuses:
        raise HTTPException(status_code=400, detail="Invalid status")
    db.query("UPDATE zamowienia SET status_zamowienia = ? WHERE id_zamowienia = ?", (status, order_id))
    return {"message": "Order status updated"}
