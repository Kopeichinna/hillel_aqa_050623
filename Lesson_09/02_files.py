# # fh = open('some_file_new.txt')
# # data = fh.read()
# # print(data)
# # fh.close()
#
#
#
# # # fh = open('some.txt', 'rt')  # default
# #
# #
# # fh = open('some.txt', 'w')
# # fh.write('Smth')
# # fh.write('SmthOther')
# # fh.close()
# #
# # # open(file, mode='r', buffering=None, encoding=None, errors=None, newline=None, closefd=True)
# #
# # # The default mode is 'rt' (open for reading text)
# #
# # #  errors is an optional string that specifies how encoding errors are to
# # #     be handled---this argument should not be used in binary mode. Pass
# # #     'strict' to raise a ValueError exception if there is an encoding error
# # #     (the default of None has the same effect), or pass 'ignore' to ignore
# # #     errors.
# #
# # # Character Meaning
# # #     --------- ---------------------------------------------------------------
# # #     'r'       open for reading (default)
# # #     'w'       open for writing, truncating the file first
# # #     'x'       create a new file and open it for writing
# # #     'a'       open for writing, appending to the end of the file if it exists
# # #     'b'       binary mode
# # #     't'       text mode (default)
# # #     '+'       open a disk file for updating (reading and writing)
# # #     'U'       universal newline mode (deprecated)
# #
# #
# # fh = open('some.txt', 'r')
# # data = fh.readlines()
# # print(data)
# # fh.close()
# #
# fh = open('some.txt', 'a+')
# fh.seek(0)    # read position
# data = fh.readlines()
# print(data)
# fh.write('AdditionalSmth')
# fh.close()
# #
# #
# #
# load structures
car_data = {
    'Mercedes': ('silver', 2019, 1.8, 'sedan', 50000),
    'Audi': ('black', 2020, 2.0, 'sedan', 55000),
    'BMW': ('white', 2018, 3.0, 'suv', 70000),
    'Lexus': ('gray', 2016, 2.5, 'coupe', 45000),
    'Toyota': ('blue', 2021, 1.6, 'hatchback', 25000),
    'Honda': ('red', 2017, 1.5, 'sedan', 30000),
    'Ford': ('green', 2019, 2.3, 'suv', 40000),
    'Chevrolet': ('purple', 2020, 1.4, 'hatchback', 22000),
    'Nissan': ('pink', 2018, 1.8, 'sedan', 35000),
    'Volkswagen': ('brown', 2021, 1.4, 'hatchback', 28000),
    'Hyundai': ('gray', 2019, 1.6, 'suv', 32000),
    'Kia': ('white', 2020, 2.0, 'sedan', 28000),
    'Volvo': ('silver', 2017, 1.8, 'suv', 45000),
    'Subaru': ('blue', 2018, 2.5, 'wagon', 35000),
    'Mazda': ('red', 2019, 2.5, 'sedan', 32000),
    'Porsche': ('black', 2017, 3.0, 'coupe', 80000),
    'Jeep': ('green', 2021, 3.0, 'suv', 50000),
    'Chrysler': ('gray', 2016, 2.4, 'sedan', 22000),
    'Dodge': ('yellow', 2020, 3.6, 'suv', 40000),
    'Ferrari': ('red', 2019, 4.0, 'coupe', 500000),
    'Lamborghini': ('orange', 2021, 5.0, 'coupe', 800000),
    'Maserati': ('blue', 2018, 4.7, 'coupe', 100000),
    'Bugatti': ('black', 2020, 8.0, 'coupe', 2000000),
    'McLaren': ('yellow', 2017, 4.0, 'coupe', 700000),
    'Rolls-Royce': ('white', 2019, 6.8, 'sedan', 500000),
    'Bentley': ('gray', 2020, 4.0, 'coupe', 300000),
    'Jaguar': ('red', 2016, 2.0, 'suv', 40000),
    'Land Rover': ('green', 2018, 3.0, 'suv', 60000),
    'Tesla': ('silver', 2020, 0.0, 'sedan', 60000),
    'Acura': ('white', 2017, 2.4, 'suv', 40000),
    'Cadillac': ('black', 2019, 3.6, 'suv', 55000),
    'Infiniti': ('gray', 2018, 2.0, 'sedan', 35000),
    'Lincoln': ('white', 2021, 2.0, 'suv', 50000),
    'GMC': ('blue', 2016, 1.5, 'pickup', 30000),
    'Ram': ('black', 2019, 5.7, 'pickup', 40000),
    'Chevy': ('red', 2017, 2.4, 'pickup', 35000),
    'Dodge Ram': ('white', 2020, 3.6, 'pickup', 45000),
    'Ford F-Series': ('gray', 2021, 3.5, 'pickup', 50000),
    'Nissan Titan': ('silver', 2018, 5.6, 'pickup', 35000)
}
#
import pickle
fh = open('some.bin', 'wb')
pickle.dump(car_data, fh)
fh.close()
#
from pprint import pprint
fh = open('some.bin', 'rb')
data = pickle.load(fh)
print(type(data))
pprint(data)

fh = None
try:
    fh = open('some_file_new.txt')
    data = fh.read()
    print(data)
except Exception as g_exc:
    print(g_exc)
finally:
    print('we closed file')
    if fh:
        fh.close()

# with context manager
try:
    with open('some_file_new.txt') as fh:
        data = fh.read()
        print(data)
except Exception as g_exc:
    print(g_exc)