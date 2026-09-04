# Geometric Lib Documentation

## Общее описание решения
Geometric Lib — это библиотека на Python для работы с геометрическими фигурами. 
Она предоставляет базовые функции для вычисления площади и периметра (или длины окружности) таких фигур, как круг, квадрат, прямоугольник и треугольник.

---

## Описание функций с примерами вызова

### 1. Круг (circle.py)
- **`area(r)`**
  Принимает радиус круга `r`, возвращает его площадь.
  Пример вызова:
  `import circle`
  `res = circle.area(5)`

- **`perimeter(r)`**
  Принимает радиус круга `r`, возвращает длину его окружности.
  Пример вызова:
  `import circle`
  `res = circle.perimeter(5)`

### 2. Квадрат (square.py)
- **`area(a)`**
  Принимает сторону квадрата `a`, возвращает его площадь.
  Пример вызова:
  `import square`
  `res = square.area(5)`

- **`perimeter(a)`**
  Принимает сторону квадрата `a`, возвращает его периметр.
  Пример вызова:
  `import square`
  `res = square.perimeter(5)`

### 3. Прямоугольник (rectangle.py)
- **`area(a, b)`**
  Принимает стороны прямоугольника `a` и `b`, возвращает его площадь.
  Пример вызова:
  `import rectangle`
  `res = rectangle.area(3, 5)`

- **`perimeter(a, b)`**
  Принимает стороны прямоугольника `a` и `b`, возвращает его периметр.
  Пример вызова:
  `import rectangle`
  `res = rectangle.perimeter(3, 5)`

### 4. Треугольник (triangle.py)
- **`area(a, h)`**
  Принимает основание `a` и высоту `h`, возвращает площадь треугольника.
  Пример вызова:
  `import triangle`
  `res = triangle.area(3, 4)`

- **`perimeter(a, b, c)`**
  Принимает стороны треугольника `a`, `b` и `c`, возвращает его периметр.
  Пример вызова:
  `import triangle`
  `res = triangle.perimeter(3, 4, 5)`

---

## История изменения проекта

* d08b24f Add triangle.py and fix perimeter in rectangle.py
* 8a12c3e Add rectangle.py
* 8ba9aeb L-03: Circle and square added