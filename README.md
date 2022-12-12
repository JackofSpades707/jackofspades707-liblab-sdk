## Lord of the Rings SDK
This is a sample SDK as a take home assessment for liblab

## Install
* `pip install jackofspades_lib_lab_lotr`

## Example uses:
```python

from lotr_sdk import Book, Movie
# Get all books
books = Book.get()

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

# And so on...
```

## Testing:
* Install pytest `python -m pip install pytest`
* run `bash test.sh`
* or run `python -m pytest tests` from the projects root directory
