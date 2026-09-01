# Python Practice 🐍

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=flat-square)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

Structured Python practice covering core programming, data manipulation, visualization, and SQL — progressing toward NLP and LLM engineering.

## Structure

| Folder | Contents |
|---|---|
| `python-core/` | Variables, OOP, file handling, pathlib, shutil |
| `NumPy/` | Array operations, broadcasting, linear algebra, mini-project |
| `pandas/` | DataFrames, cleaning, groupby, merging, mini-project |
| `matplotlib/` | Charts, styling, subplots |
| `sql-practice/` | PostgreSQL exercises (14-day track), completed with the Smart Care Clinic capstone |
| `sqlalchemy-practice/` | SQLAlchemy basics, database models, and ORM learning examples |
| `fastapi-practice/` | FastAPI path parameters, query parameters, validation, and Swagger UI |
| `docker/` | Container basics and Dockerized app examples |

## Setup

```bash
pip install -r requirements.txt
```

## Usage

```bash
python python-core/01_variables_and_print.py
python NumPy/09_numpy_basics.py
python pandas/20_pandas_series_dataframes.py
```

For SQL practice:
- This project is set up for PostgreSQL, not SQLite.
- Use your own PostgreSQL database and client to run the SQL files in `sql-practice`.
- Example using `psql`:

```bash
cd sql-practice
psql -f day01.sql -d your_database_name
```

For SQLAlchemy practice:
- Use the environment installed from `requirements.txt`.
- Import SQLAlchemy in your scripts to practice connections, models, and ORM operations.
- Example:

```bash
python sqlalchemy-practice/day01_core_basics.py
```

For FastAPI practice:
- Activate the virtual environment before running the API.
- Start the development server from the `fastapi-practice` directory:

```bash
cd fastapi-practice
uvicorn day01_basics:app --reload --port 8001
```

- Open `http://127.0.0.1:8001/docs` to test the endpoints in Swagger UI.
- `GET /items/{item_id}` demonstrates typed path parameters and returns the item ID and its Python type.
- `GET /search` demonstrates a required query parameter and an optional query parameter with a default value.
- `GET /items/{item_id}/reviews` demonstrates a typed path parameter and an optional float query parameter.
- Invalid values such as `/items/abc` or `min_rating=abc` return HTTP `422` because FastAPI validation rejects values with the wrong type.

For Docker practice:
- Docker is included in the project requirements for container and image work.
- Run Docker commands from the project root or inside the relevant lesson folder.
- Example:

```bash
docker --version
cd fastapi-practice/day09_docker
docker build -t day09_docker .
```

## Author

Rania Rashid — BS Artificial Intelligence, Ghazi University DG Khan

## License

MIT — see [LICENSE](LICENSE) for details.