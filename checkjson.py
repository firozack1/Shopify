import json

def extract_orders_with_discount_code(file_path, discount_code):
    # Load the JSON data
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    # Extract orders where the discount code was used and financial_status is paid
    filtered_orders = [
        {
            "id": order["id"],
            "currency_subtotal_price": order["current_subtotal_price"],
            "contact_email": order["contact_email"],
            "phone": order["phone"]
        }
        for order in data["orders"]
        if order["financial_status"] == "paid" and any(code["code"] == discount_code for code in order.get("discount_codes", []))
    ]
    
    # Print the extracted details
    for order in filtered_orders:
        print(f"ID: {order['id']}")
        print(f"Subtotal Price: {order['currency_subtotal_price']}")
        print(f"Contact Email: {order['contact_email']}")
        print(f"Phone: {order['phone']}")
        print("---------")

if __name__ == "__main__":
    file_path = 'response.json'  # Path to the JSON file
    discount_code = input("Enter the discount code: ")
    extract_orders_with_discount_code(file_path, discount_code)
