def is_divisible_by_11(n):
    even_sum = 0
    odd_sum = 0
    is_even = True

    while n > 0:
        digit = n % 10
        if is_even:
            even_sum += digit
        else:
            odd_sum += digit
        is_even = not is_even
        n //= 10

    return (even_sum - odd_sum) % 11 == 0

N = int(input())  # N ni o'zgartiring

result = is_divisible_by_11(N)

if result:
    print("Yes")
else:
    print("No")
