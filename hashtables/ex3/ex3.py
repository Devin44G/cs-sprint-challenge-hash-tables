def intersection(arrays):
    """
    YOUR CODE HERE
    """
    cache = {}

    for arr in arrays:
        for i in arr:
            if i not in cache:
                cache[i] = 0
            cache[i] += 1
    result = [item[0] for item in cache.items() if item[1] == len(arrays)]
    return result
    # print(cache)


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
