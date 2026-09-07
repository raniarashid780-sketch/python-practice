"""Alembic Day 6 worksheet.

Run these commands from the sqlalchemy-practice directory. Do not run this
file as the migration command; Alembic reads the configuration and models.
"""

# Before running the first command, predict the result:
# The patients and appointments tables already exist, so the initial
# migration should be empty if the database schema matches models.py.

# Task 1: Generate the initial migration.
# Command:
# alembic revision --autogenerate -m "init"
# Result: created alembic/versions/7597e5769d72_init.py
# Actual migration:
# def upgrade() -> None:
#     pass
#
# def downgrade() -> None:
#     pass

# Task 2: Read the generated file in alembic/versions/.
# The migration is empty because the existing tables already match the models.

# Task 3: Apply the initial migration.
# Prediction: Alembic should record the migration in alembic_version. If the
# migration is empty, it should not recreate the existing application tables.
# Command:
# alembic upgrade head
# Result: command completed successfully with exit code 0.
# Alembic recorded the revision in alembic_version without recreating tables.

# Task 4: Add this nullable field to Patient in models.py:
# phone: Mapped[str | None]
#
# Then generate and inspect the migration:
# alembic revision --autogenerate -m "add patient phone"
# Expected operation to confirm in the generated file:
# op.add_column("patients", sa.Column("phone", sa.String(), nullable=True))
# Actual generated operation in d2106fd9e41b_add_patient_phone.py:
# op.add_column('patients', sa.Column('phone', sa.String(), nullable=True))
# The generated downgrade contains:
# op.drop_column('patients', 'phone')
#
# Apply and verify it:
# alembic upgrade head
# DBeaver verification:
# Confirm that patients.phone exists and has type character varying.