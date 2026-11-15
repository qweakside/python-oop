from mushrooms import MushroomsCollector
def test_different_baskets():
    first=MushroomsCollector()
    second = MushroomsCollector()
    first.add_mushroom("Лисичка")
    assert first.mushrooms== ['Лисичка']
    assert second.mushrooms == []
def test_poisonous():
    first=MushroomsCollector()
    second = MushroomsCollector()
    first.add_mushroom("Поганка")
    second.add_mushroom("Мухомор")
    assert first.mushrooms==[]
    assert second.mushrooms==[]
def test_string():
    first=MushroomsCollector()
    first.add_mushroom("Поганка")
    first.add_mushroom("Лисичка")
    first.add_mushroom("Опенок")
    assert str(first)=="Лисичка, Опенок"
def test_empty():
    first=MushroomsCollector()
    assert str(first)==''
