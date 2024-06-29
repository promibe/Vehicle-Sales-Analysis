# Vehicle-Sales-Analysis
Analyzing the sales of car vehicles

# Objectives:
## 1 Importing the Libraries
The various Librabries was used for this analysis:
pandas, matplotlib, numpy, and seaborn Library

## 2 Loading of Dataset
The Dataset for this Analysis was gotten from kaggle, below is the Link to the dataset:
https://www.kaggle.com/datasets/syedanwarafridi/vehicle-sales-data

## 3 Dataset Information (Description)
### Dataset Description:
The "Vehicle Sales and Market Trends Dataset" provides a comprehensive collection of information pertaining to the sales transactions of various vehicles. This dataset encompasses details such as the * year - The year that the vehicle was manufactured
* make - The make, i.e the brand or company name that manufactured the vehicle
* model - The vehicle design and structure
* trim - The trim level means the system of packaging of the particular vehicle
* body type - Different model and make has different body type
* transmission type - the transmission Type could me automatic or manual
* VIN (Vehicle Identification Number)
* state of registration - The state where the vehicle was registered
* condition rating - This condition means that the car is either in excellent state or average state, and its value is from 1 Excellent to a certain value as the case maybe
* odometer reading - This reading indicate the number of miles the vehicle has traveled.
* exterior and interior colors - it tells of the color of the car both interior and exterior
* seller information
* Manheim Market Report (MMR) values - This value is the premier indicator of whole sales prices, it can be likened as the estimated whole sale price
* selling prices
* sale dates.

<b>Key Features:</b>

* Vehicle Details: Includes specific information about each vehicle, such as its make, model, trim, and manufacturing year.

* Transaction Information: Provides insights into the sales transactions, including selling prices and sale dates.

* Market Trends: MMR values offer an estimate of the market value of each vehicle, allowing for analysis of market trends and fluctuations.

* Condition and Mileage: Contains data on the condition of the vehicles as well as their odometer readings, enabling analysis of how these factors influence selling prices.

<b>Potential Use Cases:</b>

* Market Analysis: Researchers and analysts can utilize this dataset to study trends in the automotive market, including pricing fluctuations based on factors such as vehicle condition and mileage.

* Predictive Modeling: Data scientists can employ this dataset to develop predictive models for estimating vehicle prices based on various attributes.

* Business Insights: Automotive industry professionals, dealerships, and financial institutions can derive insights into consumer preferences, market demand, and pricing strategies.

* Format: The dataset is typically presented in tabular format (e.g., CSV) with rows representing individual vehicle sales transactions and columns representing different attributes associated with each transaction.

* Data Integrity: Efforts have been made to ensure the accuracy and reliability of the data; however, users are encouraged to perform their own validation and verification processes.

* Update Frequency: The dataset may be periodically updated to include new sales transactions and market data, providing fresh insights into ongoing trends in the automotive industry.

### 4. Problem Statement:
Analyse the Dataset and get meaning insight

### 5 Data Information and Insights - Exploratory Data Analysis
Below are the general insights gotten from the Analysis 

* We have 558,837 rows and 16 columns in our Dataset
* From the above we noticed that there are null values
* We have 4 columns which are float64 datatype, 1 int64 datatype then 11 object datatype, the saledate should be of datetime datatype, we might be having categorical data, we'll check
* Almost all of the columns in the dataset has null values except the year, state and the seller, we cant just remove them because they are reasonable amount of null, lets see if some or all can be treated.
* From the make column, we noticed that the letter case are not consistent, even the space between the makes (e.g) we have 'Lincoln', and 'lincoln' which are the same make, and others so these has to be treated. So we cant ascertain the total number of make, will do that after the Data cleaning process.
* Note that this column also contain NaN
* we have 973 categories including the NaN, we need to replace every whitespace within with a dash and change the case type of all the values.
* We have 1963 trim level categories.

### 6 Data Cleaning
The dataset does not contain duplicated.
The NaN columns were removed since the NaN is not up to 30%

### 7 Data Analysis and  Visualization
The Dataset was analysed and visualized to get insight from it

### 8 Result gotten from analysis
1. KPI's:
- Total number of Sales: 472,325 USD
- Total Sales Amount: 6,466,371,108 USD
- Total MMR value: 6,535,588,875 USD
- Average Sales Amount: 13,837.06 USD
- Average MMR: 13,690.51 USD

* We had approximately 1.06% discount of the total mmr value from the total selling price which is count 69,217,767 USD

