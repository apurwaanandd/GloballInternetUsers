ndas as pd
import plotly.express as px

# ✅ Load the dataset from your Desktop
file_path = "/Users/apurwaanand/Desktop/Global Internet users.csv"
df = pd.read_csv(file_path)

# ✅ Rename columns for easier use
df.rename(columns={
    'Entity': 'Country',
    'Internet Users(%)': 'Internet Penetration Rate'
}, inplace=True)

# ✅ Drop missing values from key columns
df.dropna(subset=['Country', 'Internet Penetration Rate', 'Year'], inplace=True)

# ✅ Convert Year column to integer (if not already)
df['Year'] = df['Year'].astype(int)

# ✅ Create interactive choropleth map with time animation
fig = px.choropleth(
    df,
    locations='Country',
    locationmode='country names',
    color='Internet Penetration Rate',
    hover_name='Country',
    hover_data={
        'Year': True,
        'Cellular Subscription': True,
        'No. of Internet Users': True,
        'Broadband Subscription': True
    },
    animation_frame='Year',
    color_continuous_scale='YlGnBu',
    range_color=(0, 100),
    title='🌍 Global Internet Penetration (1980–2020)'
)

# ✅ Display the map
fig.show()
