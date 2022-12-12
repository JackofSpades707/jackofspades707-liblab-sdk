## Lord of the Rings SDK
This is a sample SDK as a take home assessment for liblab

## Install
* `pip install jackofspades_lib_lab_lotr`

## Example uses:
```python

from lotr_sdk import Book, Movie, Quote
# Get all books
books = Book.get()

# Create a custom book
book = Book(id="some_id", name="My Fanfic book")

# Get only 2 books
books = Book.get(limit=2)

# Get a certain book
id = "5cf5805fb53e011a64671582"
book = Book.get(id)

# Get all movies
movies = Movie.get()

# Get a certain movie
id = "5cd95395de30eff6ebccde56"
movie = Movie.get(id)

# Get all quotes from a movie
movie = Movie.get(id)
quotes = movie.quotes

# Get 2nd page of quotes
quotes = Quote.get(page=2)

# And so on...
```
* Check out the `get` method [here](https://github.com/JackofSpades707/jackofspades707-liblab-sdk/blob/master/lotr_sdk/mixins.py) for more details
* The following classes all inherit from the `ApiMixIn` class
  - Book
  - Movie
  - Character
  - Quote
  - Chapter

## Testing:
* Install pytest `python -m pip install pytest`
* run `bash test.sh`
* or run `python -m pytest tests` from the projects root directory
