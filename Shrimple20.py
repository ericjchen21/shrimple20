print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC, Key
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.macros import Macros, Press, Release, Tap, Delay

keyboard = KMKKeyboard()
layers = Layers()
encoder_handler = EncoderHandler()
macros = Macros()
keyboard.modules = [layers, encoder_handler, macros]
keyboard.extensions.append(MediaKeys())
keyboard.col_pins = (board.D0,board.D1,board.D2,board.D3)
keyboard.row_pins = (board.D4,board.D5,board.D6,board.D7,board.D8,board.D9)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

encoder_handler.pins = (
    (board.A1, board.A0, None),
)

xxxxxxx = KC.NO

LYR_STD, LYR_2, LYR_SHRIMP = 0, 1, 2

TO_LYR2 = KC.MO(LYR_2)

TO_SHRIMP = KC.DF(LYR_SHRIMP)

TAB_NXT = KC.LCTL(KC.TAB)

TAB_PRV = KC.LCTL(KC.LSFT(KC.TAB))

WND_NXT = KC.LALT(KC.TAB)

WND_PRV = KC.LALT(KC.LSFT(KC.TAB))

PG_BCK = KC.LALT(KC.LEFT)

PG_FWD = KC.LALT(KC.RGHT)

SPOTIFY = KC.MACRO(
    Tap(KC.LGUI),
    Tap(KC.S),
    Tap(KC.P),
    Tap(KC.O),
    Tap(KC.T),
    Tap(KC.I),
    Tap(KC.F),
    Tap(KC.Y),
    Delay(5),
    Tap(KC.ENT),
)

SHRIMP = KC.MACRO("shrimp")

keyboard.keymap = [

    [KC.BSPC, KC.LPRN, KC.RPRN, KC. PSLS,
     KC.N7  , KC.N8  , KC.N9  , KC.PAST,
     KC.N4  , KC.N5  , KC.N6  , KC.PMNS,
     KC.N1  , KC.N2  , KC.N3  , KC.PPLS,
     TO_LYR2, KC.N0  , KC.DOT , KC.PENT,
     xxxxxxx, xxxxxxx, xxxxxxx, KC.MUTE,
     ],

    [KC.DEL , KC.MPRV, KC.MPLY, KC.MNXT,
     KC.HOME, KC.UP  , KC.END , KC.PGUP,
     KC.LEFT, KC.DOWN, KC.RGHT, KC.PGDN,
     TAB_PRV, TAB_NXT, WND_PRV, WND_NXT,
     TO_LYR2, SPOTIFY, PG_BCK , PG_FWD ,
     xxxxxxx, xxxxxxx, xxxxxxx, TO_SHRIMP,
    ],

    [SHRIMP , SHRIMP , SHRIMP , SHRIMP ,
     SHRIMP , SHRIMP , SHRIMP , SHRIMP ,
     SHRIMP , SHRIMP , SHRIMP , SHRIMP ,
     SHRIMP , SHRIMP , SHRIMP , SHRIMP ,
     SHRIMP , SHRIMP , SHRIMP , SHRIMP ,
     xxxxxxx, xxxxxxx, xxxxxxx, SHRIMP ,
    ],
]

encoder_handler.map = [

    ((KC.VOLU, KC.VOLD, KC.MUTE),),

    ((KC.VOLU, KC.VOLD, KC.MUTE),),

    ((SHRIMP , SHRIMP , SHRIMP ),),
]

if __name__ == '__main__':
    keyboard.go()