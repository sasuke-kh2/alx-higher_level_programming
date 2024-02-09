#!/usr/bin/python3
txt = "{alph}"
for acsi in range(97, 123):
    print(txt.format(alph=chr(acsi)), end="")
