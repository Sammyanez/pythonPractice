queries = [3, 2, 1, 2, 6]


def minimumWaitingTime(queries):
    i = 0
    iterator = 0
    queries.sort()
    for x in queries:
        i += x * (len(queries) - iterator - 1)
        iterator += 1
    return i


print(minimumWaitingTime(queries))
