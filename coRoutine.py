#https://raw.githubusercontent.com/datasets/population-city/master/data/unsd-citypopulation-year-both.csv
import csv, argparse , os

#define a decorator function which will create coroutine in python
def coroutine_dec(func):
    def wrap(*arg, **kwargs):
        corouted = func(*arg, **kwargs)
        corouted.__next__()
        return corouted
    return wrap

@coroutine_dec
#create seperate files with header name 
def coordinator(writers):
    try:
        while True:
            line = yield 
            splitted = line.split(',')
            i = 0
            for writer in writers:
                writer.send(splitted[i])
                i += 1
    except GeneratorExit:
        for writer in writers:
            writer.close()

@coroutine_dec
def file_writer(filename): #def a file writer function which will recieve a filename
    try:
        with open(filename, 'a') as file:
            while True:
                line = yield
                file.write(line + '\n')
    except GeneratorExit:
        file.close()

#make it bullet proof use the parse function
parser = argparse.ArgumentParser('This tool is to split arbitrary CSV files based on the header into different files')
parser.add_argument('-f', '--fileToProcess', type = str, help = 'Specifiess the file to b processed:' )
args = parser.parse_args()

#check if the file to be processed is csv
if not args.fileToProcess:
    print('Input should be a csv file')
    raise SystemExit
#if the file specifed could not be found
if not os.path.isfile(args.fileToProcess):
    print('Specified file: {} could not be found'.format(args.fileToProcess))
    raise SystemExit
#make seperate files wit header names
with open(args.fileToProcess, 'r') as csvfile:
    reader = csv.reader(csvfile)
    header = reader.__next__()
    header = [_.replace(' ', '') for _ in header]


#create writers for the coordinators
writers = [file_writer(_+'.txt') for _ in header]
coordinator = coordinator(writers)

#open specified files to process
with open(args.fileToProcess, 'r') as csvfile:
    for line in csvfile.readlines()[2:]:
        coordinator.send(line)
    coordinator.close()















            












