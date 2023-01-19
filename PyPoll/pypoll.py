#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import csv



with open(os.path.join("Resources","election_data.csv"), "r") as in_file:
    in_csv = csv.reader(in_file)
    header = next(in_csv) 
    data = list(in_csv)

    count = 0
    for row in data:
        count += 1
    

    print('Election Results')

    print("-" * 30)
    print(f"Total votes: {count:,}"  )
    print("-" * 30)



    candidate_names = []

    for row in data:
        if row[2].strip() not in candidate_names:

            candidate_names.append(row[2])
        else:
            continue

    voters = {}
    for cand in candidate_names:
        total_vote = 0
        for row in data:
            if row[2] == cand:
                total_vote +=1
                
        voters[cand]= total_vote
                

        print(f"{cand}: {round((total_vote/count)*100, 3)} % ({total_vote:,}) ")
    winner_vote = max(voters.values()) 
    winner = list(voters.keys())[list(voters.values()).index(winner_vote)]


    print("-" * 30)

    print(f"Winner:  {winner}")

    print("-" * 30)


# In[ ]:





# In[ ]:




