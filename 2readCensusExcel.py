import openpyxl,pprint

#Read the spreadsheet data
print('Opening workbook')
wb = openpyxl.load_workbook('censuspopdata.xlsx')
sheet = wb.active
countyData = {}

#Fill in countryData with each city's pop and tract
for row in range(2,sheet.max_row+1):
    #Each row in the spreasheet has data
    state = sheet['B' + str(row)].value
    county = sheet['C' + str(row)].value
    pop = sheet['D' + str(row)].value

    #make sure the key state exists
    countyData.setdefault(state,{})
    # make sure the key county in state exists
    countyData[state].setdefault(county,{'tract':0,'pop':0})
    #Each row represents one census tract , so increment by one
    countyData[state][county]['tract'] += 1
    #Increase the county pop by the pop in this census tract
    countyData[state][county]['pop'] += int(pop)

#Open a new text file and write the contents of countryData to in
print('Writing results...')
resultFile = open('census.py','w')
resultFile.write('allData = ' + pprint.pformat(countyData))
