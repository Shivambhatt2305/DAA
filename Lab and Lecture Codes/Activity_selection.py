def activity_selection(start, end):
    n = len(start)
    activities = list(zip(end, start))  # (end, start)
    activities.sort()  # sort by end time

    selected = []
    last_end = -1

    for e, s in activities:
        if s >= last_end:
            selected.append((s, e))
            last_end = e

    print("Selected activities (start, end):", selected)


start = [5, 6, 0, 4, 10]
end = [8, 10, 5, 7, 12]

activity_selection(start, end)
