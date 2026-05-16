import pybiomart
import Bio
from faker import Faker
import pandas as pd
import numpy as np
import random
import datetime
column = ["patient_id", "age", "sex", "sample_date", "gene_name", "stop_codon", "start_codon", "length", "gc_content", "strand", "chrom_num","axone_num", 
          "m_name", "m_category", "m_type", "m_length",  
          "w_t_codon", "m_codon", "codon_pos", "w_t_aa", "m_aa", 
          "Phen_Status", "Phen_Name"]
data = pd.DataFrame(columns=column)
data["patient_id"] = np.arange(1000, 2600)
data["age"] = np.random.randint(0.1, 100, size=1600)
data["sex"] = np.random.choice(["male","female"], size=1600)
data["sample_date"] = sorted(np.random.choice(pd.date_range("2020-01-01", periods=1600 ), size=1600))
data["chrom_num"] = np.random.randint(1,24 , size=1600)
data["w_t_codon"] = np.random.choice(["A", "T", "G", "C"], size=1600) + np.random.choice(["A", "T", "G", "C"], size=1600) + np.random.choice(["A", "T", "G", "C"], size=1600)
n="abcdefghijklmnopqrstuvwxyz"
m ="123456789"
data["gene_name"] = np.random.choice(list(n), size=1600) + np.random.choice(list(n), size=1600) + "_" + np.random.choice(list(m), size=1600) + np.random.choice(list(m), size=1600)
data["strand"] = np.random.choice(["+", "-"], size=1600)
for i in range(data["strand"].size):
    if data["strand"][i] == "+":
        data["stop_codon"][i] = np.random.choice(["TAA", "TAG", "TGA"], size=1)
    else: 
        data["stop_codon"][i] = np.random.choice(["TAA", "TAG", "TGA"], size=1)

for i in range(data["strand"].size):
    if data["strand"][i] == "+":
        data["start_codon"][i] = "ATG"
    else:
        data["start_codon"][i] = "CAT"
  
data["length"] = np.random.randint(100, 100000, size=1600)
data["gc_content"] = np.random.uniform(20.0, 80.0, size=1600)
data["axone_num"] = np.random.randint(6, 11, size=1600)

m_name_ext = "1234567890"
for i in range (data["gene_name"].size):
    data["m_name"][i] = data["gene_name"][i] + "_m" + np.random.choice(list(m_name_ext), size=1) + np.random.choice(list(m_name_ext), size=1)

data["m_type"] = np.random.choice( ["SNP", "insertion", "deletion", "substitution"], size=1600)
for i in range(data["m_type"].size):
    if data["m_type"][i] == "SNP":
        data["m_length"][i] = 1
    else:
        data["m_length"][i] = np.random.randint(2, 50, size=1)

for i in range(data["m_type"].size):
    if data["m_type"][i] == "SNP":
        data["m_category"][i] = np.random.choice(["missense", "nonsense", "silent"], size=1)
    elif data["m_type"][i] == "substitution" :
        data["m_category"][i] = np.random.choice(["missense", "nonsense", "silent"], size=1)
    elif (data["m_type"][i] == "insertion" or data["m_type"][i] == "deletion") and data["m_length"][i] % 3 == 0:
        data["m_category"][i] = np.random.choice(["missense", "nonsense", "silent"], size=1) 
    elif (data["m_type"][i] == "insertion" or data["m_type"][i] == "deletion") and data["m_length"][i] % 3 != 0:
        data["m_category"][i] = "frameshift"


c_table = {"phe" : ["TTT" , "TTC"], "leu" : ["TTA", "TTG", "CTT", "CTC", "CTA", "CTG"], "ile" : ["ATT", "ATC", "ATA"], 
           "met" : ["ATG"], "val" : ["GTT", "GTC", "GTA", "GTG"], "ser" : ["TCT", "TCC", "TCA", "TCG", "AGT", "AGC"],
           "pro" : ["CCT", "CCC", "CCA", "CCG"], "thr" : ["ACT", "ACC", "ACA", "ACG"], "ala" : ["GCT", "GCC", "GCA", "GCG"],
           "tyr" : ["TAT", "TAC"], "his" : ["CAT", "CAC"], "gln" : ["CAA", "CAG"], "asn" : ["AAT", "AAC"],
           "lys" : ["AAA", "AAG"], "asp" : ["GAT", "GAC"], "glu" : ["GAA", "GAG"], "cys" : ["TGT", "TGC"],
           "trp" : ["TGG"], "arg" : ["CGT", "CGC", "CGA", "CGG", "AGA", "AGG"], "gly" : ["GGT", "GGC", "GGA", "GGG"],
           "stop" : ["TAA", "TAG", "TGA"]}

for i in range(data["w_t_codon"].size):
    data["w_t_aa"][i] = np.random.choice([value for value in c_table if data["w_t_codon"][i] in c_table[value] ], size=1)

mandf_codon = ["TTT", "TTC","TTA", "TTG", "CTT", "CTC", "CTA", 
           "CTG","ATT", "ATC", "ATA","ATG","GTT", "GTC", "GTA",
             "GTG","TCT", "TCC", "TCA", "TCG", "AGT", "AGC","CCT",
               "CCC", "CCA", "CCG","ACT", "ACC", "ACA", "ACG", "GCT",
                 "GCC", "GCA", "GCG","TAT", "TAC","CAT", "CAC","CAA", 
                 "CAG","AAT", "AAC","AAA", "AAG","GAT", "GAC","GAA", 
                 "GAG","TGT", "TGC","TGG","CGT", "CGC", "CGA", "CGG", 
                 "AGA", "AGG","GGT", "GGC", "GGA", "GGG", "TAA", "TAG", "TGA"]



