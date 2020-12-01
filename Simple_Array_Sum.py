def simpleArraySum(ar):
    answer = sum(ar)
    return answer

if __name__ == '__main__':
    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)
    print(result)