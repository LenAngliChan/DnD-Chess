# Сообщение о начале игры
START_GAME_MSG = (
    "Добро пожаловать в подземелье драконов!\n"
    "В поисках сокровищ вы встретили вражескую команду.\n"
    "Немедленно избавьтесь от конкурентов и заберите все богатства подземелья себе!\n"
    "Для начала игры нажмите СТАРТ.\n"
    "Для выбора фигуры нажмите ЛКМ.\n"
    "Затем выберите действие из нижней панели.\n"
    "Затем выберите цель действия при помощи ПКМ.\n"
    "Удачной охоты на драконов!"
)
DEFAULT_MSG = "Выберите фигуру!"
NEXT_DOMAIN_MSG = "Начинается ход фракции {domain}!"

# Сообщения применения способности
PERK_STATUS_DONE_MSG = "Способность {name} перезаряжается!"
PERK_STATUS_BLOCKED_MSG = "Способность {name} заблокирована!"
PERK_ACTIVATE_MSG = "Способность {name} использована на цели {target} с модификатором {modifier}"
PERK_HIT_CHANCE_MSG = "Бросок на попадание фигуры"
PERK_CRIT_CHANCE_MSG = "Бросок на критический удар фигуры"
EFFECT_HIT_VALUE_MSG = "Урон способности {value}, бонус мастерства {mastery}"
RESIST_VALUE_MSG = "У цели {resist} магической защиты!"
EFFECT_CRIT_VALUE_MSG = "Критический урон {value}"
MELEE_ATTACK_MSG = "Результат физической атаки: {result} {type} урона по цели {name}"
SHIELD_APPLY_MSG = "Результат защитной стойки: {result} дополнительной защиты для {name}"
MAGIC_ATTACK_MSG = "Результат магической атаки: {result} {type} урона по цели {name}"
HEAL_APPLY_MSG = "Результат лечения: исцеление {name} на {result} единиц"

# сообщение о бросках кости
DICE_ROLL_MSG = "Бросок кости равен {value}, штраф {penalty}"
CHECK_ROLL_MSG = "Бросок на попадание: успех {success}, провал {failure}, результат {result}"
CRIT_SUCCESS_MSG = "Бросок на попадание {value}: Критических Успех!"
CRIT_FAILURE_MSG = "Бросок на попадание {value}: Критических Провал!"

# Сообщения использования действия
ACTION_CHOOSE_MSG = "Выбрано действие {action}"
ACTION_USE_MSG = "Фигура {figure} использует {action} на противнике {target}"
ACTION_MOVE_MSG = "Фигура {figure} перемещается на {cell}"
ACTION_DEFEND_MSG = "Фигура {figure} пропускает ход!"
ACTION_NO_TARGET_MSG = "Не выбрана цель!"
ACTION_WRONG_MOVE_MSG = "Невозможно переместиться на клетку с другой фигурой!"
ACTION_WRONG_USE_MSG = "Нельзя атаковать самого себя оружием или магией!"
ACTION_NO_FIGURE_MSG = "Чтобы использовать способность нужна цель!"
ACTION_CANNOT_MOVE_MSG = "Фигура не может передвигаться!"
ACTION_NO_SACRIFICE_MSG = "Нет жертвы, чтобы пожертвовать алтарю!"
ACTION_SACRIFICE_MSG = "Фигура {figure} жертвует алтарю {target} и повышает свой уровень!"

# Сообщения о выборе цели
CELL_SELECT_MSG = "Выбрана цель: {cell}"
FIGURE_SELECT_MSG = "Выбрана фигура:\n {figure}"
NO_CELL_MSG = "Сначала нужно выбрать клетку!"
WRONG_DOMAIN_MSG = "Сейчас очередь фракции {domain}!"
NO_FIGURE_MSG = "Сначала нужно выбрать фигуру!"
WRONG_RADIUS_MSG = "Необходимо выбрать клетку в пределах доступа (по горизонтали или вертикали)"
