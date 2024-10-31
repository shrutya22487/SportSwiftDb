USE SportSwiftDB;

-- Trigger 1
DELIMITER //
CREATE TRIGGER after_cart_delete
AFTER DELETE ON Cart
FOR EACH ROW
BEGIN
    INSERT INTO Orders (Customer_ID, Product_ID) VALUES (OLD.Customer_ID, OLD.Product_ID);
END
//
DELIMITER ;


-- Trigger 2
DELIMITER //

CREATE TRIGGER update_blocked_status
BEFORE UPDATE ON customer
FOR EACH ROW
BEGIN
    IF NEW.failed_attempts >= 3 THEN
        INSERT INTO check_blocked (customer_id, blocked) VALUES (NEW.Customer_ID, true);
    END IF;
END;
//

DELIMITER ;