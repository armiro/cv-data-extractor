import json
from sklearn import svm

with open('blocks/Blocks - CV%.json', 'r') as file:
    data = json.load(file)

# content = []
# for i in data:
#     for j in i['content'][0]:
#         content.append(j[0])
# print(content)
features = []
labels = []
for elements in data:
    features.append([elements['font_change'], elements['size_change'], elements['has_dot'], elements['has_keyword']])
    labels.append(elements['label'])
# print(features)
# print(labels)

clf = svm.SVC(kernel='rbf')
clf.fit(features, labels)
print(clf.predict([[0, 0, 0, 1]]))

