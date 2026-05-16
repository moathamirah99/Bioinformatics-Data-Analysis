import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

rna_data = pd.read_csv("/home/acer/test_numpy/csv_files/METABRIC_RNA_Mutation.csv",low_memory=False)
'''print (rna_data.info())'''
#print (rna_data.iloc[:5, 11:22])
#print(rna_data.columns[100:200])
#print(len(rna_data.columns))

short_data = rna_data.loc[:,["age_at_diagnosis", "pam50_+_claudin-low_subtype","her2_status"]]
print (short_data.head())
print (short_data["pam50_+_claudin-low_subtype"].unique())
#-------------------------------------------------
plt.subplot(2,2,1)
plt.rcParams.update({'font.size' : 11})
plt.bar(short_data["pam50_+_claudin-low_subtype"].value_counts().index,
         short_data["pam50_+_claudin-low_subtype"].value_counts(),
           color=['red', 'blue', 'green', 'yellow', 'purple', 'orange', 'pink'],
           edgecolor='black')
plt.title("PAM50 Subtype Distribution", pad = 10 , fontsize = 10)
plt.xlabel("PAM50 Subtypes")
plt.ylabel("Number of Patients")
#-------------------------------------------------
plt.subplot(2,2,2)
plt.bar(short_data["her2_status"].value_counts().index,
         short_data["her2_status"].value_counts(), )
plt.xticks(fontsize = 10)
plt.yticks(fontsize = 10)
plt.title("HER2 Status Overview", pad = 10 , fontsize = 10)
plt.xlabel("HER2 Status")
plt.ylabel("Count")

#-------------------------------------------------
plt.subplot(2,2,3)
age50 = (short_data["age_at_diagnosis"]>=50)
age30 = (short_data["age_at_diagnosis"]<50) & (short_data["age_at_diagnosis"]>=30)
age10 = (short_data["age_at_diagnosis"]<30) & (short_data["age_at_diagnosis"]>=0)

plt.pie([age50.sum(), age30.sum(), age10.sum(),],
        labels=['Age >= 50', 'Age 30-49', 'Age 1-29'], textprops={'fontsize': 15},
        autopct='%1.1f%%',
        startangle=140)
plt.title("Age Groups at Diagnosis", pad = 10 , fontsize = 10)

#-------------------------------------------------
basal = short_data["pam50_+_claudin-low_subtype"] == "Basal"
LumA = short_data["pam50_+_claudin-low_subtype"] == "LumA"
LumB = short_data["pam50_+_claudin-low_subtype"] == "LumB"
Her2 = short_data["pam50_+_claudin-low_subtype"] == "Her2"
normal = short_data["pam50_+_claudin-low_subtype"] == "Normal"
NC = short_data["pam50_+_claudin-low_subtype"] == "NC"
basal_age = (short_data[basal]["age_at_diagnosis"])
lumA_age = (short_data[LumA]["age_at_diagnosis"])
lumB_age = (short_data[LumB]["age_at_diagnosis"])
Her2_age = (short_data[Her2]["age_at_diagnosis"])
normal_age = (short_data[normal]["age_at_diagnosis"])
NC_age = (short_data[NC]["age_at_diagnosis"])

box_age = {"basal_age":basal_age,"lumA_age" :lumA_age, 
           "lumB_age": lumB_age, "Her2_age": Her2_age, 
           "normal_age" : normal_age, "NC_age" : NC_age}
s_age = list(box_age.keys()) 
k_age = list(box_age.values())           
plt.subplot(2,2,4)
plt.boxplot(k_age, labels= s_age , patch_artist=True,
            boxprops=dict(facecolor = 'lightblue' , color = 'blue'))
plt.xticks(fontsize = 10)
plt.yticks(fontsize = 10)
plt.title("Age Distribution by Subtype", pad = 10 , fontsize = 10)
plt.xlabel("PAM50 Subtypes")
plt.ylabel("Age at Diagnosis (Years)")

