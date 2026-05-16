import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

mortality_data = pd.read_csv("/home/acer/test_numpy/csv_files/" \
"Global Health And Disease Burden 2024.csv")
print(mortality_data.head())
print(mortality_data.info())
print(mortality_data["Country"])


# i want to see wich contry has the highest mortality rate and the highst canser death
#the i want ro see wich Country has the least 


high_mortality  = mortality_data.loc[ : , ["Country", "Cancer_Deaths_per_100k", 
                                      "Cardiovascular_Deaths_per_100k",
                                      "Healthcare_Spending_Percent_GDP"  ,  
                                       "Physician_Density_per_1000"  ,   
                                       "Hospital_Beds_per_1000"  ,
                                       "Vaccination_Coverage_DTP3_Percent"]]

sorted_cancer = high_mortality.sort_values('Cancer_Deaths_per_100k')
print(sorted_cancer)
plt.subplot(2,2,1)
most3 = sorted_cancer.tail(3)
least3 = sorted_cancer.head(3)
m_l3 = pd.concat([most3,least3])
plt.bar(m_l3["Country"],m_l3["Cancer_Deaths_per_100k"] ,
         color = "#6c0811dc" , edgecolor = 'black', )
plt.title("cancer death rate", pad=15)

plt.xticks(rotation = 45)
plt.ylabel("death pear 100k", color = 'black')

# the most cancer death is "Slovenia" and the least is "Singapore"

# now lets compare between between lowest 3 country and the highst 3 country 
# i will compare between them by the 
# 1 Healthcare_Spending_Percent_GDP    
# 2 Physician_Density_per_1000         
# 3 Hospital_Beds_per_1000             
# 4 Vaccination_Coverage_DTP3_Percent 

'''#---------------------------------------------------------------------'''


## 1 Healthcare_Spending_Percent_GDP
plt.subplot(2,2,2)
print(m_l3.info()) 
plt.bar(m_l3["Country"],m_l3["Healthcare_Spending_Percent_GDP"], 
        color = 'skyblue', edgecolor = 'black', linewidth = 3 )
plt.title("Healthcare_Spending_Percent_GDP")
plt.ylabel("Healthcare_Spending")
plt.xticks(rotation = 45)
'''#-------------------------------------------------------------------------
'''

#2Physician_Density_per_1000
plt.subplot(2,2,3)
print(m_l3.info()) 
plt.bar(m_l3["Country"],m_l3["Physician_Density_per_1000"], 
        color = "#151ce3dc", edgecolor = 'black', linewidth = 3 )
plt.title("Physician_Density_per_1000")
plt.ylabel("Physician_Density")
plt.xticks(rotation = 45)
'''#-------------------------------------------------------------------------'''


#3Hospital_Beds_per_1000
plt.subplot(2,2,4)
print(m_l3.info()) 
plt.bar(m_l3["Country"],m_l3["Hospital_Beds_per_1000"], 
        color = "#e3d215dc", edgecolor = 'black', linewidth = 3 )
plt.title("Hospital_Beds_per_1000")
plt.ylabel("Hospital_Beds")
plt.xticks(rotation = 45)
'''#---------------------------------------------------------------------------'''
plt.tight_layout()
plt.show()
'''#---------------------------------------------------------------------------'''
#this result by the bar output shows somthing abnormal 
#th more you have doctor or bed or the more you spend the more the death is higher 
#but thats not an evidence because when you have a lot of people that have cancer 
#you may also have more beds or doctor 
#so what i mean is that these bars show us that its probably 
#because these country have more patiant the have more beds and doctor and spend more on the health care  


#****(or it might be the age so because canser is realted to age that the older people 
#are more likely to get canser than the young people and the country with more death 
#in canser are maibe are have a higher rate in old people or have alot of old people)*** 

#so now i want to see if these contry that have more cancer death have a high mortality
#age
 
'''----------------------------------------------------------------------------------'''
'''----------------------------------------------------------------------------------'''
'''----------------------------------------------------------------------------------'''

print(mortality_data.loc[:,["Country","Life_Expectancy_2023"]])

c_mortality_rate = mortality_data.loc[:,["Country","Life_Expectancy_2023", 
                                         "Adult_Mortality_Rate_M_per_1000",
                                         "Adult_Mortality_Rate_F_per_1000",
                                         "Cancer_Deaths_per_100k"]]
