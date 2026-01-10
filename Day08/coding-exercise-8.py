def calculate_love_score(name1, name2):
    name1 = name1.lower()
    name2 = name2.lower()
    combined_names = name1 + name2
    
    true = ["t","r","u","e"]
    love = ["l","o","v","e"]
    true_count = 0
    love_count = 0
    
    for i in combined_names:
        if i in true:
            true_count += 1
        if i in love:
            love_count += 1
    
    score = int(str(true_count) + str(love_count))
    print(score)
    