"""
regex in python

11:52 AM    <DIR>          Anaconda3 (64-bit)\\r\\n24-07-2021  09:13 PM    <DIR>          Android Studio\\r\\n24-09-2020  10:55 PM    <DIR>          AnyDesk\\r\\n09-08-2020  10:12 AM               696 Audacity.lnk\\r\\n27-04-2021  12:21 AM             2,158 Avast Free Antivirus.lnk\\r\\n28-07-2021  

this is my string i want to separate all the folder name using regex so i need all the name between 2 continuous spaces and \\r so i use re.findall("  \[a-zA-Z0-9\]\\\\r",string1) but it give me empty output can anyone please help me

"""
text="""11:52 AM    <DIR>          Anaconda3 (64-bit)\r\n24-07-2021  09:13 PM    <DIR>          Android Studio\r\n24-09-2020  10:55 PM    <DIR>          AnyDesk\r\n09-08-2020  10:12 AM               696 Audacity.lnk\r\n27-04-2021  12:21 AM             2,158 Avast Free Antivirus.lnk\r\n28-07-2021  """

import re

#search_pattern = re.compile(r'<DIR>\s+(\w+)\s+')
search_pattern = re.compile(r'<DIR>[ ]+(.+?)(?:\r|\\r)*(?:\n|\\n)')
#search_pattern = re.compile(r'<DIR>[ ]+([A-Za-z0-9 _()-]+?)\r\n')
print(search_pattern.findall(text))
