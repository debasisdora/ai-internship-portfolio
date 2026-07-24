def get_gread(score):
    return list("A" if x>=90 else "B" if x>=75 else "C" if x>=60 else "F" for x in score)
score=[95,82,67,45,91,58]
print(get_gread(score))