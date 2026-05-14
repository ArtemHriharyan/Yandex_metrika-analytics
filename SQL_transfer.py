import pandas as pd
from sqlalchemy import create_engine

# Загружаем CSV
df = pd.read_csv("metrika_dataset.csv")

# Подключение к PostgreSQL
engine = create_engine(
    "postgresql+psycopg2://postgres:12345678@localhost:5432/Analytics"
)

# Загружаем таблицу
df.to_sql(
    "metrika_data",
    con=engine,
    if_exists="replace",
    index=False
)

print("Данные загружены в PostgreSQL")
