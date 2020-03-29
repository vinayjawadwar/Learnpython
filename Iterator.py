nums = [4,5,6,8,55,4]

print(nums[0])

# print(nums[7])           #list index out of range

iterator = iter(nums)
print(iterator)                        # print object of iterator

print(iterator.__next__())
print(iterator.__next__())

print(next(iterator))

for i in nums:
    print(i)


print( "TO PRINT TOP TEN VALUES")
class TopTen:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <=10:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration
value = TopTen()

print(value.__next__())

for i in value:
    print(i)
