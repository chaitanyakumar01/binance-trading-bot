# 🚀 Binance Futures Testnet Trading Bot

A Command-Line Interface (CLI) based trading bot built in Python to interact with the Binance Futures Testnet. This project demonstrates API integration, modular architecture, input validation, structured logging, and resilient error handling.

## ⚠️ Important Note on API Integration & Regional Constraints
During the development and testing phase, the **Binance Futures Testnet portal (`testnet.binancefuture.com`) exhibited heavy regional ISP restrictions and forced redirects** to the main Indian production site or the new demo portal (`demo.binance.com`). 

Because keys generated on the Demo portal are incompatible with the standard Testnet API endpoints, the library threw unavoidable `401: Invalid API-key` errors. 

**The Solution (Dual-Mode Architecture):**
To ensure the assignment requirements could be fully evaluated despite these regional blocks, I implemented a robust fallback mechanism in `bot/client.py`. 
1. The bot first attempts to connect to the **Real Binance API**.
2. If it catches a `401 Unauthorized` error (due to the region/demo key mismatch), it gracefully falls back to a **Simulated Binance Client**. 
This ensures the core logic—CLI argument parsing, input validation, execution flow, and logging—can be successfully demonstrated and evaluated.

## 🛠️ Features
* **Modular Codebase:** Separated logic for configuration, validation, API connection, and order execution.
* **CLI Interface:** Built using `argparse` for clean and intuitive terminal commands.
* **Strict Validation:** Pre-checks order types, sides, quantities, and prices before API execution to prevent malformed requests.
* **Comprehensive Logging:** Utilizes Python's `logging` module to output formatted logs to both the terminal and a `bot.log` file.
* **Error Handling:** Gracefully handles `BinanceAPIException`, network issues, and invalid inputs without crashing.

## ⚙️ Setup & Installation

1. **Clone the repository and navigate to the directory:**
   ```bash
   cd binance_bot_task

2. Create and activate a virtual environment:
    python -m venv venv
    source venv/bin/activate

3. Install dependencies:
    pip install python-binance python-dotenv


   
 Usage    
    For MARKET Orders:
    python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01

    For LIMIT Orders (Requires Price):
    python cli.py --symbol ETHUSDT --side SELL --type LIMIT --quantity 0.05 --price 3500.0
