# hollow pyramid number pattern
n = 5
for i in range(n):
    # printing spaces
    for j in range(n - i - 1):
        print(' ', end='')

    # printing number
    count = 1
    for k in range(2 * i + 1):
        # print number at start and end of the row
        if k == 0 or k == 2 * i:
            print(count, end='')
            count += 1
        else:
            if i == n - 1:
                print(count, end='')
                count += 1
            else:
                print(' ', end='')
    print()