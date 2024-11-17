import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go

# Data from the table
data = {
    'County': ['Bristol', 'Kent', 'Newport', 'Providence', 'Washington'],
    'Total votes cast': [28415, 93093, 46148, 272667, 76060],
    'Joe Biden Democratic': [18050, 49113, 29486, 165012, 44549],
    'Donald Trump Republican': [9745, 42001, 15722, 102551, 29818],
    'Others': [620, 1979, 940, 5104, 1693]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Create a subplot figure with 'domain' type for pie charts
fig = make_subplots(rows=1, cols=len(df), subplot_titles=df['County'], specs=[[{'type': 'domain'}] * len(df)])

# Loop through each county and add a pie chart to the subplot
for index, row in df.iterrows():
    county_data = {
        'Candidate': ['Joe Biden Democratic', 'Donald Trump Republican', 'Others'],
        'Votes': [row['Joe Biden Democratic'], row['Donald Trump Republican'], row['Others']]
    }
    county_df = pd.DataFrame(county_data)
    
    pie_chart = px.pie(county_df, values='Votes', names='Candidate')
    
    # Add the pie chart to the subplot
    fig.add_trace(pie_chart.data[0], row=1, col=index+1)

# Update layout
fig.update_layout(title_text="2020 RI County Votes Distribution", showlegend=False)

# Show the figure
fig.show()
