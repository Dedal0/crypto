#!/usr/bin/python

def base64encode(encode):
	s = encode
	keys = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
	out = ""
	nums = 0
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
	if nums != 0:
		out += keys[(ord(s[len(s) - 1]) & (2 ** nums - 1)) << (6 - nums)]

	return out

print base64encode("Base64 This")
