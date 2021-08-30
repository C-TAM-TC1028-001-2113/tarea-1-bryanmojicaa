def main():
    # escribe tu código abajo de esta línea
    new_game= int(input("Dame la cantidad de juegos nuevos: "))

    used_game= int(input("Dame la cantidad de juegos usados: "))

    total= (new_game * 1000) + (used_game * 350)

    print("El total de la compra es:", total)
    


if __name__ == '__main__':
    main()
