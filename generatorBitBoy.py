import png
import random

boysTotal = 10

colorsHistory = ''

skinColors = [(249, 200, 169), (248, 188, 150), (246, 176, 131), (245, 164, 112), (244, 152, 93), (242, 140, 74), (241, 128, 55), (240, 116, 36), (238, 104, 17), (219, 95, 15), (200, 87, 14), (181, 79, 13), (162, 70, 11), (143, 62, 10), (124, 54, 9), (105, 46, 7), (86, 37, 6)]
hatColors = [(254, 249, 246), (251, 238, 228), (249, 226, 210), (246, 215, 192), (244, 203, 174), (242, 192, 156), (239, 180, 138), (237, 169, 120), (234, 157, 102), (232, 146, 85), (229, 134, 67), (227, 123, 49), (224, 111, 31), (206, 102, 28), (188, 94, 26), (170, 85, 23), (153, 76, 21), (135, 67, 18), (117, 58, 16), (99, 49, 13), (81, 40, 11), (63, 31, 9), (45, 22, 6), (27, 13, 4), (9, 4, 1), (255, 215, 0), (248, 200, 220), (248, 200, 220)]
hairColors = [(170, 136, 102), (222, 190, 153), (36, 28, 17), (79,26,0), (154, 51, 0), (128, 128, 128)]
lassoSkillsOptions = [1, 2, 2, 3, 3, 3, 4, 4, 5]

backgroundShades = ['r', 'g', 'b']

