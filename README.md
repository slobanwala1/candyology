This repository contains an analysis of various questions about the very important topic of candy.

### Navigating This Repo
* Images folder shows images and plots generated through the data analysis
* Resources folder shows data files used (unless the source file was too big)
* Jupyter notebook includes code used for analysis and data cleanup

## Key Questions:
* To what extent is chocolate the most important element of a favorite candy?
* What is the relationship between favorite candies and candies that are purchased - in each state? Overall?
* What is the relationship between candy consumption, health expenditure, GDP, and dental health for the top 5 retail and top 5 consumption countries?
* What is the relationship between candy consumption and candy production?

## Source data:
* FiveThirtyEight Candy Match-ups (https://www.kaggle.com/fivethirtyeight/the-ultimate-halloween-candy-power-ranking)
This data set shows components of each candy, comparative sugar percentile, comparative price percentile, and percent wins of one-on-one candy match ups tested by omre then 269,000 votes from 8,371 IP addresses.
* CandyStore.com - a candy wholesaler's sales figures (https://www.candystore.com/blog/facts-trivia/favorite-candy-state-by-state-infographic/)
* Bad teeth, sugar and government health spending (https://www.kaggle.com/angelmm/healthteethsugar?select=sugar_consumption.csv)
* Global Community Trade Statistics (https://www.kaggle.com/unitednations/global-commodity-trade-statistics)

### Question One - To what extent is chocolate the most important element of a favorite candy?
This question is exploring is most important elements of favorite candies, specifically asking how chocolate factors into the mix. Our null hypothesis is that candies with chocolate and without perform the same when ranked as favorite candies. Our alternative hypothesis is that candies with chocolate perform better than candies without chocolate when ranked as favorite candies.

The FiveThirtyEight data shows that every top ten candy had chocolate as an element. Although chocolate and fruity candies were equally represented in the data set, there were no fruity candies in the top ten.

#### Total Counts of Candy Type in Dataset
![alt text](https://github.com/slobanwala1/candyology/blob/main/Images/overall_types.PNG?raw=true "Total Counts of Candy Type in Dataset")

![alt text](https://github.com/slobanwala1/candyology/blob/main/Images/Types%20of%20Candies%20in%20Top%20Ten.png?raw=true "Top Ten Candy Elements Bar Chart")

![alt text](https://github.com/slobanwala1/candyology/blob/main/Images/Types%20of%20Candies%20in%20Bottom%20Ten%20as%20Percent%20of%20Group%20Total.png?raw=true "Top Ten Candies as Percentage of Total Grouping Bar Chart")

As representatives of their data sets, peanutyalmondy candies performed better than the other groups, with half of the peanutyalmondy candies landing a spot in the top ten.

Bottom ten candies show no chocolate, nougat, crisped rice, or bar candies. 7 of the 10 bottom ten are pluribus - indicating that the candy is a box of many items, suggesting that the types of candies that end up in boxes are less preferred than single or bar candies.

![alt text](https://github.com/slobanwala1/candyology/blob/main/Images/Types%20of%20Candies%20in%20Bottom%20Ten.png?raw=true "Bottom Ten Candy Elements Bar Chart")

![alt text](https://github.com/slobanwala1/candyology/blob/main/Images/Types%20of%20Candies%20in%20Bottom%20Ten%20as%20Percent%20of%20Group%20Total.png?raw=true "Bottom Ten Candies as Percentage of Total Grouping Bar Chart")

The pluribus candies represent 16% of their total data set (with 7 candies) while peanutyalmondy represent 7% of their total (with 1 candy) in the bottom 10.

Ultimately, candies containing chocolate (n=37) performed better in the candy match ups than candies that did not contain chocolate (n=48).

![alt text](https://github.com/slobanwala1/candyology/blob/main/Images/Average%20Wins%20for%20Chocolate%20and%20Non-Chocolate%20Candies.png?raw=true "Bar graph showing Average Wins for Chocolate and Non-Chocolate Candies, Chocolate bar at 60% and Non-Chocolate Bar at 42%")

This suggests that the null hypothesis is rejected, and chocolate as an ingredient has an impact on favorite candies.

### Question Two - What is the relationship between favorite candies and candies that are purchased - in each state? Overall?

The best dataset we could find for candy purchases were from a candy wholesaler's website. They posted a chart with the top three candies purchased in each state, along with the amount of candy purchased.

To answer our question, we looked at the amount of candy purchased by each state, totaled and adjusted for population size. In retrospect, I wish I would have used population size, in all. Instead I used the population, in millions. Which still serves the purpose of giving as per capita information, but it means that the amount of candy we have for purchase data is in pounds per million, which isn't as user friendly -- and also makes for some long titles and labels.

First I looked at the amount of candy purchased, adjusted for population. The state purchasing the most candy was Arizona. They purcahsed about a third of a pound per person. Utah, Nevada, Kansas and North Dakota rounded out the top five. Looking at the rankings, by state, one could come to the conclusion that southwestern mountain states purchased the most candy.


![Pounds Per State](https://github.com/slobanwala1/candyology/blob/main/Images/PoundsPerState.png)

Next I did an analysis of the Top Choice of each state. I added the totals of this column and found that Skittles and Starburst were purchased far more than the others. In fact, I found that they were outliers among the rest of the other Top Choices. In the case of Skittles, it is because it was the most popular candy in California. California wasn't one of the states purchasing the most, per person, but because of the shear size of the population, their Top Choice was by far the greatest. And they really like Skittles. They purchased 1.5 million pounds of Skittles and that is 46 percent of total Skittle sales for all states. I created a second bar chart of Top Choices, with Skittles and Starburst removed to show that changed things. Also, it is important to note that Jolly Ranchers, Sour Patch Kids anad Hot Tamales made up the rest of the Top Five in Top Choice candies. Notice that there is no chocolate there.

![New Candy Pounds](https://github.com/slobanwala1/candyology/blob/main/Images/newcandypounds.png)

Here's a box plot, showing the outliers in total purchases.

![Candy Box](https://github.com/slobanwala1/candyology/blob/main/Images/CandyBox.png)

Here's the adjusted bar chart.

![Candy Bar](https://github.com/slobanwala1/candyology/blob/main/Images/labeledadjustedcandybar.png?raw=true)

Next I looked at total candy purchased, by brand, over all. Now this is just the top three choices, by state, but in this list, there was a little bit more chocolate -- Snickers, M&Ms, Reese's and Hershey kisses were in the top 10.

![Total Purchase Bar](https://github.com/slobanwala1/candyology/blob/main/Images/totalpurchasebar.png)

The only overlap between the top ten candies purchased from CandyStore.com and candies ranked from FiveThirtyEight are Reese's Peanut Butter Cups and Snickers, which is only 20% of the top ten, indicating a weak correlation between the two measures of favorite candy.

Lastly I looked to see if there is any correlation between candy purchases and demographics. The most likely correlation, I thought, was in age of the people in the state. So I found a dataset with the average age of residents and added a CSV with the percentage of the population under the age of 18. More kids mean more candy, right? Using Pearson's coefficient, I found a week correlation of 33 percent. Although I would point out that Utah is the youngest state and is also one of the top ranking states in terms of pounds purchased per million people.

![Scatter Plot Line](https://github.com/slobanwala1/candyology/blob/main/Images/scatterplotline.png)

### Question Three - What is the relationship between candy consumption, dental health, health expenditure, and GDP for the top 5 retail and top 5 consumption countries?

So our null hypothesis for this layer of the project was that there's no relationship between these data points. First we have to understand how the relation works.
Higher candy consumption means a greater sugar intake, and other processed ingredients which would lead to dental health information being affected by it. If more people
go to a doctor the health expenditure would go up for a Country and finally paying for medical would increase GDP. We wanted to do top 5 retail and top 5 consumption
countries but had to lower dataset due to lack of data we found. So we decided to do the top 3 consumption (US, Canada, Brazil) and top 2 production(China, Russia).

First lets look at the dental info. Sadly only one dataset was publicly available:

![Dental Visits Graph](https://github.com/slobanwala1/candyology/blob/main/Images/DentalVisitsGraph.png)

From this we can see the US doesn't have that high rate of visits while Russia and Canada do and Brazil which makes sense as those two have a high consumption while the US goes against the correlation.
So we cant definitely say theirs a positive relation but there is something there as its only one year of data so we can only take it for what it is.

Next we look at sugar consumption, Government health expenditure, and GDP relations over time per country.

![Sugar Consumption Graph](https://github.com/slobanwala1/candyology/blob/main/Images/SugarConsumptionGraph.png)

![Govt. Health Expend. Graph](https://github.com/slobanwala1/candyology/blob/main/Images/GovHealthExpendGraph.png)

![GDP Graph](https://github.com/slobanwala1/candyology/blob/main/Images/GDPGraph.png)

From this we can see that there's a clear relation with these variables as the higher the Sugar consumption the higher the gov health expenditure and higher the GDP graph. How does GDP relate in all this though?
Next we look at GDP vs Gov Health expenditure:

![GDP vs Govt. Health Expend. Graph](https://github.com/slobanwala1/candyology/blob/main/Images/GDPVsGovHealthExpend.png)

In here its harder to see due to limitations of unit weight but a higher GDP correlates to higher Gov Health Expenditure.

Finally we try to see a correlation between Sugar consumption and Gov Health Expend. for each country

![Sugar Consump. vs Gov Health Expend. for US](https://github.com/slobanwala1/candyology/blob/main/Images/SugarConsumpVsGovHealthExpendUS.png)

![Sugar Consump. vs Gov Health Expend. for CA](https://github.com/slobanwala1/candyology/blob/main/Images/SugarConsumpVsGovHealthExpendCA.png)

![Sugar Consump. vs Gov Health Expend. for BR](https://github.com/slobanwala1/candyology/blob/main/Images/SugarConsumpVsGovHealthExpendBR.png)

![Sugar Consump. vs Gov Health Expend. for CH](https://github.com/slobanwala1/candyology/blob/main/Images/SugarConsumpVsGovHealthExpendCH.png)

![Sugar Consump. vs Gov Health Expend. for RU](https://github.com/slobanwala1/candyology/blob/main/Images/SugarConsumpVsGovHealthExpendRU.png)

The issue with less data is correlation is much harder to get a concrete number however the golden goose of this lot is Canada as its correlation is very strong with higher Sugar Consumption = higher Gov health expenditure.
Same with if its lower making the other lower. The others have a very low correlation but that's a lack of enough years data as most of its privatized.

Finally lets take a look at all the variables together, however all of them are different units so it's hard to make a statement however, you can see the correlation between US and CA and a bit in BR and definitely in CH.

![Total Comparisons](https://github.com/slobanwala1/candyology/blob/main/Images/TotalComparisons2004.png)

Since we only have one years worth of data that's the only correlation we can show however clearly there's a relation between these data points thus we should that the null hypothesis is proven wrong.

### Question Four - What is the relationship between candy consumption and candy production?

As part of our analysis, we looked at chocolate and confections as a commodity for another analysis into the worldwide consumption of candy . As you can see from our chart, the US is the top importer. The amount of imports increases at a fairly steady rate, except around 2005-2006, when Hurricane Katrina affected sugar production.

![Total Sugar Production 2000-2019](https://github.com/slobanwala1/candyology/blob/main/Images/TotalSugarProductionSum2000To2019.PNG)

In this final chart, we looked at the top three countries producing the most sugar and dental visits for 12 year olds. China, the US and Russia are the top sugar-producing countries. What we found is the top producing country, although it doesn’t appear that they consume the most.

![Top 3 Sugar Production 2000-2019](https://github.com/slobanwala1/candyology/blob/main/Images/Top3SugarProductionSum2000To2019.PNG)

### Data limitations & Further discussions
* Finding data was a challenge - privately owned or very expensive
* Lots of conflicting data - different owners mean different bias
* Would like to do more comparisons with dental data and other health issues and get hands on more broad candy purchasing data

### Presentation Link
Find linked visual support for data presentation from 10/31/2020 - https://docs.google.com/presentation/d/1vw6C9iiEpf2EX1O7sxGdaLwSNd-_ESP2WSKsJGiv1ys/edit?usp=sharing
