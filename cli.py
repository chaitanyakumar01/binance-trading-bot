import argparse
import sys
import os
from dotenv import load_dotenv

load_dotenv()

from bot.logging_config import setup_logger
from bot.validators import validate_inputs
from bot.client import get_binance_client
from bot.orders import place_order

def main():
    logger = setup_logger()
    
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")
    parser.add_argument('--symbol', required=True, help="Trading pair symbol (e.g., BTCUSDT)")
    parser.add_argument('--side', required=True, choices=['BUY', 'SELL', 'buy', 'sell'], help="Order side: BUY ya SELL")
    parser.add_argument('--type', required=True, choices=['MARKET', 'LIMIT', 'market', 'limit'], help="Order type: MARKET ya LIMIT")
    parser.add_argument('--quantity', required=True, type=float, help="Amount of crypto to trade")
    parser.add_argument('--price', type=float, help="Price at which to buy/sell (Required if type is LIMIT)")
    
    args = parser.parse_args()
    
    symbol = args.symbol.upper()
    side = args.side.upper()
    order_type = args.type.upper()
    quantity = args.quantity
    price = args.price

    try:
        validate_inputs(symbol, side, order_type, quantity, price)
        
        print("\n" + "="*40)
        print("📊 ORDER REQUEST SUMMARY")
        print("="*40)
        print(f"Symbol:   {symbol}")
        print(f"Side:     {side}")
        print(f"Type:     {order_type}")
        print(f"Quantity: {quantity}")
        if order_type == 'LIMIT':
            print(f"Price:    {price}")
        print("="*40 + "\n")

        logger.info("Connecting to Binance Testnet...")
        client = get_binance_client()
        
        logger.info(f"Placing {side} {order_type} order for {quantity} {symbol}...")
        result = place_order(client, symbol, side, order_type, quantity, price)
        
        print("📡 ORDER RESPONSE DETAILS")
        print("="*40)
        if result['success']:
            data = result['data']
            print(" SUCCESS: Order Placed Successfully!")
            print(f"Order ID:     {data.get('orderId')}")
            print(f"Status:       {data.get('status')}")
            
            executed_qty = data.get('executedQty', '0')
            print(f"Executed Qty: {executed_qty}")
            if float(executed_qty) > 0:
                print(f"Avg Price:    {data.get('avgPrice', 'N/A')}")
        else:
            print("FAILURE: Order Failed!")
            print(f"Error: {result['error']}")
        print("="*40 + "\n")

    except ValueError as ve:
        logger.error(f"Validation Error: {ve}")
        print(f"\n VALIDATION ERROR: {ve}\n")
        sys.exit(1)
    except Exception as e:
        logger.error(f"System Error: {e}")
        print(f"\n SYSTEM ERROR: {e}\n")
        sys.exit(1)

if __name__ == "__main__":
    main()