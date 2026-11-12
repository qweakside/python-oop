# python-oop

[![tests](https://github.com/qweakside/python-oop/actions/workflows/tests.yml/badge.svg)](https://github.com/qweakside/python-oop/actions/workflows/tests.yml)

Учебный репозиторий: прохожу ООП на Python и складываю сюда каждый урок
как отдельную папку с кодом, тестами и конспектом.

Курс: Яндекс Практикум, «Python-разработчик».

## Как устроено

```
python-oop/
├── topics/                    # по папке на урок
│   └── 01_classes_and_objects/
│       ├── mushrooms.py       # код урока
│       ├── test_mushrooms.py  # тесты
│       └── notes.md           # конспект своими словами
├── journal.md                 # дневник: что сделал, где застрял
├── requirements.txt
└── .gitignore
```

## Прогресс

| № | Тема | Код | Тесты | Конспект |
|---|------|:---:|:-----:|:--------:|
| 01 | Объекты и классы | ✅ | ✅ | ✅ |
| 02 | Наследование | ⬜ | ⬜ | ⬜ |

## Запуск

```bash
# активировать окружение (Windows / PowerShell)
.venv\Scripts\Activate.ps1

# установить зависимости
pip install -r requirements.txt

# запустить тесты урока
cd topics/01_classes_and_objects
python -m pytest -v
```

## Правила работы

1. Один урок = одна папка = один коммит (или несколько мелких).
2. В каждом уроке есть `notes.md`: что понял, где ошибся, что осталось.
3. Любой код урока покрывается хотя бы одним тестом.
4. В `main` не попадает сломанный код: сначала тесты, потом merge.
