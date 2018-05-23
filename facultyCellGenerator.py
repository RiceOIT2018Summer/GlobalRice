import readspreadsheet

DEFAULT_FACULTY_SID = '14rWedcwXlFQdqjHw2MnAZL6qNxZYwDvZO4VF4BdrAf0'

values = readspreadsheet.read(DEFAULT_FACULTY_SID)

if not values:
    print('No data found.')
else:
    htmlstr = open("cellTemplate.html").read()
    for row in values:
        htmlstrout = htmlstr.replace("[NAME]", row[0])
        htmlstrout = htmlstrout.replace("[DEPARTMENT]", row[3])
        htmlstrout = htmlstrout.replace("[WEBSITE]", row[4])
        htmlstrout = htmlstrout.replace("[PHOTO_SOURCE]", row[5])
        print(htmlstrout)
