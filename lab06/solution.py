"""Лаба 06: три маленькие функции о путях и размерах файлов."""


def count_by_extension(paths: list[str]) -> dict[str, int]:
    """Словарь «расширение → сколько файлов». Расширение в нижнем регистре, без точки."""
    result: dict[str, int] = {}
    for path in paths:
        name = path.rsplit("/", 1)[-1]
        if "." in name:
            ext = name.rsplit(".", 1)[-1].lower()
        else:
            ext = ""
        result[ext] = result.get(ext, 0) + 1
    return result


def deepest_path(paths: list[str]) -> str:
    """Путь с наибольшей вложенностью; при равенстве — первый по алфавиту."""
    if not paths:
        return ""
    return min(paths, key=lambda p: (-p.count("/"), p))


def human_size(n_bytes: int) -> str:
    """Размер в удобных единицах: 1536 → «1.5 КБ»."""
    units = ["Б", "КБ", "МБ", "ГБ", "ТБ"]
    size = float(n_bytes)
    for unit in units:
        if size < 1024 or unit == units[-1]:
            if unit == "Б":
                return f"{int(size)} Б"
            return f"{size:.1f} {unit}"
        size /= 1024
    return f"{int(n_bytes)} Б"
