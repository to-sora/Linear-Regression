import copy
import matplotlib.pyplot as plt
import numpy as np


class Record:
    def __init__(self, inputdata, target, predict_outcome, errorpercent: bool = True):
        self.target = target
        self.prediction_outcome = predict_outcome
        self.input = inputdata[:3]
        self.errorinpercent = errorpercent
        assert type(self.target) == type(self.prediction_outcome)
        assert type(self.target) != (list or tuple or dict)
        try:
            self.target = float(self.target)
            self.prediction_outcome = float(self.prediction_outcome)
            self.abserror = abs(self.target - self.prediction_outcome)
            self.RM2 = self.abserror ** 2
            if self.errorinpercent:
                self.abserror /= self.target
                self.abserror *= 100
        except:
            try:
                self.target = str(self.target)
                self.prediction_outcome = str(predict_outcome)
                self.correct = True
            except:
                self.target = str(self.target)
                self.prediction_outcome = str(self.prediction_outcome)
        assert type(self.target) == type(self.prediction_outcome)

    def __str__(self):
        if self.errorinpercent:
            return f"Record : Input[3]{self.input[:3]} perdict :{self.prediction_outcome}  error in % {self.abserror}% target {self.target}"

        else:
            return f"Record : Input[3]{self.input[:3]} perdict :{self.prediction_outcome}  abserror {self.abserror} target {self.target}"


class Testreport():
    def __init__(self, numberouput: bool, detail: dict = None):

        self.numberouput = numberouput

        if detail is not None:
            self.detail = detail
        self.detail_record = []

    def addrecord(self, record: Record):
        assert type(record) == Record
        self.detail_record.append(record)

    def analyze(self):
        if self.numberouput:
            self.maxerror = max([x.__dict__['abserror'] for x in self.detail_record])
            self.minerror = min([x.__dict__['abserror'] for x in self.detail_record])
            self.avgerror = sum([x.__dict__['abserror'] for x in self.detail_record]) / len(self.detail_record)

            self.avgRM2 = sum([x.__dict__['RM2'] for x in self.detail_record]) / len(self.detail_record)
            self.maxRM2 = max([x.__dict__['RM2'] for x in self.detail_record])
            self.minRM2 = min([x.__dict__['RM2'] for x in self.detail_record])

    def Drop(self):
        del self.detail_record


class Trainmodelreport:
    def __init__(self):
        self.train = []
        self.val = []

    def adddata(self, datatrain: Testreport = None, datatest: Testreport = None):
        self.train.append(datatrain)
        self.val.append(datatest)

    def reset(self):
        self.val = []
        self.train = []

    def analysis(self):
        self.trainmaxerrorlist = [x.__dict__['maxerror'] if x is not None else int(-1) for x in self.train]
        self.trainminerrorlist = [x.__dict__['minerror'] if x is not None else int(-1) for x in self.train]
        self.trainavgerrorlist = [x.__dict__['avgerror'] if x is not None else int(-1) for x in self.train]
        self.trainmaxRM2list = [x.__dict__['maxRM2'] if x is not None else int(-1) for x in self.train]
        self.trainminRM2list = [x.__dict__['minRM2'] if x is not None else int(-1) for x in self.train]
        self.trainavgRM2list = [x.__dict__['avgRM2'] if x is not None else int(-1) for x in self.train]

        self.valmaxerrorlist = [x.__dict__['maxerror'] if x is not None else int(-1) for x in self.val]
        self.valminerrorlist = [x.__dict__['minerror'] if x is not None else int(-1) for x in self.val]
        self.valavgerrorlist = [x.__dict__['avgerror'] if x is not None else int(-1) for x in self.val]
        self.valmaxRM2list = [x.__dict__['maxRM2'] if x is not None else int(-1) for x in self.val]
        self.valminRM2list = [x.__dict__['minRM2'] if x is not None else int(-1) for x in self.val]
        self.valavgRM2list = [x.__dict__['avgRM2'] if x is not None else int(-1) for x in self.val]

        print(self.trainmaxerrorlist)
        print(self.valmaxerrorlist)
        self.trainindex = [x for x in range(len(self.train))]
        self.valindex = [x for x in range(len(self.val))]
        # print(self.train)
        # print(len(self.train))
        plt.plot(self.trainindex, self.trainmaxerrorlist, label='trainmaxerror')
        plt.plot(self.trainindex, self.trainminerrorlist, label='trainminerror')
        plt.plot(self.trainindex, self.trainavgerrorlist, label='trainavgerror')
        plt.ylabel('Error')
        plt.xlabel('epoch')
        plt.legend()
        plt.show()
        plt.plot(self.trainindex, self.trainmaxRM2list, label='trainmaxRM2')
        plt.plot(self.trainindex, self.trainminRM2list, label='trainminRM2')
        plt.plot(self.trainindex, self.trainavgRM2list, label='trainavgRM2')
        plt.ylabel('Error')
        plt.xlabel('epoch')
        plt.legend()
        plt.show()

        plt.plot(self.valindex, self.valmaxerrorlist, label='valmaxerror')
        plt.plot(self.valindex, self.valminerrorlist, label='valminerror')
        plt.plot(self.valindex, self.valavgerrorlist, label='valavgerror')
        plt.ylabel('Error')
        plt.xlabel('epoch')
        plt.legend()
        plt.show()
        plt.plot(self.valindex, self.valmaxRM2list, label='valmaxRM2')
        plt.plot(self.valindex, self.valminRM2list, label='valminRM2')
        plt.plot(self.valindex, self.valavgRM2list, label='valavgRM2')
        plt.ylabel('Error')
        plt.xlabel('epoch')
        plt.legend()
        plt.show()

        for i in [str(x) for x in self.val[len(self.val) - 1].detail_record]:
            print(i)
        print('trainmaxerrorlist   ' + str(self.trainmaxerrorlist[-1]))
        print('trainminerrorlist   ' + str(self.trainminerrorlist[-1]))
        print('trainavgerrorlist   ' + str(self.trainavgerrorlist[-1]))
        print('trainmaxRM2list     ' + str(self.trainmaxRM2list[-1]))
        print('trainminRM2list     ' + str(self.trainminRM2list[-1]))
        print('trainavgRM2list     ' + str(self.trainavgRM2list[-1]))

        print('valmaxerrorlist     ' + str(self.valmaxerrorlist[-1]))
        print('valminerrorlist     ' + str(self.valminerrorlist[-1]))
        print('valavgerrorlist     ' + str(self.valavgerrorlist[-1]))
        print('valmaxRM2list       ' + str(self.valmaxRM2list[-1]))
        print('valminRM2list       ' + str(self.valminRM2list[-1]))
        print('valavgRM2list       ' + str(self.valavgRM2list[-1]))


