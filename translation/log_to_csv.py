import sys
import os.path

class ContentReader:
    def __init__(self, fileloc="", exercise=""):
        self.fileloc = fileloc
        self.filename = None
        self.contents = []
        self.filehandle = None
        self.directory = None
        self.is_class = None
        self.output = []
        self.exercise = exercise

    def open_file(self):
        if os.path.isfile(self.fileloc):
            self.filehandle = open(self.fileloc, "r")
            self.filename = os.path.basename(self.fileloc)
            self.directory = os.path.dirname(self.fileloc)
            return 0
        return 1

    def close_file(self):
        self.filehandle.close()

    def read_contents(self):
        self.contents = self.filehandle.readlines()

    def handle_contents(self):
        idx = 0
        workout_data = ""
        weight = ""
        set_number = 1
        while idx < len(self.contents):
            print(self.contents[idx])

            idx += 1


def display_usage():
    print("Error: Expecting path of the data file")

def handle_args():
    fileloc = None
    if len(sys.argv) == 3:
        fileloc = sys.argv[1]
        exercise = sys.argv[2]
    return fileloc, exercise

def main():
    fileloc, exercise = handle_args()
    if fileloc == None:
        display_usage()
    else:
        data_reader = ContentReader(fileloc, exercise)
        data_reader.open_file()
        data_reader.read_contents()
        data_reader.close_file()
        data_reader.handle_contents()
    return 0

if __name__ == "__main__":
    main()