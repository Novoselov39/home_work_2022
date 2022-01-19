import os


def parent (name): #Создаем папку проекта
    try:
        os.mkdir(name)
    except FileExistsError as e:
        print(f'dir exists: {e.filename}')
    return 0

def create_folder(parent,*folder): #создаем папки проекта
    for el in folder:
        try:
            dir_patch = os.path.join(parent,el)
            os.mkdir(dir_patch)
        except FileExistsError as e:
            print(f'dir exists: {e.filename}')
    return 0
def create_starter(main_dir):
    parent(main_dir)
    create_folder(main_dir, 'settings', 'mainapp', 'adminapp', 'authapp')

if __name__ == '__main__':
    create_starter('my_porject1')