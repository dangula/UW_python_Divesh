import os

def walk(dir):
    FileList = []
    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        if os.path.isfile(path):
            FileList.append(path)
        else:
            walk(path)
    return FileList

path = os.getcwd()
print path
print walk(path)