sorted_c_mortality_rate = c_mortality_rate.sort_values('Cancer_Deaths_per_100k')
most_3 = sorted_c_mortality_rate.tail(3)
least_3 = sorted_c_mortality_rate.head(3)
ml3m = pd.concat([most_3,least_3])

'''====================================================================='''
plt.figure(figsize=(12,5))
plt.subplot(1,2,1)
plt.bar(ml3m["Country"],ml3m["Life_Expectancy_2023"])
plt.title("Life_Expectancy_2023")
plt.ylabel("Life_Expectancy")
plt.xticks(rotation = 45)

'''====================================================================='''
plt.subplot(1,2,2)
plt.bar(ml3m["Country"],ml3m["Adult_Mortality_Rate_M_per_1000"] )
plt.title("Adult_Mortality_Rate_M_per_1000")
plt.ylabel("Adult_Mortality")
plt.xticks(rotation = 45)
plt.show()

#hear we can see that there is no clear evedence that spending more on the
#health care can lower the cancer death rate 
#but we should not forgot that these country gave very good econmy and health care 
#and ther are alot of factor that can effect theas numbers like the cancer type 
#or the age that the cancer have been examined etc


#but lets see what can the Life_Expectancy show us 

plt.scatter(mortality_data["Life_Expectancy_2023"], mortality_data["Cancer_Deaths_per_100k"])
plt.xticks()
plt.show()


#this figuer showes what i expected that all tha contry in this data are 
#advanced country so all of them have a high Life_Expectancy 
#thast why nost of them have a high cancer death beacause the cancer 
#is related to the age when the person gets older the have mor risc 
#to have cancer and die from it 

'''=============================================================================
   ============================================================================='''

#now lets see the defference between the cancer 
#and other deaths to see what cause the most deaths in thease contery
#and see which contry have the youngest deaths
 
di_deaths = mortality_data.loc[:,["Country","Cardiovascular_Deaths_per_100k",
                                  "Respiratory_Deaths_per_100k",
                                    "Diabetes_Deaths_per_100k", 
                                     "Road_Injury_Deaths_per_100k",
                                     "Cancer_Deaths_per_100k"]]
         
t_Cardiovascular_Deaths = di_deaths["Cardiovascular_Deaths_per_100k"].sum()
t_Respiratory_Deaths = di_deaths["Respiratory_Deaths_per_100k"].sum()
t_Diabetes_Deaths = di_deaths["Diabetes_Deaths_per_100k"].sum()
t_Road_Injury_Deaths_per_100k = di_deaths["Road_Injury_Deaths_per_100k"].sum()
t_Cancer_Deaths_per_100k = di_deaths["Cancer_Deaths_per_100k"].sum()

t_label_dict = {"Cardiovascular_Deaths":t_Cardiovascular_Deaths,
                "Respiratory_Deaths" : t_Respiratory_Deaths, 
                "Diabetes_Deaths" : t_Diabetes_Deaths,
            "Road_Injury_Deaths" : t_Road_Injury_Deaths_per_100k,
             "Cancer_Deaths" : t_Cancer_Deaths_per_100k}

plt.pie(t_label_dict.values(), labels= t_label_dict.keys(), autopct = '%1.1f%%')
plt.show()
'''=============================================================================='''
#this pie chart shows us that the most diease that causing death 
#is cancer this is conceder normal because that the contry that
#im macking the analisis are developed countery 
#but ther is an importanat question what are the factor that control the 
#cancer dises 
#now i want to get another data to compare these contry with less developed
#countrys to see the cancer spreading between countrys and the factor that control it 
#is it that the more the have polution or any other factor 
#and i will get data from less country this time

'''============================================================================='''
'''============================================================================='''

#befor we get another data lets make one last thing 
#lets see the continental distribution of cancer

cacer_contenent = mortality_data.loc[:,["Region", "Cancer_Deaths_per_100k"]]
contenent_avg = cacer_contenent.groupby('Region')["Cancer_Deaths_per_100k"].mean()
print(contenent_avg)
plt.subplot(1,2,1)
plt.pie(contenent_avg, labels=contenent_avg.index, autopct = '%1.1f%%' )
plt.subplot(1,2,2)
plt.bar(contenent_avg.index, contenent_avg)
plt.show()

         
 
 
 







#age_of_death = mortality_data.loc[: , ["Population_2023","Life_Expectancy_2023","Infant_Mortality_Rate_per_1000",  ]]





