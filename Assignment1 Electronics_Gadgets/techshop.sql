CREATE DATABASE TechShop;

USE TechShop;

CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Email VARCHAR(100),
    Phone VARCHAR(20),
    Address VARCHAR(255)
);

INSERT INTO Customers VALUES
(1, 'Sid', 'Mundhe', 'sidmun@email.com', '7654765489', '123 amravati '),
(2, 'Vedu', 'Wagh', 'veduwagh@email.com', '9873451234', '456 jalna'),
(3, 'Sonu', 'Jaybhay', 'sonujay@email.com', '9865321468', '123 pune'),
(4, 'Tejas', 'Mundhe', 'tejmun@email.com', '9865321476', '123 cheenai'),
(5, 'Satish', 'More', 'satishmore@email.com', '7654321981', '23 Mumbai'),
(6, 'Teju', 'Patel', 'teju.patel@email.com', '987654321', '67 Badisadak'),
(7, 'Ankit', 'Dudhani', 'andudhani@email.com', '765432198', 'delhi'),
(8, 'Shubham', 'Charkha', 'shubchar@email.com', '9753124680', 'stand banglore'),
(9, 'Akanksha', 'Negi', 'akupnegi@email.com', '7890654321', 'cheenai'),
(10, 'Ishan', 'Mitall', 'ishmittal@email.com', '987651234', 'jaipur');

Select * from Customers;

CREATE TABLE Products (
    ProductID INT PRIMARY KEY,
    ProductName VARCHAR(100),
    Description TEXT,
    Price INT
);

INSERT INTO Products VALUES
(1, 'Laptop', 'High-performance laptop', 50000),
(2, 'Smartphone', 'Latest smartphone model', 20000),
(3, 'Tablet', '10-inch tablet with high-resolution display', 15000),
(4, 'Smartwatch', 'Fitness and smart features in a sleek design', 5000),
(5, 'Wireless Earbuds', 'Bluetooth earbuds with noise cancellation', 2500),
(6, '4K Smart TV', '65-inch smart TV with 4K UHD resolution', 17000),
(7, 'Gaming Laptop', 'Powerful laptop for gaming enthusiasts', 70000),
(8, 'Portable Bluetooth Speaker', 'Compact speaker with great sound quality', 1000),
(9, 'Digital Camera', 'High-resolution camera for photography enthusiasts',40000),
(10, 'External Hard Drive', '1TB external hard drive for extra storage', 3500);

select * from Products;

CREATE TABLE Orders (
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    OrderDate DATE,
    TotalAmount INT,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

INSERT INTO Orders VALUES
(1, 1, '2023-01-01', 50000),
(2, 2, '2023-02-15', 20000),
(3, 1, '2023-03-10', 15000),
(4, 2, '2023-04-02', 5000),
(5, 1, '2023-05-15', 2500),
(6, 3, '2023-06-20', 17000),
(7, 2, '2023-07-05', 70000),
(8, 3, '2023-08-12', 1000),
(9, 1, '2023-09-25', 40000),
(10, 2, '2023-10-18', 3500);

select * from Orders;
CREATE TABLE OrderDetails (
    OrderDetailID INT PRIMARY KEY,
    OrderID INT,
    ProductID INT,
    Quantity INT,
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);

INSERT INTO OrderDetails VALUES
(1, 1, 1, 2),
(2, 2, 2, 1),
(3, 3, 3, 1),
(4, 4, 4, 2),
(5, 5, 5, 1),
(6, 6, 6, 1),
(7, 7, 7, 3),
(8, 8, 8, 2),
(9, 9, 9, 1),
(10, 10, 10, 4);

select * from OrderDetails;

CREATE TABLE Inventory (
    InventoryID INT PRIMARY KEY,
    ProductID INT,
    QuantityInStock INT,
    LastStockUpdate DATE,
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);