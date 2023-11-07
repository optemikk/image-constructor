from loader import *


class BackgroundFormat:
    def get_background_path(self) -> str:
        background = random.choices(['background/', 'background-left/', 'background-right/'], weights=[50, 25, 25])
        background_path = f'Creomaker/joints/{background[0]}'
        backgrounds = os.listdir(background_path)
        background_path = background_path + random.choice(backgrounds)
        return background_path


    def get_background_object(self, bg_path: str) -> Image:
        background = Image.open(bg_path)
        return background


background_form = BackgroundFormat()