import json

import discord
from collections import Counter

rcolor = [
    discord.Colour.purple(),
    discord.Colour.orange(),
    discord.Colour.green(),
    discord.Colour.blue(),
    discord.Colour.red(),
    discord.Colour.teal(),
    discord.Colour.dark_teal(),
    discord.Colour.dark_green(),
    discord.Colour.dark_blue(),
    discord.Colour.dark_purple(),
    discord.Colour.magenta(),
    discord.Colour.gold(),
    discord.Colour.dark_gold(),
    discord.Colour.dark_orange(),
    discord.Colour.dark_red(),
    discord.Colour.lighter_gray(),
    discord.Colour.dark_gray(),
    discord.Colour.light_gray(),
    discord.Colour.darker_gray(),
    discord.Colour.blurple(),
    discord.Colour.greyple()
]

def add_opening_brace(filename):
  """Checks and adds an opening curly brace to the beginning of a file.

  Args:
    filename: The name of the file to modify.

  Returns:
    None
  """
  with open(filename, "r+") as f:
    content = f.read()
    if content[0] != "{":
      content = "{" + content
      f.seek(0)  # Move the pointer to the beginning of the file
      f.write(content)

def add_closing_brace(filename):
  """Checks and adds a closing curly brace to the end of a file.

  Args:
    filename: The name of the file to modify.

  Returns:
    None
  """
  with open(filename, "r+") as f:
    content = f.read()
    if content[-1] != "}":
      content = content + "}"
      f.seek(0)  # Move the pointer to the beginning of the file
      f.write(content)
    
add_closing_brace("database.txt")
add_opening_brace("database.txt")

def load_data():
    try:
        with open('database.txt', 'r') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError as e:
                print("JSON Decode Error:", e)
    except FileNotFoundError:
        pass
    return data

data = load_data()

def save_data(data):
    with open('database.txt', 'w') as file:
        json.dump(data, file)


def insert_data(key, value):
    data[key] = value
    save_data(data)


def get_data(key):
    return data.get(key)


def delete_data(key):
    if key in data:
        del data[key]
        save_data(data)


def list_all_keys():
    return list(data.keys())


def list_keys_with_prefix(prefix):
    return [key for key in data.keys() if key.startswith(prefix)]

def developer_check(id):
    devs = [
        559080343085514772,
        742079317101641778,
        886279024710656040
    ]
    for i in devs:
        if int(id) == i:
            return True
    return False

def additem(tag,item,count):
    try:
      try:
        data[f"{tag}"][item] += count
      except:
        data[f"{tag}"][item] = count
    except:
      try:
        data[f"{tag}"][item] = data[f"i{tag[2:-1]}"][item]
      except:
        data[f"{tag}"][item] = {}
      
      try:
        data[f"{tag}"][item] += count
      except:
        data[f"{tag}"][item] = count
    save_data(data)

def loadinv(tag):
    temp = dict(data[tag])
    for i in data[tag]:
        if not data[tag][i] > 0:
            temp.pop(i)
    return Counter(temp)

def createinv(tag):
    try:
        data[tag] = dict(Counter(data[f"i{tag[3:]}"]))
        data[f"i{tag[3:]}"] = None
    except:
        data[tag] = {}
    save_data(data)

def profile_intialization_check(guild_id_and_tag):
    try:
        a = data['xp' + guild_id_and_tag]
        if a < 1:
            a = 1
            data['xp' + guild_id_and_tag] = 1
        b = data['lvl' + guild_id_and_tag]
    except:
        data['xp' + guild_id_and_tag] = 1
        data['lvl' + guild_id_and_tag] = 1
    try:
        tryi = data["inv" + guild_id_and_tag]
    except:
        createinv("inv" + guild_id_and_tag)
    try:
        trym = data["m" + guild_id_and_tag]
    except:
        data["m" + guild_id_and_tag] = 0
    try:
        tryww = data["ww" + guild_id_and_tag]
    except:
        data['ww' + guild_id_and_tag] = []
    try:
        tryww = data["bm" + guild_id_and_tag]
    except:
        data['bm' + guild_id_and_tag] = 0
    try:
        money_in_bank = data["mb" + guild_id_and_tag]
    except:
        data['mb' + guild_id_and_tag] = 0
