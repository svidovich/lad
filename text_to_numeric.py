# We are going to load data from a file. If this package is installed,
# it needs to be able to find the file properly
import pkg_resources
import re


# Data files are to be newline delimited lists, space separated
def load_device_name_data_from_file(path):
    file_stream = pkg_resources.resource_string(__name__, path)
    data = filter(bool, file_stream.decode('utf-8').split('\n'))
    device_name_dictionary = {}
    for datapoint in data:
        split = datapoint.split(' ')
        common_name = split[0]
        numeric_name = split[1]
        device_name_dictionary[common_name] = numeric_name
    return device_name_dictionary


def construct_hash_lookup():
    linux_allocated_devices = {
        'scsi_disk_devices':
        load_device_name_data_from_file('data/scsi_disk_devices.txt')
    }
    return linux_allocated_devices


lookup_table = construct_hash_lookup()


def convert_common_to_numeric(string):
    if re.search('^sd[a-p][0-9]{1,3}', string.lower()):
        return lookup_table['scsi_disk_devices'][string]
