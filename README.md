# YouTube Trending

**Before we begin, let us introduce some of the most trending videos in youtube across the globe!!!**


<img src="youtube-trending/Image/Collage_Giffy.gif" alt="Headline" width="1000"/>



**After watching a couple of them, we asked ourselves, what makes the videos popular !!! and what if we could predict the popularity !!! 
Afterall, we want to help the struggling youtuber/influencer community by providing them the valuable insights on trending. At the same time, predicting popularity would help the advertising firms to identify the best videos to invest upon.** 

**Above all, we want to know, if there are any interesting insights underlying the trending patterns ?**

**This project is all about our journey towards finding these answers. Stay tuned !!!**


## Team Members

[Bincy Narath](https://github.com/bnarath), [Sogra Bilal Memon](https://github.com/SograMemon) & [Megan McGlashan](https://github.com/McGlash)

## Inspiration:

After finding [this](https://www.kaggle.com/datasnaek/youtube-new) dataset in [Kaggle](https://www.kaggle.com/), we thought of leveraging this data to derive meaningful insights. 

The Data set consists of useful but limited details on the trending videos for a span of 205 days across 10 countries. It is mentioned that "To determine the top-trending videos, YouTube uses a combination of factors including measuring users interactions (number of views, shares, comments and likes)" which is not revealed publicly. Though, many interesting explorations were already done by many Kagglers on the same dataset, we identified a huge scope ahead; especially, in the direction of predicting popularity and identifying behavioural patterns. This deemed possible by identifying and formulating usecases and solving them by incorporating many more features with API retrieved data, engineering new features, and building efficient models etc.

## Data Retrieval and Modelling:

The Data Retrieval and Modelling of this project are explained in the below ERD(Entity Relationship Diagram)
<img src="youtube-trending/Image/Data_Modelling.png" alt="Data_Modelling" width="1000"/>



Many data frames are created with this data for various analyses and model building. Because of the file size limits in GitHub, they are uploaded [here](https://drive.google.com/drive/folders/1ovyTyDPmwY9NIAqOC7C4y1SWwoec3Nmj?usp=sharing) as a pickle files. Please refer the table below for the details on the files.

<img src="youtube-trending/Image/FileNames.png" alt="Data_Modelling" width="1000"/>



### Codebase for Data Retrieval and Cleanup
We separated out the codebase of data modelling and clean-up from analysis and the model. Please refer the codebase for data retrieval and clean-up [here](youtube-trending/Code/youtube_trending_preprocessing.ipynb).

## Research Questions

1. Regional Analysis: How does trending in different countries impact one another?
    1. [Which countries generate videos that trend on Youtube and which consume them?](#)
    1. [Which categories of videos trend more often in different countries?](#) 
    1. [What is the composition of languages on trending videos across countries?](#)
    1. [What is the composition of categories on trending videos across countries?](#)
    1. [How similar or different are the countries based on what(which videos) gets trending in countries?](#)
    1. [How similar or different are the countries based on the categories they like?](#)

1. Popularity Analysis: What impacts how long videos trend on Youtube?  

   Factors considered:
     1. [Country of viewership](#) 
     1. [Video language](#) 
     1. [Video features](#)
     1. [Interval between publishing and when videos first trending](#)
  

## Regional Analysis: Findings

**Overall, the vast majority (92.5%) of videos trended in a single country.**

<img src="youtube-trending/Image/No._of_Countries_Video_Trended_In.png" alt="No_of_countries"/>


<hr>


**Videos that trended in multiple countries most often trended in Canada (over 1 in 4) followed by Germany (over 1 in 5) and France (just under 1 in 6). Few Videos that trended in multiple countries trended in the US, suggesting it has less impact on trending in other countries.**

<img src="youtube-trending/Image/Percentage_of_Videos_Trending_in_Multiple_Countries_by_Country_of_Viewership.png" alt="Trending_in_Multiple_Countries"/>


<hr>


**As we would expect, The local language seems to play a big role in trending.**   
**We studied the ratio of languages of trending videos across countries (English is Top3 for all except Russia, Japan and Korea).**

<img src="youtube-trending/Image/Lang1.png" alt="Country_Language_Composition" width="700" height="900"/>


<hr>


**Also, Videos made in English trend significantly longer than that of other languages.**

<img src="youtube-trending/Image/Popularity_for_Languages.png" alt="Language_Vs_Trending"/>


<hr>


**We studied trending categories across countries and found "Entertainment" is the most trending category in all countries except Great Britain(GB) and Russia.**  **In GB, Music outnumbered the Entertainment whereas in Russia "People & Blogs" surmounted Entertainment!**

<img src="youtube-trending/Image/Cat1_with_360217.png" alt="Country_Category_Composition" width="700" height="900"/>


<hr>


**We define popularity(longevity) as the number the days of trending. Almost all categories have a varying popularity.**  
**However, it looks like "Non-profit & Activism" tend to have relatively shorter limelight.**

<img src="youtube-trending/Image/Popularity_Across_Categories.png" alt="Category_Vs_Trending" width="800"/>


<hr>


**Similarity between countries based on what they watch: We mapped countries into large dimensional vectors and measured cosine similarity between them to understand with countries watch the same content. It appears that all countries watch mostly distinct videos. When, only countries with at least 10% similarity is taken into account, it shows Canada is similar to all other interconnected countries. This shows cross culture links in Canada (possibly because of welcoming Immigration across the globe)**


<img src="youtube-trending/Image/country_relations_sc_giffy.gif" alt="Country_Relationships" width="850"/>


<hr>


**Similarity between countries based on the categories they watch: We clustered countries based on the how much they watch in each categories. The clustering chosen is hierarchical  as we have only 10 countries to compare**

- **Cluster1 - Canada, Germany,and India - Common interest in Entertainment, News & Politics**
- **Cluster2 - Japan, Mexico & France - Common interest in Entertainment, People&Blogs, Sports**
- **Cluster3 - Korea & Russia - Common interest in Entertainment, News & Politics, People&Blogs**
- **Cluster4 - UK & US - Common interest in Entertainment, Music**


<img src="youtube-trending/Image/country_cluster_sc_giffy.gif" alt="Country_Cluster" width="800"/>


<hr>


**Origin of Videos: Most video have an unknown origin. Of those that do, the highest proportion originate from the US** 


![Origin](youtube-trending/Image/Origin_of_Channels.png)


<hr>


**Canada, Germany and France watch videos originating from over 80 known countries.** 

 
![Origins_by_viewership](youtube-trending/Image/Variation_in_Origin_of_Videos_Watched_in_Each_Country.png)


<hr>


**Canada and the UK watched little content known to originate from within the respective countries, rather most videos watched in these countries orignate in the US. Comparatively, most videos watched in other countries originate from within the respective countries.**


![Origins_vs_viewership](youtube-trending/Image/Source_of_Videos_watched_by_Country.png)


<hr>


**Impact of trending in one region on trending in Others: Just under 8 in 10 videos that trended in multple countries first did so on same day across countries. This suggests that there is no single regional origin of trending for the majority of videos that trend in multiple countries.** 

![Timing_of_Trending_vs_Region](youtube-trending/Image/Whether_videos_that_trended_in_multiple_countries_first_did_so_on_the_same_day_or_different_days.png)

<br>
<br>

## Popularity Analysis: Findings

**What is typically the pattern of trend ? Is it continuous trending or sporadic ?**  
**Trending videos show a continuous trend rather than intermittent**  
**A very high correlation (0.98) between the total trend days and the maximum of  continuous trend days show Trending is a continuous pattern**.  
**Also, 99% of the trends is continuous without a break and only 1% had a break in trending**. 

<img src="youtube-trending/Image/Total_Trending_Vs_Continuous_Trending.png" alt="Total_Trending_Vs_Continuous_Trending" width="800"/>


<hr>


**The more countries videos trended in, the greater the proportion that trend for more than a single day.**

![Days_By_countries_Trended_In](youtube-trending/Image/Mean_Days_Videos_Trended_by_No._of_Countries_Trended_In.png)


<hr>



**For six of ten countries, the majority of videos trend for a single day.In Korea, just under half of videos trend for 2 to 5 days whereas over half of videos in India trended for that interval. US and UK are outliers amoung the countries as the majority of videos that trended in these countries did so for more than five days.** 

![Days_By_countries](youtube-trending/Image/Days_Videos_Trended_by_Country.png)

<hr>

**Maximum Trending days per Country**
- Videos trend in UK from 1 to 38 days
- Videos trend in US from 1 to 29 days
- Videos trend in India from 1 to 10 days
- Videos trend in Canada from 1 to 8 days
- Videos trend in all other countries for less than 8 days

![Max_Trending_per_country](youtube-trending/Image/maxTrendingPerCountry.png)

<hr>

**Top Trending Videos Vs. Viewing Countries**
- Each of the top longest trending videos have trended the longest in the UK
- The same videos that achieves such a high popularity in the UK by trending for 38 days only trends for 0 to 6 days in most other countries and in the US trends for about 10 to 20 days 
- There is a very large difference in the number of days videos trend in UK compared to other countries
- This raises the question do all occurrences of total trending days that are higher than 20 occur in UK ? If this is the case why does this happen?

<img src="youtube-trending/Image/PopularityVsVideoid.png" alt="Popularity_Vs_Videoid"/>

<hr>

**Time To trend Vs Trending Days: Most of the trending videos were published in less than a month ago. There are only few videos those are lateblooms !**

![Latebloom_perc](youtube-trending/Image/Perc_of_Lateblooms.png)

<br>

**The so called "latebloom effect" : Given that a latebloom video is trending, the chance of this video trends >5 days increases with its age !!**
**This shows some light on the external factors behind a video trending**

![Latebloom_effect](youtube-trending/Image/Latebloom_effect.png)


<hr>

 




