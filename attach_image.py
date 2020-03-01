import os
from fire import Fire


class ImageAttachment(object):
    def __init__(self):
        pass
    
    def execute(self, img_path='', code_path='', output_path='result.txt'):

        with open(code_path, "r") as f:
            lines = f.read()
        code_list = [line for line in lines.split('\n')]

        filename_list = os.listdir(img_path)
        with open(output_path, 'w') as f:
            for code in code_list:
                match_filename = ''
                for filename in filename_list:
                    if code == filename.split('_')[0]:
                        match_filename = filename
                        break
                if match_filename:
                    f.write(f'{code}\t{match_filename}\n')
                else:
                    f.write(f'{code}\n')


if __name__ == '__main__':
    Fire(ImageAttachment)