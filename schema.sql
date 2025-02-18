DROP TABLE IF EXISTS PhoneNumber;
DROP TABLE IF EXISTS Borrows;
DROP TABLE IF EXISTS Book_Edition;
DROP TABLE IF EXISTS fines;
DROP TABLE IF EXISTS Book;
DROP TABLE IF EXISTS Publisher;
DROP TABLE IF EXISTS Author;
DROP TABLE IF EXISTS Phone_Number;
DROP TABLE IF EXISTS Student;

CREATE TABLE IF NOT EXISTS Student (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(30) NOT NULL,
    street VARCHAR(30),
    city VARCHAR(30),
    state CHAR(5)
);
CREATE TABLE IF NOT EXISTS Phone_Number (
    student_id INT NOT NULL,
    phone_number CHAR(15) NOT NULL,
    PRIMARY KEY (student_id, phone_number),
    FOREIGN KEY (student_id) REFERENCES Student(student_id)
);
CREATE TABLE IF NOT EXISTS Author (
    author_id INT PRIMARY KEY,
    name VARCHAR(30) NOT NULL
);
CREATE TABLE IF NOT EXISTS Publisher (
    publisher_id INT PRIMARY KEY,
    publisher_name VARCHAR(30) NOT NULL
);

CREATE TABLE IF NOT EXISTS Book (
    book_id INT PRIMARY KEY,
    title VARCHAR(30) NOT NULL,
    author_id INT NOT NULL,
    publisher_id INT,
    FOREIGN KEY (author_id) REFERENCES Author(author_id),
    FOREIGN KEY (publisher_id) REFERENCES Publisher(publisher_id)
);
CREATE TABLE IF NOT EXISTS Book_Edition (
    book_id INT NOT NULL,
    edition_number INT NOT NULL,
    year INT NOT NULL,
    PRIMARY KEY (book_id, edition_number),
    FOREIGN KEY (book_id) REFERENCES Book(book_id)
);

CREATE TABLE IF NOT EXISTS Borrows (
    student_id INT,
    book_id INT,
    check_out_date DATE NOT NULL,
    due_date DATE,
    return_date DATE,
    PRIMARY KEY (student_id, book_id, check_out_date, due_date),
    FOREIGN KEY (student_id) REFERENCES Student(student_id),
    FOREIGN KEY (book_id) REFERENCES Book(book_id)
);

CREATE TABLE IF NOT EXISTS fines (
    fine_id SERIAL PRIMARY KEY,
    student_id INT NOT NULL,
    book_id INT NOT NULL,
    days_overdue INT NOT NULL,
    fine_amount DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (student_id) REFERENCES Student(student_id),
    FOREIGN KEY (book_id) REFERENCES Book(book_id)
);





