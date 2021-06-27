import os
from PIL import Image, UnidentifiedImageError


# get current working dir
cwd = os.path.abspath(os.getcwd())
# TODO and dirname with targets from params
dirname_to_crop = '/gen_4/'

# get filenames of  targets
# TODO join pathes with os.path.join()
_, _, filenames = next(os.walk(f'{cwd}{dirname_to_crop}'))

counter = 0
# crop all target files
for filename in filenames:
    # split filename and extension
    name, ext = os.path.splitext(filename)

    # TODO join pathes with os.path.join()
    path_to_target = f'{cwd}{dirname_to_crop}{filename}'

    # open target image
    try:
        with Image.open(path_to_target) as im:
            width, height = im.size

            # TODO set crop settings in params
            left = 0
            top = 0
            right = width - 0
            bottom = height - 60

            # crop image
            im_crpd = im.crop((left, top, right,  bottom))

            # TODO join pathes with os.path.join()
            im_crpd.save(f'{cwd}{dirname_to_crop}{name}_crpd{ext}')
            counter += 1
    except UnidentifiedImageError:
        pass

print(f'{counter} images was cropped')
