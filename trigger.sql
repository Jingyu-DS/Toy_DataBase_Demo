CREATE OR REPLACE FUNCTION calculate_fine()
RETURNS TRIGGER AS $$
DECLARE
    days_overdue INT;
    fine_rate DECIMAL(10, 2) := 0.50;  -- Daily fine rate
    fine_due DECIMAL(10, 2);
BEGIN
    IF NEW.return_date > NEW.due_date THEN
        days_overdue := NEW.return_date - NEW.due_date;
        fine_due := days_overdue * fine_rate;
        INSERT INTO fines (student_id, book_id, days_overdue, fine_amount)
        VALUES (NEW.student_id, NEW.book_id, days_overdue, fine_due);

    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER trigger_calculate_fine
BEFORE INSERT OR UPDATE OF return_date ON Borrows
FOR EACH ROW
WHEN (NEW.return_date IS NOT NULL)
EXECUTE FUNCTION calculate_fine();