for count in range(boysTotal):

    width = 1600
    height = 1600
    img = []
    imgTransp = []

    backShadeSelect = random.choice(backgroundShades)

    if backShadeSelect == 'b':
        randomColor = (random.randint(0,100), random.randint(0,100), random.randint(100,255))
    elif backShadeSelect == 'r':
        randomColor = (random.randint(100,255), random.randint(0,100), random.randint(0,100))
    else:
        randomColor = (random.randint(0,100), random.randint(100,255), random.randint(0,100))

    hatColor = random.choice(hatColors)
    skinColor = random.choice(skinColors)
    shirtColor = (random.randint(100,255), random.randint(0,100), random.randint(0,100))
    eyeColor = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
    moustacheColor = random.choice(hairColors)
    lassoSkills = random.choice(lassoSkillsOptions)

    def generateColors():
        randomColor = (random.randint(0,100), random.randint(0,100), random.randint(100,255))
        hatColor = random.choice(hatColors)
        skinColor = random.choice(skinColors)
        shirtColor = (random.randint(100,255), random.randint(0,100), random.randint(0,100))
        eyeColor = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
        moustacheColor = (random.randint(100,255), random.randint(0,100), random.randint(0,100))
        lassoSkills = random.choice(lassoSkillsOptions)

        textTest = "Background = " + str(rgb_to_hex(randomColor)) + ", Hat Color = " + str(rgb_to_hex(hatColor)) + ", Skin Color = " + str(rgb_to_hex(skinColor)) + ", Shirt Color = " + str(rgb_to_hex(shirtColor)) + ", Eye Color = " + str(rgb_to_hex(eyeColor)) + ", Moustache Color = " + str(rgb_to_hex(moustacheColor)) + ", Lasso Skills = " + str(lassoSkills) 

        if textTest in colorsHistory:
            generateColors()

        if abs(skinColor[0] - hatColor[0]) < 50 and abs(skinColor[1] - hatColor[1]) < 50 and abs(skinColor[2] - hatColor[2]) < 50:
            generateColors()
        
    countDisplay = count + 1

    filenameMeta = 'cowboyMeta' + str(countDisplay) + '.txt'

    def rgb_to_hex(rgb):
        return '%02x%02x%02x' % rgb

    metText = "Background = " + str(rgb_to_hex(randomColor)) + ", Hat Color = " + str(rgb_to_hex(hatColor)) + ", Skin Color = " + str(rgb_to_hex(skinColor)) + ", Shirt Color = " + str(rgb_to_hex(shirtColor)) + ", Eye Color = " + str(rgb_to_hex(eyeColor)) + ", Moustache Color = " + str(rgb_to_hex(moustacheColor)) + ", Lasso Skills = " + str(lassoSkills)
    colorsHistory = colorsHistory + metText

    text_file = open(filenameMeta, "w")
    n = text_file.write(metText)
    text_file.close()

    n = 100

    row = ()
    rowTransp = ()
    
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + (0, 0, 0)
    for i in range(n):
        row = row + hatColor
    for i in range(n):
        row = row + hatColor
    for i in range(n):
        row = row + hatColor
    for i in range(n):
        row = row + hatColor
    for i in range(n):
        row = row + hatColor
    for i in range(n):
        row = row + hatColor
    for i in range(n):
        row = row + (0, 0, 0)
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        img.append(row)

    row = ()
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + (0, 0, 0)
    for i in range(n):
        row = row + hatColor
    for i in range(n):
        row = row + hatColor
    for i in range(n):
        row = row + hatColor
    for i in range(n):
        row = row + hatColor
    for i in range(n):
        row = row + hatColor
    for i in range(n):
        row = row + hatColor
    for i in range(n):
        row = row + (0, 0, 0)
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        img.append(row)
        
    row = ()
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + (0, 0, 0)
    for i in range(n):
        row = row + hatColor
    for i in range(n):
        row = row + hatColor
    for i in range(n):
        row = row + hatColor
    for i in range(n):
        row = row + hatColor
    for i in range(n):
        row = row + hatColor
    for i in range(n):
        row = row + hatColor
    for i in range(n):
        row = row + (0, 0, 0)
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        img.append(row)
        
    row = ()
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + (0, 0, 0)
    for i in range(n):
        row = row + hatColor
    for i in range(n):
        row = row + hatColor
    for i in range(n):
        row = row + hatColor
    for i in range(n):
        row = row + hatColor
    for i in range(n):
        row = row + hatColor
    for i in range(n):
        row = row + hatColor
    for i in range(n):
        row = row + (0, 0, 0)
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        img.append(row)
        
    row = ()
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + (0, 0, 0)
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + (0, 0, 0)
    for i in range(n):
        row = row + hatColor
    for i in range(n):
        row = row + hatColor
    for i in range(n):
        row = row + hatColor
    for i in range(n):
        row = row + hatColor
    for i in range(n):
        row = row + hatColor
    for i in range(n):
        row = row + hatColor
    for i in range(n):
        row = row + (0, 0, 0)
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + (0, 0, 0)
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        img.append(row)
        
    row = ()
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + (0, 0, 0)
    for i in range(n):
        row = row + (0, 0, 0)
    for i in range(n):
        row = row + (0, 0, 0)
    for i in range(n):
        row = row + (0, 0, 0)
    for i in range(n):
        row = row + (0, 0, 0)
    for i in range(n):
        row = row + (0, 0, 0)
    for i in range(n):
        row = row + (0, 0, 0)
    for i in range(n):
        row = row + (0, 0, 0)
    for i in range(n):
        row = row + (0, 0, 0)
    for i in range(n):
        row = row + (0, 0, 0)
    for i in range(n):
        row = row + (0, 0, 0)
    for i in range(n):
        row = row + (0, 0, 0)
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        img.append(row)
        
    row = ()
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + (0, 0, 0)
    for i in range(n):
        row = row + skinColor
    for i in range(n):
        row = row + skinColor
    for i in range(n):
        row = row + skinColor
    for i in range(n):
        row = row + skinColor
    for i in range(n):
        row = row + skinColor
    for i in range(n):
        row = row + skinColor
    for i in range(n):
        row = row + skinColor
    for i in range(n):
        row = row + skinColor
    for i in range(n):
        row = row + (0, 0, 0)
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        img.append(row)
        
    row = ()
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + (0, 0, 0)
    for i in range(n):
        row = row + skinColor
    for i in range(n):
        row = row + (255, 255, 255)
    for i in range(n):
        row = row + (255, 255, 255)
    for i in range(n):
        row = row + skinColor
    for i in range(n):
        row = row + skinColor
    for i in range(n):
        row = row + (255, 255, 255)
    for i in range(n):
        row = row + (255, 255, 255)
    for i in range(n):
        row = row + skinColor
    for i in range(n):
        row = row + (0, 0, 0)
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        img.append(row)
        
    row = ()
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + (0, 0, 0)
    for i in range(n):
        row = row + skinColor
    for i in range(n):
        row = row + eyeColor
    for i in range(n):
        row = row + (0, 0, 0)
    for i in range(n):
        row = row + skinColor
    for i in range(n):
        row = row + skinColor
    for i in range(n):
        row = row + (0, 0, 0)
    for i in range(n):
        row = row + eyeColor
    for i in range(n):
        row = row + skinColor
    for i in range(n):
        row = row + (0, 0, 0)
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        img.append(row)
        
    row = ()
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + (0, 0, 0)
    for i in range(n):
        row = row + skinColor
    for i in range(n):
        row = row + skinColor
    for i in range(n):
        row = row + skinColor
    for i in range(n):
        row = row + skinColor
    for i in range(n):
        row = row + skinColor
    for i in range(n):
        row = row + skinColor
    for i in range(n):
        row = row + skinColor
    for i in range(n):
        row = row + skinColor
    for i in range(n):
        row = row + (0, 0, 0)
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        img.append(row)
        
    row = ()
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + (0, 0, 0)
    for i in range(n):
        row = row + skinColor
    for i in range(n):
        row = row + skinColor
    for i in range(n):
        row = row + moustacheColor
    for i in range(n):
        row = row + moustacheColor
    for i in range(n):
        row = row + moustacheColor
    for i in range(n):
        row = row + moustacheColor
    for i in range(n):
        row = row + skinColor
    for i in range(n):
        row = row + skinColor
    for i in range(n):
        row = row + (0, 0, 0)
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        img.append(row)
        
    i = 0
    row = ()
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + (0, 0, 0)
    for i in range(n):
        row = row + skinColor
    for i in range(n):
        row = row + moustacheColor
    for i in range(n):
        row = row + skinColor
    for i in range(n):
        row = row + skinColor
    for i in range(n):
        row = row + skinColor
    for i in range(n):
        row = row + skinColor
    for i in range(n):
        row = row + moustacheColor
    for i in range(n):
        row = row + skinColor
    for i in range(n):
        row = row + (0, 0, 0)
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        img.append(row)
        
    row = ()
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + (0, 0, 0)
    for i in range(n):
        row = row + skinColor
    for i in range(n):
        row = row + skinColor
    for i in range(n):
        row = row + skinColor
    for i in range(n):
        row = row + moustacheColor
    for i in range(n):
        row = row + moustacheColor
    for i in range(n):
        row = row + skinColor
    for i in range(n):
        row = row + skinColor
    for i in range(n):
        row = row + skinColor
    for i in range(n):
        row = row + (0, 0, 0)
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        img.append(row)
        
    row = ()
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + (0, 0, 0)
    for i in range(n):
        row = row + (0, 0, 0)
    for i in range(n):
        row = row + (0, 0, 0)
    for i in range(n):
        row = row + (0, 0, 0)
    for i in range(n):
        row = row + (0, 0, 0)
    for i in range(n):
        row = row + (0, 0, 0)
    for i in range(n):
        row = row + (0, 0, 0)
    for i in range(n):
        row = row + (0, 0, 0)
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        img.append(row)
        
    row = ()
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + (0, 0, 0)
    for i in range(n):
        row = row + shirtColor
    for i in range(n):
        row = row + shirtColor
    for i in range(n):
        row = row + shirtColor
    for i in range(n):
        row = row + shirtColor
    for i in range(n):
        row = row + (0, 0, 0)
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        img.append(row)
        
    row = ()
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + (0, 0, 0)
    for i in range(n):
        row = row + shirtColor
    for i in range(n):
        row = row + shirtColor
    for i in range(n):
        row = row + shirtColor
    for i in range(n):
        row = row + shirtColor
    for i in range(n):
        row = row + shirtColor
    for i in range(n):
        row = row + shirtColor
    for i in range(n):
        row = row + (0, 0, 0)
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        row = row + randomColor
    for i in range(n):
        img.append(row)

    filename2 = 'cowboyNoBackground#' + str(countDisplay) + '.png'

    filename = 'cowboy#' + str(countDisplay) + '.png'
        
    with open(filename, 'wb') as f:
        w = png.Writer(width, height, greyscale=False)
        w.write(f, img)