#--------------------------------------------------------
plt.tight_layout()
plt.show()

#--------------------------------------------------------
#--------------------------------------------------------
#--------------------------------------------------------


death_data = rna_data.loc[ : , ["overall_survival_months",
                                "overall_survival",
                                "age_at_diagnosis",
                                "pam50_+_claudin-low_subtype",
                                "her2_status"]]
print(death_data)

m_age60= (death_data["age_at_diagnosis"] >=60) 
m_age50= (death_data["age_at_diagnosis"] <60) & (death_data["age_at_diagnosis"] >=50) 
m_age40=(death_data["age_at_diagnosis"] <50) & (death_data["age_at_diagnosis"] >=40) 
m_age30=(death_data["age_at_diagnosis"] <40) & (death_data["age_at_diagnosis"] >=30) 
m_age_bellow30 =( death_data["age_at_diagnosis"] <30) & (death_data["age_at_diagnosis"] >0) 
osm_m60 = (death_data[m_age60]["overall_survival_months"])
osm_m50 = (death_data[m_age50]["overall_survival_months"])
osm_m40 = (death_data[m_age40]["overall_survival_months"])
osm_m30 = (death_data[m_age30]["overall_survival_months"])
osm_m30_b = (death_data[m_age_bellow30]["overall_survival_months"])

box_age_suviaval_dict = {"osm_m60": osm_m60 , "osm_m50":osm_m50,
                          "osm_m40":osm_m40, "osm_m30":osm_m30,
                          "m_age_bellow30":osm_m30_b}


plt.subplot(2,2,1)
plt.boxplot(box_age_suviaval_dict.values(),
             labels=["m_age60", "m_age50" ,
                     "m_age40" , "m_age30", "m_age_bellow30"],
                     patch_artist= True,
                     boxprops= dict(facecolor = 'lightblue'))
plt.xticks(fontsize = 10)
plt.yticks(fontsize = 10)
plt.xlabel("Age Groups")
plt.ylabel("Overall Survival (Months)")

#---------------------------------------------------------------
# بدي اطلع الاعمار اللي ماتو فيها المرضى 
plt.subplot(2,2,2)
only_dide_mask = death_data["overall_survival"] == 1
only_alive_mask = death_data["overall_survival"] == 0

only_dide = death_data[only_dide_mask].copy()
only_dide["only_dide_age"] = ((only_dide["age_at_diagnosis"]) +
                               (only_dide["overall_survival_months"]/12))
print(only_dide["only_dide_age"])
d70 = only_dide["only_dide_age"] >= 70
d60 = (only_dide["only_dide_age"] < 70 )& (only_dide["only_dide_age"] >= 60)
d50 = (only_dide["only_dide_age"] < 60) & (only_dide["only_dide_age"] >= 50)
d40 = (only_dide["only_dide_age"] < 50) & (only_dide["only_dide_age"] >= 40)
d30 = (only_dide["only_dide_age"] < 40) & (only_dide["only_dide_age"] >= 30)
d20 = (only_dide["only_dide_age"] < 30) 

only_dide_dict = [d70.sum(), d60.sum(), d50.sum(), 
                  d40.sum(), d30.sum(), d20.sum()]
plt.pie(only_dide_dict ,labels= ["age70+","age60-69","age50-59",
                                 "age40-49","age30-39","age<30"],
                                  autopct='%1.1f%%' ,
                                  textprops= {'fontsize' : 10})


#-------------------------------------------------------------------
#بدي اربط بين ال pam50 و حالة العيش اذا المريض مات او لا 
plt.subplot(2,2,3)
b_basal = death_data["pam50_+_claudin-low_subtype"] == "Basal"
b_LumA = death_data["pam50_+_claudin-low_subtype"] == "LumA"
b_LumB = death_data["pam50_+_claudin-low_subtype"] == "LumB"
b_Her2 = death_data["pam50_+_claudin-low_subtype"] == "Her2"
b_normal = death_data["pam50_+_claudin-low_subtype"] == "Normal"
b_NC = death_data["pam50_+_claudin-low_subtype"] == "NC"

