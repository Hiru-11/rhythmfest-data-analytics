Python 3.14.4 (tags/v3.14.4:23116f9, Apr  7 2026, 14:10:54) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#Load the DataSet
df=pd.read_excel(r"C:\Users\Owner\Downloads\RythmFest_Full_Data.xlsx")
print(df.head())
  Event_ID        Date  ... Sponsor_Name Sponsorship_Contribution
0     E001  2025-07-01  ...       Nestle                   787995
1     E002  2025-07-01  ...      RedBull                   425352
2     E003  2025-07-01  ...    Coca-Cola                   920260
3     E004  2025-07-02  ...      Mobitel                   511927
4     E005  2025-07-02  ...       Dialog                   889852

[5 rows x 21 columns]
#Cleaning the Data
#Checking if there are any missing values
print(df.isnull().sum())
Event_ID                    0
Date                        0
Venue                       0
Stage                       0
Artist                      0
Genre                       0
Time_Slot                   0
Ticket_Type                 0
Tickets_Sold                0
Ticket_Price                0
Food_Sales                  0
Crowd_Size                  0
Rating                      0
Day_Type                    0
Food_Type                   0
Food_Item                   0
User_Name                   0
User_Age                    0
Favorite_Artist             0
Sponsor_Name                0
Sponsorship_Contribution    0
dtype: int64
#Re,ove Duplicate values
df=df.drop_duplicates()
print("Total rows:", len(df))
Total rows: 100
print("Remaining duplicates:", df.duplicated().sum())
Remaining duplicates: 0
#convert the data types
df['Date']=pd.to_datetime(df['Date'])
print(df.dtypes)
Event_ID                               str
Date                        datetime64[us]
Venue                                  str
Stage                                  str
Artist                                 str
Genre                                  str
Time_Slot                              str
Ticket_Type                            str
Tickets_Sold                         int64
Ticket_Price                         int64
Food_Sales                           int64
Crowd_Size                           int64
Rating                             float64
Day_Type                               str
Food_Type                              str
Food_Item                              str
User_Name                              str
User_Age                             int64
Favorite_Artist                        str
Sponsor_Name                           str
Sponsorship_Contribution             int64
dtype: object
#converting the data type to proper numbers
cols = ['Tickets_Sold','Ticket_Price','Food_Sales','Crowd_Size','Rating']for col in cols:
    
SyntaxError: invalid syntax
cols = ['Tickets_Sold','Ticket_Price','Food_Sales','Crowd_Size','Rating']
for col in cols:
df[col] = pd.to_numeric(df[col], errors='coerce')
SyntaxError: expected an indented block after 'for' statement on line 1
cols = ['Tickets_Sold','Ticket_Price','Food_Sales','Crowd_Size','Rating']
for col in cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

 
cols = ['Tickets_Sold','Ticket_Price','Food_Sales','Crowd_Size','Rating']

for col in cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')
    
SyntaxError: multiple statements found while compiling a single statement
cols = ['Tickets_Sold','Ticket_Price','Food_Sales','Crowd_Size','Rating']
for col in cols:
     df[col] = pd.to_numeric(df[col], errors='coerce')

     
print(df.dtypes)
Event_ID                               str
Date                        datetime64[us]
Venue                                  str
Stage                                  str
Artist                                 str
Genre                                  str
Time_Slot                              str
Ticket_Type                            str
Tickets_Sold                         int64
Ticket_Price                         int64
Food_Sales                           int64
Crowd_Size                           int64
Rating                             float64
Day_Type                               str
Food_Type                              str
Food_Item                              str
User_Name                              str
User_Age                             int64
Favorite_Artist                        str
Sponsor_Name                           str
Sponsorship_Contribution             int64
dtype: object
#Fill missing values
df.fillna(0,inplace=True)
   Event_ID       Date  ... Sponsor_Name Sponsorship_Contribution
