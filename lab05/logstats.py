def parse_event(line):
    line = line.strip()
    if not line:
        raise ValueError("empty line")
    parts = line.split(" ", 2)
    if len(parts) < 3:
        raise ValueError("not enough parts")
    time, level, message = parts
    if level not in ("DEBUG", "INFO", "WARNING", "ERROR"):
        raise ValueError("bad level")
    return {"time": time, "level": level, "message": message}


def count_levels(lines):
    counts = {}
    for line in lines:
        if not line.strip():
            continue
        try:
            event = parse_event(line)
            level = event["level"]
        except ValueError:
            level = "BROKEN"
        counts[level] = counts.get(level, 0) + 1
    return counts


def top_errors(lines, n):
    errors = {}
    for line in lines:
        if not line.strip():
            continue
        try:
            event = parse_event(line)
        except ValueError:
            continue
        if event["level"] == "ERROR":
            msg = event["message"]
            errors[msg] = errors.get(msg, 0) + 1
    # сортировка: сначала по убыванию количества, потом по алфавиту
    sorted_items = sorted(errors.items(), key=lambda kv: (-kv[1], kv[0]))
    return [[msg, cnt] for msg, cnt in sorted_items[:n]]


def format_report(counts, errors):
    lines = ["Отчёт по журналу", ""]
    for level in sorted(counts):
        lines.append(f"{level}: {counts[level]}")
    lines.append("")
    lines.append("Частые ошибки:")
    for msg, cnt in errors:
        lines.append(f"- {msg} — {cnt}")
    return "\n".join(lines) + "\n"
