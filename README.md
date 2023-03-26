# book_service

The project is written in Python 3.10

How to run project:
1. clone this repository
2. open project folder in IDE
3. run in IDE terminal: 
	- poetry update (https://python-poetry.org/docs/ - if you don't have poetry)
	- cd book
	- python manage.py makemigrations
	- python manage.py migrate
	- python manage.py runserver
4. use endpoints to make requests:
	- api/v1 (to get list of available endpoints)
	- api/v1/book (to get list of existing books or create new book)
	- api/v1/book/pk where 'pk' is book id (to get info about existing particular book or change existing book)
	- api/v1/author (to get list of existing authors or create new author)
	- api/v1/author/pk where 'pk' is author id (to get info about existing particular author book or change existing author)
	- api/v1/book_themes (to get list of existing book themes or create new theme)
	- api/v1/book_themes/pk where 'pk' is theme id (to get info about existing particular book theme or change existing theme)
	- api/v1/book_genres (to get list of existing book genres or create new genre)
	- api/v1/book_genres/pk where 'pk' is genre id (to get info about existing particular book genre or change existing genre)
