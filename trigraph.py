import matplotlib.pyplot as plt

CSVFILE = "raw.csv"
DELIM = ","
COLWIDTH = .35
BUFFER = 0.07

# save headings as an array headings, 
# save values as a 2d array data, where data[i] contains all data in the ith column of the csv
with open(CSVFILE,"r") as f:
    headings = (f.readline().strip().split(DELIM))
    cols = len(headings)
    data = [[] for _ in range(len(headings))]
    for line in f:
        points = [float(i) for i in line.strip().split(DELIM)]
        for i in range(cols):
            data[i].append(points[i])

fig, ax = plt.subplots()

ax.grid(axis='y',color='#DDDDDD')
ax.set_axisbelow(True)

x_indexes = range(1,len(data[0])+1)

# Graph the two bars (each bar composed of 3 sub-bars) per sample.
barsets = []
for i in range(cols//2):
    for barpos in range(2):
        adjustedindex = [
            i-((COLWIDTH+BUFFER)/2)+((COLWIDTH+BUFFER)*barpos)
            for i in x_indexes
        ]

        barsets.append(ax.bar(
            adjustedindex,
            data[(i*2)+barpos],
            width=COLWIDTH,
            edgecolor="black"
        ))

# Labels each pair of bars as the appropriate sample.
ax.set_xticks(
    x_indexes,
    labels=["Sample " + str(i) for i in x_indexes],
    rotation=45
)

# Organizes the legend to pair Given/Tested values.
ax.legend(
    labels=headings,
    loc='upper center',
    bbox_to_anchor=(0.5, 1),
    ncol=cols/2
)

ax.set_title("Comparison of Given and Tested Soil Proportions")
ax.set_ylabel("Relative Proportions")

plt.show()