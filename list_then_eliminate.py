import pandas as pd

data = pd.read_csv("enjoysport.csv")

X = data.iloc[:, :-1].values
y = data.iloc[:, -1].values

number_of_feature = len(X[0])
version_space = list()

l = [set(X[:,i]) for i in range(number_of_feature)]
[ i.add("?") for i in l]
[ i.add("O") for i in l]

version_space = []
def all_hypothesis(i , l , n , li: list ):
    if i == n :
        version_space.append(li.copy())
        return 
    for j in l[i] : 
        li.append(j)
        all_hypothesis(i+1  , l , n , li )
        li.pop()
        
def check(a : list, b : list):
    n = len(a)
    for i in range(n):
        if (( a[i] != "?" and a[i] != b[i]) or (a[i] == "O")):
            return False
    return True
      
all_hypothesis(0,l,number_of_feature,[]) 


for i in range(len(X)):
    if (y[i]) == "yes":
        hypothesis = []
        for a in version_space:
            if check(a , X[i] ):
                hypothesis.append(a)
        version_space = hypothesis

        



print(version_space)
print(len(version_space))
    
    
        

