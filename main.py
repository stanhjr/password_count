import re


def read_in_lines(file_object) -> str:
    """
    :param file_object: file with strings
    :return: data from file by string
    """
    while True:
        data = file_object.readline().rstrip('\n')
        if not data:
            break
        yield data


def get_info_of_valid_password(string_in_file) -> bool:
    """
    :param string_in_file:
    :return: bool
    if the string doesn't match the re-pattern return false
    """

    if re.search(r'^(\w?)\s(\d+?)-(\d+?):\s(\w+?)$', string_in_file):
        pass_symbol, count_of_met, password = string_in_file.replace(':', ' ').split()
        count_of_met = count_of_met.split('-')
        count_of_met = min(map(lambda x: int(x), count_of_met))
        return count_of_met <= password.count(pass_symbol) <= count_of_met
    return False


def calculate(file_name) -> str:
    """
    Function to run calculation
    :param file_name: str with name of file
    :return: str with count of valid passwords or information about file is not exists
    """
    try:
        with open(file_name, encoding='utf-8') as file:
            return str(sum(get_info_of_valid_password(file_line) for file_line in read_in_lines(file)))
    except FileNotFoundError:
        return 'File not found'


if __name__ == '__main__':

    print('Count of valid password in file =', calculate('data_test.txt'))
