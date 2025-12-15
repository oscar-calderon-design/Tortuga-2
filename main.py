from mini_turtle_oo import Tortuga


def mostrar_estado(nombre: str, tortuga: Tortuga) -> None:
    """Imprime en consola la posición X actual de la tortuga indicada."""
    print(f"{nombre} -> posicion_x = {tortuga.obtener_posicion()}")


def main() -> None:
    # Crear dos instancias que mantienen su propio estado encapsulado
    t1 = Tortuga()
    t2 = Tortuga()

    # Mover cada tortuga distancias diferentes
    t1.adelante(10)
    t1.abajo(8)

    t2.adelante(8)
    t2.adelante(5)
    t2.abajo(1)

    print("Estados independientes de cada tortuga:")
    mostrar_estado("t1", t1)
    mostrar_estado("t2", t2)

    # Reiniciar sólo la primera y comprobar que no afecta a la segunda
    t1.reiniciar()
    print("\nTras reiniciar t1:")
    mostrar_estado("t1", t1)
    mostrar_estado("t2", t2)


if __name__ == "__main__":
    main()