0      E001 2025-07-01  ...       Nestle                   787995
1      E002 2025-07-01  ...      RedBull                   425352
2      E003 2025-07-01  ...    Coca-Cola                   920260
3      E004 2025-07-02  ...      Mobitel                   511927
4      E005 2025-07-02  ...       Dialog                   889852
..      ...        ...  ...          ...                      ...
95     E096 2025-08-02  ...      RedBull                   821772
96     E097 2025-08-02  ...      RedBull                   289407
97     E098 2025-08-02  ...       Nestle                   549395
98     E099 2025-08-03  ...       Nestle                   562894
99     E100 2025-08-03  ...      Mobitel                   311810

[100 rows x 21 columns]
#creation of important columns
#creation of the Revenue Column
df['Revenue'] = df['Tickets_Sold'] * df['Ticket_Price']
print(df.columns)
Index(['Event_ID', 'Date', 'Venue', 'Stage', 'Artist', 'Genre', 'Time_Slot',
       'Ticket_Type', 'Tickets_Sold', 'Ticket_Price', 'Food_Sales',
       'Crowd_Size', 'Rating', 'Day_Type', 'Food_Type', 'Food_Item',
       'User_Name', 'User_Age', 'Favorite_Artist', 'Sponsor_Name',
       'Sponsorship_Contribution', 'Revenue'],
      dtype='str')
#viewing the column to see if the multiplication worked
print(df[['Tickets_Sold', 'Ticket_Price', 'Revenue']].head())
   Tickets_Sold  Ticket_Price  Revenue
0           120         15000  1800000
1           300          8000  2400000
2           150          5000   750000
3           200         12000  2400000
4           350          7000  2450000
#creation of the Total Value Column
df['Total_Value'] = df['Revenue'] + df['Food_Sales']
print(df.columns)
Index(['Event_ID', 'Date', 'Venue', 'Stage', 'Artist', 'Genre', 'Time_Slot',
       'Ticket_Type', 'Tickets_Sold', 'Ticket_Price', 'Food_Sales',
       'Crowd_Size', 'Rating', 'Day_Type', 'Food_Type', 'Food_Item',
       'User_Name', 'User_Age', 'Favorite_Artist', 'Sponsor_Name',
       'Sponsorship_Contribution', 'Revenue', 'Total_Value'],
      dtype='str')
#viewing the column to see if the addition actually worked
print(df[['Revenue','Food_Sales','Total_Value']].head())
   Revenue  Food_Sales  Total_Value
0  1800000      250000      2050000
1  2400000      180000      2580000
2   750000       90000       840000
3  2400000      220000      2620000
4  2450000      200000      2650000
#creation of the Assumed Profit Column
#assuming that the profit is 30% and the cost is 70%
df['Profit'] = df['Total_Value'] * 0.3
print(df.columns)
Index(['Event_ID', 'Date', 'Venue', 'Stage', 'Artist', 'Genre', 'Time_Slot',
       'Ticket_Type', 'Tickets_Sold', 'Ticket_Price', 'Food_Sales',
       'Crowd_Size', 'Rating', 'Day_Type', 'Food_Type', 'Food_Item',
       'User_Name', 'User_Age', 'Favorite_Artist', 'Sponsor_Name',
       'Sponsorship_Contribution', 'Revenue', 'Total_Value', 'Profit'],
      dtype='str')
#viewing the column to see if the profit is calculated properly
print(df[['Total_Value', 'Profit']].head())
   Total_Value    Profit
0      2050000  615000.0
1      2580000  774000.0
2       840000  252000.0
3      2620000  786000.0
4      2650000  795000.0
#Age Classification
df['Age_Group']=pd.cut(df['User_Age'],
                       bins=[0,18,25,35,50,100],
                       labels=['Teen','Young','Adult','Mid-Age','Senior'])
print(df[['User_Age', 'Age_Group']].head())
   User_Age Age_Group
0        56    Senior
1        46   Mid-Age
2        32     Adult
3        60    Senior
4        25     Young
#Quick Summary of the Dataser
df.info()
<class 'pandas.DataFrame'>
RangeIndex: 100 entries, 0 to 99
Data columns (total 25 columns):
 #   Column                    Non-Null Count  Dtype         
