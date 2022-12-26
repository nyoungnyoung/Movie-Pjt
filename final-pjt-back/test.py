# movie1= {'title':'제목1','like':3}
# movie2= {'title':'제목2','like':5}
# movie3= {'title':'제목3','like':4}

# movies = [movie1,movie2,movie3]
# sorts = []
# for movie in movies :
#     sorts.append((
#         movie['like'],
#         movie
#     ))
# print(sorts)
# sorts.sort(key=lambda x : -x[0])
# print(sorts)



d = {'A': 3, 'C': 1, 'G': 5, 'T': 2}
d= sorted(d.items(),key=lambda x : (-x[1]))
print(d[0][0])

