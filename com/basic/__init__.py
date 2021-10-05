import keyword

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    name = input('What is your name?\n')
    print_hi(name)

    friends = ['john', 'pat', 'gary', 'michael']
    for i, name in enumerate(friends):
        print(f'iteration {i} is {name}')

    print(keyword.kwlist)

