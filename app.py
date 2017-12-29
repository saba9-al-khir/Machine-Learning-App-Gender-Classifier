from sklearn import tree

clf = tree.DecisionTreeClassifier()

# CHALLENGE - create 3 more classifiers...
# 1
# 2
# 3

# [height, weight, shoe_size]
X = [[21,181,76,43],[20,175,59,35],[21,160,53,35],[24,180,115,46],[21,170,57,40],[21,175,60,40],[22,183,75,43],[23,181,75,42]
	,[28,157,65,37],[20,181,70,42]]
#[20,168,55,39]
Y = ['male','male', 'female','male','male','male','male','male','female','female']
names = ['elyes','mahmoud','wafa','ghofrane','fedi','sabri','riadh','louez']
Z=['lesbian','straight','gay','lolicon','straight','trap']


# CHALLENGE - ...and train them on our data
clf = clf.fit(X, Y)
age = input("Enter new person's age : ")
height = input("Enter new person's height: ")
weight = input("Enter new person's weight: ")
shoesize = input("Enter new person's shoe size : ")
prediction = clf.predict([[age,height, weight, shoesize]])


# CHALLENGE compare their reusults and print the best one!
print(prediction)