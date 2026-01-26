# 42_Python_Module_07
42_Python_Module_07

## DataDeck: Master the Art of Abstract Card Architecture

¡Bienvenido a DataDeck! Este proyecto consiste en diseñar el motor de un juego de cartas coleccionables (estilo Magic o Pokémon) utilizando patrones avanzados de Programación Orientada a Objetos (POO) en Python. El objetivo principal es dominar las clases abstractas, interfaces y la herencia múltiple para crear un sistema modular y extensible.

### Ficha Técnica

- **Lenguaje:** Python 3.10+
- **Nivel de Dificultad:** 7.5/10
- **¿Por qué?** Aunque la lógica del juego debe ser simple, requiere un dominio sólido de la arquitectura de software, manejo de abc (Abstract Base Classes) y una estructura de importaciones absoluta muy estricta.
- **Enfoque:** Arquitectura, Polimorfismo y Composición de Interfaces.

### Normas a Cumplir (Obligatorio)

Para que el proyecto sea válido, debes seguir estas reglas a rajatabla:

- **Código Limpio:** Cumplir estrictamente con el estándar de codificación flake8.
- **Tipado:** Uso obligatorio de type hints en todas las firmas de funciones y métodos.
- **Importaciones:** Utilizar exclusivamente importaciones absolutas (ej: `from ex0.Card import Card`). Las relativas están prohibidas.
- **Memoria:** No se permite el uso de archivos (I/O). Todo el procesamiento debe ser en memoria.
- **Prohibidos:** Nada de librerías externas (pip), ni funciones peligrosas como `eval()` o `exec()`.
- **Estructura:** El archivo `__init__.py` en la raíz es MANDATORIO para que Python reconozca los paquetes.

### Estructura del Proyecto

El sistema se construye por capas progresivas:

| Capa       | Ejercicio | Concepto Clave                       | Archivos Principales                          |
|------------|-----------|--------------------------------------|-----------------------------------------------|
| Foundation | ex0       | Abstract Base Classes (ABC)          | Card.py, CreatureCard.py                      |
| Implementation | ex1   | Polimorfismo y Gestión de Decks     | SpellCard.py, ArtifactCard.py, Deck.py       |
| Ability    | ex2       | Interfaces y Herencia Múltiple      | Combatable.py, Magical.py, EliteCard.py      |
| Engine     | ex3       | Patrones Strategy y Factory          | CardFactory.py, GameEngine.py                 |
| Platform   | ex4       | Composición Avanzada                | TournamentPlatform.py, Rankable.py            |

### Cómo ejecutar

Todos los ejercicios deben ejecutarse desde la raíz del repositorio usando el parámetro `-m`:

```bash
# Ejemplo para ejecutar el Ejercicio 0
python3 -m ex0.main
```
(Repite cambiando `ex0` por el número del ejercicio correspondiente).

### Reflexión para la Defensa

Durante la evaluación, prepárate para explicar:

- ¿Por qué usar una clase abstracta en lugar de una clase normal para Card?
- ¿Cómo ayuda el polimorfismo a que la clase Deck maneje distintos tipos de cartas sin saber qué son?
- ¿Qué ventajas tiene separar las habilidades en interfaces como Combatable y Magical?

**Nota del Arquitecto:** No te compliques con reglas de juego complejas. El evaluador busca ver patrones de diseño limpios, no el próximo juego del año.
