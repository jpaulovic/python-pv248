def count(start=0, step=1):
    # count(10) --> 10 11 12 13 14 ...
    # count(2.5, 0.5) -> 2.5 3.0 3.5 ...
    n = start
    while True:
        yield n
        n += step


def square(src):
    while True:
        number = next(src)
        yield number*number

squares = square(count())
for i in range(100):
    s = next(squares)
    print(s)

# alternativně (s použití enumerate())
for i, s in enumerate(square(count())):
    if i > 50:
        break
    print(s)