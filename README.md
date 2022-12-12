## Install
* `pip install jackofspades_liblab_lotr`

## Example uses:
```python

from lotr_sdk import Book, Movies
# Get all books
books = Book.get()

# Get a certain book
id = "5cf5805fb53e011a64671582"
book = Book.get(id)


# Get all movies
movies = Movies.get()

# Get a certain movie
id = "5cd95395de30eff6ebccde56"
movie = Movie.get(id)

# Get all quotes from a movie
movie = Movie.get(id)
quotes = movie.quotes

# And so on...
```
