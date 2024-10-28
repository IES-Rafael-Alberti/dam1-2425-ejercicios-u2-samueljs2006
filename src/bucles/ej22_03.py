def num_impares(num):
    impares = [str(i) for i in range(1, num + 1, 2)]
    print(", ".join(impares))

def main():
    num = int(input("Introduce un número positivo: "))
    num_impares(num)

if __name__ == "__main__":
    main()
