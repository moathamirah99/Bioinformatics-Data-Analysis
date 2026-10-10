first_step = str(input("what do you want to analyze DNA or RNA?"))
if first_step == "DNA".lower():
    alynin_or_analyze = str(input("do you want to alynin two SEQ or analyze one SEQ?"))
    if alynin_or_analyze == "alynin":
        seq1 = str(input("enter oreginal SEQ:")).upper()
        seq2 = str(input("enter your SEQ:")).upper()
        z = ""
        for i in range(len(seq1)):
            
            if seq1[i] == seq2[i]:
                z += " "
            else:
                z += "x"

        print(seq1)
        print("mutations location: ", z)
        print(seq2)
        semilarity = z.count(" ") / len(seq1) * 100
        print("semilarity = ", semilarity)
        mutations = z.count("x")
        print("mutation = ", mutations)
    elif alynin_or_analyze == "analyze":
        seq = str(input("please enter your SEQ:")).upper()
        a_count = seq.count("A")
        t_count = seq.count("T")
        c_count = seq.count("C")
        g_count = seq.count("G")
        total_count = len(seq)
        C_G_content = (c_count + g_count) / total_count * 100
        ceq_complement = ""
        for i in seq:
            if i == "A":
                ceq_complement += "T"
            elif i == "T":
                ceq_complement += "A"
            elif i == "C":
                ceq_complement += "G"
            elif i == "G":
                ceq_complement += "C"
        rev_complement = ceq_complement[::-1]
        print(total_count)
        print(C_G_content)
        print(ceq_complement)  
        print(rev_complement)      


