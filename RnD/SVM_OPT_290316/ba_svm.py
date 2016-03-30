import numpy as np
import csv
from sklearn.svm import SVR
import matplotlib.pyplot as plt

reader   = csv.reader(open("BA.csv","rt"),delimiter=',')
raw_data = np.array(list(reader)[1:])

x_train = []
x_valid = []

y_train = []
y_valid = []

raw_data_list = np.array(raw_data).tolist()

x_train = raw_data_list[:int(len(raw_data_list) / 2)]
x_valid = raw_data_list[int(len(raw_data_list) / 2):]

for i in range(len(x_train)):
    if x_train[i][1] < x_train[i][4]:
        y_train.append(1)
    else:
        y_train.append(-1)

for i in range(len(x_valid)):
    if x_valid[i][1] < x_valid[i][4]:
        y_valid.append(1)
    else:
        y_valid.append(-1)

# remove date column
x_train = [t[1:] for t in x_train]
x_valid = [t[1:] for t in x_valid]

diff = 0
for i in range(0, len(y_train)):
    if y_train[i] != y_valid[i]:
        diff = diff + 1

print(diff)

clf = SVR(C=1.0, epsilon=0.3)
fit = clf.fit(x_train, y_train)

# y_pred = fit.predict(X)

score = clf.score(x_valid, y_valid)

print(score)
# look at the results
#plt.scatter(X, y, c='k', label='data')
# plt.hold('on')
# plt.plot(X, y_pred, c='g', label='RBF model')
# plt.xlabel('data')
# plt.ylabel('target')
# plt.title('Support Vector Regression')
# plt.legend()
# plt.show()
