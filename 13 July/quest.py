import json
import time

my_file =open("quests\m_game.json", encoding="utf-8")
game = json.load(my_file)
my_file.close()

greeting =  f"""Добро пожаловать в игру "{game["game_info"]["NAME"]}"!
Автор  - {game["game_info"]["AUTHOR"]}
Версия - {game["game_info"]["VERSION"]}
Год выпуска - {game["game_info"]["YEAR"]}"""

def show_description(scene):
    description = game["game"][scene]["DESCRIPTION"]
    print(description)

    
def is_game_end(scene):
    if "GO" in game["game"][scene]["ACTIONS"][0]["EFFECT"]:
        return False
    return True

def show_actions(actions):
    print("Что будете делать?")
    for action in actions:
        print(" -> ", action)

def get_user_action():
    while True:
        user_in = input()
        if user_in:
            return user_in

def get_available_actions(scene):
    available_actions = []
    unavailable_actions = []
    for action in game["game"][scene]["ACTIONS"]:
        if "WHEN" in action:
                if "HAVE_T" in action["WHEN"] and "HAVE_S" in action["WHEN"]:
                    if action["WHEN"]["HAVE_T"] in pocket_items and action["WHEN"]["HAVE_S"] in skills:
                        available_actions.append(action["NAME"])
                    else: 
                        unavailable_actions.append(action["NAME"])
        else:
            available_actions.append(action["NAME"])
    return available_actions, unavailable_actions

  
def check_action(scene, action_name):
    for act in game["game"][scene]["ACTIONS"]:
        if action_name == act["NAME"]:
            return act["EFFECT"]
    print("Нет такого действия!")


     
def get_effect(effect, current_scene,pocket_items,skills, thanks):
    if "COLLECT_THING" in effect:
        pocket_items.append(effect["COLLECT_THING"])
    if  "COLLECT_SKILL" in effect:
        skills.append(effect["COLLECT_SKILL"])
    if "ALERT" in effect:
        print(effect["ALERT"])
    if "DISPOSE" in effect:
        pocket_items = [item for item in pocket_items if item != effect["DISPOSE"]]
        if effect["DISPOSE"] == "дрова" or effect["DISPOSE"] == "корыто":
            thanks += 1
            print("Большое тебе спасибо!")
        current_scene = effect["GO"]
    else:
        current_scene = effect["GO"]
    return current_scene, pocket_items, skills, thanks
    

line = '-' * 50
print(greeting)
print(f"\n {line} \n")
time.sleep(3)
print(game["Backstory"])
pocket_items = []
skills  = []
available_actions = []
thanks = 0

current_scene = "PALACE"
game_end = False
while True:
    time.sleep(3)
    print(f"\n {line} \n")
    if current_scene == "FINAL":
        if thanks > 0:
            print(game["game"]["FINAL"]["final_1"]["DESCRIPTION"])
            print("конец")
            break
        else:
            print(game["game"]["FINAL"]["final_2"]["DESCRIPTION"])
            print("конец")
            break
    else:
        show_description(current_scene)
        available_actions, unavailable_actions = get_available_actions(current_scene)
        if len(unavailable_actions) > 0:
            st = ", ".join(unavailable_actions)
            print(f"Некоторые действия: '{st}' вам не доступны, из за отсутствия соответсвующих предметов или навыков.")
        show_actions(available_actions)
        us_action = get_user_action()
        effect = check_action(current_scene, us_action)
        current_scene, pocket_items, skills, thanks = get_effect(effect, current_scene,pocket_items,skills,thanks )


