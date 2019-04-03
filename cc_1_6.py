def sCompress(s):
	current = ''
	cnt =0
	r = ''
	for i in range(len(s)):
		print('s[i],cnt:',s[i],cnt)
		if s[i] == current:
			cnt+=1
		else:
			if cnt >0: r+=str(cnt)
			current =s[i]
			r+=current
			cnt =1		
		#r= r+current+str(cnt)
	r+=str(cnt)
	if len(r)>len(s): return s
	return r

def main():
	s = 'aaaabcc'
	r = sCompress(s)
	print(r)

main()
