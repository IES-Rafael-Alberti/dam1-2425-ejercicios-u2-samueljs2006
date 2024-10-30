def todos_años_cumplido(edad):
    for i in range(0 ,edad +1):
        print(i)




def main():
    edad = int(input("Introduce tu edad: "))
    todos_años_cumplido(edad)




if __name__ == "__main__":
    main()