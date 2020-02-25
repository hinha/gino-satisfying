from sklearn.datasets import load_iris

myiris = load_iris()

x=myiris.data
y=myiris.target
print(x)

feature_names = myiris.feature_names
target_names = myiris.target_names

print("Feature names: ", feature_names)
print("Target names: ", target_names)

print(type(x))
print("5 baris", x[:5])
