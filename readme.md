Trading Bot (Simulation)

Description:
This is a simple command-line trading bot written in Python. 
It simulates placing market and limit orders based on user input.

Features:
- Takes input from user (symbol, side, order type, quantity)
- Supports MARKET and LIMIT orders
- Simulates order execution and status
- Logs activity to a file (bot.log)

How to Run:
1. Open terminal
2. Run the file:
   python3 bot.py

Example Input:
BTCUSDT
BUY
MARKET
0.01

Output:
Displays order ID and final order status.

Note:
This project simulates trading logic and does not connect to any real trading API.
