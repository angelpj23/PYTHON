txt = "I like bananas"

x = txt.replace("bananas", "apples")

print(x)


# varios replace de un string
def normalize(record):
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
        ("Á", "A"),
        ("É", "E"),
        ("Í", "I"),
        ("Ó", "O"),
        ("Ú", "U"),
    )
    for a, b in replacements:
        record = record.replace(a, b)
    return record