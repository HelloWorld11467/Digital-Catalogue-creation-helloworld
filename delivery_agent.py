from typing import Optional
import random

# Mock delivery partners (can be pulled from DB later)
local_delivery_partners = [
    {"name": "Ravi", "phone": "9876543210", "area": "Nellore"},
    {"name": "Meena", "phone": "9876512345", "area": "Gudur"},
    {"name": "Arun", "phone": "9876509876", "area": "Tirupati"}
]

def assign_delivery(order_id: str, delivery_type: str, location: Optional[str] = None) -> dict:
    if delivery_type.lower() == "self":
        return {
            "status": "confirmed",
            "message": f"Seller has opted for self delivery of order {order_id}"
        }
    elif delivery_type.lower() == "assign":
        if location:
            partner = random.choice(local_delivery_partners)
            return {
                "status": "assigned",
                "partner": partner,
                "message": f"Assigned {partner['name']} to deliver order {order_id} in {location}"
            }
        else:
            return {"error": "Please provide delivery location to assign a local partner"}
    else:
        return {"error": "Invalid delivery type. Use 'self' or 'assign'"}
