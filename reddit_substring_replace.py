"""
More efficient substring replacement of large list of strings?

I have over >300K dict in a list, each dict has about 20 keys and they all need to have a substring replaced. The only solution I could think of is looping through the list, and then through the dictionaries and replacing the keys like so:

    new_list = []
    for each_dict in my_list:
        new_dict = {}
        for key, value in each_dict.items():
            new_dict[key.replace("substring", "newstring")] = value
        new_list.append(new_dict)

There has to be a better way, is there?
"""
my_list = [{"asubstring": 1}, {"asubstring": 2}]


new_list = [
    {key.replace("substring", "newstring"): value for key, value in each_dict.items()}
    for each_dict in my_list
]
