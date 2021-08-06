import csv


def collatz(n, res):

    res.append(n)
    #print(n)

    if n == 1:
        return

    if (n % 2) == 0: # Even
        collatz(n // 2, res)
    else:
        collatz(3*n + 1, res)


def main():
    with open('output.csv', 'w', newline='')as csvfile:  
        csvwriter = csv.writer(csvfile, delimiter=' ',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        res = list()

        for n in range(1000):
            collatz(n+1, res)
            print(res)
            csvwriter.writerow(res)


if __name__ == '__main__':
    main()
