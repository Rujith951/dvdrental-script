import csv
from mapper import qstring, tables, is_integer_string


for table in tables:
    with open(f"csv/{table}.csv") as file:
        reader = csv.reader(file)
        index, string = 0, qstring(table)
        for row in reader:
            # prepare query string
            if index == 0:
                string += f"""({', '.join(row)}) VALUES """
                index += 1
                continue

            for idx, col_val in enumerate(row):
                if is_integer_string(col_val):
                    string += f"""({col_val},"""
                    continue
                string += f"""'{col_val}'{'' if idx == len(row)-1 else ','}"""
            string += "),"
        string += ","
        # append values for query string

    with open(f"{table}.sql", "w") as file:
        file.write(string)
