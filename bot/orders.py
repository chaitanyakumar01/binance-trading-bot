import logging
from binance.exceptions import BinanceAPIException, BinanceRequestException

logger = logging.getLogger(__name__)

def place_order(client, symbol, side, order_type, quantity, price=None):
    """
    Places an order on the Binance Futures Testnet.
    """
    try:
        # Basic parameters
        params = {
            'symbol': symbol.upper(),
            'side': side.upper(),
            'type': order_type.upper(),
            'quantity': quantity
        }
        
        # LIMIT order rules
        if order_type.upper() == 'LIMIT':
            if not price:
                raise ValueError("Price is required for a LIMIT order.")
            params['price'] = price
            params['timeInForce'] = 'GTC' 
            
        logger.info(f"Sending order request: {params}")
        
        # Order placement in Futures market  
        response = client.futures_create_order(**params)
        
        logger.info(f"Order Successful! Order ID: {response.get('orderId')}")
        return {"success": True, "data": response}
        
    except BinanceAPIException as e:
        # Errors coming from Binance API 
        error_msg = f"Binance API Error (Code {e.status_code}): {e.message}"
        logger.error(error_msg)
        return {"success": False, "error": error_msg}
        
    except BinanceRequestException as e:
        # Network/Internet issues
        error_msg = f"Network Error: Could not connect to Binance. Details: {e}"
        logger.error(error_msg)
        return {"success": False, "error": error_msg}
        
    except Exception as e:
        error_msg = f"Unexpected Error: {str(e)}"
        logger.error(error_msg)
        return {"success": False, "error": error_msg}