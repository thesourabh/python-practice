str = """SGV5IGZvbGtzDQoNCkZvciB0aGlzIGNoYWxsZW5nZSwgeW91IGhhdmUgYmVlbiBnaXZlbiBhIHppcCBmaWxlIChQYXNzd29yZDogYmFzZTY0ZnR3KSB0aGF0IGNvbnRhaW5zIGEgcGhwIGZpbGUuDQoNCllvdSBuZWVkIHRvIHJ1biB0aGF0IHBocCBmaWxlIGluIGEgYnJvd3NlciBhbmQgbWFrZSBpdCBleGVjdXRlIHRoZSBwaHBpbmZvKCk7IGNvbW1hbmQuDQoNCllvdSBjYW4gYW5hbHlzZSB0aGUgc291cmNlIGNvZGUgYW5kIGZpZ3VyZSBvdXQgYSB3YXkgdG8gZG8gdGhhdC4NCg0KR29vZCBMdWNr"""


print str

for i in xrange(len(str)):
 a = str[i]
 b = str.find(a,i+1)
 if (b==-1):
  continue
 if (b == i):
  continue
 if (b==len(str)-1):
  continue
 if(str[i+1] == str[b+1]):
  if(str[i+2] == str[b+2]):
   print str[i:i+3]