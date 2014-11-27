#!/usr/bin/python

import random

def baseDencode(encode):
	s = encode
	keys = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
	keys2 = "ABCDEfghijkLMNoPQrstUVwXyZ"
	pad1 = "="
	x = [random.choice(keys2) for u in range(3)]
	d = ''.join(x)
	pad2 = "*"
	out = ""
	nums = 0
	a = random.choice(keys)
	b = random.choice(keys)
	i = 0
	while (i<len(s)):
		if nums == 6:
			out += keys[ord(s[i - 1]) & 63]
			out += keys[ord(s[i]) >> 2]
			nums = 2
		else:
			chr1 = ord(s[i - 1]) & (2 ** nums - 1)
			chr2 = ord(s[i]) >> (nums + 2)
			chrt = (chr1 << (6 - nums)) | chr2
			out += keys[chrt]
			nums += 2
		i = i + 1
	c = a + b
	if nums != 0:
		out += keys[(ord(s[len(s) - 1]) & (2 ** nums - 1)) << (6 - nums)]

	outs = c + out + d + pad1	
	return outs

print baseDencode("BaseD This")
