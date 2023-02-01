from linearRegression import *
def Perform(name):


    data = list(csv.reader(open('test.csv')))
    test = list(csv.reader(open('val.csv')))
    for x in data:
        for y in x:
            y = float(y)
    for x in test:
        for y in x:
            y = float(y)
    model=LinearRegression(data,constant=5,errorpercent=False,path='vartest')
    print(model.__dict__)

    model.trainsimpleLR(100,0.0000001,printable=False,selftest=True,testdata=test.copy(),showdot=110)
    model.save()
    model.report()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Perform('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
