with open('input.txt', encoding='ascii') as f:
    reports = f.readlines()

safe_reports = 0
for report in reports:
    levels = list(map(int, report.split()))

    check = True
    order = None
    last_level = None
    for level in levels:
        if last_level is None:
            last_level = level
            continue
        if order is None:
            if level < last_level:
                order = "DESC"
            else:
                order = "ASC"

        if (
            order == "ASC" and level <= last_level
        ) or (
            order == "DESC" and level >= last_level
        ) or (
            (delta := abs(last_level - level)) < 1 or delta > 3
        ):
            check = False
            break

        last_level = level

    safe_reports += int(check)

print(safe_reports)
