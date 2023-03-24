from datetime import datetime as dt, timedelta as timedelta
import datetime as datetime
from random import randint, uniform


def main():
    to_file_writer()


def sample_generation():
    amount_of_rows = 200
    # amount_of_rows = int(input("How many rows should i generate? "))
    rows_at_once = 10_000
    file_openings = int(amount_of_rows / rows_at_once)
    if file_openings > 0:
        rows_at_once = int(amount_of_rows / 10000)
        return rows_at_once, file_openings
    else:
        file_openings = 1
        rows_at_once = int(amount_of_rows % rows_at_once)
        return rows_at_once, file_openings


def to_file_writer():
    rows_at_once, file_openings = sample_generation()
    print(rows_at_once, file_openings)

    for file_open in range(file_openings):
        res = ""

        for addition in range(rows_at_once):
            time = dt.now() - timedelta(hours=randint(-24, 24), minutes=randint(-60, 60))
            time = time.strftime("%H:%m")
            time = str(time + ";").split(":")[0]
            col_1 = str(randint(1, 100)) + ";"
            col_2 = str(round(uniform(0, 1), 2)) + ";"
            col_3 = str(float(col_1)*float(col_2)) + "\n"

        with open("test_data.txt", "a", encoding="utf-8") as file:
            file.write(res)


if __name__ == "__main__":
    main()

