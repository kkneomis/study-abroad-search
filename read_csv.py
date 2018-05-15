import re

def read_project_csv(thisFileName):
    fileHandler= open(thisFileName, 'r', encoding='utf-8')
    lines=fileHandler.readlines()
    fileHandler.close()
    totalAmountOfLines = len(lines)
    return lines;

def get_programName_list(thisList):
    totalAmountOfLines=len(thisList)
    programName = list()
    
    for i in range(1, totalAmountOfLines, 1):
        commaSplitList = re.split('[,]', thisList[i]);
        for i in range(0, 1, 1):
            programName.append(commaSplitList[i])

    return programName;

def get_databaseTopic_list(thisList):
    totalAmountOfLines=len(thisList)
    databaseTopic = list()
    
    for i in range(1, totalAmountOfLines, 1):
        commaSplitList = re.split('[,]', thisList[i]);
        for i in range(0, 1, 1):
            databaseTopic.append(commaSplitList[i+1])

    return databaseTopic;

def get_durationLength_list(thisList):
    totalAmountOfLines=len(thisList)
    durationLength = list()
    
    for i in range(1, totalAmountOfLines, 1):
        commaSplitList = re.split('[,]', thisList[i]);
        for i in range(0, 1, 1):
            durationLength.append(commaSplitList[i+2])

    return durationLength;

def get_geographicArea_list(thisList):
    totalAmountOfLines=len(thisList)
    geographicArea = list()
    
    for i in range(1, totalAmountOfLines, 1):
        commaSplitList = re.split('[,]', thisList[i]);
        for i in range(0, 1, 1):
            geographicArea.append(commaSplitList[i+3])

    return geographicArea;

def get_priceRange_list(thisList):
    totalAmountOfLines=len(thisList)
    priceRange = list()
    
    for i in range(1, totalAmountOfLines, 1):
        commaSplitList = re.split('[,]', thisList[i]);
        for i in range(0, 1, 1):
            priceRange.append(commaSplitList[i+4])

    return priceRange;

def get_minYear_list(thisList):
    totalAmountOfLines=len(thisList)
    minYear = list()
    
    for i in range(1, totalAmountOfLines, 1):
        commaSplitList = re.split('[,]', thisList[i]);
        for i in range(0, 1, 1):
            minYear.append(commaSplitList[i+5])

    return minYear;

def get_maxYear_list(thisList):
    totalAmountOfLines=len(thisList)
    maxYear = list()
    
    for i in range(1, totalAmountOfLines, 1):
        commaSplitList = re.split('[,]', thisList[i]);
        for i in range(0, 1, 1):
            maxYear.append(commaSplitList[i+6])

    return maxYear;

def get_reqMajor_list(thisList):
    totalAmountOfLines=len(thisList)
    reqMajor = list()
    
    for i in range(1, totalAmountOfLines, 1):
        commaSplitList = re.split('[,]', thisList[i]);
        for i in range(0, 1, 1):
            reqMajor.append(commaSplitList[i+7])

    return reqMajor;

def get_languages_list(thisList):
    totalAmountOfLines=len(thisList)
    languages = list()
    
    for i in range(1, totalAmountOfLines, 1):
        commaSplitList = re.split('[,]', thisList[i]);
        for i in range(0, 1, 1):
            languages.append(commaSplitList[i+8])

    return languages;

def get_minGPA_list(thisList):
    totalAmountOfLines=len(thisList)
    minGPA = list()
    
    for i in range(1, totalAmountOfLines, 1):
        commaSplitList = re.split('[,]', thisList[i]);
        for i in range(0, 1, 1):
            commaSplitList[i+9]=commaSplitList[i+9].replace('\n','')
            minGPA.append(commaSplitList[i+9])

    return minGPA;

# myLines = read_project_csv('Project_Master_Sheet_V2.csv')
# print("Output: ", get_minGPA_list(myLines))