for i in range (data["m_category"].size):
    if data["m_category"][i] == "nonsense":
        data["m_codon"][i] =np.random.choice(c_table["stop"])
    elif data["m_category"][i] == "silent":
        for j in c_table:
            if data["w_t_codon"][i] in c_table[j] :
                if len(c_table[j]) > 1:
                    data["m_codon"][i] = np.random.choice([codons for codons in c_table[j] if codons != data["w_t_codon"][i]])
                else:
                    data["m_codon"][i] =np.random.choice([codons for codons in mandf_codon if codons != data["w_t_codon"][i] and codons not in ["TAA", "TAG", "TGA"]])
    elif data["m_category"][i] == "missense" or data["m_category"][i] == "frameshift":
        if data["w_t_codon"][i] in mandf_codon:
            data["m_codon"][i] = np.random.choice([codons for codons in mandf_codon if codons != data["w_t_codon"][i] and codons not in ["TAA", "TAG", "TGA"]])

data["codon_pos"] = np.random.randint(1, 100000, size=1600)
for i in range (data["m_codon"].size):
    for j in c_table:
        if data["m_codon"][i] in c_table[j]:
            data["m_aa"][i] = j

for i in range (data["m_category"].size):
    if data["m_category"][i] == "nonsense":
        data["Phen_Status"][i] = "pathogenic"
    elif data["m_category"][i] == "silent":
        data["Phen_Status"][i] = "benign"
    elif data["m_category"][i] == "missense":
        data["Phen_Status"][i] = np.random.choice (["pathogenic", "benign"], p=[0.4, 0.6], size=1)
    elif data["m_category"][i] == "frameshift":
        data["Phen_Status"][i] = np.random.choice (["pathogenic", "benign"], p=[0.9, 0.1], size=1)


for i in range (data["m_category"].size):
    if data["m_category"][i] == "nonsense":
        data["Phen_Name"][i] = np.random.choice (["disease A", "disease B", "disease C"], size=1)
    elif data["m_category"][i] == "silent":
        data["Phen_Name"][i] = "healthy"
    else:
        data["Phen_Name"][i] = np.random.choice (["d_a13", "d_b2", "d_c1", "d_d12", "d_e1" , "d_e12", "d_r12", "d_r1", "f_a18"], size=1)



'''elif data["m_category"][i] == "missense" or data["m_category"][i] == "frameshift":
        for j in c_table:
            if data["w_t_codon"][i] in c_table[j]:
                data["m_codon"][i] = np.random.choice([codons for codons in c_table[j] if codons != data["w_t_codon"][i]], size=1)'''
    

'''def mutanat_codon(m_codon, w_t_codon, m_category):
    m_codon = data["m_codon"]
    w_t_codon = data["w_t_codon"]
    m_category = data["m_category"]
    if m_category == "nonsense":
        m_codon = np.random.choice(c_table["stop"], size=1)
    elif m_category == "silent":
        m_codon = np.random.choice([codons for codons in c_table[i] if w_t_codon in c_table[i] and codons != "stop" and codons != w_t_codon and len(c_table[i]) >1], size=1 )
    elif m_category == "missense":
        m_codon = '''
    
    
    
    
    
    
    
    
    
'''m_category == "silent":
        for i in c_table:
            if w_t_codon in c_table[i]:
                m_codon = np.random.choice(c_table[i], size=1)
    elif m_category == "frameshift" or m_category == "missense":
        m_codon  = np.random.choice(["A", "U", "G", "C"], size=1) + np.random.choice(["A", "U", "G", "C"], size=1) + np.random.choice(["A", "U", "G", "C"], size=1) and m_codon != w_t_codon
    return m_codon'''

'''for i in range(data["m_category"].size):
    if data["m_category"][i] == "nonsense":
        data["m_codon"][i] = np.random.choice(["TAA", "TAG", "TGA"], size=1)
    elif data["m_category"][i] == "silent":
        data["m_codon"][i] = 
    elif data["m_category"][i] == "frameshift":
        data["m_codon"][i] = '''
    

'''data["codon_pos"] = np.random.randint(1, data["m_length"] +1 , size=1600)
'''

'''data["m_length"] = np.random.randint(1, 50, size=1600)
data["m_type"] = np.random.choice(["SNP", "insertion", "deletion"], size=1600)
for i in range(data["m_type"].size):
    if data["m_type"][i] == "SNP" and data["m_length"][i] == 1:
        data["m_category"][i] = np.random.choice(["missense", "nonsense", "silent"], size=1)
    elif data["m_type"][i] == "SNP" and data["m_length"][i] % 3 == 0:
        data["m_category"][i] = np.random.choice(["missense", "nonsense", "silent"], size=1)
    elif data["m_type"][i] == "SNP" and data["m_length"][i] % 3 != 0:
        data["m_category"][i] = "frameshift"
    elif (data["m_type"][i] == "insertion" or data["m_type"][i] == "deletion") and data["m_length"][i] % 3 == 0:
        data["m_category"][i] = np.random.choice(["missense", "nonsense", "silent"], size=1)
    elif (data["m_type"][i] == "insertion" or data["m_type"][i] == "deletion") and data["m_length"][i] % 3 != 0:
        data["m_category"][i] = "frameshift"'''



'''data["m_length"] = np.where(data["m_type"] == "SNP", 1, np.random.randint(2, 100, size=1600))
data["start"] = np.random.randint(1, 100000, size=1600)
data["end"] = data["start"] + data["m_length"] - 1'''





print(data)
print (data.info())


