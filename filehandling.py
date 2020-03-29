# if you want to store temprary data in some variable ,but what if you want to save data in persistant way simply for alonger period
# when you close the application you will loss all the data ,so we want even if i close app my data should be stored somewere
# using
# relational database but it is diff
# so best is "  its text"


f = open("My Data", 'r')                    #'r' & f.read() is for read 'MyData'
print(f.read())

#print(f.readline())                      # read first line
#print(f.readline())                      # read second line
#print(f.readline(4),end="")                 read 4 characters

#f1 = open("abc" , 'w')                 # 'w' means to write in file if file not present then it will create new file

#f1.write("something  ")
#f1.write("people")

f1 = open("abc", 'w')
f1.write("laptop  ")                         # after above code removing and writing new data if we use 'w' then we get lost previous data

# to avoide data loss we have to append 'a' file instead of write

f1 = open("abc", 'a')

f1.write("something  ")
f1.write("people    ")


# for copying data from mydata to abc
f = open("My Data", 'r')
f1 = open("abc", 'a')

for data in f:                        # it feaching data one by one
    f1.write(data)                  # get written all data from f to f1


# for reading image.jpg file

f3 = open('capture.JPG','rb')                    # image.jpg read in binary format so 'rb'
f4 = open('mypic.JPG','wb')                    # write binary


for i in f3:
    f4.write(i)                 # now we get copy of image in mypic.JPG  like capture.JPG

for i in f3:
    print(i)                       # printing binary format