---  ------                    --------------  -----         
 0   Event_ID                  100 non-null    str           
 1   Date                      100 non-null    datetime64[us]
 2   Venue                     100 non-null    str           
 3   Stage                     100 non-null    str           
 4   Artist                    100 non-null    str           
 5   Genre                     100 non-null    str           
 6   Time_Slot                 100 non-null    str           
 7   Ticket_Type               100 non-null    str           
 8   Tickets_Sold              100 non-null    int64         
 9   Ticket_Price              100 non-null    int64         
 10  Food_Sales                100 non-null    int64         
 11  Crowd_Size                100 non-null    int64         
 12  Rating                    100 non-null    float64       
 13  Day_Type                  100 non-null    str           
 14  Food_Type                 100 non-null    str           
 15  Food_Item                 100 non-null    str           
 16  User_Name                 100 non-null    str           
 17  User_Age                  100 non-null    int64         
 18  Favorite_Artist           100 non-null    str           
 19  Sponsor_Name              100 non-null    str           
 20  Sponsorship_Contribution  100 non-null    int64         
 21  Revenue                   100 non-null    int64         
 22  Total_Value               100 non-null    int64         
 23  Profit                    100 non-null    float64       
 24  Age_Group                 100 non-null    category      
dtypes: category(1), datetime64[us](1), float64(2), int64(8), str(13)
memory usage: 19.2 KB
#Analysing the Data
#calculating the total revenue generated from all the events
print("Total Revenue:", df['Revenue'].sum())
Total Revenue: 250825000
#calculating the total revenue generated for music genres
print(df.groupby('Genre')['Revenue'].sum())
Genre
Acoustic      11760000
Classical      8250000
Pop          165025000
Rap           34020000
Rock          31770000
Name: Revenue, dtype: int64
#calculating the revenue generated for each venue
print(df.groupby('Venue')['Revenue').sum())
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
print(df.groupby('Venue')['Revenue'].sum())
Venue
Colombo    59675000
Galle      43930000
Jaffna     45110000
Kandy      56995000
Negombo    45115000
Name: Revenue, dtype: int64
#Fidning the top 5 artists based on the total tickets sold in descendig order
print(df.groupby('Artist')['Tickets_Sold'].sum().sort_values(ascending=False).head())
Artist
Yohani                4670
Centigradz            4020
Bathiya & Santhush    3820
Daddy                 3530
Windy G               2430
Name: Tickets_Sold, dtype: int64
#Finding the ticket sales for each artist based on the ticket type
df.groupby(['Artist', 'Ticket_Type'])['Tickets_Sold'].sum()
Artist                 Ticket_Type      
Bathiya & Santhush     General Admission    3820
Centigradz             General Admission    4020
Daddy                  General Admission    3530
Kasun Kalhara          Early Bird           1960
Nadeemal Perera        Early Bird           1760
Sanuka Wickramasinghe  VIP                  1920
Umaria                 Early Bird           1650
Windy G                VIP                  2430
Yohani                 VIP                  4670
Name: Tickets_Sold, dtype: int64
#Saving the cleaned and column added excel file
df.to_excel(r"C:\Users\Owner\Downloads\RythmFest_Cleaned_Data.xlsx", index=False)

#Graph Generation
#Bar Chart Generation for Revenue by Genre
df.groupby('Genre')['Revenue'].sum().plot(kind='bar')
<Axes: xlabel='Genre'>
plt.title("Revenue By Genre")
Text(0.5, 1.0, 'Revenue By Genre')
plt.xlabel("Genre")
Text(0.5, 0, 'Genre')
plt.ylabel("Revenue")
Text(0, 0.5, 'Revenue')
plt.show()
#Bar Chart Generation for Revenue by Venue
df.groupby('Venue')['Revenue'].sum().plot(kind='bar')
<Axes: xlabel='Venue'>
plt.title("Revenue by Venue")
Text(0.5, 1.0, 'Revenue by Venue')
plt.xlabel("Venue")
Text(0.5, 0, 'Venue')
plt.ylabel("Revenue")
Text(0, 0.5, 'Revenue')
plt.show()


