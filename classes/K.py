class Kangaroo:  # my own corrected codes

    def __init__(self, name, contents=None):
        self.name = name
        if contents is None:
            contents = []
        self.pouch_contents = contents

    def put_in_pouch(self, item):
        self.pouch_contents.append(item)

    def __str__(self):
        t = [self.name + ' has pouch contents:']
        for item in self.pouch_contents:
            s = '    ' + object.__str__(item)
            t.append(s)
        return '\n'.join(t)


k = Kangaroo('first_K')
k.put_in_pouch('apple')
k.put_in_pouch('second')
print(k)
r = Kangaroo('second_K')
k.put_in_pouch(r)
print(k)
print(r)