class LinearRegression():

    def __init__(self, data: list, path: str = None, constant: float = float(1), errorpercent: bool = True):
        self.constant = constant  # number of input
        self.path = path  # output path
        self.rawdata = copy.deepcopy(data)
        self.errorpercent = errorpercent  # calculate error in percentage
        self.traindataoutput = [float(x[-1]) for x in copy.deepcopy(data)]

        self.numberOfDimensionincludeconstant = int(len(data[0]))
        self.var = [float(0)] * self.numberOfDimensionincludeconstant
        self.trainreport = Trainmodelreport()
        for x in data:
            x[-1] = constant
        self.traindatainput = data
        self.numberofdata = len(data)
        # print(self.rawdata)

    def report(self):

        self.trainreport.analysis()

    def var_multi_input(self, input):
        output = 0
        assert type(input) == list
        for i in range(self.numberOfDimensionincludeconstant):
            output += float(self.var[i]) * float(input[i])
        return output

    def testonvar(self, data, showdetail=False):
        out = Testreport(numberouput=True)

        testoutput = [float(x[-1]) for x in copy.deepcopy(data)]

        for x in data:
            x[-1] = self.constant
        testinput = copy.deepcopy(data)
        numberoftest = len(data)

        for i in range(numberoftest):
            temprecord = Record(testinput[i], float(testoutput[i]), float(self.var_multi_input(testinput[i])),
                                errorpercent=self.errorpercent)
            out.addrecord(temprecord)
        out.analyze()

        return out

    def trainsimpleLR(self, epoch: int = 1, learning_rate: float = 1, learning_decay: bool = True,
                      learning_decay_rate: float = 0.7,
                      printable: bool = True, testdata: list = None,
                      selftest: bool = True, showdot=1):
        self.trainreport.reset()

        for epochs in range(epoch):
            # print( self.traindataoutput)
            if learning_decay:
                a = (1 / (1 + epochs * learning_decay_rate)) * learning_rate
            else:
                a = learning_rate
            for i in range(self.numberOfDimensionincludeconstant):
                temp = [(self.var_multi_input(self.traindatainput[x]) - self.traindataoutput[x])
                        * float(self.traindatainput[x][i])
                        for x in range(self.numberofdata)]
                self.var[i] -= a * sum(temp) / len(temp)
            if printable:
                print(self.var)
            if showdot:
                if epochs % int(showdot) == 0:
                    print()
                print('>', end='')
            temptest = None
            tempselftest = None
            if testdata is not None:
                # print(testdata)
                temptest = self.testonvar(copy.deepcopy(testdata))
                if epochs != epoch - 1:
                    temptest.Drop()
            if selftest:
                tempselftest = self.testonvar(copy.deepcopy(self.rawdata.copy()))
                if epochs != epoch - 1:
                    tempselftest.Drop()
            self.trainreport.adddata(tempselftest, temptest)

    def save(self):
        np.save(self.path, np.asarray(self.var))


def use(input: list, var, constant: float = 1.0):
    """Predict an output using the trained variables.

    Parameters
    ----------
    input : list
        Input feature vector.
    var : list
        Trained weights including the bias as the last element.
    constant : float, optional
        Constant value appended to the input to model the bias term.

    Returns
    -------
    float
        The predicted value.
    """

    assert isinstance(input, list)
    assert len(input) + 1 == len(var)

    data = input + [constant]
    return sum(float(v) * float(x) for v, x in zip(var, data))
# data = list(csv.reader(open('test.csv')))
# test = list(csv.reader(open('val.csv')))
# for x in data:
#     for y in x:
#         y = float(y)
# for x in test:
#     for y in x:
#         y = float(y)
# model=LinearRegression(data,constant=5,errorpercent=False,path='vartest')
# print(model.__dict__)
#
# model.trainsimpleLR(100,0.0000001,printable=False,selftest=True,testdata=test.copy(),showdot=110)
# model.save()
# model.report()
