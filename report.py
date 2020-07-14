#!/usr/bin/env python
# coding: utf-8

# # Final report

# # Capstone-project
# 
# ## Porject requirements(2weeks):
# 
# For this week, you will required to submit the following:
# ## Part1:
# A description of the problem and a discussion of the background. (15 marks)
# A description of the data and how it will be used to solve the problem. (15 marks)
# 
# ## Part2:
# For the second week, the final deliverables of the project will be:
# A link to your Notebook on your Github repository, showing your code. (15 marks)
# A full report consisting of all of the following components (15 marks):
# Introduction where you discuss the business problem and who would be interested in this project.
# Data where you describe the data that will be used to solve the problem and the source of the data.
# Methodology section which represents the main component of the report where you discuss and describe any exploratory data analysis that you did, any inferential statistical testing that you performed, if any, and what machine learnings were used and why.
# Results section where you discuss the results.
# Discussion section where you discuss any observations you noted and any recommendations you can make based on the results.
# Conclusion section where you conclude the report.
# 3. Your choice of a presentation or blogpost. (10 marks)
# 
# # Part1:
# # Introduction: 
# In this section I will clearly define the idea of my choosing, where I leverage the Foursquare location data to solve the imagined business opportunity.
# 
# Toronto is a colorful city, people could fulfill their dreams here and they also might loss their money due to the bad choice in thier business. My friend Kelly just graduated from University and he wants to find a neighborhood in Toronto to live.  Therefore, I am going to find the best location of neighborhood in Toronto for my fiend Kelly. 
# I will combine with the rates of crimes, top sites in city, the income and population of each neighborhood as well as the educated level present on the same regions.
# 
# # problems:
# The major purpose of this project, is to suggest a better neighborhood in a new city for the Kelly who firstly comes there. Social presence in society in terms of like minded people. Connectivity to the airport, bus stand, city center, markets and other daily needs things nearby.
# 
# Sorted list of house in terms of housing prices in a ascending or descending order
# Sorted list of schools in terms of location, fees, rating and reviews
# 
# 
# To provide him with the necessary information, I'll be combining  Chicago's 2016 Census that contains Population, Average income per Neighborhood with  Chicago's Neighborhoods shapefile and Foursquare API to collect competitors on the same neighborhoods
# 
# # Foursquare API:
# This project would use Four-square API as its prime data gathering source as it has a database of millions of places, especially their places API which provides the ability to perform location search, location sharing and details about a business.
# 
# # Data we use:
# 
# Data Description:
# Data Link: https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M
# 
# Will use Scarborough dataset which we scrapped from wikipedia on Week 3. Dataset consisting of latitude and longitude, zip codes.
# 
# Foursquare API Data:
# We will need data about different venues in different neighborhoods of that specific borough. In order to gain that information we will use "Foursquare" locational information. Foursquare is a location data provider with information about all manner of venues and events within an area of interest. Such information includes venue names, locations, menus and even photos. As such, the foursquare location platform will be used as the sole data source since all the stated required information can be obtained through the API.
# 
# After finding the list of neighborhoods, we then connect to the Foursquare API to gather information about venues inside each and every neighborhood. For each neighborhood, we have chosen the radius to be 100 meter.
# 
# The data retrieved from Foursquare contained information of venues within a specified distance of the longitude and latitude of the postcodes. The information obtained per venue as follows:
# 
# 1. Neighborhood
# 2. Neighborhood Latitude
# 3. Neighborhood Longitude
# 4. Venue
# 5. Name of the venue e.g. the name of a store or restaurant
# 6. Venue Latitude
# 7. Venue Longitude
# 8. Venue Category
# 
# # Libraries Which are Used to Develope the Project:
# Pandas: For creating and manipulating dataframes.
# 
# Folium: Python visualization library would be used to visualize the neighborhoods cluster distribution of using interactive leaflet map.
# 
# Scikit Learn: For importing k-means clustering.
# 
# JSON: Library to handle JSON files.
# 
# XML: To separate data from presentation and XML stores data in plain text format.
# 
# Geocoder: To retrieve Location Data.
# 
# Beautiful Soup and Requests: To scrap and library to handle http requests.
# 
# Matplotlib: Python Plotting Module.
# 
# # Clustering Approach:
# To compare the similarities of two cities, we decided to explore neighborhoods, segment them, and group them into clusters to find similar neighborhoods in a big city like New York and Toronto. To be able to do that, we need to cluster data which is a form of unsupervised machine learning: k-means clustering algorithm.
# 
# # Part2:
# 
# 
# ##  Methodology Section
# 
# #### Clustering Approach:
# To compare the similarities of two cities, we decided to explore neighborhoods, segment them, and group them into clusters to find similar neighborhoods in a big city like New York and Toronto. To be able to do that, we need to cluster data which is a form of unsupervised machine learning: k-means clustering algorithm.
# 
# **Using K-Means Clustering Approach**
# ![Using-K-Means-Clustering-Approach-10th-Most-Common-Venue-768x437.png](attachment:Using-K-Means-Clustering-Approach-10th-Most-Common-Venue-768x437.png)
# 
# 
# 
# **Most Common venues near Neighborhood**
# ![Most-Common-venues-near-neighborhood-768x434.png](attachment:Most-Common-venues-near-neighborhood-768x434.png)
# 
# 
# 
# #### Work Flow:
# Using credentials of Foursquare API features of near-by places of the neighborhoods would be mined. Due to http request limitations the number of places per neighborhood parameter would reasonably be set to 100 and the radius parameter would be set to 500.
# 
# 
# 
# ##  Results Section
# 
# **Map of Clusters in Scarborough**
# ![Map-of-Clusters-Scarborough-768x434.png](attachment:Map-of-Clusters-Scarborough-768x434.png)
# 
# 
# 
# **Average Housing Price by Clusters in Scarborough**
# ![FireShot%20Capture%20003%20-%20Capstone-project_Capstone%20Project%20Kelly's%20new%20home.ipynb%20at%20master%20%C2%B7%20_%20-%20github.com.png](attachment:FireShot%20Capture%20003%20-%20Capstone-project_Capstone%20Project%20Kelly's%20new%20home.ipynb%20at%20master%20%C2%B7%20_%20-%20github.com.png)
# 
# 
# 
# **School Ratings by Clusters in Scarborough**
# ![FireShot%20Capture%20007%20-%20Capstone-project_Capstone%20Project%20Kelly's%20new%20home.ipynb%20at%20master%20%C2%B7%20_%20-%20github.com.png](attachment:FireShot%20Capture%20007%20-%20Capstone-project_Capstone%20Project%20Kelly's%20new%20home.ipynb%20at%20master%20%C2%B7%20_%20-%20github.com.png)
# 
# 
# 
# #### The Location:
# Scarborough is a popular destination for new immigrants in Canada to reside. As a result, it is one of the most diverse and multicultural areas in the Greater Toronto Area, being home to various religious groups and places of worship. Although immigration has become a hot topic over the past few years with more governments seeking more restrictions on immigrants and refugees, the general trend of immigration into Canada has been one of on the rise.
# 
# ## Conclusion Section:
# In this project, using k-means cluster algorithm I separated the neighborhood into 10(Ten) different clusters and for 180 different lattitude and logitude from dataset, which have very-similar neighborhoods around them. Using the charts above results presented to a particular neighborhood based on average house prices and school rating have been made.
# 
# I feel rewarded with the efforts and believe this course with all the topics covered is well worthy of appreciation. This project has shown me a practical application to resolve a real situation that has impacting personal and financial impact using Data Science tools. The mapping with Folium is a very powerful technique to consolidate information and make the analysis and decision better with confidence.
# 
# Future Works:
# This project can be continued for making it more precise in terms to find best house in Scarborough. Best means on the basis of all required things(daily needs or things we need to live a better life) around and also in terms of cost effective.
#     

# In[ ]:




