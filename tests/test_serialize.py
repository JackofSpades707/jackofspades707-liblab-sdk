import sys

sys.path.append("..")
from lotr_sdk.sdk import Book, Movie, Character, Quote, Chapter


def test_serialize_book():
    data = {"_id": "5cf5805fb53e011a64671582", "name": "The Fellowship Of The Ring"}
    book = Book.serialize([data])

    assert isinstance(book, Book)
    assert book.id == data["_id"]
    assert book.name == data["name"]


def test_serialize_movie():
    data = {
        "_id": "3948hfg834n029347n94f3nf",
        "name": "Foobar",
        "run_time": 5,
        "budget": 500,
        "revenue": 2000,
        "nominations": 500,
        "nomination_wins": 37,
        "score": 92,
    }
    movie = Movie.serialize([data])

    assert isinstance(movie, Movie)
    assert movie.id == data['_id']
    assert movie.name == data['name']
