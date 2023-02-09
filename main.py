from linearRegression import *
import numpy as np
import csv
def Perform(name):
    data = list(csv.reader(open('traindata.csv')))   # save excel as csv dos
    test = list(csv.reader(open('testdata.csv')))
    for x in data:
        for y in x:
            y = float(y)
    for x in test:
        for y in x:
            y = float(y)
    model=LinearRegression(data,constant=1,errorpercent=False,path='vartest')
    print(model.__dict__)

    model.trainsimpleLR(50,1.5, learning_decay=False,learning_decay_rate=0.9,
                        testdata=test.copy(), selftest=True, showdot=1000,printable=False)
    model.save()
    model.report()
    print()
    print(np.load("vartest.npy"))
    print("weight from seed : A90*3+B90*9+C90*0.23+D90+ 0 *E90")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Perform('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
