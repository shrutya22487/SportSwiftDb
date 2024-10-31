Create database IF NOT EXISTS SportSwiftDB;
USE SportSwiftDB;


CREATE TABLE IF NOT EXISTS Customer
(
    Customer_ID     INT                 NOT NULL AUTO_INCREMENT,
    Name            VARCHAR(255)        NOT NULL,
    Address         VARCHAR(255)        NOT NULL,
    email_ID        VARCHAR(255) UNIQUE NOT NULL,
    Password        VARCHAR(255)        NOT NULL,
    failed_attempts INT DEFAULT 0,
    PRIMARY KEY (Customer_ID)
);

CREATE TABLE IF NOT EXISTS Product
(
    Product_ID  INT            NOT NULL AUTO_INCREMENT,
    Name        VARCHAR(255)   NOT NULL,
    Category    VARCHAR(255)   NOT NULL,
    Description TEXT           NOT NULL,
    Price       DECIMAL(10, 2) NOT NULL,
    Quantity    INT            NOT NULL,
    Image_Path  VARCHAR(255),
    PRIMARY KEY (Product_ID)
);
CREATE TABLE IF NOT EXISTS Cart
(
    Customer_ID INT NOT NULL,
    Product_ID  INT NOT NULL,
    Quantity    INT NOT NULL DEFAULT 1,
    Deleted     BOOL         DEFAULT FALSE,
    FOREIGN KEY (Customer_ID) REFERENCES Customer (Customer_ID),
    FOREIGN KEY (Product_ID) REFERENCES Product (Product_ID)
);


CREATE TABLE IF NOT EXISTS check_blocked
(
    Customer_ID INT  NOT NULL,
    blocked     BOOL NOT NULL DEFAULT FALSE,
    PRIMARY KEY (Customer_ID)
);


CREATE TABLE IF NOT EXISTS Orders
(
    Customer_ID INT NOT NULL,
    Product_ID  INT NOT NULL,
    Quantity    INT NOT NULL DEFAULT 1,
    FOREIGN KEY (Customer_ID) REFERENCES Customer (Customer_ID),
    FOREIGN KEY (Product_ID) REFERENCES Product (Product_ID)
);

SELECT *
from Customer;
SELECT * FROM Product
