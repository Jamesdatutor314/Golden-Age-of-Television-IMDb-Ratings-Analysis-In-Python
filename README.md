# Golden Age of Television: IMDb Ratings Analysis
By James Weaver

# Introduction
This project analyzes IMDb ratings and votes to explore the assumption that highly-rated TV shows released during the "Golden Age" of television (1999–present) also receive the most audience votes. By examining relationships between IMDb scores, votes, and release years, the project provides insights into audience engagement and content quality trends.

# Files
golden_age_analysis.ipynb: Jupyter Notebook containing all code, analysis, and visualizations.
movies_and_shows.csv: Dataset with information on IMDb ratings, votes, and metadata for movies and TV shows.
README.md: Documentation summarizing the project.

# Goals
1. Preprocess the dataset by renaming columns, handling missing values, and removing duplicates.
2. Filter the dataset to focus on TV shows released in or after 1999.
3. Analyze trends between IMDb scores and votes to validate the assumption.
4. Provide insights into audience engagement during the "Golden Age."

# Steps in the Analysis
1. Data Preprocessing
- Renamed columns for readability and consistency.
- Addressed missing values and duplicates to ensure data accuracy.
- Filtered data to focus on TV shows released during or after 1999.
2. Exploratory Data Analysis
- Grouped IMDb scores into rounded buckets (e.g., 7, 8, 9) for trend analysis.
- Calculated average votes for each score bucket to identify engagement patterns.
- Visualized IMDb scores and votes to highlight relationships.
3. Outlier Detection
- Removed outliers (e.g., shows with very few votes) to avoid skewed results.
- Justified exclusions based on meaningful engagement thresholds.

# Key Insights
1. Validation of Assumption: TV shows with higher IMDb scores (7–9) generally received more votes, validating the assumption.
2. Audience Engagement: Scores of 9 peaked in votes, suggesting a strong audience preference for highly-rated shows.
3. Mid-Tier Trends: Shows with scores between 4–6 had significantly fewer votes, reflecting reduced engagement.
4. Outliers: Some low-rated shows (e.g., scores of 2–3) had insufficient votes for meaningful analysis.

# Skills Used
- Python (pandas, matplotlib, seaborn)
- Data Cleaning and Preprocessing
- Exploratory Data Analysis
- Data Visualization
- Statistical Analysis

# Future Work
1. Expand analysis to explore genre-specific trends and their impact on IMDb votes and ratings.
2. Add predictive models to forecast audience engagement based on early ratings and votes.
3. Visualize IMDb scores over time to track trends in TV quality during the "Golden Age."

# Conclusion
This project demonstrates how IMDb data can validate assumptions about audience engagement and content quality. By leveraging Python's data analysis capabilities, the project highlights meaningful trends and relationships within the entertainment industry during the "Golden Age of Television."
