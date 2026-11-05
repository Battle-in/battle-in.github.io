# Учебные материалы: базы данных и смежные темы

Набор самостоятельных HTML-страниц с заданиями для студентов. Материалы не требуют сборки: достаточно браузера. SQL-практики рассчитаны на **SQLite** (DB Browser for SQLite, `sqlite3` в терминале или любая SQL-песочница).

## Быстрый старт

1. Клонируйте или скачайте репозиторий.
2. Откройте нужный файл двойным щелчком или из терминала:

   ```bash
   open sql_where_distinct.html   # macOS
   ```

3. Для SQL-работ выполняйте запросы в SQLite, опираясь на скрипты создания таблиц на странице.

## Материалы

| Файл | Тема | Формат |
|------|------|--------|
| [hr_platform_sql.html](./hr_platform_sql.html) | Проектирование БД по ТЗ («Кадровый хаб», связи 1:1, N:1, N:M) | Задача на ER/схему |
| [sql_check.html](./sql_check.html) | Ограничение `CHECK` — примеры (SQLite) | Краткая шпаргалка |
| [sql_where_distinct.html](./sql_where_distinct.html) | `WHERE`, `DISTINCT`, `BETWEEN`, `IN`, `LIKE` | Практика с решениями |
| [sql_group_by.html](./sql_group_by.html) | `GROUP BY`, агрегаты, `HAVING` | Практика с решениями |
| [sql_sets_subqueries.html](./sql_sets_subqueries.html) | `UNION`, `INTERSECT`, `EXCEPT`, подзапросы, `EXISTS`, `IN`, MAX/MIN (SQLite) | Практика с решениями |
| [sql_capstone.html](./sql_capstone.html) | Итог: SkillPoint — проектирование БД, индексы, 21 бизнес-отчёт (SQLite) | Самостоятельная работа |
| [pizza.html](./pizza.html) | Декомпозиция и сложная бизнес-логика (калькулятор доставки) | Задача на программирование |
| [python_map.html](./python_map.html) | Функция `map`: синтаксис, варианты, итератор | Справка + мини-задания |
| [oop-practice.html](./oop-practice.html) | ООП в Python: классы, методы, задания | Теория + практика |

## Рекомендуемый порядок по SQL

1. **Фильтрация и выборка** — [sql_where_distinct.html](./sql_where_distinct.html): условия, уникальные значения, диапазоны и шаблоны.
2. **Группировка** — [sql_group_by.html](./sql_group_by.html): агрегатные функции и фильтрация групп.
3. **Множества и подзапросы** — [sql_sets_subqueries.html](./sql_sets_subqueries.html): объединение результатов и вложенные SELECT.
4. **Ограничения в таблице** — [sql_check.html](./sql_check.html): правила `CHECK` (диапазоны, списки значений, связь полей) — удобно перед проектированием схемы.
5. **Проектирование (ТЗ)** — [hr_platform_sql.html](./hr_platform_sql.html): схема БД по техническому заданию на сервис «Кадровый хаб».
6. **Итоговая интеграция** — [sql_capstone.html](./sql_capstone.html): SkillPoint — своя модель, индексы и бизнес-отчёты по заявкам отделов.

Порядок можно менять: страницы по `WHERE`, `GROUP BY` и подзапросам дают готовые данные для SQL; [sql_check.html](./sql_check.html) — короткая справка; capstone — без готовой схемы.

## Что внутри SQL-практик

| Тип | Файлы | Содержание |
|-----|--------|------------|
| Справка | [sql_check.html](./sql_check.html) | `CHECK`: примеры ограничений, мини-задание |
| Практика с решениями | `sql_where_distinct`, `sql_group_by`, `sql_sets_subqueries` | теория, задания, кнопки «Показать решение» |
| Проектирование | [hr_platform_sql.html](./hr_platform_sql.html) | ТЗ без готовой ER-модели |
| Итоговый проект | [sql_capstone.html](./sql_capstone.html) | предметная область SkillPoint, этапы проектирования, заявки R01–R21 |

## Прочие задания

- **Пицца** — тренировка чтения требований, порядка применения правил, валидации и структуры кода без привязки к конкретной СУБД.
- **map** — [python_map.html](./python_map.html): применение функции к элементам последовательности, lambda, несколько iterable, сравнение с comprehension.
- **ООП** — [oop-practice.html](./oop-practice.html): классы пишутся в `.py` или Jupyter; на странице — теория, критерии проверки и задания.

## Инструменты

| Задача | Инструмент |
|--------|------------|
| SQL | [DB Browser for SQLite](https://sqlitebrowser.org/) или `sqlite3` |
| ООП | Python 3, редактор или Jupyter |
| Просмотр материалов | Любой современный браузер |

## Структура репозитория

```
database_tasks/
├── README.md
├── hr_platform_sql.html
├── sql_check.html
├── sql_where_distinct.html
├── sql_group_by.html
├── sql_sets_subqueries.html
├── sql_capstone.html
├── pizza.html
├── python_map.html
└── oop-practice.html
```

## Обратная связь

Замечания по формулировкам заданий и опечатки удобно править через issue или pull request в репозитории курса.
