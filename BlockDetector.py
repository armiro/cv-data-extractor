import json
from sklearn import svm

features_train = []
labels_train = []
for i in (4, 5, 6, 7, 9, 10, 12, 13, 14):
    path = 'blocks/Blocks - CV%d.json' % i
    with open(path, 'r') as f:
        data = json.load(f)
    for elements in data:
        features_train.append(
            [elements['font_change'], elements['size_change'], elements['has_dot'], elements['has_keyword']])
        labels_train.append(elements['label'])
# content = []
# for i in data:
#     for j in i['content'][0]:
#         content.append(j[0])
# print(content)

features_test = []
labels_test = []
with open('./Blocks.json', 'r') as test:
    data_test = json.load(test)

for e in data_test:
    features_test.append(
        [e['font_change'], e['size_change'], e['has_dot'], e['has_keyword']])

# print(features_train)
# print(labels_train)
print(features_test)

clf = svm.SVC(kernel='rbf')
clf.fit(features_train, labels_train)

for f in features_test:
    labels_test.append(clf.predict([f]))

print(labels_test)
