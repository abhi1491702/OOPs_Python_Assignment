from util.DatabaseConnector import DatabaseConnector
from Entity.Customers import Customers
from Entity.Products import Products
from Entity.Orders import Orders
from Entity.OrderDetails import OrderDetails
from Entity.Inventory import Inventory

db_connector = DatabaseConnector(host ="localhost", database ="techshop", user ="root", password ="Ram@12345")
db_connector.open_connection()
customers_manager= Customers(db_connector)


# customers_manager.create_customer("121","Shan","Bai", "shanbi@gmail.com", "123458759","Latur")
#
# customers_manager.update_customer_Info("11", "abhishek@gmail.com", "123458907", "kanpur,up")
#
# customers_manager.get_Customer_Details(112)
#
# customers_manager.calculate_Total_Orders(102)
#
# products_manager=Products(db_connector)
#
# products_manager.get_product_details(1)
#
# products_manager.update_Product_Info("11","Dolby 5.2.0 atmos ",2500)
#
# products_manager.is_Product_InStock(1)
# orders_manager=Orders(db_connector)
#
# orders_manager.get_Order_Details(1001)
# orders_manager.Calculate_Total_Amount(1001)
# orders_manager.place_order(1015,2015,102,2,2)
#
# orderdetails_manager=OrderDetails(db_connector)
# orderdetails_manager.get_OrderDetail_Info(2001)
# orderdetails_manager.update_Quantity(2001,3)
# orderdetails_manager.Calculate_Subtotal(2001)
#
# inventory_manager=Inventory(db_connector)
# inventory_manager.Get_Product(301)
#
# inventory_manager.get_QuantityInStock(301)
#
# inventory_manager.add_To_Inventory(20,301)
#
# inventory_manager.remove_From_Inventory(20,301)
#
# inventory_manager.update_Stock_Quantity(20,301)
#
# inventory_manager.Is_Product_Available(20,301)
#
# inventory_manager.Get_InventoryValue()
#
# inventory_manager.List_LowStock_Products(10)
#
# inventory_manager.List_OutOf_StockProducts()
#
# inventory_manager.List_All_Products()
#
# db_connector.close_connection()