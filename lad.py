

def numbers_to_name(device_numbers):
    major_minor = device_numbers.split(':')
    major = major_minor[0]
    minor = major_minor[1]
    print(f'{major} {minor}')


numbers_to_name('8:0')