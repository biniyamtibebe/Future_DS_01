# Social Media Sentiment Analysis Project
----


## Overview 

This project performs sentiment analysis on the Social Media Sentiments Analysis Dataset, which captures user-generated content across social media platforms like Twitter, Instagram, and Facebook. The dataset comprises text, sentiment labels, timestamps, user details, platforms, hashtags, engagement metrics (likes and retweets), and geographical data. The goal is to analyze sentiments, identify trends, and visualize insights using Python.

----

## Dataset Description

The dataset (sentimentsdataset.csv) contains user posts with the following key features:

    - ✅ Text: User-generated content.
    
    - ✅ Sentiment: Categorized emotions (e.g., Positive, Negative, Neutral, Joy).
    
    - ✅ Timestamp: Date and time of the post.
    
    - ✅ User: Unique user identifiers.
    
    - ✅ Platform: Social media platform (e.g., Twitter, Instagram, Facebook).
    
    - ✅ Hashtags: Tags indicating trending topics.
    
    - ✅ Likes/Retweets: Engagement metrics.
    
    - ✅ Country: Geographical origin of posts.
    
    - ✅ Year/Month/Day/Hour: Extracted timestamp components.
    


The dataset is publicly available under the CC0: Public Domain license and is used for sentiment analysis, temporal trends, platform comparisons, and geographical insights.

----

## Project Objectives

  - ✅ Perform sentiment analysis to validate or refine sentiment labels using NLP techniques.
  - ✅ Conduct temporal analysis to identify trends over time.
  - ✅ Analyze user engagement through likes and retweets.
  - ✅Explore platform-specific sentiment and hashtag trends.
  - ✅ Visualize geographical sentiment distribution.
----

## Prerequisites

To run this project, ensure you have the following installed:

 - python 3.13
   
 - Libraries:
   
    bash
 
    pip install pandas numpy nltk matplotlib seaborn wordcloud
 

- Download the NLTK data:
  
 python 
 
    import nltk
  
    nltk.download('vader_lexicon')
  
    nltk.download('stopwords')
  
    nltk.download('punkt')

    ----
  

    import nltk

     nltk.download('vader_lexicon')

     nltk.download('stopwords')

     nltk.download('punkt')

- The dataset file: df = pd.read_csv(r'C:\Users\hp\Downloads\archive (1)\sentimentdataset.csv', encoding='latin-1')----

## Project Structure 

plain

   sentiment-analysis/

  ├── data/

   │   └── sentimentsdataset.csv

   ├── src/

  │   └── sentiment_analysis.py

   ├── README.md

   ├── requirements.txt

   └── output/

    ├── sentiment_distribution.png
    
    ├── temporal_trends.png
    
    ├── platform_sentiment.png
    
    ├── hashtag_wordcloud.png
    
----

  - ✅ data/: Contains the dataset file.
  
  - ✅ src/: Python script for analysis and visualization.
  
  - ✅ output/: Stores generated visualizations.
  
  - ✅ requirements.txt: Lists required Python libraries.
  
  - ✅ README.md: This file. 
----

## Setup Instructions

----

### 1. Clone the Repository:

  git clone <repository-url>

  cd sentiment-analysis

----
### 2. Install Dependencies:

    pip install -r requirements.txt

----
### 3. Place the Dataset:

    Ensure sentimentsdataset.csv is in the data/ directory.

----

### 4. Run the Analysis:

    python src/sentiment_analysis.py

----

## Analysis Steps


### The Python script (sentiment_analysis.py) performs the following:

### 1. Data Loading:


  Load the sentiments dataset.csv using pandas.

  Clean data by removing duplicates, handling missing values, and standardizing text (e.g., lowercasing Sentiment, Platform).

### 2.Sentiment Analysis:

   Use NLTK’s VADER (Valence Aware Dictionary and sEntiment Reasoner) to compute sentiment scores for the Text column.

  Compare VADER scores with the dataset’s Sentiment labels to validate or refine classifications.

  Group sentiments into broader categories (e.g., Positive, Negative, Neutral).


### 3.Temporal Analysis:

   Aggregate posts by Year, Month, or Date to identify trends.

  Calculate average engagement (Likes + Retweets) over time.

### 4. Platform-Specific Analysis:

  Compare sentiment distribution across platforms (Twitter, Instagram, Facebook).

   Compute the average number of Likes and Retweets per platform.

### 5.Hashtag Trends:

   Extract and count unique hashtags.

   Generate a word cloud of top hashtags.

### 6.Geographical Analysis:

   Group posts by Country to analyze sentiment distribution.

  Visualize engagement metrics by country.


### 7.Visualization:

 - Create plots using matplotlib and seaborn:

 - Pie chart: Sentiment distribution.

 -Line chart: Engagement trends over time.

  -Bar chart: Sentiment by platform.

  -Word







