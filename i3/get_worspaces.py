import i3 


def main():
    workspaces = i3.get_workspaces()
    for workspace in workspaces:
        print(workspace['name'])


if __name__ == '__main__':
    main()
