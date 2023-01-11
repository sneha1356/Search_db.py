import os,string
def locate_drives():
    a = [x + ":" + "\\" for x in string.ascii_uppercase if os.path.exists(x + ":")]
    return a
locate_drives()