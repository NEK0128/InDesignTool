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


        d = {}
        for filename in filename_list:
            code = filename.split('_')[0]
            if code in d:
                d[code] = f'{d[code]}\t{filename}' 
                continue

            if code in code_list:
                d[code] = filename


        with open(output_path, 'w') as f:
            for k,v in d.items():
                f.write(f'{k}\t{v}\n')
 





if __name__ == '__main__':
    Fire(ImageAttachment)