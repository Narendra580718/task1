def odd(n):
    return n % 2 == 1

x = [1,2,3,4,5,10,15]

ans = filter(odd, x)
print(f"Original List: {x}")
print(f"Filtered List: {list(ans)}")        