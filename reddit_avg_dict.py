
def avg_dict(dict_list):
    return list(zip(*(dl.items() for dl in dict_list)))

dl = [
    {
        "val": 1,
        "dist": 1000.0,
        "fact": 1.0
    },
    {
        "val": 2,
        "dist": 1000.0,
        "fact": 1.0
    },
    {
        "val": 3,
        "dist": 1000.0,
        "fact": 1.0
    }
]

#ld = (zip(*t) for t in zip(*(d.items() for d in dl)))

#for col in ld:
#    print('col')
#    for row in col:
#        print(row)
        


avgs = (sum(row[col] for row in dl) for col in set(col for row in dl for col in row))

#print(dict(zip(cols, avgs)))
    
"""
Dict deduplication

Hi,

I'm trying to deduplicate following dict within a list:

    # duplicated lst
    [
      {
        "val": 1,
        "dist": 1000.0,
        "fact": 1.0
      },
      {
        "val": 2,
        "dist": 1000.0,
        "fact": 1.0
      },
      {
        "val": 3,
        "dist": 1000.0,
        "fact": 1.0
      }
    ]

and build following with an average `val` along with keeping all common elements:

    # new
    [
      {
        "val_avg": 2,
        "dist": 1000.0,
        "fact": 1.0
      }
    ]

So far I've managed to deduplicate it, and am currently trying to write average to it:

    [dict(t) for t in {tuple(d.items()) for d in lst}]
    # [{'dist': 1000.0, 'fact': 1.0}]

Thanks for looking and any help is appreciated!
"""