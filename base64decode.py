#!/usr/bin/python

def decodebase64(decode):
	s = decode
	keys = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
	out = ""
	nums = 0
	i = 0
	while(i<len(s)):
		if nums == 0:
			nums = 6
		else:
			chr1 = keys.index(s[i - 1]) & (2 ** nums - 1)
			chr2 = keys.index(s[i]) >> (nums - 2)
			chrt = (chr1 << (8 - nums)) | chr2
			out += chr(chrt)
			nums -= 2
		i = i + 1
	return out

print decodebase64("QmFzZTY0IFRoaXM");
