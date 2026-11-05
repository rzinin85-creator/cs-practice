"""Лаба 07: перевод между CSV, JSON и учебным YAML."""

import json


def csv_to_records(text: str) -> list[dict]:
    """CSV с заголовком → список словарей; значения остаются строками."""
    lines = text.splitlines()
    if not lines:
        return []
    header = lines[0].split(",")
    records = []
    for line in lines[1:]:
        if line == "":
            continue
        values = line.split(",")
        records.append(dict(zip(header, values)))
    return records


def parse_settings(lines: list[str]) -> dict:
    """Простой YAML: «ключ: значение», списки через «- », комментарии после #."""
    result: dict = {}
    current_list_key: str | None = None

    for raw in lines:
        # отбрасываем комментарий
        line = raw.split("#", 1)[0].rstrip()
        if line == "":
            continue

        stripped = line.strip()

        # элемент списка
        if stripped.startswith("- "):
            if current_list_key is not None:
                result[current_list_key].append(_convert_scalar(stripped[2:].strip()))
            continue

        # новая пара ключ: значение — сбрасываем режим списка
        if ":" in stripped:
            key, _, value = stripped.partition(":")
            key = key.strip()
            value = value.strip()
            if value == "":
                # открывается список
                result[key] = []
                current_list_key = key
            else:
                result[key] = _convert_scalar(value)
                current_list_key = None

    return result


def _convert_scalar(value: str):
    """Приводит строку к числу/булеву/строке по правилам учебного YAML."""
    low = value.lower()
    if low in ("true", "yes"):
        return True
    if low in ("false", "no"):
        return False
    # целое?
    try:
        return int(value)
    except ValueError:
        pass
    # дробное?
    try:
        return float(value)
    except ValueError:
        pass
    return value


def merge_by_key(rows: list[dict], extra: dict, key: str = "id") -> list[dict]:
    """Дополняет записи сведениями из словаря extra по значению ключа key."""
    merged = []
    for row in rows:
        # копия, чтобы не менять оригинал
        new_row = dict(row)
        row_key = row.get(key)
        if row_key in extra:
            # поля из row важнее: сначала extra, потом row поверх
            new_row = {**extra[row_key], **row}
        merged.append(new_row)
    return merged


def records_to_json(records: list[dict]) -> str:
    """Список словарей → JSON: отступ 2, ключи по алфавиту, кириллица как есть."""
    return json.dumps(records, indent=2, sort_keys=True, ensure_ascii=False)
