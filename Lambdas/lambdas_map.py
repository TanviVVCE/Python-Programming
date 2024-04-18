# people = ['Ravi', 'Ajit', 'Nitanshu', 'Thanmayi'] 
# peoples = list(map(lambda x:x.upper(),people))
# for x in peoples:
#     print(x)

# people = ['Ravi', 'Ajit', 'Nitanshu', 'Thanmayi', 'Tanvi'] 
# peoples = list(filter(lambda x: x[0] == 'T',people))
# # for x in peoples:
# #     print(x)

# print(type(people))

# def is_all_strings(l):
#     return all(type(x) == 'str' for x in l)
# print(is_all_strings([2,'a','b']))
# names = ['Arya','Samson','Dora','Tim','Olliwander']
# # print(max([len(x) for x in names]))
# # print(max(names, key = lambda x : len(x)))
# # print(min(songs, lambda x : x['playcount']))['title']

# l = [1,2,3,4,5]
# def extremes(l):
#     return (min(l),max(l))
# print(extremes(l))

# def max_magnitude(l):
#     return max( abs(x)  for x in l)

# print(max_magnitude([1,-2]))

# def sum_even_values(*args):
#     return sum(arg for arg in args if arg % 2 == 0)

# print(sum_even_values(1,2,3,8))

# def sum_floats(*args):
#     return sum(arg for arg in args if type(arg) == float)
# print(sum_floats(1.5, 2.4, 'awesome', [], 1))

# import keyword
# def contains_keyword(*args):
#     return list(filter( lambda arg : keyword.iskeyword(arg) ,list(arg for arg in args if keyword.iskeyword(arg))))
    
# print(contains_keyword("hi","lol","return"))



