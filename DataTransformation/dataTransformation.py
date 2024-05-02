import pandas as pd;
class Transform:
    def readData(data,self):
        dataFrame = pd.read_csv(data);
        return dataFrame
    def describeData(dataFrame,self):
        dataFrame.describe()

    def findMissingValues(dataFrame,self):
        data.isNull().sum()
