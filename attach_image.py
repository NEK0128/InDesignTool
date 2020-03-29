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
        sorted_filename_list = sorted(filename_list)
        with open(output_path, 'w') as f:
            for code in code_list:
                match_filename_list = [] 
                for filename in sorted_filename_list:
                    if code == filename.split('_')[0]:
                        match_filename_list.append(filename)
                if len(match_filename_list):
                    f.write(f'{code}\t' + '\t'.join(match_filename_list) + '\n')
                else:
                    f.write(f'{code}\n')


if __name__ == '__main__':
    Fire(ImageAttachment)