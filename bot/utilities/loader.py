def load_input(as_string=False):
    import urllib.request

    uf = urllib.request.urlopen('https://pastebin.com/raw/610rHMi0')
    content = uf.readlines()

    if as_string:
        return content[0].decode('utf-8').replace('\r\n', '')
    return [line.decode('utf-8').strip('\r\n') for line in content]