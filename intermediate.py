color_name = {"Aliceblue":'#f0f8ff', 'Antiquewhite':'#faebd7', 'Antiquewhite1':'#ffefdb', 'Antiquewhite2':'#eedfcc', 'Antiquewhite3':'#cdc0b0', 'Antiquewhite4':'#8b8378', 'Aquamarine1':'#7fffd4', 'Aquamarine2':'#76eec6', 'Aquamarine4':'#458b74', 'Azure1':'#f0ffff'}
colorinput=input("Enter a color name: ").capitalize()

for key,value in color_name.items():
    if colorinput == key:
        print(value)