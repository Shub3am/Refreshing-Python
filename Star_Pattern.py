times = int(input("How Many Times"))

for i in range(0, times+1):
    x = int((times) / (i+1))
    print(f"{' ' * x}{'*' * i}")


for i in range(0, 6):
    if (i == 0 or i == 5):
        print(f"{'*' * 6}")
    else:
        print(f"*{' ' * 4}*")
