import os

def path_scan(path):
    print('Scanning... {path}'.format(path=path))

    dir_scan = os.scandir(path)
    for entry in dir_scan:
        print(entry.name)


if __name__ == "__main__":
    path_scan("/media/cpd/USB2")

