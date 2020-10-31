This repository contains an analysis of various questions about the very important topic of candy.

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


### To what extent is chocolate the most important element of a favorite candy?
This question is exploring is most important elements of favorite candies, specifically asking how chocolate factors into the mix. Our null hypothesis is that candies with chocolate and without perform the same when ranked as favorite candies. Our alternative hypothesis is that candies with chocolate perform better than candies without chocolate when ranked as favorite candies.

The FiveThirtyEight data shows that every top ten candy had chocolate as an element. Although chocolate and fruity candies were equally represented in the data set, there were no fruity candies in the top ten.

#### Total Counts of Candy Type in Dataset
![alt text](https://github.com/slobanwala1/candyology/blob/candyTest/images/overall_types.PNG?raw=true "Total Counts of Candy Type in Dataset")

![alt text](https://github.com/slobanwala1/candyology/blob/candyTest/images/Types%20of%20Candies%20in%20Top%20Ten.png?raw=true "Top Ten Candy Elements Bar Chart")

![alt text](https://github.com/slobanwala1/candyology/blob/candyTest/images/Types%20of%20Candies%20in%20Bottom%20Ten%20as%20Percent%20of%20Group%20Total.png?raw=true "Top Ten Candies as Percentage of Total Grouping Bar Chart")

As representatives of their data sets, peanutyalmondy candies performed better than the other groups, with half of the peanutyalmondy candies landing a spot in the top ten.

Bottom ten candies show no chocolate, nougat, crisped rice, or bar candies. 7 of the 10 bottom ten are pluribus - indicating that the candy is a box of many items, suggesting that the types of candies that end up in boxes are less preferred than single or bar candies.

![alt text](https://github.com/slobanwala1/candyology/blob/candyTest/images/Types%20of%20Candies%20in%20Bottom%20Ten.png?raw=true "Bottom Ten Candy Elements Bar Chart")

![alt text](https://github.com/slobanwala1/candyology/blob/candyTest/images/Types%20of%20Candies%20in%20Bottom%20Ten%20as%20Percent%20of%20Group%20Total.png?raw=true "Bottom Ten Candies as Percentage of Total Grouping Bar Chart")

The pluribus candies represent 16% of their total data set (with 7 candies) while peanutyalmondy represent 7% of their total (with 1 candy) in the bottom 10.

Ultimately, candies containing chocolate (n=37) performed better in the candy match ups than candies that did not contain chocolate (n=48).

![alt text](https://github.com/slobanwala1/candyology/blob/candyTest/images/Average%20Wins%20for%20Chocolate%20and%20Non-Chocolate%20Candies.png?raw=true "Bar graph showing Average Wins for Chocolate and Non-Chocolate Candies, Chocolate bar at 60% and Non-Chocolate Bar at 42%")

This suggests that the null hypothesis is rejected, and chocolate as an ingredient has an impact on favorite candies.

### What is the relationship between favorite candies and candies that are purchased - in each state? Overall?

Christine enter write up here including graphs in the format below
![alt text](githublink "alt_text")

The only overlap between the top ten candies purchased from CandyStore.com and candies ranked from FiveThirtyEight are Reese's Peanut Butter Cups and Snickers, which is only 20% of the top ten, indicating a weak correlation between the two measures of favorite candy.

### What is the relationship between candy consumption, health expenditure, GDP, and dental health for the top 5 retail and top 5 consumption countries?

Shanil enter write up here including graphs in the format below
![alt text](githublink "alt_text")

### What is the relationship between candy consumption and candy production?

Colin enter write up here including graphs in the format below
![alt text](githublink "alt_text")

### Data limitations & Further discussions
*Finding data was a challenge - privately owned or very expensive
*Lots of conflicting data - different owners mean different bias
*Would like to do more comparisons with dental data and other health issues and get hands on more broad candy purchasing data
