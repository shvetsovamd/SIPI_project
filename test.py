n = int(input())
fn = [0 for i in range(n + 1 + (n == 0))]
fn[1] = 1

for i in range(2, n + 1):
    fn[i] = fn[i - 1] + fn[i - 2]
print(fn[-1] % 10)