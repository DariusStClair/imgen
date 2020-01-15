from io import BytesIO

from PIL import Image, ImageDraw
from flask import send_file

from utils.endpoint import Endpoint, setup
from utils.textutils import wrap, render_text_with_emoji


@setup
class SneakyFox(Endpoint):
    params = ['text']

    def generate(self, avatars, text, usernames, kwargs):
        base = Image.open(self.assets.get('assets/sneakyfox/sneakyfox.bmp'))
        font = self.assets.get_font('assets/fonts/arimobold.ttf', size=36)
        canv = ImageDraw.Draw(base)
        fox, otherthing = text.replace(' ,', ',', 1).split(',', 1)
        fox = wrap(font, fox, 500)
        otherthing = wrap(font, otherthing, 450)
        render_text_with_emoji(base, canv, (50, 385), fox[:180], font=font, fill='Black')
        render_text_with_emoji(base, canv, (670, 150), otherthing[:180], font=font, fill='Black')

        base = base.convert('RGB')
        b = BytesIO()
        base.save(b, format='jpeg')
        b.seek(0)
        return send_file(b, mimetype='image/jpeg')