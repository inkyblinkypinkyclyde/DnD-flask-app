# DnD simple calculator & Stat tracker


This is a simple lightweight web tracker made in Python running a Flask web server connecting to a PostgreSQL database.

Installation

Clone the repo with:

```bash
git clone https://github.com/inkyblinkypinkyclyde/DnD-flask-app
```

Create a postgres database...

```bash
createdb dnd_web
```

...and connect it to the provided schema by entering the following command from within the project's main directory:

```bash
psql -d dnd_web -f db/dnd_web.sql
```

You can populate the app with test data by entering:

```bash
python console.py
```

Or run the app straight away without test data by entering: 

```bash
python app.py
```


## Technologies used
* Python (v3.9.12)
* PostgreSQL (v14.5)
* Flask (v2.1.2)
* Jinja2 (v3.1.2)
* Psycopg2 (v2.9.3)