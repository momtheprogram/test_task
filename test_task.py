def solution_long(n: int) -> str:
    result = []
    for elem in range(1, n + 1):
        result.append(str(elem) * elem)

    return "".join(result)


def solution_short(n: int) -> str:
    return "".join([str(elem) * elem for elem in range(1, n + 1)])


if __name__ == "__main__":
    assert solution_long(1) == "1"
    assert solution_long(2) == "122"
    assert solution_long(3) == "122333"
    assert solution_long(4) == "1223334444"

    assert solution_short(1) == "1"
    assert solution_short(2) == "122"
    assert solution_short(3) == "122333"
    assert solution_short(4) == "1223334444"
