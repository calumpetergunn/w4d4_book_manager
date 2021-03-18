class Book:

    def __init__(self, title, year, genre, author, purchased = False, id = None):
        self.title = title
        self.year = year
        self.genre = genre
        self.author = author
        self.purchased = purchased
        self.id = id
        
    def mark_purchased(self):
        self.purchased = True