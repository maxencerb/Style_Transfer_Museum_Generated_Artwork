import os
from src.fast_style_transfer import complete_fast_algorithm as cfa

ARTWORK_DIR = 'artwork'

def get_dirs():
    dirs = [os.path.join(ARTWORK_DIR, d) for d in os.listdir(ARTWORK_DIR) if os.path.isdir(
        os.path.join(ARTWORK_DIR, d)
    )]
    return dirs

def create_img(dir):
    data_file = open(os.path.join(dir, 'image.dat'))
    [content_path, style_path, result_path, size_str, todo] = data_file.readlines()[0].split(sep=';')
    if todo == "False":
        print("This image is not done...")
        return
    size = int(size_str)
    image_result = cfa(os.path.join(dir, content_path),
    os.path.join(dir, style_path), size)
    print('saving...')
    image_result.save(os.path.join(dir, result_path))


if __name__ == "__main__":
    dirs = get_dirs()
    for i in range(len(dirs)):
        print('image %s for %s' % (i + 1, dirs[i]))
        create_img(dirs[i])
        
