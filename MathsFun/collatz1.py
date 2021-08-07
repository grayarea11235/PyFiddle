"""Simple recursive implementation of the collatz conjecture."""
import csv


def collatz(n, res):
    res.append(n)

    if n == 1:
        return

    if (n % 2) == 0:  # Even
        collatz(n // 2, res)
    else:             # Odd
        collatz(3*n + 1, res)


def main():
    with open('output.csv', 'w', newline='\n')as csvfile:  
        csvwriter = csv.writer(csvfile, delimiter=',',
                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        res = []

        for number in range(1, 1000):
            collatz(number, res)
            print(res)
            csvwriter.writerow(res)
            res = []


if __name__ == '__main__':
    main()
