"""Урок 7. Объекты и классы: корзина грибника.

Правила:
- у каждой корзины (объекта) свой список грибов;
- ядовитые грибы добавлять нельзя.
"""

POISONOUS_MUSHROOMS = frozenset({"Мухомор", "Поганка"})


class MushroomsCollector:
    """Корзина грибника."""

    def __init__(self) -> None:
        # ВАЖНО: список создаётся внутри __init__, то есть у каждого объекта свой.
        # Если объявить его в теле класса, он будет один на все объекты.
        self.mushrooms: list[str] = []

    def is_poisonous(self, mushroom_name: str) -> bool:
        """Вернуть True, если гриб ядовит."""
        return mushroom_name in POISONOUS_MUSHROOMS

    def add_mushroom(self, mushroom_name: str) -> None:
        """Добавить гриб в корзину. Ядовитый гриб не добавляется."""
        if self.is_poisonous(mushroom_name):
            print("Нельзя добавить ядовитый гриб")
            return
        self.mushrooms.append(mushroom_name)

    def __str__(self) -> str:
        """Грибы через запятую: 'Подберёзовик, Лисичка'."""
        return ", ".join(self.mushrooms)


if __name__ == "__main__":
    basket = MushroomsCollector()
    basket.add_mushroom("Подберёзовик")
    basket.add_mushroom("Мухомор")
    basket.add_mushroom("Лисичка")

    second_basket = MushroomsCollector()
    second_basket.add_mushroom("Белый гриб")

    print("Корзина 1:", basket)
    print("Корзина 2:", second_basket)