#Graph Generation
#Bar chart for Revenue by Genre
genre_revenue = df.groupby('Genre')['Revenue'].sum()
genre_revenue.plot(kind='bar')
<Axes: xlabel='Genre'>
plt.title("Revenue by Genre")
Text(0.5, 1.0, 'Revenue by Genre')
plt.xlabel("Genre")
Text(0.5, 0, 'Genre')
plt.ylabel("Revenue")
Text(0, 0.5, 'Revenue')
plt.show()
print(genre_revenue)
Genre
Acoustic      11760000
Classical      8250000
Pop          165025000
Rap           34020000
Rock          31770000
Name: Revenue, dtype: int64


#Graph Generation
#Bar chart for Revenue by Genre
genre_revenue = df.groupby('Genre')['Revenue'].sum()
genre_revenue.plot(kind='bar')
<Axes: xlabel='Genre'>
plt.title("Revenue by Genre")
Text(0.5, 1.0, 'Revenue by Genre')
plt.xlabel("Genre")
Text(0.5, 0, 'Genre')
plt.ylabel("Revenue")
Text(0, 0.5, 'Revenue')



#Graph Generation
#Bar chart for Revenue by Genre
genre_revenue = df.groupby('Genre')['Revenue'].sum() / 1_000_000 #converting into millions
genre_revenue.sort_values(ascending=False).plot(kind='bar')
<Axes: title={'center': 'Revenue by Genre'}, xlabel='Genre', ylabel='Revenue'>
plt.title("Revenue by Genre (in Millions)")
Text(0.5, 1.0, 'Revenue by Genre (in Millions)')
plt.xlabel("Genre")
Text(0.5, 0, 'Genre')
plt.ylabel("Revenue (Millions)")
Text(0, 0.5, 'Revenue (Millions)')
plt.xticks(rotation=45) # for better visualization and prevent overlapping
(array([0, 1, 2, 3, 4]), [Text(0, 0, 'Pop'), Text(1, 0, 'Rap'), Text(2, 0, 'Rock'), Text(3, 0, 'Acoustic'), Text(4, 0, 'Classical')])
plt.show()


#Graph Generation
#Bar chart for Revenue by Genre
genre_revenue = df.groupby('Genre')['Revenue'].sum() / 1_000_000 #converting into millions
ax = genre_revenue.sort_values(ascending=False).plot(kind='bar')
plt.title("Revenue by Genre (in Millions)")
Text(0.5, 1.0, 'Revenue by Genre (in Millions)')
plt.xlabel("Genre")
Text(0.5, 0, 'Genre')
plt.ylabel("Revenue (Millions)")
Text(0, 0.5, 'Revenue (Millions)')
plt.xticks(rotation=45)
(array([0, 1, 2, 3, 4]), [Text(0, 0, 'Pop'), Text(1, 0, 'Rap'), Text(2, 0, 'Rock'), Text(3, 0, 'Acoustic'), Text(4, 0, 'Classical')])
#Disabling the scientific notation
ax.ticklabel_format(style='plain', axis='y')
plt.show()

#Bar chart for Revenue by Venue
venue_revenue = df.groupby('Venue')['Revenue'].sum() / 1_000_000  # convert to millions
venue_revenue.sort_values(ascending=False).plot(kind='bar')
<Axes: xlabel='Venue'>
plt.title("Revenue by Venue (in Millions)")
Text(0.5, 1.0, 'Revenue by Venue (in Millions)')
plt.xlabel("Venue")
Text(0.5, 0, 'Venue')
plt.ylabel("Revenue (Millions)")
Text(0, 0.5, 'Revenue (Millions)')
plt.xticks(rotation=45)
(array([0, 1, 2, 3, 4]), [Text(0, 0, 'Colombo'), Text(1, 0, 'Kandy'), Text(2, 0, 'Negombo'), Text(3, 0, 'Jaffna'), Text(4, 0, 'Galle')])
ax.ticklabel_format(style='plain', axis='y')
plt.show()
print(venue_revenue)
Venue
Colombo    59.675
Galle      43.930
Jaffna     45.110
Kandy      56.995
Negombo    45.115
Name: Revenue, dtype: float64

#Line Graph for Revenue Over time
revenue_time = df.groupby('Date')['Revenue'].sum() / 1_000_000
ax = revenue_time.plot() #plotting the line graph
plt.title("Revenue Trend Over Time (in Millions)")
Text(0.5, 1.0, 'Revenue Trend Over Time (in Millions)')
plt.xlabel("Date")
Text(0.5, 0, 'Date')
plt.ylabel("Revenue (Millions)")
Text(0, 0.5, 'Revenue (Millions)')
ax.yaxis.set_major_formatter(mtick.StrMethodFormatter('{x:,.0f}'))
Traceback (most recent call last):
  File "<pyshell#150>", line 1, in <module>
    ax.yaxis.set_major_formatter(mtick.StrMethodFormatter('{x:,.0f}'))
NameError: name 'mtick' is not defined
ax.ticklabel_format(style='plain', axis='y')
plt.show()
print(revenue_time)
Date
2025-07-01    4.950
2025-07-02    5.930
2025-07-03    6.480
2025-07-04    7.010
2025-07-05    6.000
2025-07-06    7.255
2025-07-07    6.170
2025-07-08    6.860
2025-07-09    6.785
2025-07-10    7.840
2025-07-11    6.035
2025-07-12    7.710
2025-07-13    7.845
2025-07-14    6.900
2025-07-15    6.650
2025-07-16    7.840
2025-07-17    6.740
2025-07-18    8.340
2025-07-19    6.530
2025-07-20    7.450
2025-07-21    7.620
2025-07-22    7.890
2025-07-23    6.970
2025-07-24    8.520
2025-07-25    7.460
2025-07-26    8.600
2025-07-27    7.530
2025-07-28    8.415
2025-07-29    8.060
2025-07-30    9.030
2025-07-31    8.010
2025-08-01    9.240
2025-08-02    8.060
2025-08-03    8.100
Name: Revenue, dtype: float64

#Pie chart to see the Ticket Type Distribution
df['Ticket_Type'].value_counts().plot(kind='pie', autopct='%1.1f%%')
<Axes: >
plt.title("Ticket Type Distribution")
Text(0.5, 1.0, 'Ticket Type Distribution')
plt.show()
print(df['Ticket_Type'].value_counts())
Ticket_Type
VIP                  34
General Admission    34
Early Bird           32
Name: count, dtype: int64

#Bar Chart for the Top Artists
df['Artist'].value_counts().head(5).plot(kind='bar')
<Axes: xlabel='Artist'>
plt.title("Top Artists")
Text(0.5, 1.0, 'Top Artists')
plt.xlabel("Artist")
Text(0.5, 0, 'Artist')
plt.ylabel("Number of Events")
Text(0, 0.5, 'Number of Events')
plt.xticks(rotation=45)
(array([0, 1, 2, 3, 4]), [Text(0, 0, 'Yohani'), Text(1, 0, 'Centigradz'), Text(2, 0, 'Bathiya & Santhush'), Text(3, 0, 'Umaria'), Text(4, 0, 'Kasun Kalhara')])
plt.show()


#Bar Chart for Food Sales by Type
df.groupby('Food_Type')['Food_Sales'].sum().plot(kind='bar')
<Axes: xlabel='Food_Type'>
plt.title("Food Sales by Type")
Text(0.5, 1.0, 'Food Sales by Type')
plt.xlabel("Food Type")
Text(0.5, 0, 'Food Type')
plt.ylabel("Total Sales")
Text(0, 0.5, 'Total Sales')
plt.xticks(rotation=45)
(array([0, 1, 2, 3]), [Text(0, 0, 'Dessert'), Text(1, 0, 'Drink'), Text(2, 0, 'Meal'), Text(3, 0, 'Snack')])
plt.show()
print(df.groupby('Food_Type')['Food_Sales'].sum())
Food_Type
Dessert    5440000
Drink      5910000
Meal       5200000
Snack      5190000
Name: Food_Sales, dtype: int64
#Error in graph - appearing of the scientific notation

