#!/usr/bin/python3
txt = "{alph}"
for acsi in range(0, 99):
    print(acsi, "=", txt.format(alph=hex(acsi)))
