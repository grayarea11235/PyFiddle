import os 


def scan_path(path):
    obj = os.scandir(path)

    print("Files and Directories in '% s':" % path)
    for entry in obj :
        if entry.is_dir() or entry.is_file():
            print(entry.name)

    obj.close()
#

def main():
    scan_path('/home/cpd/Downloads/Dirk Gently Series by Douglas Adams-Narrated by Stephen Mangan' + 
            '/Dirk Gently\'s Holistic Detective Agency by Douglas Adams')

if __name__ == '__main__':
    main()
