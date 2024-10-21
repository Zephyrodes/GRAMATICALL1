# GRAMATICALL1

Este proyecto implementa el cálculo de los conjuntos **FIRST**, **FOLLOW**, **PREDICT** y transforma gramáticas a **LL(1)** en Python. Es útil para el análisis sintáctico en compiladores y otras aplicaciones que requieren procesamiento de lenguajes formales.

## Tabla de Contenidos

- [Características](#características)
- [Instalación](#instalación)
- [Uso](#uso)
- [Ejemplo de Gramática](#ejemplo-de-gramática)

## Características

- Cálculo de conjuntos FIRST.
- Cálculo de conjuntos FOLLOW.
- Cálculo de conjuntos PREDICT.
- Eliminación de recursión izquierda.
- Factorización de producciones.
- Visualización de los resultados en la terminal.

## Instalación

1. Asegúrate de tener Python 3 instalado en tu sistema. Puedes verificarlo ejecutando:

   ```bash
   python3 --version
   ```
   
## Uso

Para utilizar el script que analiza y transforma gramáticas a LL(1), sigue estos pasos:

1. **Definir la Gramática**:
   Abre el archivo `gll1.py` y localiza la sección donde se define la gramática. Deberías ver algo como esto:

   ```python
   productions = {
       'S': ['Sa', 'b'],
       'A': ['ε', 'a'],
       'B': ['b']
   }
   ```

2. **Ejecutar el Script:**
 Abre un terminal y navega hasta el directorio donde se encuentra ll1.py. Luego ejecuta el siguiente comando:

```bash
python3 ll1.py
```

3. **Visualizar Resultados:**
Después de ejecutar el script, se mostrarán los conjuntos FIRST, FOLLOW, PREDICT y las producciones transformadas en la terminal. Por ejemplo:

```yaml
Producciones transformadas:
S -> [b, aS']
S' -> [aS', ε]

FIRST sets:
FIRST(S) = {b, a}
FIRST(A) = {ε, a}
FIRST(B) = {b}

FOLLOW sets:
FOLLOW(S) = {$}
FOLLOW(A) = {b}
FOLLOW(B) = {a}

PREDICT sets:
PREDICT(S) = {b, a}
```

## Ejemplo de Gramática

En el archivo `ll1.py`, puedes modificar el diccionario `productions` para probar diferentes gramáticas. Por ejemplo:

```python
productions = {
    'S': ['Sa', 'b'],
    'A': ['ε', 'a'],
    'B': ['b']
}
