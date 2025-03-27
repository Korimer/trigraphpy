import matplotlib.pyplot as plt

CSVFILE = "raw.csv"
DELIM = ","
COLWIDTH = .35
BUFFER = 0.07

with open(CSVFILE,"r") as f:
    headinglist = (f.readline().strip().split(DELIM))
    cols = len(headinglist)
    data = [[] for _ in range(len(headinglist))]
    for line in f:
        points = [float(i) for i in line.strip().split(DELIM)]
        for i in range(cols):
            data[i].append(points[i])

fig, ax = plt.subplots()

ax.grid(axis='y',color='#DDDDDD')
ax.set_axisbelow(True)

x_indexes = range(1,len(data[0])+1)
barsets = []

for i in range(cols//2):
    '''for j in range(2):
        offests = [
            (x*2) - (COLWIDTH/2) + (COLWIDTH*j)
            for x in x_indexes
        ]
        print(offests)
        print([i-(COLWIDTH/2) for i in x_indexes])
        print([i+(COLWIDTH/2) for i in x_indexes])
        barsets.append(ax.bar(
            offests,
            data[(i)+j],
            width=COLWIDTH,
        ))'''
    barsets.append(ax.bar(
        [i-(COLWIDTH/2)-(BUFFER/2) for i in x_indexes],
        data[i*2],
        width=COLWIDTH,
        edgecolor="black"
    ))
    barsets.append(ax.bar(
        [i+(COLWIDTH/2)+(BUFFER/2) for i in x_indexes],
        data[(i*2)+1],
        width=COLWIDTH,
        edgecolor="black"
    ))

'''for bars in barsets:
    for bar in bars:
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 0.3,
            round(bar.get_height(), 1),
            horizontalalignment='center',
            color=bar.get_facecolor(),
            weight='bold'
        )'''


ax.set_xticks(
    x_indexes,
    labels=["Sample " + str(i) for i in x_indexes],
    rotation=45
)


ax.legend(
    labels=headinglist,
    loc='upper center',
    bbox_to_anchor=(0.5, 1),
    ncol=cols/2
)

ax.set_title("Comparison of Given and Tested Soil Proportions")
ax.set_ylabel("Relative Proportions")
plt.show()