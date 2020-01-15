from io import BytesIO

from PIL import Image, ImageDraw
from flask import send_file

from utils.endpoint import Endpoint, setup
from utils.textutils import wrap, render_text_with_emoji


@setup
class ViolentSparks(Endpoint):
    params = ['text']

    def generate(self, avatars, text, usernames, kwargs):
        base = Image.open(self.assets.get('assets/violentsparks/violentsparks.bmp'))
        font = self.assets.get_font('assets/fonts/medium.woff', size=36)
        canv = ImageDraw.Draw(base)
        me, sparks = text.replace(' ,', ',', 1).split(',', 1)
        me = wrap(font, me, 550)
        sparks = wrap(font, sparks, 400)
        render_text_with_emoji(base, canv, (15, 5), me, font=font, fill='White')
        render_text_with_emoji(base, canv, (15, 567), sparks, font=font, fill='White')

        base = base.convert('RGB')
        b = BytesIO()
        base.save(b, format='jpeg')
        b.seek(0)
        return send_file(b, mimetype='image/jpeg')