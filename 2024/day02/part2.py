def check_levels(levels):
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
            return False

        last_level = level

    return True

with open('input.txt', encoding='ascii') as f:
    reports = f.readlines()

safe_reports = 0
for report in reports:
    lvls = list(map(int, report.split()))

    args = [lvls]
    for i in range(len(lvls)):
        arr = lvls.copy()
        arr.pop(i)
        args.append(arr)

    safe_reports += int(any(map(check_levels, args)))

print(safe_reports)
