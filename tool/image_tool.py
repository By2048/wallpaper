
import hashlib
import os


def get_md5(file_path):
    if not os.path.isfile(file_path):
        return
    hash = hashlib.md5()
    file = open(file_path, 'rb')
    while True:
        block = file.read(8096)
        if not block:
            break
        hash.update(block)
    file.close()
    return hash.hexdigest()


def rename(file_path):
    img_md5 = get_md5(file_path)
    folder_path = os.path.dirname(file_path)
    img_type = os.path.splitext(file_path)[1]
    new_path = os.path.join(folder_path, (img_md5 + img_type))
    # 如果存在重复文件 删除 否则 重命名
    if os.path.isfile(new_path) and file_path != new_path:
        os.remove(file_path)
    else:
        os.rename(file_path, new_path)


def _test():
    path = '..\\media\\6.jpg'
    print('绝对路径   ' + os.path.abspath(path))
    print('MD5       ' + get_md5(path))




if __name__ == '__main__':
    _test()
