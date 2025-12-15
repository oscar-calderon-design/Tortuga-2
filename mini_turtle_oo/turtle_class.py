# mini_turtle_oo/turtle_class.py
#
# Implementación orientada a objetos (POO) para la mini-tortuga.
# La clase Tortuga encapsula completamente su estado interno y expone
# una interfaz simple para desplazarse a lo largo del eje X.

class Tortuga:
    """
    Clase que modela una tortuga que se desplaza sobre el eje X.

    Encapsula su estado mediante el atributo de instancia `posicion_x`,
    evitando cualquier uso de variables globales.
    """

    def __init__(self) -> None:
        """
        Inicializa una nueva tortuga con `posicion_x = 0`.

        Este constructor garantiza que cada objeto mantenga su propio
        estado independiente del resto de instancias.
        """
        self.posicion_x: float = 0.0

    def adelante(self, distancia: float) -> float:
        """
        Avanza la tortuga hacia la derecha (incrementa `posicion_x`).

        Parámetros:
        - distancia: magnitud no negativa del desplazamiento.

        Retorna:
        - La nueva posición en X tras el movimiento.
        """
        if distancia < 0:
            raise ValueError("La distancia debe ser no negativa")
        self.posicion_x += float(distancia)
        return self.posicion_x

    def abajo(self, distancia: float) -> float:
        """
        Desplaza la tortuga hacia la izquierda (decrementa `posicion_x`).

        Parámetros:
        - distancia: magnitud no negativa del desplazamiento.

        Retorna:
        - La nueva posición en X tras el movimiento.
        """
        if distancia < 0:
            raise ValueError("La distancia debe ser no negativa")
        self.posicion_x -= float(distancia)
        return self.posicion_x

    def reiniciar(self) -> float:
        """
        Reinicia la posición de la tortuga estableciendo `posicion_x = 0`.

        Retorna:
        - La posición en X tras el reinicio (siempre 0).
        """
        self.posicion_x = 0.0
        return self.posicion_x

    def obtener_posicion(self) -> float:
        """
        Devuelve la posición actual en X de la tortuga.
        """
        return self.posicion_x