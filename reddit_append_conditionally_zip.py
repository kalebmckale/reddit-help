import pandas as pd
"""
Append conditionally within nested for loops by inex

    #Here is my code now to produce a list of strings to later have eval() applied:
    list0 = ('string') #can be of greater length upto 49, but should not have condition
    list1 = ('a','b')
    list2 = ('c','d')
    x_eval=[]
        for location in list0:
            for viewed in list1:
                for doms in list2:
                    x_eval.append(f'df.loc[(df["short_desc"]=="{viewed}") & (df
                    ["location_desc"]=="{location}") & (df["domaincat_desc"]=="
                    {doms}"), "year"]')
    
    # Currently all combinations are being paired; 
    so a and c, a and d, b and c, b and # d, etc. 
    I only want where the indices in list1 and list 2 match to be appended into 
    x_eval; so a and c, b and d pairings only. 
    How would I accomplish this?
"""
list0 = ("string",)
list1 = ("a", "b")
list2 = ("c", "d")

# x_eval = []
# for viewed, doms in zip(list1, list2):
#    x_eval.append(
#        f'df.loc[(df["short_desc"] == "{viewed}") & '
#        f'(df["location_desc"] == "{location}") & '
#        f'(df["domaincat_desc"] == "{doms}"), "year"]'
#    )

x_eval = [
    f'df.loc[(df["short_desc"] == "{viewed}") & '
    f'(df["location_desc"] == "{location}") & '
    f'(df["domaincat_desc"] == "{doms}"), "year"]'
    for viewed, doms in zip(list1, list2)
    for location in list0
]

print(x_eval)

def get_results(df):
    results = [
        df.loc[
            df["short_desc"] == f"{viewed}" & 
            df["location_desc"] == f"{location}" &
            df["domaincat_desc"] == f"{doms}",
            "year"
        ]
        for viewed, doms in zip(list1, list2)
        for location in list0
    ]