#Bar Chart for Food Sales by Type
food_sales = df.groupby('Food_Type')['Food_Sales'].sum() / 1_000_000
ax = food_sales.sort_values(ascending=False).plot(kind='bar')
plt.title("Food Sales by Type (in Millions)")
Text(0.5, 1.0, 'Food Sales by Type (in Millions)')
plt.xlabel("Food Type")
Text(0.5, 0, 'Food Type')
plt.ylabel("Sales (Millions)")
Text(0, 0.5, 'Sales (Millions)')
plt.xticks(rotation=45)
(array([0, 1, 2, 3]), [Text(0, 0, 'Drink'), Text(1, 0, 'Dessert'), Text(2, 0, 'Meal'), Text(3, 0, 'Snack')])
plt.show()


#HeatMap to show which factors increase or decrease revenue and ticket sales
plt.figure(figsize=(10,6))
<Figure size 1000x600 with 0 Axes>
sns.heatmap(
    df[['Tickets_Sold','Ticket_Price','Revenue','Crowd_Size','Rating']].corr(),annot=True,cmap='coolwarm')
<Axes: >
plt.title("Correlation Heatmap")
Text(0.5, 1.0, 'Correlation Heatmap')
plt.show()
print(df[['Tickets_Sold','Ticket_Price','Revenue','Crowd_Size','Rating']].corr())
              Tickets_Sold  Ticket_Price   Revenue  Crowd_Size    Rating
Tickets_Sold      1.000000      0.345261  0.710482    0.835302  0.184104
Ticket_Price      0.345261      1.000000  0.889626    0.762097  0.475423
Revenue           0.710482      0.889626  1.000000    0.965179  0.467867
Crowd_Size        0.835302      0.762097  0.965179    1.000000  0.423359
Rating            0.184104      0.475423  0.467867    0.423359  1.000000


#Bar chart to demontstrate which age generates the most income
df.groupby('Age_Group')['Revenue'].sum().plot(kind='bar')
<Axes: xlabel='Age_Group'>
plt.title("Revenue by Age Group")
Text(0.5, 1.0, 'Revenue by Age Group')
plt.xlabel("Age Group")
Text(0.5, 0, 'Age Group')
plt.ylabel("Total Revenue")
Text(0, 0.5, 'Total Revenue')
plt.xticks(rotation=45)
(array([0, 1, 2, 3, 4]), [Text(0, 0, 'Teen'), Text(1, 0, 'Young'), Text(2, 0, 'Adult'), Text(3, 0, 'Mid-Age'), Text(4, 0, 'Senior')])
plt.show()
#Error - displaying the scientific notation

#Bar chart to demontstrate which age generates the most income
revenue_age = df.groupby('Age_Group')['Revenue'].sum() / 1_000_000
ax = revenue_age.plot(kind='bar')
plt.title("Revenue by Age Group (in Millions)")
Text(0.5, 1.0, 'Revenue by Age Group (in Millions)')
plt.xlabel("Age Group")
Text(0.5, 0, 'Age Group')
plt.ylabel("Revenue (Millions)")
Text(0, 0.5, 'Revenue (Millions)')
plt.xticks(rotation=45)
(array([0, 1, 2, 3, 4]), [Text(0, 0, 'Teen'), Text(1, 0, 'Young'), Text(2, 0, 'Adult'), Text(3, 0, 'Mid-Age'), Text(4, 0, 'Senior')])
plt.show()


#Scatter plt to see the ticket price vs Revenue
plt.figure(figsize=(8,5))
<Figure size 800x500 with 0 Axes>
sns.scatterplot(
    data=df,
    x='Ticket_Price',
    y='Revenue'
    )
<Axes: xlabel='Ticket_Price', ylabel='Revenue'>
plt.title("Ticket Price vs Revenue")
Text(0.5, 1.0, 'Ticket Price vs Revenue')
plt.xlabel("Ticket Price")
Text(0.5, 0, 'Ticket Price')
plt.ylabel("Revenue")
Text(0, 0.5, 'Revenue')
plt.show()
#output seems wrong for a scatter graph


