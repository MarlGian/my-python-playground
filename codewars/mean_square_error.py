def solution(array_a, array_b):
    result = 0
    length = len(array_b)
    for i in range(len(array_a)):
        ls = array_a[i] - array_b[i]
        result += ls * ls
        print(result)


    return result / length


print(solution([10, 20, 10, 2], [10, 25, 5, -2] ))
