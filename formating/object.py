from loader import *


class ObjectFormat:
    def __init__(self):
        pass


    def get_object_path(self, user_obj: bool = False) -> str:
        obj_path = 'Creomaker/joints/user-objects/' if user_obj else 'Creomaker/joints/object/'
        objects = os.listdir(obj_path)
        obj_path = obj_path + random.choice(objects)
        return obj_path

    def get_object_resized(self, obj_path: str) -> Image:
        obj_img = Image.open(obj_path)
        x, y = obj_img.size
        if x > 400 or y > 400:
            scale = (y - 400) / y if y > x else (x - 400) / x
            res_x, res_y = x - round(scale * x), y - round(scale * y)
            obj_img = obj_img.resize((res_x, res_y))
        return obj_img


object_form = ObjectFormat()