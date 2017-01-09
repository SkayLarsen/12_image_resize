import argparse
import os.path
from PIL import Image


def init_argparser():
    parser = argparse.ArgumentParser(description="Изменение размера изображения")
    parser.add_argument('input', help="Путь к исходному изображению")
    parser.add_argument('-w', '--width', help="Ширина результирующего изображения", type=int)
    parser.add_argument('-H', '--height', help="Высота результирующего изображения", type=int)
    parser.add_argument('-s', '--scale', help="Коэффициент масштабирования", type=float)
    parser.add_argument('-o', '--output', help="Путь к результирующему изображению")
    return parser


def resize_image(path_to_original, width, height, scale):
    image = Image.open(path_to_original)
    original_width, original_height = image.size
    proportion = original_width / original_height
    if scale:
        resized_image = image.resize([round(original_width * scale), round(original_height * scale)])
    elif width and height:
        if width / height != proportion:
            print("Предупреждение: новые пропорции не совпадают с исходным изображением.")
        resized_image = image.resize([width, height])
    elif width:
        resized_image = image.resize([width, round(width / proportion)])
    elif height:
        resized_image = image.resize([round(height * proportion), height])
    else:
        print("Указано недостаточно опций")
        return None
    return resized_image


def save_image(image, path_to_original, path_to_result):
    if not path_to_result:
        original_name, extension = os.path.splitext(path_to_original)
        path_to_result = '{}__{}x{}{}'.format(original_name, *image.size, extension)
    image.save(path_to_result, image.format)


if __name__ == '__main__':
    argparser = init_argparser()
    args = argparser.parse_args()
    if args.scale and (args.width or args.height):
        print("Нельзя одновременно указывать и коэффициент масштабирования, и ширину/высоту")
    elif not os.path.exists(args.input):
        print("Указанный файл не найден")
    else:
        new_image = resize_image(args.input, args.width, args.height, args.scale)
        save_image(new_image, args.input, args.output)
