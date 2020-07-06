#file handling

f = open("fh.txt","r")

"""             READING              """

print(f.read())
print(f.read(4))
print(f.readline())
print(f.readline(5))
print(f.readlines())

"""             WRITING             """

f = open("fh.txt","w")
f.write("hi how are you?")

"""             APPEND             """

f = open("fh.txt","a")
f.write("hi who are you?")