dbasal = (b_basal & only_dide_mask).sum()
abasal = (b_basal & only_alive_mask).sum()
dLumA = (b_LumA & only_dide_mask).sum()
aLumA = (b_LumA & only_alive_mask).sum()
dLumB = (b_LumB & only_dide_mask).sum()
aLumb = (b_LumB & only_alive_mask).sum()
dHer2 = (b_Her2 & only_dide_mask).sum()
aHer2 = (b_Her2 & only_alive_mask).sum()
dnormal = (b_normal &only_dide_mask).sum()
anormal = (b_normal & only_alive_mask).sum()
dNC = (b_NC & only_dide_mask).sum()
aNC = (b_NC & only_alive_mask).sum()
pam50_death_stat_dict = ["b_basal","b_LumA" ,"b_LumB" ,"b_Her2",
                            "b_normal" ,"b_NC" ] 
alive_count = [abasal,aLumA,aLumb,aHer2,anormal,aNC]
dead_count = [dbasal,dLumA,dLumB,dHer2,dnormal,dNC]
plt.bar(pam50_death_stat_dict, alive_count, label = "alive" , color = 'lightblue')
plt.bar(pam50_death_stat_dict, dead_count,bottom=alive_count, label = "dead", color = 'red')
plt.xticks(fontsize = 10)
plt.yticks(fontsize = 10)
plt.xlabel("PAM50 Subtypes")
plt.ylabel("Number of Patients")
#------------------------------------------------------------
#قبل شوي عرفت انو في اشي اسمو crosstab اسهل اللي 🙂🙂

plt.subplot(2,2,4)
her2_pam50 = pd.crosstab(death_data["pam50_+_claudin-low_subtype"],
                         death_data["her2_status"])
her2_pam50.plot(kind = 'bar', stacked= False, ax=plt.gca())
plt.xticks(fontsize = 10)
plt.yticks(fontsize = 10)
plt.xlabel("PAM50 Subtypes")
plt.ylabel("Frequency")
plt.legend(title='HER2 Status') 
plt.show()
#-----------------------------------------------------------------
#-----------------------------------------------------------------
#-----------------------------------------------------------------
plt.subplot(1,2,1)
print(rna_data["tp53"])
gen_data = rna_data.loc[:,["tp53","pam50_+_claudin-low_subtype",
                        "brca1","brca2"]]
x = gen_data["pam50_+_claudin-low_subtype"]
y = gen_data["tp53"]
gen_data.boxplot(column = "tp53", by = "pam50_+_claudin-low_subtype",
                  color ='C1', ax= plt.gca())
plt.xticks(fontsize = 10)
plt.yticks(fontsize = 10)
plt.xlabel("PAM50 Subtypes")
plt.ylabel("TP53 Expression Level")

#--------------------------------------------------------------------
plt.subplot(1,2,2)
gen_corr = gen_data[["tp53","brca1","brca2"]].corr(numeric_only= True)
plt.imshow(gen_corr, cmap= 'coolwarm')
plt.title("tp53 ,brca1 ,brca2 heatmap ", pad = 20)
plt.xticks([0,1,2],["tp53", "brca1", "brca2"])
plt.yticks([0,1,2],["tp53", "brca1", "brca2"])
for i in range(3):
 for j in range(3):
  value = gen_corr.iloc[i, j]
  plt.text(j, i, round(value,2) , ha = 'center', va = 'center' , color = 'white', fontsize = 10)
plt.colorbar()
plt.xticks(fontsize = 10)
plt.yticks(fontsize = 10)
plt.show()

print(rna_data.corr(numeric_only= True))
m_data = rna_data.iloc[:, :15]
plt.imshow(m_data.corr(numeric_only = True), cmap= 'coolwarm')
plt.show()
# 'line', 'bar', 'barh', 'kde', 'density', 'area', 'hist', 'box', 'pie', 'scatter', 'hexbin'