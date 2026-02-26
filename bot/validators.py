def validate_inputs(symbol, side, order_type, quantity, price):
    """
    Validates user inputs directly from the CLI.
    """
    valid_sides = ['BUY', 'SELL']
    valid_types = ['MARKET', 'LIMIT']

    if side.upper() not in valid_sides:
        raise ValueError(f"Invalid side: '{side}'. Only 'BUY' or 'SELL' are allowed.")
    
    if order_type.upper() not in valid_types:
        raise ValueError(f"Invalid order type: '{order_type}'. Only 'MARKET' or 'LIMIT' are allowed.")
    
    try:
        qty = float(quantity)
        if qty <= 0:
            raise ValueError("Quantity must be greater than 0.")
    except ValueError:
        raise ValueError("Quantity must be a valid number.")
        
    if order_type.upper() == 'LIMIT':
        if price is None:
            raise ValueError("Price is required for a LIMIT order.")
        try:
            p = float(price)
            if p <= 0:
                raise ValueError("Price must be greater than 0.")
        except ValueError:
            raise ValueError("Price must be a valid number.")
            
    return True