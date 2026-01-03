student_scores = [158, 143, 336, 76, 92, 243, 49, 87, 223]

sum=0
for score in student_scores:
    sum+=score
print(sum)

max=student_scores[0]
for score in student_scores:
    if score>max:
        max=score

print(max)