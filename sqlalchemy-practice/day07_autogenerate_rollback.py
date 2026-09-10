# Task 7: Autogenerate blind spots + rollback safety

# Part 1 — expose the rename problem
# - In models.py, rename Patient.phone to Patient.contact_number
# - PREDICT (before running): will autogenerate produce an alter_column/rename,
#   or will it produce drop_column + add_column? Justify in one sentence.
# - Run: alembic revision --autogenerate -m "rename phone to contact_number"
# - Paste the FULL generated migration content
# - Confirm whether your prediction was right

# Part 2 — fix it manually
# - If the generated migration used drop_column/add_column, manually rewrite
#   upgrade() and downgrade() to use op.alter_column(..., new_column_name=...) instead
# - PREDICT: if you had applied the AUTO version instead of your manual fix,
#   and a row already had a phone number saved, what would happen to that data?

# Task 8 — test rollback for real, don't just trust the code
# - Run: alembic current          -> record the actual output
# - Run: alembic upgrade head     -> apply your manual rename migration
# - Manually insert one row with a value in contact_number (paste the INSERT + confirmation)
# - Run: alembic downgrade -1     -> paste FULL output
# - Query the table again: did contact_number/phone column survive, and did the
#   VALUE you inserted survive, or is it gone?
# - PREDICT this outcome BEFORE running downgrade, then compare to what you actually got