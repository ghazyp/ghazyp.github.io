import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

data = {
    'Province': ['Aceh', 'North Sumatra', 'West Sumatra', 'Riau', 'Jambi', 'South Sumatra', 'Bengkulu', 'Lampung', 'Bangka Belitung Islands', 'Riau Islands', 'Banten', 'Jakarta', 'West Java', 'Central Java', 'Yogyakarta', 'East Java', 'West Kalimantan', 'Central Kalimantan', 'South Kalimantan', 'East Kalimantan', 'North Kalimantan', 'Bali', 'West Nusa Tenggara', 'East Nusa Tenggara', 'North Sulawesi', 'Gorontalo', 'Central Sulawesi', 'Southeast Sulawesi', 'West Sulawesi', 'South Sulawesi', 'Maluku', 'North Maluku', 'Papua', 'West Papua', 'Southwest Papua', 'Central Papua', 'Highland Papua', 'South Papua', 'Overseas'],
    'Anies Baswedan': [2369534, 2339620, 1744042, 1400093, 532605, 997299, 229681, 791892, 204348, 370671, 2451383, 2653762, 9099674, 2866373, 496280, 4492652, 718641, 256811, 849948, 448046, 72065, 99233, 850539, 153446, 119103, 227354, 386743, 361585, 223153, 2003081, 228557, 200459, 67592, 37459, 48405, 128577, 284184, 41906, 125110],
    'Prabowo Subianto': [787024, 4660408, 1217314, 1931113, 1438952, 3649651, 893499, 3554310, 529883, 641388, 4035052, 2692011, 16805854, 12096454, 1269265, 16716603, 1964183, 1097070, 1407684, 1542346, 284209, 1454640, 2154843, 1798753, 1229069, 504662, 1251313, 1113344, 533757, 3010726, 665371, 454943, 378908, 172965, 209403, 638616, 838382, 162852, 427871],
    'Ganjar Pranowo': [64677, 999528, 124044, 357298, 234251, 606681, 145570, 764486, 151109, 140733, 720275, 1115138, 2820995, 7827335, 741220, 4434805, 534450, 158788, 159950, 240143, 51451, 1127134, 241106, 958505, 283796, 41508, 160594, 90727, 62514, 265948, 186395, 91293, 178534, 120565, 99899, 335089, 175956, 110003, 118385]
}

# Summarize the total votes for each candidate
total_votes = {
    'Anies Baswedan': sum(data['Anies Baswedan']),
    'Prabowo Subianto': sum(data['Prabowo Subianto']),
    'Ganjar Pranowo': sum(data['Ganjar Pranowo'])
}

# Create the pie chart
fig_pie = px.pie(names=total_votes.keys(), values=total_votes.values(), title='2024 Indonesian Election Results by Candidate')

# Create the bar chart
fig_bar = px.bar(data, x='Province', y=['Anies Baswedan', 'Prabowo Subianto', 'Ganjar Pranowo'], title='Votes by Province and Candidate', barmode='group')

# Create a subplot layout with a pie chart and a bar chart
fig = make_subplots(rows=1, cols=2, specs=[[{'type': 'domain'}, {'type': 'xy'}]], subplot_titles=('Pie Chart', 'Bar Chart'))

# Add the pie chart to the first subplot
fig.add_trace(fig_pie.data[0], row=1, col=1)

# Add the bar chart to the second subplot
for trace in fig_bar.data:
    fig.add_trace(trace, row=1, col=2)

# Update layout
fig.update_layout(title_text='2024 Indonesian Election Results')

# Show the combined plot
fig.show()
