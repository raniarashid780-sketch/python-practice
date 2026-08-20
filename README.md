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

## Author

Rania Rashid — BS Artificial Intelligence, Ghazi University DG Khan

## License

MIT — see [LICENSE](LICENSE) for details.