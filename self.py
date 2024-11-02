def d(n):
    return n + sum(int(digit) for digit in str(n))

def generate_self_numbers(limit):
    generated = [False] * limit
    for i in range(1, limit):
        dn = d(i)
        if dn < limit:
            generated[dn] = True
    
    self_numbers = [i for i in range(1, limit) if not generated[i]]
    return self_numbers

def main():
    self_numbers = generate_self_numbers(10000)
    with open("self.out", "w") as f:
        for number in self_numbers:
            f.write(f"{number}\n")

if __name__ == "__main__":
    main()
