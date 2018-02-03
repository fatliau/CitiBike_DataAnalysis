# CitiBike_DataAnalysis
## Citi Bike New Jersey Bike Rental Program
Chieh-Chi Chen, Marissa Miller, Shane St. Luce

## Dataset Description
“Where do Citi Bikers ride?
When do they ride?
How far do they go?
Which stations are most popular?
What days of the week are most rides taken on?

We've heard all of these questions and more from you, and we're happy to provide the data to help you discover the answers to these questions and more.”
- from https://www.citibikenyc.com/system-data

### Our Approach
Using Naïve Bayes to train and test the data
Creating Chou Liu Trees model the attribute dependencies
Training Set
2016 New Jersey
247,584 samples
Testing Set
March 2017 New Jersey
12,201 samples

### Raw Data Attributes
Trip Duration (seconds)
Start Time and Date
Stop Time and Date
Start and End Station
Name
ID
Lat/Long
Bike ID
User Type
Customer = 24-hour pass or 7-day pass user
Subscriber = Annual Member
Gender
0 – N/A
1 – Male
2 – Female
Year of Birth

### Data Attributes used for Analysis
Trip Duration 
Hour
Hour bucket bike is returned to a station
Start Station ID
End Station ID
User Type
Gender
Age
5 year buckets based on year of birth


## Result
### Naïve Bayes: Classifications
Start Station: 31.45% (34 stations)
End Station: 31.42% (34 stations)
Age: 29.65% (21 different age assignments)
Gender: 79.13% (3 different assignments)

### Chou Liu Tree shows that: Hour, Gender, and UserType are important attributes

### Naïve Bayes and Chou Liu Trees gave supporting results

### Predict missing attributes for Customer data
Use Gaussian Distribution
“Hour”
“Age”
“Duration”

## Want to learn more? Visit:
https://www.citibikenyc.com/system-data

