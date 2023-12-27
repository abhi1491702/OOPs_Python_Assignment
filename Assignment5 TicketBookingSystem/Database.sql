-- 1. Create the database named "TicketBookingSystem"
CREATE DATABASE TicketBookingSystem;

-- 2. Create tables with appropriate data types, constraints, and relaƟonships

-- Venu Table
CREATE TABLE Venu (
 venue_id INT PRIMARY KEY,
 venue_name VARCHAR(255),
 address VARCHAR(255)
);
-- Event Table
CREATE TABLE Event (
 event_id INT PRIMARY KEY,
 event_name VARCHAR(255),
 event_date DATE,
 event_Ɵme TIME,
 venue_id INT,
 total_seats INT,
 available_seats INT,
 Ɵcket_price DECIMAL,
 event_type ENUM('Movie', 'Sports', 'Concert'),
 booking_id INT,
 FOREIGN KEY (venue_id) REFERENCES Venu(venue_id)
);
-- Customer Table
CREATE TABLE Customer (
 customer_id INT PRIMARY KEY,
 customer_name VARCHAR(255),
 email VARCHAR(255),
 phone_number VARCHAR(15),
 booking_id INT

);
-- Booking Table
CREATE TABLE Booking (
 booking_id INT PRIMARY KEY,
 customer_id INT,
 event_id INT,
 num_Ɵckets INT,
 total_cost DECIMAL,
 booking_date DATE,
 FOREIGN KEY (customer_id) REFERENCES Customer(customer_id),
 FOREIGN KEY (event_id) REFERENCES Event(event_id)
);
ALTER TABLE Event
ADD CONSTRAINT Ņ_event_booking
FOREIGN KEY (booking_id) REFERENCES Booking(booking_id);
ALTER TABLE Customer
ADD CONSTRAINT Ņ_customer_booking
FOREIGN KEY (booking_id) REFERENCES Booking(booking_id);


-- 1. Insert at least 10 sample records into each table
-- Insert sample data into Venu Table
INSERT INTO Venu (venue_id, venue_name, address) VALUES
(1, 'Raj Mahal', '12A MG Road, Mumbai, Maharashtra'),
(2, 'Taj Gardens', '34 Nehru Street, Delhi'),
(3, 'Lotus ConvenƟon Center', '56 Vivekananda Nagar, Bangalore, Karnataka'),
(4, 'Maratha Palace', '78 Shivaji Marg, Pune, Maharashtra'),
(5, 'Golden Sands Arena', '90 Beach Road, Goa'),
(6, 'Mysore Grand Hall', '45 Chamundi Hills, Mysuru, Karnataka'),
(7, 'Jaipur Pavilion', '23 Hawa Mahal Road, Jaipur, Rajasthan'),
(8, 'Chennai ConvenƟon Center', '67 Mount Road, Chennai, Tamil Nadu'),
(9, 'Kolkata Heights', '89 Park Street, Kolkata, West Bengal'),
(10, 'Hyderabad Hub', '78 Charminar Road, Hyderabad, Telangana');
-- Insert sample data into Event Table
INSERT INTO Event (event_id, event_name, event_date, event_Ɵme, venue_id, total_seats,
available_seats, Ɵcket_price, event_type, booking_id) VALUES
(1, 'Bollywood Extravaganza', '2023-12-15', '18:00:00', 1, 200, 150, 1500.00, 'Movie', 1),
(2, 'Cricket Championship', '2023-12-20', '19:30:00', 2, 5000, 4000, 250.00, 'Sports', 2),
(3, 'Classical Concert', '2023-12-25', '20:00:00', 3, 10000, 8000, 500.00, 'Concert', 3),
(4, 'Tech Summit', '2023-12-18', '09:00:00', 4, 500, 300, 10000.00, 'Conference', 4),
(5, 'Stand-up Comedy Night', '2023-12-22', '21:00:00', 5, 300, 250, 200.00, 'Comedy', 5),
(6, 'Cultural Fest', '2023-12-28', '17:00:00', 6, 1000, 800, 300.00, 'FesƟval', 6),
(7, 'Rajasthani Folk Evening', '2023-12-10', '19:30:00', 7, 800, 600, 400.00, 'Cultural', 7),
(8, 'Tech Workshop', '2023-12-15', '14:00:00', 8, 200, 150, 1200.00, 'Workshop', 8),
(9, 'Durga Puja CelebraƟon', '2023-12-20', '18:30:00', 9, 1200, 1000, 300.00, 'FesƟval', 9),
(10, 'Hyderabadi Biryani Cook-off', '2023-12-22', '13:00:00', 10, 150, 120, 250.00, 'Culinary', 10);
-- Insert sample data into Customer Table
INSERT INTO Customer (customer_id, customer_name, email, phone_number, booking_id) VALUES
(1, 'Rahul Sharma', 'rahul.sharma@email.com', '9876543210', 1),
(2, 'Priya Patel', 'priya.patel@email.com', '8765432109', 2),
(3, 'Amit Singh', 'amit.singh@email.com', '7654321098', 3),
(4, 'Sneha Gupta', 'sneha.gupta@email.com', '6543210987', 4),
(5, 'Kunal Verma', 'kunal.verma@email.com', '5432109876', 5),
(6, 'Neha Kapoor', 'neha.kapoor@email.com', '4321098765', 6),
(7, 'Rajat Verma', 'rajat.verma@email.com', '3210987654', 7),
(8, 'Anika Das', 'anika.das@email.com', '2109876543', 8),
(9, 'Vikram Joshi', 'vikram.joshi@email.com', '1098765432', 9),
(10, 'Aishwarya Singh', 'aishwarya.singh@email.com', '0987654321', 10);
-- Insert sample data into Booking Table
INSERT INTO Booking (booking_id, customer_id, event_id, num_Ɵckets, total_cost, booking_date)
VALUES
(1, 1, 1, 3, 4500.00, '2023-12-10'),
(2, 2, 2, 5, 1250.00, '2023-12-12'),
(3, 3, 3, 2, 1000.00, '2023-12-14'),
(4, 4, 4, 2, 20000.00, '2023-12-16'),
(5, 5, 5, 4, 800.00, '2023-12-19'),
(6, 6, 6, 3, 900.00, '2023-12-22'),
(7, 7, 7, 2, 800.00, '2023-12-24'),
(8, 8, 8, 1, 1200.00, '2023-12-28'),
(9, 9, 9, 5, 1500.00, '2023-12-30'),
(10, 10, 10, 3, 750.00, '2023-12-31');