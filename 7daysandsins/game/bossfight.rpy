label start_battle:
    $ player = MyCharacter("Player", 100, 100, 2, 2, 2)
    $ difficult = 3 #твоя переменная сложности, эту можно убить отсюда
    $ hardness_multiplier = 1
    if difficult >= 3:
        $ hardness_multiplier = 2 #собственно накрутка сложности для врага
    $ enemy = MyCharacter("Enemy", hardness_multiplier * 1000, 9999, 0, 0, 0)
    show screen battle_ui
    while player.hp > 0 and enemy.hp > 0:

        call player_turn
        if enemy.hp <= 0:
            if player.mind <= 0:
                "Вы сходите с ума..."
                hide screen battle_ui
                jump end_battle

            "Победа!"
            hide screen battle_ui
            jump end_battle

        if player.hp > 0:
            call enemy_turn
            if player.hp <= 0:
                "Вы терпите поражение..."
                hide screen battle_ui
                jump end_battle

label player_turn:
    "Ваш ход."
    menu:
        "Атаковать":
            jump perform_player_attack
        "Умения":
            jump open_player_skills
        "Предметы":
            jump open_inventory
    return

label perform_player_attack:
    $ damage = random.randint(100, 300)
    $ player.perform_attack(enemy, damage)
    "Нанесено урона: [damage]"
    return

label open_player_skills:
    menu:
        "Действие 1 (стоимость - 30)":
            $ damage = random.randint(200, 400)
            $ player.perform_attack(enemy, damage)
            $ player.mind -= 30;
            "Нанесено урона: [damage]"
            return
        "Действие 2 (стоимость - 40)":
            $ damage = random.randint(300, 600)
            $ player.perform_attack(enemy, damage)
            $ player.mind -= 40;
            "Нанесено урона: [damage]"
            return
        "Назад":
            jump player_turn

label open_inventory:
    show screen inventory_ui
    menu:
        "Бутерброд - восстанавливает 25 единиц здоровья":
            if player.healing_items > 0: #проверяем, есть ли ваще предмет, который мы хотим использовать
                "Вкуснятина..."
                $ player.hp = min(100, player.hp + 25)
                $ player.healing_items -= 1
                hide screen inventory_ui
                return
            else: #если нет идём обратно
                "Нечего использовать."
                hide screen inventory_ui
                jump player_turn
        "Энергетик - восстанавливает 30 единиц психики":
            if player.mind_items > 0:
                "some text i dunno"
                $ player.mind = min(100, player.mind + 30)
                $ player.mind_items -= 1
                hide screen inventory_ui
                return
            else:
                "Нечего использовать."
                hide screen inventory_ui
                jump player_turn
        "Какой-то предмет с уроном хз":
            if player.damaging_items > 0:
                $ damage = random.randint(150, 450)
                $ player.perform_attack(enemy, damage)
                "Нанесено урона: [damage]"
                $ player.damaging_items -= 1
                hide screen inventory_ui
                return
            else:
                "Нечего использовать."
                hide screen inventory_ui
                jump player_turn
        "Назад":
            hide screen inventory_ui
            jump player_turn

label enemy_turn:
    "Ход врага!"
    $ action = random.randint(1, 3) #воу теперь враг иногда будет бить по рассудку
    $ damage = random.randint(10, 30)
    if action == 3:
        $ enemy.perform_mind_attack(player, damage) #собственно тут он это и делает
        "Враг атакует ваш психику, получено урона: [damage]"
    else:
        $ enemy.perform_attack(player, damage)
        "Враг делает что-то, получено урона: [damage]"
    return

label end_battle:
    "Битва завершена."
    return

screen battle_ui:
    frame:
        xalign 0.5 yalign 0.1
        has vbox
        text "Ваше здоровье: [player.hp]"
        text "Ваша психика: [player.mind]"

screen inventory_ui:
    frame:
        xalign 0.5 yalign 0.9
        has vbox
        text "Бутерброды: [player.healing_items]"
        text "Энергетики: [player.mind_items]"
        text "Дамажилки бум бум: [player.damaging_items]"