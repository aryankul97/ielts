import language_check
tool = language_check.LanguageTool('en-US')
matches = tool.check('<p>this are apple</p>')
print(len(matches)) #this will show the number of errors in the text
#print(matches[1])   #the number in [] points at the Nth error( 0 <= n < len). remove the [] to see all the errors.
#print(language_check.correct(text, matches)) #displays corrected text.