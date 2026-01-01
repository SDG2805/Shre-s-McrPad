import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.endoder import EncoderHandler
from kmk.extensions.RGB import RGB

keyboard = KMKKeyboard()

rgb = RGB(pixel_pin=board.D2, num_pixels=4)
keyboard.extensions.append(rgb)

encoder_handler = EncoderHandler()
keyboard.modules = [encoder_handler]

keyboard.col_pins = (board.D8, board.D9, board.D10)
keyboard.row_pins = (board.D7, board.D6, board.D4)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Regular GPIO Encoder
encoder_handler.pins = (
    # regular direction encoder and a button
    (board.D0, board.D1, None,), # encoder #1 
    # reversed direction encoder with no button handling and divisor of 2
    (board.D4, board.GP5, None,), # encoder #2
    )

encoders.map = [ ((KC.VOLD, KC.VOLU),   (KC.BRIU, KC.BRID))]

keyboard.keymap = [
    [
        rbg.off(),  KC.RGB_MODE_PLAIN,  KC.RGB_MODE_RAINBOW,
        KC.N67,  KC.PGUP;   KC.PGDOWN;
        KC.LEFT;    KC.PAUSE;   KC.RIGHT;
    ]
]

if __name__ == '__main__':
    keyboard.go()
