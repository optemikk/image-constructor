from loader import *


class PersonFormat:
    def __init__(self):
        pass


    def get_person_path(self) -> str:
        pose = random.choice(['pers-left', 'pers-right'])
        pers_path = f'Creomaker/joints/{pose}/'
        persons = os.listdir(pers_path)
        pers_path = pers_path + random.choice(persons)
        return pers_path


    def get_person_resized(self, pers_path: str, max_height: int = 1000) -> Image:
        pers = Image.open(pers_path).convert("RGBA")
        x, y = pers.size
        scale = ((max_height - y) / y) + 1
        res_x, res_y = round(x * scale), round(y * scale)
        if res_x <= 500:
            pass
        elif res_x > 500:
            scale = ((600 - x) / x) + 1
            res_x, res_y = round(x * scale), round(y * scale)
        pers = pers.resize((res_x, res_y))
        return pers

    def resize_person(self, pers_path: str, height: int) -> Image:
        pers = Image.open(pers_path)
        x, y = pers.size
        scale = ((height - y) / y) + 1
        res_x, res_y = round(x * scale), round(y * scale)
        pers = pers.resize((res_x, res_y))
        return pers


person_form = PersonFormat()