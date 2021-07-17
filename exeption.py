# class IncorrectValueNumber(BaseException):
#     pass
#
# try:
#     first = int(input('Enter your number = '))
#     second = int(input('Enter your 2 number = '))
#     print(first/second)
# except (ValueError, ZeroDivisionError) as ex:
#     raise IncorrectValueNumber(ex)
# except Exception as ex:
#     print(ex)
#     # print('firts number is not int!')

# class MyKeyError(KeyError):
#     pass
#
sample_dictionary = {'name': 'OTUS', 'site': 'otus.ru'}
# try:
#     print(sample_dictionary['uh'])
# except KeyError as ex:
#     raise (ex)

if 'site' in sample_dictionary.keys():
    print('site in sample_dictionary')
else:
    print("Fuck!, site is not in")




# if first < 10:
#     raise  IncorrectValueNumber('First need > 10')
#
#
# try:
#     print(first / second)
# except ZeroDivisionError:
#     raise BaseException('Do not wr devide by zero')
#     # print('На нуль делить нельзя!')