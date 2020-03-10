#! python3

import re, pyperclip

# phone number regex
phoneRegex = re.compile(r'''
((\d\d\d-|\(\d\d\d\)\s)? #area code
(\d\d\d-)                  #three digits
(\d\d\d\d))                #four digits

''' , re.VERBOSE)
#email regex
emailRegex = re.compile(r'''
[a-zA-Z0-9_.+]+  #username
@                #@
[a-zA-Z0-9_.+]+  #domain

''', re.VERBOSE)

#copy text off clipboard
text = pyperclip.paste()

#extract phone and email
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhone = []
for P in extractedPhone:
    allPhone.append(P[0])


#copy extracted phone and email to clipboard
results = '\n'.join(allPhone) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)
