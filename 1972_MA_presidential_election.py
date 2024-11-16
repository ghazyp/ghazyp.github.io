import matplotlib.pyplot as plt
import pandas as pd

# 1972 presidential election in MA

# DataFrame structure
data = {
    'County': ['Barnstable', 'Berkshire', 'Bristol', 'Dukes', 'Essex', 'Franklin', 'Hampden', 'Hampshire', 'Middlesex', 'Nantucket', 'Norfolk', 'Plymouth', 'Suffolk', 'Worcester'],
    'Democratic': [22336, 35391, 103163, 2001, 157324, 11968, 94945, 28572, 345343, 952, 150732, 69124, 166250, 144139],
    'Republican': [36340, 30380, 84390, 2312, 138040, 16088, 86164, 24529, 269064, 1418, 134459, 76062, 85272, 127560],
    'Other': [466, 513, 1215, 23, 1719, 202, 1024, 553, 3244, 10, 1558, 878, 1299, 1428]
}

df = pd.DataFrame(data)

# Creating the bar graph
fig, ax = plt.subplots(figsize=(14, 8))
bar_width = 0.3

# Set position of bar on X axis
r1 = range(len(df))
r2 = [x + bar_width for x in r1]
r3 = [x + bar_width for x in r2]

# Make the plot
ax.bar(r1, df['Democratic'], color='b', width=bar_width, edgecolor='grey', label='Democratic')
ax.bar(r2, df['Republican'], color='r', width=bar_width, edgecolor='grey', label='Republican')
ax.bar(r3, df['Other'], color='g', width=bar_width, edgecolor='grey', label='Other')

# Add xticks on the middle of the group bars
ax.set_xlabel('County', fontweight='bold', fontsize=15)
ax.set_ylabel('Votes', fontweight='bold', fontsize=15)
ax.set_title('1972 Massachusetts Election Results by County', fontweight='bold', fontsize=16)
ax.set_xticks([r + bar_width for r in range(len(df))])
ax.set_xticklabels(df['County'], rotation=45, ha='right')

# Create legend & Show graphic
plt.legend()
plt.tight_layout()
plt.show()
