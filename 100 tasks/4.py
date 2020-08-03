a = {
    'age' : 10,
    'loc_x': 70,
}

b = {
    'loc_y': 50,
    'HP' : 100,
}

c={}

for d in a,b,c:
    c.update(d)

print(c)