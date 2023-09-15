import requests
from bs4 import BeautifulSoup
import sqlite3

response = requests.get("https://sinoptik.ua/")
if response.status_code == 200:
    bs = BeautifulSoup(response.text, features="html.parser")
    temperature = bs.find("p", {"class": "today-temp"}).text
    time = bs.find("p", {"class": "today-time"}).text

    print(f"Курс Євро: {temperature}")

    # Підключення до бази даних
    connection = sqlite3.connect("Database.sl3")
    cur = connection.cursor()
    # Створення таблиці
    #cur.execute("DROP TABLE first_table;")
    cur.execute("CREATE TABLE IF NOT EXISTS first_table (name TEXT, names TEXT)")

    # Вставка даних
    cur.execute("INSERT INTO first_table (name, names) VALUES (?, ?)", (time, temperature))

    # Збереження змін
    connection.commit()
    connection.close()
