from pynput.keyboard import Key, Listener

maxCommandLength = 50
recorder = {
    is_listening: False,
    keys_recorded: []
}
commandStartKey = '`'

def on_press(key):
    try:
        if key.char == commandStartKey:
            recorder['keys_recorded'].clear()
            if not recorder['is_listening']:
                recorder['is_listening'] = True
            return
    except SOMEEXCEPTION: # which exception and for what line are you expecting one?
        return
    if len(recorder['keys_recorded']) > maxCommandLength:
        recorder['keys_recorded'].clear()
        if recorder['is_listening']:
            recorder['is_listening'] = False
        return
    #if not listening:
    #    return
    recorder['keys_recorded'].append(key.char)
    print(recorder['keys_recorded'])
