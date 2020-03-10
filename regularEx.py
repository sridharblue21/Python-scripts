import re
message = 'Call me at 111-222-1234 tomorrow. 333-444-1234 is my office line.'
message1 = 'Superusers and Superman met at sudo park.'
message2 = 'Superwowowoman and Superusers met at sudo park.'
message3 = 'are you ready for dinner?'
message4 = 'my phone numbers are 111-222-0000,444-2222,444-515-9090,000-989-9999'
message5 = 'I have two phone numbers, they are 111-222-1234 and 333-444-1234.'
message6 = '10 lords a-leaping 11 pipers piping 12 drummers drumming'
message7 = 'this is to test user defined character class.'
message8 = '5949494094309'
message9 = 'this is to test user defined character class.'
message10 = 'first name sri last name dhar'
message11 = '<this is a test> continues till here>>>'
message12 = 'this is line one. \nthis is line two. \nthis is line three'
message13 = 'this is tO test USER defined character class.'
message14 = 'Agent Sam gave the secret document to Agent Bob'

regex = re.compile(r'(\d\d\d-)?(\d\d\d)-(\d\d\d\d)')
regex1 = re.compile(r'Super(man|women|sudo|user)')
regex2 = re.compile(r'Super(wo)+man')
regex3 = re.compile(r'dinner\?')
regex4 = re.compile(r'((\d\d\d-)?(\d\d\d)-(\d\d\d\d)(,)?){2,5}?')
regex5 = re.compile(r'((\d\d\d)-(\d\d\d-\d\d\d\d))')
regex6 = re.compile(r'\d+\s\w+')
regex7 = re.compile(r'[^aeiouAEIOU]')
regex8 = re.compile(r'^\d+$')
regex9 = re.compile(r'.{2}a')
regex10 = re.compile(r'first name(.*) last name(.*)')
regex11 = re.compile(r'(<.*>)')
regex12 = re.compile(r'.*', re.DOTALL)
regex13 = re.compile(r'[aeiou]',re.I)
regex14 = re.compile(r'Agent \w+')
mo = regex14.sub(r'Agent ****' , message14)
#print(mo[0:2])
print(mo)





