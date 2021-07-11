import os

from argparse import ArgumentParser
from pathlib import Path
from PIL import Image, UnidentifiedImageError


# read cli arguments
parser = ArgumentParser()

# set dirs
parser.add_argument('-s', '--source', dest='source',
                    help='where to get source images')
parser.add_argument('-d', '--destination', dest='destination',
                    help='where to place cropped images')

'''
Use Pillow documentation for more information about its params
https://pillow.readthedocs.io/en/stable/reference/Image.html?highlight=crop#PIL.Image.Image.crop
'''
# set crop params
parser.add_argument('-l', '--left', dest='left',
                    help='crop from the left')
parser.add_argument('-t', '--top', dest='top',
                    help='crop from the top')
parser.add_argument('-r', '--right', dest='right',
                    help='crop from the right')
parser.add_argument('-b', '--bottom', dest='bottom',
                    help='crop from the bottom')

args = parser.parse_args()


# get filenames
try:
    _, _, filenames = next(os.walk(args.source))
except Exception:
    print('Pass -s parameter with absolute source directory path!', '\n')
    raise ValueError

# create destination dir if it not exists
try:
    Path(args.destination).mkdir(parents=True, exist_ok=True)
except TypeError:
    # and use source dir like destination if -d is empty
    args.destination = args.source


# do crop job and count it
counter = 0
# crop all target files
for filename in filenames:
    # split filename and extension
    name, ext = os.path.splitext(filename)
    target_path = os.path.join(args.source, filename)

    # open image
    try:
        with Image.open(target_path) as image:
            width, height = image.size

            '''
            if your crop parameters are not static, you can set it like this:
                left = 0
                top = 0
                right = width - 0
                bottom = height - 60
            '''

            # catch empty params
            if args.left is None:
                left = 0
            else:
                left = int(args.left)

            if args.top is None:
                top = 0
            else:
                top = int(args.top)

            if args.right is None:
                right = width - 0
            else:
                right = int(args.right)

            if args.bottom is None:
                bottom = height - 0
            else:
                bottom = int(args.bottom)

            # crop image
            image_crpd = image.crop((left, top, right, bottom))

            # save image with new name
            if args.destination:
                image_crpd.save(os.path.join(args.destination,
                                             f'{name}_crpd{ext}'))
            else:
                image_crpd.save(os.path.join(args.source,
                                             f'{name}_crpd{ext}'))

            counter += 1

    except UnidentifiedImageError:
        pass


# print results
print(f'Amount of cropped images: {counter}')
