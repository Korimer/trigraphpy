import matplotlib.pyplot as plt

CSVFILE = "raw.csv"
DELIM = ","

with open(CSVFILE,"r") as f:
    headinglist = (f.readline().strip().split(DELIM))
    cols = len(headinglist)
    data = [[] for _ in range(len(headinglist))]
    for line in f:
        points = [float(i) for i in line.strip().split(DELIM)]
        for i in range(cols):
            data[i].append(points[i])

fig, ax = plt.subplots()

x_indexes = list(range(cols))

ax.bar(x_indexes,[sum(i) for i in data])
ax.bar([i+.5 for i in x_indexes], [sum(i) for i in data])

ax.plot()

plt.show()