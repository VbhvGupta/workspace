x = int(input())
x -= 1      # x not included in the range
n = x // 3
m = x // 5
nm = x // 15


sum_n = n * (2 * 3 + (n-1) * 3) // 2
sum_m = m * (2 * 5 + (m-1) * 5) // 2
sum_nm = nm * (2 * 15 + (nm -1) * 15) // 2

sum = sum_n + sum_m - sum_nm
print(sum)
