if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    values = range(x)

    coords = [[a, b, c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a + b + c != n]

    filtered_coords = [coord for coord in coords if sum(coord) != n]

    print(filtered_coords)
