import json
import os
from sklearn import svm

features_train = []
labels_train = []

for i in range(1, 10):
    path = 'blocks/Blocks - CV%d.json' % i
    if os.path.exists(path):
        with open(path, 'r') as f:
            data = json.load(f)
        for elements in data:
            features_train.append(
                [elements['font_change'], elements['size_change'], elements['has_dot'], elements['has_keyword']])
            labels_train.append(elements['label'])


features_test = []
labels_test = []
with open('./Blocks.json', 'r') as test:
    data_test = json.load(test)

content = []
for e in data_test:
    content.append(e['content'][0])
    features_test.append(
        [e['font_change'], e['size_change'], e['has_dot'], e['has_keyword']])


# print(features_train)
# print(labels_train)
# print(features_test)

clf = svm.SVC(kernel='rbf')
clf.fit(features_train, labels_train)

for f in features_test:
    labels_test.append(clf.predict([f]))

# for i in range(len(content)):
#     print(content[i], labels_test[i])

new_content = []
l = 0
while l < len(labels_test):
    if labels_test[l] == 1:
        # print(l)
        con = content[:l]
        print(con)
        new_content.append(con)
        content = content[l:]
        # print(content)

    l += 1

# print(new_content)
# for i in new_content:
#     print(i)
