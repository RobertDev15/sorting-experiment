import random

# Read the original file
with open("length5c.txt", "r") as f:
    n = int(f.readline())
    a = [int(i) for i in f.readline().split()]

# Choose the transformation you want:
mode = input("Choose mode: sorted / reverse / mostly / none: ").strip().lower()

if mode == "sorted":
    a.sort()

elif mode == "reverse":
    a.sort(reverse=True)

elif mode == "mostly":
    # Start sorted
    a.sort()
    # Introduce a few random swaps (5% of the list)
    swaps = max(1, n // 20)
    for _ in range(swaps):
        i = random.randint(0, n - 1)
        j = random.randint(0, n - 1)
        a[i], a[j] = a[j], a[i]

elif mode == "none":
    pass  # leave the list unchanged

else:
    print("Invalid mode. No changes applied.")

# Write the output in UTF-8 (compatible with your bubble-sort script)
with open("length5c1.txt", "w") as f:
    f.write(str(n) + "\n")
    f.write(" ".join(str(i) for i in a))