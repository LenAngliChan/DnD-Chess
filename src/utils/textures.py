from arcade import load_texture, load_spritesheet, LRBT
from src.sprites import (
    switch_green,
    switch_red,
    red_button,
    red_button_hovered,
    red_button_pressed,
    red_domain,
    blue_domain,
    gray_domain,
)
from src.sprites.perks import (
    move_action,
    pass_action,
    healing_hand,
    light_shield,
    medium_shield,
    great_shield,
    ds_sword,
    dagger,
    two_daggers,
    sword_oh,
    sword_bastard,
    sword_th,
    axe,
    bow,
    fists,
    d_s_spell,
    f_b_spell,
    f_t_spell,
    i_s_spell,
    s_b_spell,
    m_m_spell,
)
from src.sprites.units import units_sheet
from src.sprites.buildings import altar_path, castle_path, crypt_path

# текстуры кнопок
SWITCH_GREEN_TEXTURE = load_texture(file_path=switch_green)
SWITCH_RED_TEXTURE = load_texture(file_path=switch_red)
RED_BUTTON_NORMAL_TEXTURE = load_texture(file_path=red_button)
RED_BUTTON_HOVER_TEXTURE = load_texture(file_path=red_button_hovered)
RED_BUTTON_PRESS_TEXTURE = load_texture(file_path=red_button_pressed)

# текстуры зданий
ALTAR_TEXTURE = load_texture(file_path=altar_path)
CASTLE_TEXTURE = load_texture(file_path=castle_path)
CRYPT_TEXTURE = load_texture(file_path=crypt_path)

# Текстуры доменов
RED_DOMAIN_TEXTURE = load_texture(file_path=red_domain)
BLUE_DOMAIN_TEXTURE = load_texture(file_path=blue_domain)
GRAY_DOMAIN_TEXTURE = load_texture(file_path=gray_domain)

# текстуры фигур
# BARBARIAN_TEXTURE = load_texture(file_path="src/sprites/units/Barbarian.png")
# BARD_TEXTURE = load_texture(file_path="src/sprites/units/Bard.png")
# CLERIC_TEXTURE = load_texture(file_path="src/sprites/units/Cleric.png")
# DRUID_TEXTURE = load_texture(file_path="src/sprites/units/Druid.png")
# FIGHTER_TEXTURE = load_texture(file_path="src/sprites/units/Fighter.png")
# MONK_TEXTURE = load_texture(file_path="src/sprites/units/Monk.png")
# PALADIN_TEXTURE = load_texture(file_path="src/sprites/units/Paladin.png")
# RANGER_TEXTURE = load_texture(file_path="src/sprites/units/Ranger.png")
# ROGUE_TEXTURE = load_texture(file_path="src/sprites/units/Rogue.png")
# SORCERER_TEXTURE = load_texture(file_path="src/sprites/units/Sorcerer.png")
# WARLOCK_TEXTURE = load_texture(file_path="src/sprites/units/Warlock.png")
# WIZARD_TEXTURE = load_texture(file_path="src/sprites/units/Wizard.png")
# через один рисунок
UNIT_SPRITE_SHEET = load_spritesheet(file_name=units_sheet)
# и позиции текстур на этом рисунке (в пикселях)
BARBARIAN_MALE_RECT = LRBT(left=10, right=175, bottom=730, top=900)
BARBARIAN_FEMALE_RECT = LRBT(left=175, right=340, bottom=720, top=900)
BARD_MALE_RECT = LRBT(left=380, right=530, bottom=580, top=725)
BARD_FEMALE_RECT = LRBT(left=530, right=705, bottom=570, top=725)
CLERIC_MALE_RECT = LRBT(left=345, right=520, bottom=930, top=1065)
CLERIC_FEMALE_RECT = LRBT(left=540, right=680, bottom=930, top=1065)
DRUID_MALE_RECT = LRBT(left=335, right=490, bottom=10, top=175)
DRUID_FEMALE_RECT = LRBT(left=505, right=685, bottom=15, top=180)
FIGHTER_MALE_RECT = LRBT(left=180, right=345, bottom=920, top=1065)
FIGHTER_FEMALE_RECT = LRBT(left=15, right=180, bottom=920, top=1065)
MONK_MALE_RECT = LRBT(left=20, right=160, bottom=570, top=725)
MONK_FEMALE_RECT = LRBT(left=175, right=330, bottom=590, top=720)
PALADIN_MALE_RECT = LRBT(left=340, right=520, bottom=720, top=900)
PALADIN_FEMALE_RECT = LRBT(left=515, right=690, bottom=730, top=900)
RANGER_MALE_RECT = LRBT(left=35, right=185, bottom=405, top=570)
RANGER_FEMALE_RECT = LRBT(left=185, right=365, bottom=420, top=570)
ROGUE_MALE_RECT = LRBT(left=380, right=530, bottom=430, top=565)
ROGUE_FEMALE_RECT = LRBT(left=555, right=680, bottom=415, top=565)
SORCERER_MALE_RECT = LRBT(left=45, right=165, bottom=220, top=390)
SORCERER_FEMALE_RECT = LRBT(left=195, right=310, bottom=225, top=390)
WARLOCK_MALE_RECT = LRBT(left=360, right=500, bottom=220, top=390)
WARLOCK_FEMALE_RECT = LRBT(left=500, right=635, bottom=220, top=390)
WIZARD_MALE_RECT = LRBT(left=50, right=165, bottom=50, top=170)
WIZARD_FEMALE_RECT = LRBT(left=185, right=310, bottom=50, top=170)

# иконки действий
MOVE_ACTION_TEXTURE = load_texture(file_path=move_action)
PASS_ACTION_TEXTURE = load_texture(file_path=pass_action)

# иконки способностей
HEALING_HAND_TEXTURE = load_texture(file_path=healing_hand)
LIGHT_SHIELD_TEXTURE = load_texture(file_path=light_shield)
MEDIUM_SHIELD_TEXTURE = load_texture(file_path=medium_shield)
GREAT_SHIELD_TEXTURE = load_texture(file_path=great_shield)
DS_SWORD_TEXTURE = load_texture(file_path=ds_sword)
DAGGER_TEXTURE = load_texture(file_path=dagger)
TWO_DAGGERS_TEXTURE = load_texture(file_path=two_daggers)
SWORD_OH_TEXTURE = load_texture(file_path=sword_oh)
SWORD_BASTARD_TEXTURE = load_texture(file_path=sword_bastard)
SWORD_TH_TEXTURE = load_texture(file_path=sword_th)
AXE_TEXTURE = load_texture(file_path=axe)
BOW_TEXTURE = load_texture(file_path=bow)
FISTS_TEXTURE = load_texture(file_path=fists)
D_S_SPELL_TEXTURE = load_texture(file_path=d_s_spell)
F_B_SPELL_TEXTURE = load_texture(file_path=f_b_spell)
F_T_SPELL_TEXTURE = load_texture(file_path=f_t_spell)
I_S_SPELL_TEXTURE = load_texture(file_path=i_s_spell)
S_B_SPELL_TEXTURE = load_texture(file_path=s_b_spell)
M_M_SPELL_TEXTURE = load_texture(file_path=m_m_spell)
