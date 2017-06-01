"""
CSV parser

parse data from a CSV file and render it in JSON
"""

import csv


# describe full path to CSV file
# todo: make so user can pass filename from command line as parameter
file_name = "data/cb_2013/ny_13.csv"


def parse(raw_file, delimiter):
    """parse raw CSV file to JSON-like object"""

    # open file to prep for safe close when done
    open_file = open(raw_file)

    # read data
    csv_data = csv.reader(open_file, delimiter=delimiter)

    # prepare empty list
    parsed_data = []

    # skip over first line of file to drop headers
    fields = csv_data.next()

    # iterate over each row of the CSV file to zip together field & value
    for row in csv_data:
        parsed_data.append(dict(zip(fields, row)))

    # close file
    open_file.close()

    # return result
    return parsed_data


def main():
    """use above parse function"""

    # call parse function and pass it necessary parameters
    new_data = parse(file_name, ",")

    # open the output file in write mode
    # todo: call the file name passed as parameter here too
    new_file = open("new_file.txt", "w")

    # print lines to file
    for item in new_data:
        print >> new_file, item


if __name__ == "__main__":
    main()