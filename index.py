# file = open ('data.txt', 'a+')

# file.write('Hello Python')

# file.close()


# file = open ('data.txt', 'a+')
# file.read()
# file.readline(100)       # считает по байту 
# lines = file.readlines()  
# print(lines)
# file.close()





# lines = []
# file = open ('data.txt', 'a+')
# for line in file:
#     lines.append(line)
# print(lines)

# file.close()



# file = open ('number.txt', 'w')
# for number in range(1, 11):
#     file.write(f'{number}\n')

# file.close()
# умножает все числа 
# file = open ('number.txt', 'r+')


# numbers = file.readlines()
# file.seek(0)              #найди курсор по документе 
#                         .tell() возвращает курсор

# for num in numbers:
#     file.write(f'{str(int(num)*2)}\n')
# print(file.tell)

# file.close()
# print(file.closed)




# file = open ('data.txt', 'r+')

# names = file.readlines()

# file.seek(0)

# for name in names:
#     file.write(name.upper())


# file.close()
# print(file.closed)



years = [2001, 1994, 2002, 1999, 2008, 2002, 2002, 1992]
file = open ('data.txt', 'r+')

names = file.readlines()
new_names = []
file.seek(0)
for i in range(0, len(years)):
    new_names.append(f'{names[i].strip()} {years[i]}\n')

file.writelines(new_names)

file.close()
print(file.closed)


# .writelines (iterable) tuple, list  все списки 