#Bar chart to represent favourite artist and revenue
fav_artist_revenue = df.groupby('Favorite_Artist')['Revenue'].sum() / 1_000_000
ax = fav_artist_revenue.sort_values(ascending=False).head(10).plot(kind='bar')
plt.title("Revenue by Favorite Artist (in Millions)")
Text(0.5, 1.0, 'Revenue by Favorite Artist (in Millions)')
plt.xlabel("Favorite Artist")
Text(0.5, 0, 'Favorite Artist')
plt.ylabel("Revenue (Millions)")
Text(0, 0.5, 'Revenue (Millions)')
plt.xticks(rotation=45)
(array([0, 1, 2, 3, 4, 5, 6, 7, 8]), [Text(0, 0, 'Yohani'), Text(1, 0, 'Sanuka Wickramasinghe'), Text(2, 0, 'Umaria'), Text(3, 0, 'Centigradz'), Text(4, 0, 'Windy G'), Text(5, 0, 'Nadeemal Perera'), Text(6, 0, 'Kasun Kalhara'), Text(7, 0, 'Daddy'), Text(8, 0, 'Bathiya & Santhush')])
plt.show()


#Pie chart for Ticket Type distribution by the users
df['Ticket_Type'].value_counts().plot(
     kind='pie',
     autopct='%1.1f%%',
     startangle=90
     )
<Axes: >
>>> plt.title("Ticket Type Distribution")
Text(0.5, 1.0, 'Ticket Type Distribution')
>>> plt.ylabel("")  # hides ugly "count" label
Text(0, 0.5, '')
>>> plt.show()
>>> #same chart as generated earlier
>>> 
>>> 
>>> #Revenue for Ticket Bar chart
>>> df['Revenue_per_Ticket'] = df['Revenue'] / df['Tickets_Sold']
>>> rev_ticket = df.groupby('Genre')['Revenue_per_Ticket'].mean() / 1_000
>>> ax = rev_ticket.sort_values().plot(kind='bar')
>>> plt.title("Average Revenue per Ticket by Genre (in Thousands)")
Text(0.5, 1.0, 'Average Revenue per Ticket by Genre (in Thousands)')
>>> plt.ylabel("Revenue per Ticket (Thousands)")
Text(0, 0.5, 'Revenue per Ticket (Thousands)')
>>> plt.xticks(rotation=45)
(array([0, 1, 2, 3, 4]), [Text(0, 0, 'Classical'), Text(1, 0, 'Acoustic'), Text(2, 0, 'Rock'), Text(3, 0, 'Pop'), Text(4, 0, 'Rap')])
>>> plt.show()
>>> print(df.groupby('Genre')['Revenue_per_Ticket'].mean().sort_values())
Genre
Classical     5000.000000
Acoustic      6000.000000
Rock          9000.000000
Pop          10181.034483
Rap          14000.000000
Name: Revenue_per_Ticket, dtype: float64
>>> plt.show()
>>> 
>>> 
>>> #Chart- To save the chart for the revenue for ticket bar chart
>>> df['Revenue_per_Ticket'] = df['Revenue'] / df['Tickets_Sold']
>>> rev_ticket = df.groupby('Genre')['Revenue_per_Ticket'].mean() / 1000
>>> ax = rev_ticket.sort_values().plot(kind='bar')
>>> plt.title("Average Revenue per Ticket by Genre (in Thousands)")
Text(0.5, 1.0, 'Average Revenue per Ticket by Genre (in Thousands)')
>>> plt.ylabel("Revenue per Ticket (K)")
Text(0, 0.5, 'Revenue per Ticket (K)')
>>> plt.xticks(rotation=45)
(array([0, 1, 2, 3, 4]), [Text(0, 0, 'Classical'), Text(1, 0, 'Acoustic'), Text(2, 0, 'Rock'), Text(3, 0, 'Pop'), Text(4, 0, 'Rap')])
>>> plt.show()
