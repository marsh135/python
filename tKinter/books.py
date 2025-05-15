import random

class Book:
    def __init__(self, title, author, genre, rating, fnf):
        self.title = title
        self.author = author
        self.genre = genre
        self.rating = rating
        self.fnf = fnf

    def __str__(self):
        return f"{self.genre}: {self.title} by {self.author} "

class BookRecommendation:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def suggest_book(self, preferred_genre=None):
        if not self.books:
            return "No books available for recommendation."

        if preferred_genre:
            genre_books = [book for book in self.books if book.genre.lower() == preferred_genre.lower()]
            if not genre_books:
                return f"No books available in the preferred genre '{preferred_genre}'."

            return random.choice(genre_books)
        else:
            return random.choice(self.books)

# Example usage:
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "Classic", 4, "Fiction")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "Classic", 3, "Fiction")
book3 = Book("1984", "George Orwell", "Dystopian", 4, "Fiction")
book4 = Book("Long Way Down", "Jason Reynolds", "Fiction", 5, "Fiction")

recommendation_system = BookRecommendation()
recommendation_system.add_book(book1)
recommendation_system.add_book(book2)
recommendation_system.add_book(book3)
recommendation_system.add_book(book4)

# Get user input for preferred genre
preferred_genre = input("Enter your preferred genre (or press Enter to get a random suggestion): ")

# Get a book suggestion based on user input
suggested_book = recommendation_system.suggest_book(preferred_genre)
print("I suggest you read:", suggested_book)
