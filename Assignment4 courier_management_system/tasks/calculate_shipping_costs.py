def calculate_shipping_cost(parcel_weight):
    distance = 200
    cost_per_km = 2.5
    shipping_cost = distance * cost_per_km * parcel_weight
    return shipping_cost

# Example usage
source_address = "Source City, Source State"
destination_address = "Destination City, Destination State"
parcel_weight = 7.5

shipping_cost = calculate_shipping_cost(parcel_weight)
print("Source Address:", source_address)
print("Destination Address:", destination_address)
print("Shipping Cost:", shipping_cost)