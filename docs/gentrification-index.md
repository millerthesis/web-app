# Gentrification index

This index was created by using Census data from the 2000 Decennial and 2016 American Community Survey and attempts to quantify the level of gentrification of an area by measuring the changes in population of white people, median age, median home value, number of owner-occupied homes, number of people with at least a bachelor's degree and income per capita. These data points were chosen based on similar gentrification analyses by Governing magazine, Cleveland Federal Reserve and the Voorhees Center at the University of Illinois, Chicago.


## The most gentrified areas

(chart/table showing this)

## The factors for this index

This index and composite scoring method is based on the gentrification index produced by the <a href="http://voorheescenter.red.uic.edu/wp-content/uploads/sites/122/2017/10/Voorhees-Center-Gentrification-Index-Oct-14.pdf">Voorhees Center</a> at the University of Illinois, Chicago. These variables are based on factors found to be associated with gentrification in an analysis conducted by Richard Florida of CityLab. In thay analysis, they found the factors that impact gentrification most to be income per capita (positive correlation of .61), number of college-educated residents (.51), and housing prices (.40). They did not rate the number of owner-occupied units or median age for their correlation with gentrification, and they found no correlation between race and gentrification at the neighborhood level. However, the number of owner-occupied units, ages and race are included in the gentrification index produced by the Voorhees center, so I include them in my index.

The index score is assigned to geographies at the Census tract level. This score is calculated by comparing the Census tract's performance in each of the six variables relative to the county it is in. If the Census tract outperformed the county, it received a +1 for that particular variable. If that community underperformed relative to the county, it received a score of -1. Some variables (median home value, income per capita) are associated positively with higher economic status. In these cases, Census tracts that have higher home values than the county received a +1, while home values below the county received a -1. On the other hand, the variable poverty is negatively associated with economic status, so Census tracts that have higher rates of poverty than the County received -1 for that score, and tracts with poverty rates lower than the county received a +1. If the values are equal to that of the county, the variables were assigned a 0. 

To calculate the Gentrification index score for a given Census tract, its scores for each of the six variables were added together. Potential scores range from +6 to -6. 


Based on their index score, Census tracts are divided into three groups: low, middle, and high socioeconomic status. Census tracts with a score between -6 and -3 are considered "low", tracts with a score between -2 and 2 are considered "middle", and tracts with a score between 3 and 6 are considered "high."

To determine whether a tract has changed or not, its index score for 2016 and 2000/2009 were compared. A community is considered to have changed if its index score increases or decreases by more than two points. Then, each tract is categorized by the rate of change. If a tract has changed by more than +3/4 points, it is considered to be gentrified.


**From 2000 to 2016**
The variable score assignments are as follows:

- Percent white population (non-hispanic), Above City Average - Positive (+1)
- % Below Poverty, Above City Average - Negative (-1)
- Median home values, Above City Average - Positive (+1)
- % Owner-occupied home, Above City Average - Positive (+1)
- % of population with bachelor's degree or higher, Above City Average - Positive (+1)
- Income per capita, Above City Average - Positive (+1)



### Change in white population

This is considered to be a factor in gentrification based on the study by Governing magazine. In their analysis on gentrification, they found that "compared to lower-income areas that failed to gentrify, gentrifying Census tracts recorded increases in the non-Hispanic white population." However, in the analysis conducted by Richard Florida of CityLab, they did not find the population of white residents to be correlated with gentrification. That said, the increase in the total white population is often considered to be a sign of gentrification in a neighborhood, so I include it in my index. However, because it was not found to have a significant correlation with gentrification, I give it a low weighting of .05.

### Below poverty level

As neighborhoods gentrify, poorer residents become displaced by rising rents. This change may be reflected in Census data through fewer amounts of people who live below the poverty level, as those communities move to other areas that are more affordable. In their <a href="http://voorheescenter.red.uic.edu/wp-content/uploads/sites/122/2017/10/Voorhees-Center-Gentrification-Index-Oct-14.pdf">Gentrification index</a>, the Voorhees Center at the University of Illinois, Chicago included percent of people below poverty in their index. They based their inclusion of this variable on the research done by David Ley, specifically, “Gentrification in Recession: Social Change in Six Canadian Inner Cities, 1981-1986.”  


### Change in median home value

Both the CityLab analysis and the Cleveland Federal Reserve report include rising home values as indicators of gentrifying areas. In the Cleveland Federal Reserve study, Hartley exclusively used median home prices to measure whether an area had gentrified between 2000 and 2007. He defines gentrification as a Census Tract "that moved from the bottom half of the distribution of home prices in the metropolitan area to the top half between 2000 and 2007." Meanwhile, the CityLab analysis found that home values had a positive correlation with gentrification of .40. Therefore, I chose to give it a weight of .20 in my index.

### Change in owners v. renters

As neighborhoods gentrify, rent prices tend to <a href="https://gjplp.org/2017/09/05/examining-the-negative-impacts-of-gentrification/">increase</a> as luxury condominiums and high-rises replace poorer, older buildings. Similarly, units become converted from rental apartments to condominiums, townhomes and single-family homes for <a href="https://www.tandfonline.com/doi/pdf/10.1080/02723638.2016.1276718">ownership</a>. While the other analyses did not use the proportion of owner-occupied homes as a factor in measuring gentrification, I include it in my index, but give it a lesser weight of (.15).

### Change in population with bachelor's degree

Both analyses that I considered in creating my index rate the population of college-educated residents as an important factor in measuring gentrification. The CityLab analysis found that college-educated residents had a positive correlation with gentrification of .51. Similarly, the University of Massachusetts - Boston found that in gentrifying neighborhoods the population of those with college-degrees <a href="https://scholarworks.umb.edu/cgi/viewcontent.cgi?referer=https://www.google.com/&httpsredir=1&article=1027&context=honors_theses">increased</a> over time. Therefore, I give it a weight of .25 in my index.

### Income per capita

Finally, I include income per capita in the index because it was found to have a positive correlation of .61 with gentrification, the highest of any other factor measured in the CityLab study. Thomas B. Edsall, an opinion writer and researcher, <a href="https://www.nytimes.com/2015/02/25/opinion/the-gentrification-effect.html">wrote</a> in 2015 that "education and income move in tandem – that is, levels of per capita income follow the same pattern as levels of educational attainment." Because of its perceived impact on the level of gentrification in areas, I include it in my index with the highest weight of .30.






