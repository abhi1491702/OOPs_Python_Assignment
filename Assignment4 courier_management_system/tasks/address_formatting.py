def format_address(street, city, state, zip_code):
    formatted_address = f"{street.title()}, {city.title()}, {state.title()} {zip_code}"
    return formatted_address


# Example usage
street = "133/1"
city = "Lko"
state = "AP"
zip_code = "209010"

formatted_address = format_address(street, city, state, zip_code)
print("Formatted Address:", formatted_address)