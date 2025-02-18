import random
from datetime import datetime, timedelta
from database_actions import database_actions

def random_date(start_date, end_date):
    """
    This function is meant to help the data point creation in Borrows table
    Start date --> checkout date
    End date --> due date
    The random function would generate a random days added to checkout date to generate return date
    The return date, therefore, can fall before the due date or can pass the due.
    """
    delta = end_date - start_date 
    # in order to make some overdue cases
    threshold = 100
    random_days = random.randint(1, max(delta.days, 100)) 
    return start_date + timedelta(days=random_days) 

def random_phone_num():
    """
    This function is meant to generate a valid phone number for the multi-value phone number field. 
    """
    first3 = str(random.randint(100, 999))
    middle3 = str(random.randint(100, 999))
    last4 = str(random.randint(1000, 9999))
    return first3 + '-' + middle3 + '-' + last4


def book_generator_insertion(num_entries=200):
    """
    This function is to generate data points and insert into the Book table.
    """
    table_name = "Book"
    fields = ('book_id', 'title', 'author_id', 'publisher_id')
    titles = ["Pride", "War", "Peace", "Adventure", "Legacy", "Destiny", "Fortune", "Victory", "Glory", "Honor"]
    for i in range(1, num_entries + 1):
        title = random.choice(titles)  # Randomly choose a title from the list
        author_id = random.randint(1, 20)  # Random integer in the range [1, 20]
        publisher_id = random.randint(1, 3)   # Random integer in the range [1, 3]
        v = (i, title, author_id, publisher_id)
        database_actions.execute_insert(table_name, fields, v)
    

def edition_generator_insertion(num_entries = 200):
    """
    This function is to generate data points and insert into the Edition table. 
    """
    table_name = 'Book_Edition'
    fields = ('book_id', 'edition_number', 'year')

    for i in range(1, num_entries + 1):
        edition_number = random.randint(1, 5)
        edition_year = random.randint(1990, 2023)
        v = (i, edition_number, edition_year)
        database_actions.execute_insert(table_name, fields, v)



def student_generator_insertion(num_entries = 100):
    """
    This function is to generate data points and insert into Student table. 
    """
    table_name = 'Student'
    fields = ('student_id', 'student_name', 'street', 'city', 'state')

    student_name = ['John Smith', 'Olivia Garcia', 'James Brown', 'David Brown', 'Sarah Williams', 'Emily Davis', 'Sarah Johnson']
    street = ['4827 2nd Ave', '3903 Main St', '4834 4th St', '8601 2nd Ave', '5186 3rd Blvd', '9273 Main St']
    city = ['Philadelphia', 'New York', 'San Diego', 'Dallas', 'Austin', 'San Antonio']
    home_state = ['GA', 'FL', 'PA', 'CA', 'NY', 'OH', 'MI', 'AZ']
    for i in range(1, num_entries + 1):
        name = random.choice(student_name)
        st = random.choice(street)
        ct = random.choice(city)
        h_st = random.choice(home_state)
        v = (i, name, st, ct, h_st)
        database_actions.execute_insert(table_name, fields, v)


def borrows_generator_insertion(num_entries = 500):
    """
    This function is to generate data points for the Borrows table with the help from the random date generation function
    """
    table_name = 'Borrows'
    fields = ('student_id', 'book_id', 'check_out_date', 'due_date', 'return_date')

    for i in range(1, num_entries + 1):
        sid = random.randint(1, 100)
        bid = random.randint(1, 200)
        # Generate a checkout date and set 30 days threshold to get duedate
        checkout_date = datetime(2024, random.randint(1, 12), random.randint(1, 27))
        due_date = checkout_date + timedelta(days=30) 
        return_date = random_date(checkout_date, due_date)
        v = (sid, bid, checkout_date.strftime("%Y-%m-%d"), due_date.strftime("%Y-%m-%d"), return_date.strftime("%Y-%m-%d"))
        database_actions.execute_insert(table_name, fields, v)


def phonenumber_generation_insertion(nums_entries = 100, multivalue = True):
    """
    This function is to generate data points for the multivalue field phone number
    In order to best mirror the multivalue quality, the if statement is added to add one more data points
    """
    table_name = 'Phone_Number'
    fields = ('student_id', 'phone_number')

    for i in range(1, nums_entries + 1):
        phone_num1 = random_phone_num()
        v1 = (i, phone_num1)
        database_actions.execute_insert(table_name, fields, v1)
        # mirror the case when there can be more than one phone number
        if multivalue and i % 10 == 0:
            phone_num2 = random_phone_num()
            v2 = (i, phone_num2)
            database_actions.execute_insert(table_name, fields, v2)


def seed_database():
    """
    Insert data for 3 publishers.
    Add 20 authors.
    Create 200 book entries.
    Tie each book to an edition.
    Register 100 students.
    Record 500 borrow transactions, associating books with students.
    """
    table_name = "Publisher"
    fields = ('publisher_id', 'publisher_name')
    values = [
    (1, "HarperCollins"), (2, "Scholastic Corp"), (3, "Penguin Books")
    ]
    for v in values:
        database_actions.execute_insert(table_name, fields, v)
    
    # Insert data to Author
    table_name = "Author"
    fields = ("author_id", "name")
    values = [(1, "Jane Austen"),(2, "Mark Twain"),(3, "George Orwell"),
    (4, "J.K. Rowling"),(5, "F. Scott Fitzgerald"),(6, "Ernest Hemingway"),
    (7, "Harper Lee"),(8, "Stephen King"),(9, "Agatha Christie"),
    (10, "Isaac Asimov"),(11, "Virginia Woolf"),(12, "Leo Tolstoy"),
    (13, "J.D. Salinger"),(14, "Charles Dickens"),(15, "H.G. Wells"),
    (16, "Emily Dickinson"),(17, "Franz Kafka"),(18, "Toni Morrison"),
    (19, "Gabriel García Márquez"),(20, "Ray Bradbury")
    ]
    for v in values:
        database_actions.execute_insert(table_name, fields, v)
    
    book_generator_insertion()
    edition_generator_insertion()
    student_generator_insertion()
    borrows_generator_insertion()
    phonenumber_generation_insertion()




if __name__ == '__main__':
    seed_database()
