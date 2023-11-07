import random
from PIL import ImageDraw
from formating import text_form, object_form, person_form, background_form


text_colors = ['#000000', '#FFFFFF', '#FFD13E', '#FF0000', '#52C74E', '#88D7FD', '#B500C3', '#E4285C', '#CCFDBC']


class ImageConstructor:
    @staticmethod
    def main(num: int = 0) -> None:
        # setting bg
        bg_path = background_form.get_background_path()
        bg_type = bg_path.split('/')[-2]
        print(bg_type)
        bg_obj = background_form.get_background_object(bg_path)
        draw = ImageDraw.Draw(bg_obj)

        # text params
        font_path = text_form.get_font_path()
        font = text_form.get_image_font_object(font_path)
        text_placing = True
        text_pos_y = random.choice([True, False])
        text_lines = text_form.get_text_sized(font, text_placing)
        text_heights = text_form.draw_text(text_lines, font, text_placing)
        text_color = random.choice(text_colors)
        text_stroke = text_form.get_text_stroke_color(text_color=text_color) if random.choice([True, False]) else None
        print(text_heights)

        if bg_type == 'background':
            pers_path = person_form.get_person_path()
            pers_obj = person_form.get_person_resized(pers_path)
            pers_type = pers_path.split('/')[-2]

        # obj_use = random.choice([True, False])
        obj_use = True
        if obj_use or bg_type != 'background':
            obj_path = object_form.get_object_path()
            obj_obj = object_form.get_object_resized(obj_path)

        # pers placing
        if bg_type == 'background':
            pers_size = pers_obj.size
            if pers_size[1] == 1000:
                text_placing = False
                text_lines = text_form.get_text_sized(font, text_placing)
                text_heights = text_form.draw_text(text_lines, font, text_placing)
                x, y = pers_obj.size
                if pers_type == 'pers-left':
                    bg_obj.paste(pers_obj, (500, 0, 500 + x, y), pers_obj)
                else:
                    bg_obj.paste(pers_obj, (0, 0, x, y), pers_obj)
            elif pers_size[1] < 1000:
                pers_obj = person_form.resize_person(pers_path=pers_path, height=1000 - text_heights[0])
                pers_size = pers_obj.size
                if pers_type == 'pers-left':
                    if text_pos_y:
                        bg_obj.paste(pers_obj, (0, text_heights[0]), pers_obj)
                    else:
                        bg_obj.paste(pers_obj, (0, 0), pers_obj)
                else:
                    if text_pos_y:
                        bg_obj.paste(pers_obj, (500, text_heights[0]), pers_obj)
                    else:
                        bg_obj.paste(pers_obj, (500, 0), pers_obj)

        # text frame placing
        text_frame_placing = random.choice([True, False])
        if not text_placing:
            if bg_type == 'background-left' or pers_type == 'pers-right':
                text_pos = random.randint(3, 4)
            elif bg_type == 'background-right' or pers_type == 'pers-left':
                text_pos = random.randint(1, 2)
            elif bg_type == 'background':
                text_pos = random.randint(1, 4)
        if text_frame_placing:
            frame_filling = text_form.get_text_frame_filling(text_color=text_color)
            if text_placing:
                if text_pos_y:
                    draw.rectangle(xy=(0, 0, 999, text_heights[0]), fill=frame_filling)
                else:
                    draw.rectangle(xy=(0, 1000 - text_heights[0], 999, 999), fill=frame_filling)
            else:
                if text_pos == 1:
                    draw.rectangle(xy=(0, 0, 500, 500), fill=frame_filling)
                elif text_pos == 2:
                    draw.rectangle(xy=(0, 500, 500, 999), fill=frame_filling)
                elif text_pos == 3:
                    draw.rectangle(xy=(500, 0, 999, 500), fill=frame_filling)
                elif text_pos == 4:
                    draw.rectangle(xy=(500, 500, 999, 999), fill=frame_filling)
        else:
            text_pos_y = True
            text_stroke = text_form.get_text_stroke_color(text_color=text_color)


        # object placing
        if obj_use and bg_type != 'background':
            obj_pos = random.choice([True, False])
            print(obj_pos)
            if text_placing:
                if bg_type == 'background-right':
                    if obj_pos:
                        bg_obj.paste(obj_obj, (50, 50 + text_heights[0] if text_pos_y else 50), obj_obj)
                    else:
                        obj_y = 0
                        if not text_pos_y:
                            obj_y = 1000 - text_heights[0] - 400
                        elif text_heights[1] != 0:
                            obj_y = 1000 - text_heights[0] - 400
                        else:
                            obj_y = 550
                        bg_obj.paste(obj_obj, (50, obj_y), obj_obj)
                else:
                    if obj_pos:
                        bg_obj.paste(obj_obj, (550, 50 + text_heights[0] if text_pos_y else 50), obj_obj)
                    else:
                        obj_y = 0
                        if not text_pos_y:
                            obj_y = 1000 - text_heights[0] - 400
                        elif text_heights[1] != 0:
                            obj_y = 1000 - text_heights[0] - 400
                        else:
                            obj_y = 550
                        bg_obj.paste(obj_obj, (550, obj_y), obj_obj)

        # saving without text
        bg_obj.save(f'output/output{num}.png')

        # text placing
        text_offset = 0
        if text_placing:
            for i in text_lines:
                if text_pos_y:
                    length = font.getlength(i)
                    draw.text(xy=((1000 - length) / 2, 30 + text_offset), text=i, font=font, fill=text_color,
                              stroke_fill=text_stroke, stroke_width=random.randint(10, 15) if text_stroke else 0)
                    text_offset += 65
                else:
                    length = font.getlength(i)
                    draw.text(xy=((1000 - length) / 2, 1000 - text_heights[0] + 30 + text_offset), text=i, font=font,
                              fill=text_color, stroke_fill=text_stroke, stroke_width=random.randint(10, 15) if text_stroke else 0)
                    text_offset += 65
        else:
            for i in text_lines:
                length = font.getlength(i)
                if text_pos == 1:
                    draw.text(xy=((525 - length) / 2, (500 - text_heights[0]) / 2 + text_offset), text=i, font=font, fill=text_color,
                              stroke_fill=text_stroke, stroke_width=random.randint(10, 15) if text_stroke else 0)
                    text_offset += 65
                elif text_pos == 2:
                    draw.text(xy=((525 - length) / 2, 500 + (500 - text_heights[0]) / 2 + text_offset), text=i, font=font, fill=text_color,
                              stroke_fill=text_stroke, stroke_width=random.randint(10, 15) if text_stroke else 0)
                    text_offset += 65
                elif text_pos == 3:
                    draw.text(xy=(500 + (525 - length) / 2, (500 - text_heights[0]) / 2 + text_offset), text=i, font=font, fill=text_color,
                              stroke_fill=text_stroke, stroke_width=random.randint(10, 15) if text_stroke else 0)
                    text_offset += 65
                elif text_pos == 4:
                    draw.text(xy=(500 + (525 - length) / 2, 500 + (500 - text_heights[0]) / 2 + text_offset), text=i, font=font, fill=text_color,
                              stroke_fill=text_stroke, stroke_width=random.randint(10, 15) if text_stroke else 0)
                    text_offset += 65

        # saving with text
        bg_obj.save(f'output/output_text{num}.png')