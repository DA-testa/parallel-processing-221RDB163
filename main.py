# python3

def parallel_processing(n, m, data):
    output = []

    threadings = [0] * n

    for i in range(m):
        smales_value = min( threadings )
        index = threadings.index( smales_value )

        output.append( [index, smales_value] )

        threadings[index] += data[i]

    return output

def main():
    first_line = input().split(" ")
    n = first_line[0]
    m = first_line[1]

    data = input().split()

    result = parallel_processing(int(n), int(m), list(map(int, data)))

    for i, j in result:
        print(i, j)

if __name__ == "__main__":
    main()