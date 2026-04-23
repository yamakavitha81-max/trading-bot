import logging
import random
import time

logging.basicConfig(
    filename="bot.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def get_input():
    symbol = input("Symbol (e.g., BTCUSDT): ").upper()
    side = input("Side (BUY/SELL): ").upper()
    order_type = input("Type (MARKET/LIMIT): ").upper()
    qty = float(input("Quantity: "))

    price = None
    if order_type == "LIMIT":
        price = float(input("Price: "))

    return symbol, side, order_type, qty, price


def create_order(symbol, side, order_type, qty, price=None):
    order = {
        "id": random.randint(1000, 9999),
        "symbol": symbol,
        "side": side,
        "type": order_type,
        "qty": qty,
        "price": price,
        "status": "NEW"
    }

    if order_type == "MARKET":
        order["status"] = "FILLED"

    logging.info(f"Created order: {order}")
    return order


def check_status(order):
    time.sleep(1)

    if order["type"] == "LIMIT":
        order["status"] = random.choice(["FILLED", "CANCELED"])

    logging.info(f"Checked status: {order}")
    return order


def main():
    symbol, side, order_type, qty, price = get_input()

    order = create_order(symbol, side, order_type, qty, price)

    print("Order ID:", order["id"])

    order = check_status(order)

    print("Final Status:", order["status"])


if __name__ == "__main__":
    main()
