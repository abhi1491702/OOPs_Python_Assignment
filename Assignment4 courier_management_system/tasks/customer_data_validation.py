import re


def validate_customer_info(data, detail):
    if detail == "name":
        return data.isalpha() and data.istitle()
    elif detail == "address":
        return not bool(re.search('[!@#$%^&*(),.?":{}|<>]', data))
    elif detail == "phone_number":
        return bool(re.match(r'\d{3}-\d{3}-\d{4}', data))
    else:
        return False


# Example usage
customer_name = "olivia"
customer_address = "Delhi "
customer_phone = "8756117054"

name_valid = validate_customer_info(customer_name, "name")
address_valid = validate_customer_info(customer_address, "address")
phone_valid = validate_customer_info(customer_phone, "phone_number")

print(f"Name Valid: {name_valid}, Address Valid: {address_valid}, Phone Valid: {phone_valid}")