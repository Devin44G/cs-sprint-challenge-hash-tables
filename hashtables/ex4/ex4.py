def has_negatives(a):
    seen = {}
    result = []

    for each in a:
        seen[each] = None

        if each != 0 and -each in seen:
            result.append(abs(each))

    return result



if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
