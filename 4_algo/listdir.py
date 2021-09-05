import os

def list_dir(path=os.getcwd(),l=0):
    type = 'file' if not os.path.isdir(path) else 'dir'
    # print(l*" "+f"{l} {type}: "+os.path.basename(path))
    print(l*"  "+f"{os.path.basename(path)}")
    if os.path.isdir(path):
        dir = os.listdir(path)
        for e in dir:
            list_dir(os.path.join(path, e),l+1)


if __name__ == '__main__':
    list_dir()
