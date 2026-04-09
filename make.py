#!/usr/bin/env python3
import re, sys
out = []
for line in sys.stdin.read().splitlines():
    m = re.match(r"^\s*\d+\|(.*)$", line)
    if m:
        out.append(m.group(1))
text = "\n".join(out) + ("\n" if out else "")
open("/tmp/slf-1373/index.html", "w", newline="\n").write(text)
