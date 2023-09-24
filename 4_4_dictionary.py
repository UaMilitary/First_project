def get_grade(key):
    dict = {"F":1, "FX":2,"E":3,"D":3,"C":4, "B":5, "A":5}
    a = dict.get(key)
    return a
 
def get_description(key):
    dict = {"F":"Unsatisfactorily", "FX":"Unsatisfactorily","E":"Enough","D":"Satisfactorily","C":"Good", "B":"Very good", "A":"Perfectly"}
    a = dict.get(key)
    return a

a= get_grade("F")
print(a)

b= get_description("F")
print(b)
