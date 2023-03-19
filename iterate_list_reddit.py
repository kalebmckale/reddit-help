lst = ['nonoffensive', ['What', 'in', 'the', 'actual', 'fuck', '?', '#mkr'], ['#mkr', 'WHAT', 'A', 'GODDAMN', 'SURPRISE'], ['This', 'is', 'why', 'this', 'show', 'is', 'ridiculous', '-', "it's", 'not', 'about', 'the', 'cooking', '...', "it's", 'about', 'the', 'game', 'playing', '.', '#mkr', '#whogivesa1'], ['Absolute', 'bloody', 'bullshit', '.', 'So', 'much', 'shit', 'of', 'bull', '.', '#mkr'], ['@MKR_Official', 'a', '1', "isn't", 'strategy', ',', "it's", 'bastedry', '#mkr2015', '#mkr'], 'offensive', ['WTF', '!', '!', '!', 'I', 'not', 'a', 'huge', 'fans', 'of', 'the', 'promo', 'girls', 'but', 'they', 'never', 'voted', 'strategically', '!', 'This', 'sucks', '!', 'Soo', 'annoyed', '!', '#mkr', '#killerblondes']]

for sublst in lst:
    if not isinstance(sublst, list):
        sublst = [sublst]
    for item in sublst:
        print(item)