# Mini-Turtle (POO) – Ejercicio 2

Este paquete implementa la versión orientada a objetos de la práctica "Evolución de Mini-Turtle". Se elimina por completo el uso de variables globales, encapsulando el estado en instancias de la clase `Tortuga`.

## Objetivo
Refactorizar la versión funcional a una arquitectura basada en clases que garantice encapsulamiento e independencia de objetos.

## Estructura
```
mini_turtle_oo_task/
├── mini_turtle_oo/
│   ├── __init__.py        # Exporta la clase Tortuga
│   └── turtle_class.py    # Define la clase Tortuga
├── main.py                # Script de prueba con objetos
└── README.md              # Documentación
```

## Uso
Importa la clase desde el paquete y crea múltiples instancias independientes:

```python
from mini_turtle_oo import Tortuga

# Cada instancia mantiene su propio estado
t1 = Tortuga()
t2 = Tortuga()

# Movimientos independientes
t1.adelante(10)
 t1.abajo(3)

 t2.adelante(5)
 t2.adelante(2)
 t2.abajo(1)

print(t1.obtener_posicion())  # 7.0
print(t2.obtener_posicion())  # 6.0
```

Para ejecutar el demo incluido:

```bash
python mini_turtle_oo_task/main.py
```

## Encapsulamiento e Independencia
- Encapsulamiento: el estado `posicion_x` es un atributo de instancia (`self.posicion_x`) inicializado en `__init__`. Nunca se usan variables globales.
- Independencia: cada `Tortuga()` crea su propio espacio de memoria para `posicion_x`, por lo que las operaciones en una instancia no afectan a las demás.

## Imagenes 
<img width="1450" height="368" alt="image" src="https://github.com/user-attachments/assets/a80a478f-6e9e-4886-9d7b-751248dd807c" />

