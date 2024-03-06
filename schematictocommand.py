import sys, nbtlib, json, pyperclip

schem = nbtlib.load(sys.argv[1])['Schematic']

commands = []

palette = json.loads(nbtlib.serialize_tag(schem['Blocks']['Palette']))
i = 0

offsetx = int(sys.argv[2])
offsety = int(sys.argv[3])
offsetz = int(sys.argv[4])

text_to_numericals = {
    "minecraft:air": "minecraft:air 0",
    "minecraft:stone": "minecraft:stone 0",
    "minecraft:granite": "minecraft:stone 1",
    "minecraft:polished_granite": "minecraft:stone 2",
    "minecraft:diorite": "minecraft:stone 3",
    "minecraft:polished_diorite": "minecraft:stone 4",
    "minecraft:andesite": "minecraft:stone 5",
    "minecraft:polished_andesite": "minecraft:stone 6",
    "minecraft:grass_block": "minecraft:grass 0",
    "minecraft:dirt": "minecraft:dirt 0",
    "minecraft:coarse_dirt": "minecraft:dirt 1",
    "minecraft:podzol": "minecraft:dirt 2",
    "minecraft:cobblestone": "minecraft:cobblestone 0",
    "minecraft:oak_planks": "minecraft:planks 0",
    "minecraft:spruce_planks": "minecraft:planks 1",
    "minecraft:birch_planks": "minecraft:planks 2",
    "minecraft:jungle_planks": "minecraft:planks 3",
    "minecraft:acacia_planks": "minecraft:planks 4",
    "minecraft:dark_oak_planks": "minecraft:planks 5",
    "minecraft:oak_sapling": "minecraft:sapling 0",
    "minecraft:spruce_sapling": "minecraft:sapling 1",
    "minecraft:birch_sapling": "minecraft:sapling 2",
    "minecraft:jungle_sapling": "minecraft:sapling 3",
    "minecraft:acacia_sapling": "minecraft:sapling 4",
    "minecraft:dark_oak_sapling": "minecraft:sapling 5",
    "minecraft:bedrock": "minecraft:bedrock 0",
    "minecraft:sand": "minecraft:sand 0",
    "minecraft:red_sand": "minecraft:sand 1",
    "minecraft:gravel": "minecraft:gravel 0",
    "minecraft:gold_ore": "minecraft:gold_ore 0",
    "minecraft:iron_ore": "minecraft:iron_ore 0",
    "minecraft:coal_ore": "minecraft:coal_ore 0",
    "minecraft:oak_log": "minecraft:log 0",
    "minecraft:spruce_log": "minecraft:log 1",
    "minecraft:birch_log": "minecraft:log 2",
    "minecraft:jungle_log": "minecraft:log 3",
    "minecraft:acacia_log": "minecraft:log2 0",
    "minecraft:dark_oak_log": "minecraft:log2 1",
    "minecraft:oak_leaves": "minecraft:leaves 0",
    "minecraft:spruce_leaves": "minecraft:leaves 1",
    "minecraft:birch_leaves": "minecraft:leaves 2",
    "minecraft:jungle_leaves": "minecraft:leaves 3",
    "minecraft:acacia_leaves": "minecraft:leaves2 0",
    "minecraft:dark_oak_leaves": "minecraft:leaves2 1",
    "minecraft:sponge": "minecraft:sponge 0",
    "minecraft:wet_sponge": "minecraft:sponge 1",
    "minecraft:glass": "minecraft:glass 0",
    "minecraft:lapis_ore": "minecraft:lapis_ore 0",
    "minecraft:lapis_block": "minecraft:lapis_block 0",
    "minecraft:dispenser": "minecraft:dispenser 0",
    "minecraft:sandstone": "minecraft:sandstone 0",
    "minecraft:chiseled_sandstone": "minecraft:sandstone 1",
    "minecraft:cut_sandstone": "minecraft:sandstone 2",
    "minecraft:note_block": "minecraft:sandstone 3",
    "minecraft:powered_rail": "minecraft:golden_rail 0",
    "minecraft:detector_rail": "minecraft:detector_rail 0",
    "minecraft:sticky_piston": "minecraft:sticky_piston 0",
    "minecraft:cobweb": "minecraft:cobweb 0",
    "minecraft:fern": "minecraft:tallgrass 2",
    "minecraft:dead_bush": "minecraft:deadbush 0",
    "minecraft:piston": "minecraft:piston 0",
    "minecraft:white_wool": "minecraft:wool 0",
    "minecraft:orange_wool": "minecraft:wool 1",
    "minecraft:magenta_wool": "minecraft:wool 2",
    "minecraft:light_blue_wool": "minecraft:wool 3",
    "minecraft:yellow_wool": "minecraft:wool 4",
    "minecraft:lime_wool": "minecraft:wool 5",
    "minecraft:pink_wool": "minecraft:wool 6",
    "minecraft:gray_wool": "minecraft:wool 7",
    "minecraft:light_gray_wool": "minecraft:wool 8",
    "minecraft:cyan_wool": "minecraft:wool 9",
    "minecraft:purple_wool": "minecraft:wool 10",
    "minecraft:blue_wool": "minecraft:wool 11",
    "minecraft:brown_wool": "minecraft:wool 12",
    "minecraft:green_wool": "minecraft:wool 13",
    "minecraft:red_wool": "minecraft:wool 14",
    "minecraft:black_wool": "minecraft:wool 15"
}

total_commands = schem['Height'] * schem['Length'] * schem['Width']

for y in range(schem['Height']):
  for z in range(schem['Length'] - 1, -1, -1):
    for x in range(schem['Width'] - 1, -1, -1):

      block_id = list(palette.keys())[list(palette.values()).index(i)]

      set_command = "/setblock ~%d ~%d ~%d %s" % (
          x + offsetx,
          (y - i) + offsety, z + offsetz, text_to_numericals[block_id])

      commands.append(set_command)

      i += 1

for a in range(total_commands):
  cmd_nbt = "{id:FallingSand,Block:command_block,Time:1,TileEntityData:{Command:%s},Riding:%s}" % (
      commands[a], cmd_nbt
  ) if a > 0 else "{id:FallingSand,Block:command_block,Time:1,TileEntityData:{Command:%s}}" % commands[
      a]

p = "/summon FallingSand ~ ~1 ~ {Block:redstone_block,Time:1,Riding:{id:FallingSand,Block:command_block,Time:1,TileEntityData:{Command:/fill ~ ~-%d ~-1 ~ ~%d ~-1 redstone_block},Riding:%s}}" % (
    total_commands, total_commands, cmd_nbt)
print(p)
pyperclip.copy(p)
print("Copied to clipboard!")
