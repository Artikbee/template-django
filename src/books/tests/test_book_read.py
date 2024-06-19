import pytest

pytestmark = [pytest.mark.django_db]


@pytest.fixture
def author(mixer):
    return mixer.blend('books.Author', name='Вася')


@pytest.fixture
def book(mixer, author):
    return mixer.blend(
        'books.Book',
        author=author,
        name='Война и мир',
    )


def test_book_read(api, book, author):
    result = api.get('api/v1/books/')

    assert result[0]['id'] == book.id
    assert result[0]['name'] == 'Война и мир'
    assert result[0]['author']['id'] == author.id
    assert result[0]['author']['name'] == 'Вася'
