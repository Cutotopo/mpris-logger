import json

try:
    file = open("history.json", "r")
    data = json.loads(file.read())
    file.close()
    sorteddata = dict(sorted(data.items(), key=lambda item: item[1], reverse=True))

    print("===> Your 5 most played tracks:")
    for i, n in enumerate(sorteddata):
        if i < 5:
            print(f"{i + 1}. {n.replace(':::::', 'by')} ({data[n]} times)")
        else:
            break
    print("\n===> Your 5 most played artists:")
    artists = []
    write = 0
    for i, n in enumerate(sorteddata):
        if len(artists) < 5:
            if (n.split(" ::::: ")[1]) not in artists:
                artists.append(n.split(" ::::: ")[1])
        else:
            break
    for i, e in enumerate(artists):
        print(f"{i + 1}. {e}")
except FileNotFoundError:
    print("Run logger.py first!")
    exit(1)
