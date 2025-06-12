import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
from textblob import TextBlob

# Load your dataset
df = pd.read_csv(r'C:\Users\hp\Downloads\archive (1)\sentimentdataset.csv', encoding='latin-1')

# Function to get sentiment polarity
def get_sentiment(text):
    return TextBlob(text).sentiment.polarity

# Function to categorize sentiment
def categorize_sentiment(polarity):
    if polarity > 0:
        return 'Positive'
    elif polarity < 0:
        return 'Negative'
    else:
        return 'Neutral'
    
# Calculate polarity and categorize
df['Polarity'] = df['Sentiment'].apply(get_sentiment)
df['Sentiment_Category'] = df['Polarity'].apply(categorize_sentiment)

# Create histogram
fig = px.histogram(df, x='Sentiment_Category', title='Sentiment Distribution')

# Create Dash app
app = dash.Dash(__name__)
app.layout = html.Div([
    html.H1("Sentiment Analysis Dashboard"),
    dcc.Graph(
        id='sentiment-graph',
        figure=fig
    ),
    # You can add more components here
])
if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
    
    