* Reason for the discount is that the rating  condition and other feature are positive correlated to the selling price i.e if the feature value is low, the selling price will be low  and vice versa

2. Top 10 Make with the hightest sales count: from the visualization we can see the top 10 most purchase vehicle but ford is the highest with 81,013 vehicles purchased
<br>

3. Top 10 Make with the hightest average selling price: from the visualization we can also see the top 10 wehicles with the highest averaage selling price but that of the rolls-royce has the highest Average sellingprice of 153,456.25 USD
<br>

4. Top 10 make with the highest Average MMR value: among the top 10, the rolls-royce car has the highest mmr value of 154,812.50 USD we can also say that its the most expensive car bought for the manufacturer in our dataset.
<br>

5. List 10 car make with the Least Average MMR value: it was also noticed that the daewoo car has the least mmr value of 487.5 
<br>

6. Top 10 models with the highest sales count: the Altima model of the nissa make has the highest sale count of 16346 purchased out of the other 9 car models
<br>

* The 458 italia Ferrari car has the highest sellingprice

7. How many Category of trim do we have in total: we have about 1494 categories of trim level
<br>

8. Top 10 trim that is highly purchased and which make and model are they: The cars having the following tim level: 2.5 S, SE, XLT, 2.5, LE, Touring, GLS trim level are the top 10 trim levels that are higly purchased they are of the nissan, toyota, dodge, chrysler and hyundai car make.
<br>

9. Also the trim level as related to their average mmr: Remember that the rolls-royce had the higest average selling price and even the mmr value, Now we can see that they are of the EWR and the Base trim level category of the rolls-royce.
<br>

10. How many transmission category do we have: 2- automatic and manual
<br>

11. Which is the most sold transmission: It was observed that 96.5% of the sales are mostly automatic transmision which is a total of 455,963 sales while 3.5% is for manual transmission and a total of 16,362 sales
<br>

12. Whats the average mmr value for the transmission: The cars with automatic transmission are quite expensive or have the highest mmr value of 13916.05 in our dataset 
<br>

13. which of the transmission has the highest average sale amount: The cars that are of automatic transmission categories has an average selling price of 13774.51 USD over that of manual transmission which has about 11349.72 USD.
<br>

14. which of the transmission has the highest average sale amount: The cars with automatic transmission are quite expensive or have the highest mmr value of 13916.05 in our dataset. 
<br>

15. The state that purchased more cars: we have a total number of 34 states in our dataset, the people residing in florida (fl) purchased more vehicles of about 75,243 in our dataset.
<br>

16. The state with the highest amount spent: # from our dataset, we can understand that resident of Tennessee (tn) spend more on cars they spent there money on automatic more than manual.
<br>

17. How many condition category do we have in our dataset: we have 41 different condition state
<br>

18. Relationship between the vehicle condition and the selling price: from the dataset, we noticed that the condition is correlated to the sellingprice and its of moderate positive correlation with 0.32 correlation value.

i.e if the condition value is best/high, the sellingprice will be high
<br>

19. which condition type is sold the most: vehicle of condition 19 is being sold the most, of about 36,647, this could be because of various reason, perphase the odemeta value, color, or moderate selling price.
<br>

20. Day trend on number of sales, selling price: 

a. It was noticed that saturday had no sales, tuesday made the highest sales of 163,480 in our dataset.

b. highest sale is mostly on Wednessdays and the least sale is on sundays.

c. it was observed that sales at the 13:00:00 hrs they had the highest sellingprice
<br>     


21. Months trend on number of sales, purchase amount:

a. there was a downward trend in sales from february, and later went up in june but down in july, there was no sale from august to November

b. there was an upward trend from april which was downward from january, but from april to july the sales amount increased upwardly.
<br>

22. year trend on number of sales, purchase amount.

a. year 2015 made the highest sales count of vehicle, we can say there is an increase trend from 2014 to 2015

b. year 2015 has the highest sellingprice of vehicle, we can say there is an increase trend from 2014 to 2015

25. What is the correlation between the odometer reading and the selling price: from the visualization, we can see that the odometer has a strong negetive correlation with the selling price. i.e if the odometer reading increases, the selling price reduces and vice versa. We can say that cars that has been driven for long will really decrease in selling price compared to ones that has lower odometer
<br>

25. Top 5 best sellers with highest sales count: ford motor credit company llc, the hertz corporation, nissan-infiniti lt, santander consumer, and avis corporation are the top 5 best sellers with 17756,	16286, 15777, 14245, and 11471 number of vehicles purchased respectively
<br>

26. Top 5 best sellers with highest sellingprice
