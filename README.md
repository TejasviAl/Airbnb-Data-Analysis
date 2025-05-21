# Airbnb-Data-Analysis

This project performs exploratory data analysis (EDA) on an Airbnb dataset using Python. It involves data cleaning, transformation, and visualization to extract meaningful insights from the listings.
**DATASET:** 
The dataset used is `airbnb_data.xlsx`, which contains information on Airbnb listings such as price, room type, host details, number of reviews, etc.

**LIBRARIES:**
Pandas, matplotlib, seaborn 


**Data Cleaning**
1.Missing Values: Checked and handled using appropriate defaults:
  - Missing `reviews per month` set to 0.
  - Missing `last review` set to the earliest review date.
  - Rows with missing `name` or `host name` are dropped.
2.Date Conversion: `last review` column is converted to datetime.
3.Dollar Conversion: Columns `price` and `service fee` cleaned and converted from strings to float.
4.Duplicates: Removed duplicate entries.
5.Unnecessary Columns: Dropped irrelevant columns like `license` and `house_rules` if they exist.

**Data Exploration and Visualization**
- Distribution of Listing Prices: A histogram with a KDE plot.
- Room Type Distribution: Count of different room types using a bar chart.
- Neighborhood Group Distribution: Listings across neighborhoods visualized as a horizontal bar chart.
- Price vs Room Type: Box plot to examine how room type affects price.
- Reviews Over Time: Line chart to track how the number of reviews changes over time.
