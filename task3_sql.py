"""
Each task is a function that returns the result of a SQL query.

No other imports may be used
"""
from database_connection import DatabaseConnection


def task_3_1():
    """
    List the top 5 most borrowed books in the library.

    The result should include the books title and number of times borrowed,
    ranked from most borrowed to least borrowed.
    """
    # TODO: Implement me
    
    # I include ID as well in case there are repetitions in book name 
    # as the titles are generated using limited number of vals
    with DatabaseConnection() as cursor:
        cursor.execute(
            """
            SELECT BK.book_id,
            BK.title,
            BR.borrow_times
            FROM (
            SELECT 
            book_id, 
            COUNT(*) AS borrow_times
            FROM Borrows
            GROUP BY book_id
            ) AS BR
            JOIN 
            Book AS BK 
            ON BR.book_id = BK.book_id
            ORDER BY BR.borrow_times DESC
            LIMIT 5;
        """
        )
        popular_books = cursor.fetchall()
        res = []
        for row in popular_books:
            res.append(row)
        return res
        



def task_3_2():
    """
    For each month, calculate the total number of books borrowed and the
    average duration (in days) of a borrow.

    - If a book has not been returned yet, it should not be included in
    the average duration.
    - If a book was borrowed in month X and returned in month Y, it should
    be included in the month it was checked out.

    Display the months in a year-month format (YYYY-MM) and order
    by the month ascending.
    """
    # TODO: Implement me
    with DatabaseConnection() as cursor:
        cursor.execute(
            """
            SELECT 
            TO_CHAR(check_out_date, 'YYYY-MM') AS month_year,
            COUNT(*) AS total_borrowed,
            ROUND(AVG(return_date - check_out_date), 2) AS avg_borrow_duration
            FROM 
            Borrows
            WHERE return_date IS NOT NULL 
            GROUP BY TO_CHAR(check_out_date, 'YYYY-MM')
            ORDER BY 
            month_year ASC;
            """
        )
        month_borrows = cursor.fetchall()
        res = []
        for row in month_borrows:
            res.append(row)
        
        return res



def task_3_3():
    """
    Identify publishers that frequently collaborate with specific authors,
    where "frequent collaboration" means publishers that have published more
    than three books by the same author.
    """
    # TODO: Implement me
    with DatabaseConnection() as cursor:
        cursor.execute(
            """
            SELECT 
            b.author_id,
            a.name,
            b.publisher_id,
            p.publisher_name,
            COUNT(b.book_id) AS num_books_published
            FROM 
            Book b
            JOIN 
            Author a ON b.author_id = a.author_id
            JOIN 
            Publisher p ON b.publisher_id = p.publisher_id
            GROUP BY 
            b.author_id, a.name, b.publisher_id, p.publisher_name
            HAVING 
            COUNT(b.book_id) > 3  
            ORDER BY 
            num_books_published DESC;
            """
        )
        freq_collab = cursor.fetchall()
        res = []
        for row in freq_collab:
            res.append(row)
        return res


if __name__ == '__main__':
    print(task_3_1())
    print(task_3_2())
    print(task_3_3())
