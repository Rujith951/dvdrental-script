def qstring(table_name):
    return f"""INSERT INTO public.{table_name}"""


def is_integer_string(s):
    return s.isdigit()


tables = [
    "actor",
    "address",
    "category",
    "city",
    "country",
    "customer",
    "film",
    "film_actor",
    "film_category",
    "inventory",
    "language",
    "payment",
    "rental",
    "staff",
    "store",
]
