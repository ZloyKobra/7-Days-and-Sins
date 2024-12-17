define gg = Character("[gg_name]", color="#49df7b") # , callback=name_callback, cb_name="gg"
define e = Character('Эйлин', color="#c8ffc8")
define noname = Character("...", color="#ffac68")
define laziness = Character("Лень", color="#dd7be6")


image gg calm1 = At("gg stand", sprite_highlight("gg"))
image gg angry_ = At("gg angry", sprite_highlight("gg"))
image gg facepalm_  = At("gg facepalm", sprite_highlight("gg"))
image gg speak_ = At("gg speak", sprite_highlight("gg"))
image gg calm2 = At("gg stand1", sprite_highlight("gg"))
image gg think_ = At("gg think", sprite_highlight("gg"))
image gg talktophone_ = At("gg talkphone", sprite_highlight("gg"))
image gg looktophone_ = At("gg lookphone", sprite_highlight("gg"))

define gg_phone = Character("[gg_name]", kind=nvl, image="gg stand")
define gendir_phone = Character("Гендир", kind=nvl)

# image laziness calm1 = At("laziness stand", sprite_highlight("laziness"))
# и т.д.


