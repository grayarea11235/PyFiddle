import i3


def main():
    success = i3.layout('tabbed')

    if success:
        print('Successfully changed layout of the current workspace.')


if __name__ == '__main__':
    main()
