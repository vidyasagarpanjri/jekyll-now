import sys
t ='''
<?xml version="1.0"?>
	<!--
	API Monitor Filter
	(c) 2010-2013, Rohitab Batra <rohitab@rohitab.com>
	http://www.rohitab.com/apimonitor/
	-->
<ApiMonitor>
	<CaptureFilter>
        {0}
	</CaptureFilter>
</ApiMonitor>
'''
if len(sys.argv) != 2:
        exit(1)
api_name = open(sys.argv[1],'r').read().split('\n')
tmp1={}
for name in api_name:
    try:
        tmp = name.split('.')
        tmp1[tmp[1]]=tmp[0]
    except:
        pass

flipped = {}

for key, value in tmp1.items():
    if value not in flipped:
        flipped[value] = [key]
    else:
        flipped[value].append(key)

# printing result
modules = ''' 
    <Module Name="{0}.dll">
        {1}		
    </Module>\n'''
a = ''

for k,v in flipped.items():
    api = '''       <Api Name="{0}"/>\n'''
    api_n=''
    for va in v:
        api_n += api.format(va) 
    a += modules.format(k,api_n)
print t.format(a)



