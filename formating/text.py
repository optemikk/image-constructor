from loader import *


font_sizes = {
            'FiraSans.ttf': 54,
            'Impact.ttf': 58,
            'Montserrat.ttf': 44,
            'ObelixPro.ttf': 43
        }


class TextFormat:
    def __init__(self):
        pass


    def get_font_path(self) -> str:
        font_path = 'Creomaker/fonts/'
        all_fonts = os.listdir(font_path)
        font_path = font_path + random.choice(all_fonts)
        return font_path

    def get_text_line(self, lang: str = 'EN') -> str:
        text_path = f'Creomaker/joints/text/{lang}.txt'
        with open(text_path, encoding='utf-8') as file:
            text_lines = file.readlines()
        text_line = random.choice(text_lines).upper()
        return text_line

    def get_image_font_object(self, font_path: str) -> ImageFont:
        font_size = font_sizes[font_path.split('/')[-1]]
        font = ImageFont.truetype(font_path, font_size)
        return font

    def get_text_sized(self, font: ImageFont, placing: bool = True) -> list:
        # True: top / bottom / top&bottom
        # False: left top / left bottom / right top / right bottom
        text_lines = self.get_text_line().split(' ')
        formatted_text = list()
        line_pack = list()
        max_length = 960 if placing else 460
        font_size_offset = 0
        for num, line in enumerate(text_lines):
            line_pack_text = ' '.join(line_pack + [line])
            line_length = font.getlength(line_pack_text)
            if num + 1 == len(text_lines):
                if line_length > max_length:
                    formatted_text.append(' '.join(line_pack))
                    formatted_text.append(line)
                else:
                    formatted_text.append(' '.join(line_pack + [line]))
            elif line_length < max_length:
                line_pack.append(line)
                # font_size_offset += 1
                # font = self.get_image_font_object(font_path, font_size_offset)
            elif line_length == max_length:
                formatted_text.append(' '.join(line_pack + [line]))
                line_pack.clear()
            else:
                formatted_text.append(' '.join(line_pack))
                line_pack.clear()
                line_pack.append(line)
        return formatted_text


    def draw_text(self, text_lines: list, font: ImageFont, placing: bool = True) -> list:
        # True: top / bottom / top&bottom
        # False: left top / left bottom / right top / right bottom
        drawing = False
        bg = Image.new('RGB', (1000, 1000), 'black')
        draw = ImageDraw.Draw(bg)
        offset = 0
        text_height = [60, 0]
        for n, i in enumerate(text_lines):
            _, _, x, y = draw.textbbox(xy=(0, 0), text=i, font=font)
            if n < 3:
                length = font.getlength(i)
                if drawing:
                    draw.text(xy=((1000 - length) / 2, 30 + offset), text=i, font=font)
                offset += 50
                text_height[0] += y
            elif len(text_lines) == 4:
                _, _, x, y = draw.textbbox(xy=(0, 0), text=i, font=font)
                print(x, y)
                if drawing:
                    draw.text(xy=((1000 - x) / 2, 1000 - y - 30), text=i, font=font)
                if placing:
                    text_height[1] += y
                else:
                    text_height[0] += y
            else:
                length = font.getlength(i)
                if drawing:
                    draw.text(xy=((1000 - length) / 2, 750 + offset), text=i, font=font)
                offset += 50
                if placing:
                    text_height[1] += y
                else:
                    text_height[0] += y
        return text_height


    def get_text_frame_filling(self, text_color: str) -> str:
        filling = ''
        if text_color == '#000000':
            filling = random.choice(
                ['#FFFFFF', '#FFD13E', '#FF0000', '#52C74E', '#88D7FD', '#B500C3', '#E4285C', '#CCFDBC'])
        elif text_color == '#FFFFFF':
            filling = random.choice(
                ['#000000', '#FF0000', '#52C74E', '#B500C3', '#E4285C'])
        elif text_color == '#FFD13E':
            filling = random.choice(
                ['#000000', '#FF0000', '#52C74E', '#B500C3', '#E4285C'])
        elif text_color == '#52C74E':
            filling = random.choice(
                ['#000000', '#FFFFFF', '#CCFDBC'])
        elif text_color == '#88D7FD':
            filling = random.choice(
                ['#000000', '#FFFFFF', '#CCFDBC'])
        elif text_color == '#B500C3':
            filling = random.choice(
                ['#000000', '#FFFFFF', '#FFD13E', '#52C74E', '#88D7FD', '#CCFDBC'])
        elif text_color == '#E4285C':
            filling = random.choice(
                ['#000000', '#FFFFFF', '#FFD13E', '#52C74E', '#88D7FD', '#CCFDBC'])
        else:  # text_color == '#CCFDBC':
            filling = random.choice(
                ['#000000', '#FFFFFF', '#FFD13E', '#52C74E', '#88D7FD', '#CCFDBC'])
        return filling


    def get_text_stroke_color(self, text_color: str) -> str:
        stroke = ''
        if text_color == '#000000':
            stroke = random.choice(
                ['#FFFFFF', '#FFD13E', '#FF0000', '#52C74E', '#88D7FD', '#B500C3', '#E4285C', '#CCFDBC'])
        elif text_color == '#FFFFFF':
            stroke = random.choice(
                ['#000000', '#FF0000', '#52C74E', '#B500C3', '#E4285C'])
        elif text_color == '#FFD13E':
            stroke = random.choice(
                ['#000000', '#FF0000', '#52C74E', '#B500C3', '#E4285C'])
        elif text_color == '#FF0000':
            stroke = random.choice(
                ['#000000', '#FFFFFF', '#FFD13E', '#88D7FD', '#CCFDBC'])
        elif text_color == '#52C74E':
            stroke = random.choice(
                ['#000000', '#FFFFFF', '#CCFDBC'])
        elif text_color == '#88D7FD':
            stroke = random.choice(
                ['#000000', '#FFFFFF', '#CCFDBC'])
        elif text_color == '#B500C3':
            stroke = random.choice(
                ['#000000', '#FFFFFF', '#FFD13E', '#52C74E', '#88D7FD', '#CCFDBC'])
        elif text_color == '#E4285C':
            stroke = random.choice(
                ['#000000', '#FFFFFF', '#FFD13E', '#52C74E', '#88D7FD', '#CCFDBC'])
        else:  # text_color == '#CCFDBC':
            stroke = random.choice(
                ['#000000', '#FFFFFF', '#FFD13E', '#52C74E', '#88D7FD', '#CCFDBC'])
        return stroke


text_form = TextFormat()
