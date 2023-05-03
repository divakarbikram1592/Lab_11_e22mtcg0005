from Sepal import Sepal
from Petal import Petal
from Flower import Flower

import pickle

sepal_list = []
petal_list = []
flower_list = []

with open("/Users/apple/Documents/Projects-Test/pythonProject/pythonProject/classes/task2/iris.data") as file:
    while line := file.readline():
        extracted_line = line.rstrip()
        # print(extracted_line.split())
        split_line = extracted_line.split(",")
        sepal_length = split_line[0]
        sepal_width = split_line[1]
        petal_length = split_line[2]
        petal_width = split_line[3]
        flower_name = split_line[4]
        selectionScore = float(sepal_length)*0.5+float(sepal_width)*0.75+float(petal_length)*1.2+float(petal_width)*2.5

        objSepal = Sepal(sepal_length, sepal_width)
        objPetal = Petal(petal_length, petal_width)
        objFlower = Flower(flower_name, selectionScore)

        sepal_list.append(objSepal)
        petal_list.append(objPetal)
        flower_list.append(objFlower)


new_list = sorted(flower_list, key=lambda x: x.selectionScore, reverse=True)
top_50_perc = []
for i in range(int(len(new_list)/2)):
    top_50_perc.append(new_list[i])

# save in .pkl file
with open('filename.pickle', 'wb') as handle:
    pickle.dump(top_50_perc, handle, protocol=pickle.HIGHEST_PROTOCOL)


# load the .pkl file
with open('filename.pickle', 'rb') as handle:
    loaded_list = pickle.load(handle)

for x in loaded_list:
    print("Flower Name: ", x.flowerName, ", Selection Score: ", x.selectionScore)