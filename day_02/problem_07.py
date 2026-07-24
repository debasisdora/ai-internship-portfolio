class Dataset:
    def __init__(self,numbers):
        self.numbers=numbers

    def mean(self):
        ans=(sum(self.numbers)/len(self.numbers))
        print("mean: ",ans)
        return ans
    def maximum(self):
        ans=max(self.numbers)
        print("maximum number: ",ans)
        return ans

    def minimum(self):
        ans=min(self.numbers)
        print("minimum number: ",ans)
        return ans

    def summry(self):
        self.mean()
        self.maximum()
        self.minimum()

data=Dataset([10,20,30,40,50,60,70,91])
data.summry()