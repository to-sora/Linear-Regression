from linearRegression import *
import numpy as np
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

    model.trainsimpleLR(5000, 0.1, learning_decay=False,learning_decay_rate=0.7,
                        testdata=test.copy(), selftest=True, showdot=0,printable=False)
    model.save()
    #model.report()
    print(np.load("vartest.npy"))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Perform('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
