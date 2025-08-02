def avg(*args):
    return sum(args) / len(args)

if __name__ == "__main__":
    nums = list(map(int, input().split()))
    res = avg(*nums)
    print("{:.2f}".format(res))
