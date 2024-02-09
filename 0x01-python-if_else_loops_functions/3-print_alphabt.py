#!/usr/bin/python3
txt = "{alph}"
for asci in range(97, 123):
    if asci == 101:
        continue
    if asci == 113:
        continue
    print(txt.format(alph=chr(asci)), end="")
