import read_csv as pr

##########################################################################################
# Filter out the right programs that matches the user's profile (min GPA, min Year, Major)

def check_requirements(myLines, currUser):
    # need to filter out programs that match their year, GPA, and major????
    filterGPAListIndex=list()
    filterNonBMGTListIndex=list()
    
    filterMinYearListIndex=list()
    filterMaxYearListIndex=list()
    finalFilterYearList=list()

    finalYearGPAList=list()
    finalList=list()
    userGPA = currUser["gpa"]
    userYear = currUser["year"]
    userBMGTStatus = currUser["bschool"]

    # Find the index values that has the minGPA restriction
    gpaList=pr.get_minGPA_list(myLines)
    for i in range(0, len(gpaList), 1):
        if (gpaList[i]<=str(userGPA)):
            filterGPAListIndex.append(i)
            
    # Find the index values of programs that are only for non-BMGT students
    reqMajorList=pr.get_reqMajor_list(myLines)
    for i in range(0, len(reqMajorList), 1):
        if ("N/A" in reqMajorList[i]):
            filterNonBMGTListIndex.append(i)
            
    # Find the index values of programs that required a minimum year less or equal to our user
    minYearList=pr.get_minYear_list(myLines)
    for i in range(0, len(minYearList), 1):
        if (minYearList[i]<=str(userYear)):
            filterMinYearListIndex.append(i)

    # Find the index values of programs that required a maximum year greater or equal to our user
    maxYearList=pr.get_maxYear_list(myLines)
    for i in range(0, len(maxYearList), 1):
        if (maxYearList[i]>=str(userYear)):
            filterMaxYearListIndex.append(i)

    # Find the similarities that has the right min and max year restriction
    for i in range(0, len(filterMinYearListIndex), 1):
        for j in range(0, len(filterMaxYearListIndex), 1):
            if (filterMinYearListIndex[i]==filterMaxYearListIndex[j]):
               finalFilterYearList.append(filterMinYearListIndex[i])

    # Compare the result of GPA and Year fiter lists
    for i in range(0, len(filterGPAListIndex), 1):
        for j in range(0, len(finalFilterYearList), 1):
            if (filterGPAListIndex[i]==finalFilterYearList[j]):
                if (userBMGTStatus=="BMGT"):
                    finalList.append(filterGPAListIndex[i])
                else:
                    finalYearGPAList.append(filterGPAListIndex[i])

    # If the student is not a BMGT major, filter by the non-BMGT parameter
    if (userBMGTStatus=="NON-BMGT"):
        for i in range(0, len(finalYearGPAList), 1):
            for j in range(0, len(filterNonBMGTListIndex), 1):
                if (finalYearGPAList[i]==filterNonBMGTListIndex[j]):
                    finalList.append(filterGPAListIndex[i])

    return finalList


##########################################################################################
# Corresponding function if user select their primary goal as: Price (#1)

def get_by_price(myLines, userList, price_input):

    stop=False
    filterRequirementList=list()
    
    allPriceList=pr.get_priceRange_list(myLines)

    for i in range(0, len(allPriceList), 1):
        for j in range(0, len(userList), 1):
            if (i==userList[j]):
                filterRequirementList.append(allPriceList[i])
    
    programNameList=pr.get_programName_list(myLines)
    indexResult=list()
    result=list()
    
        
    if (price_input==1):
        for i in range(0, len(filterRequirementList), 1):
            if ("1" in filterRequirementList[i]):
                indexResult.append(i)
        for i in range(0, len(indexResult), 1):
            result.append(programNameList[indexResult[i]])
    elif (price_input==2):
        for i in range(0, len(filterRequirementList), 1):
            if ("2" in filterRequirementList[i]):
                indexResult.append(i)
        for i in range(0, len(indexResult), 1):
            result.append(programNameList[indexResult[i]])
    elif (price_input==3):
        for i in range(0, len(filterRequirementList), 1):
            if ("3" in filterRequirementList[i]):
                indexResult.append(i)
        for i in range(0, len(indexResult), 1):
            result.append(programNameList[indexResult[i]])
    elif (price_input==4):
        for i in range(0, len(filterRequirementList), 1):
            if ("4" in filterRequirementList[i]):
                indexResult.append(i)
        for i in range(0, len(indexResult), 1):
            result.append(programNameList[indexResult[i]])
 
            
            
    if (len(result))> 10:
        return result[0:9]
    elif (len(result)==0):
        return ["There are no matches."]
    else:
        return result


##########################################################################################


##def check_country():
##
##    
##


##########################################################################################
# Corresponding function if user select their primary goal as: Location (#2)

def get_by_location(myLines, userList, location_input):
    stop=False
    filterRequirementList=list()

    allLocationList = pr.get_geographicArea_list(myLines)
    programNameList = pr.get_programName_list(myLines)
    indexResult=list()
    result=list()

    for i in range(0, len(allLocationList), 1):
        for j in range(0, len(userList), 1):
            if (i==userList[j]):
                filterRequirementList.append(allLocationList[i])
    
        
    if (location_input==1):
        for i in range(0, len(filterRequirementList), 1):
            if ("Europe" in filterRequirementList[i]):
                indexResult.append(i)
        for i in range(0, len(indexResult), 1):
            result.append(programNameList[indexResult[i]])
    elif (location_input==2):
        for i in range(0, len(filterRequirementList), 1):
            if ("Asia" in filterRequirementList[i]):
                indexResult.append(i)
        for i in range(0, len(indexResult), 1):
            result.append(programNameList[indexResult[i]])
    elif (location_input==3):
        for i in range(0, len(filterRequirementList), 1):
            if ("South America" in filterRequirementList[i]):
                indexResult.append(i)
        for i in range(0, len(indexResult), 1):
            result.append(programNameList[indexResult[i]])

    elif (location_input==4):
        for i in range(0, len(filterRequirementList), 1):
            if ("Africa" in filterRequirementList[i]):
                indexResult.append(i)
        for i in range(0, len(indexResult), 1):
            result.append(programNameList[indexResult[i]])

    elif (location_input==5):
        for i in range(0, len(filterRequirementList), 1):
            if ("Australia" in filterRequirementList[i]):
                indexResult.append(i)
        for i in range(0, len(indexResult), 1):
            result.append(programNameList[indexResult[i]])

    elif (location_input==6):
        for i in range(0, len(filterRequirementList), 1):
            if ("New Zealand" in filterRequirementList[i]):
                indexResult.append(i)
        for i in range(0, len(indexResult), 1):
            result.append(programNameList[indexResult[i]])

        
    if (len(result))> 10:
        return result[0:9]
    elif (len(result)==0):
        return ["There are no matches."]
    else:
        return result

##########################################################################################
# Corresponding function if user select their primary goal as: Duration (#3)

def get_by_duration(myLines, userList, duration_input):
    stop=False
    filterRequirementList=list()

    allDurationList = pr.get_durationLength_list(myLines)
    programNameList = pr.get_programName_list(myLines)
    indexResult=list()
    result=list()

    for i in range(0, len(allDurationList), 1):
        for j in range(0, len(userList), 1):
            if (i==userList[j]):
                filterRequirementList.append(allDurationList[i])

    if (duration_input==1):
        for i in range(0, len(filterRequirementList), 1):
            if ("Summer" in filterRequirementList[i]):
                indexResult.append(i)
        for i in range(0, len(indexResult), 1):
            result.append(programNameList[indexResult[i]])

    elif (duration_input==2):
        for i in range(0, len(filterRequirementList), 1):
            if ("Short-term (Winter)" in filterRequirementList[i]):
                indexResult.append(i)
        for i in range(0, len(indexResult), 1):
            result.append(programNameList[indexResult[i]])

    elif (duration_input==3):
        for i in range(0, len(filterRequirementList), 1):
            if ("Short-term (Spring)" in filterRequirementList[i]):
                indexResult.append(i)
        for i in range(0, len(indexResult), 1):
            result.append(programNameList[indexResult[i]])

    elif (duration_input==4):
        for i in range(0, len(filterRequirementList), 1):
            if ("Semester" in filterRequirementList[i]):
                indexResult.append(i)
        for i in range(0, len(indexResult), 1):
            result.append(programNameList[indexResult[i]])

    elif (duration_input==5):
        for i in range(0, len(filterRequirementList), 1):
            if ("Year" in filterRequirementList[i]):
                indexResult.append(i)
        for i in range(0, len(indexResult), 1):
            result.append(programNameList[indexResult[i]])

 
            
    if (len(result))> 10:
        return result[0:9]
    elif (len(result)==0):
        return ["There are no matches."]
    else:
        return result
        

##########################################################################################
# Corresponding function if user select their primary goal as: Topics (#4)

def get_by_topic(myLines, userList, topic_input):
    stop=False
    filterRequirementList=list()

    allTopicsList = pr.get_databaseTopic_list(myLines)
    programNameList = pr.get_programName_list(myLines)
    indexResult=list()
    result=list()

    for i in range(0, len(allTopicsList), 1):
        for j in range(0, len(userList), 1):
            if (i==userList[j]):
                filterRequirementList.append(allTopicsList[i])


    if (topic_input==1):
        for i in range(0, len(filterRequirementList), 1):
            if ("Business" in filterRequirementList[i]):
                indexResult.append(i)
        for i in range(0, len(indexResult), 1):
            result.append(programNameList[indexResult[i]])

    elif (topic_input==2):
        for i in range(0, len(filterRequirementList), 1):
            if ("STEM" in filterRequirementList[i]):
                indexResult.append(i)
        for i in range(0, len(indexResult), 1):
            result.append(programNameList[indexResult[i]])

    elif (topic_input==3):
        for i in range(0, len(filterRequirementList), 1):
            if ("Arts" in filterRequirementList[i]):
                indexResult.append(i)
        for i in range(0, len(indexResult), 1):
            result.append(programNameList[indexResult[i]])

    elif (topic_input==4):
        for i in range(0, len(filterRequirementList), 1):
            if ("Language" in filterRequirementList[i]):
                indexResult.append(i)
        for i in range(0, len(indexResult), 1):
            result.append(programNameList[indexResult[i]])

    elif (topic_input==5):
        for i in range(0, len(filterRequirementList), 1):
            if ("Social Sciences" in filterRequirementList[i]):
                indexResult.append(i)
        for i in range(0, len(indexResult), 1):
            result.append(programNameList[indexResult[i]])

    elif (topic_input==6):
        for i in range(0, len(filterRequirementList), 1):
            if ("Health" in filterRequirementList[i]):
                indexResult.append(i)
        for i in range(0, len(indexResult), 1):
            result.append(programNameList[indexResult[i]])
        print("There are", len(result), "matches.")
        stop=True


    if (len(result))> 10:
        return result[0:9]
    elif (len(result)==0):
        return ["There are no matches."]
    else:
        return result


##########################################################################################
# Corresponding function if user select their primary goal as: Language (#5)

def get_by_language(myLines, userList, language_input):
    stop=False
    filterRequirementList=list()

    allLanguagesList = pr.get_databaseTopic_list(myLines)
    programNameList = pr.get_programName_list(myLines)
    indexResult=list()
    result=list()

    for i in range(0, len(allLanguagesList), 1):
        for j in range(0, len(userList), 1):
            if (i==userList[j]):
                filterRequirementList.append(allLanguagesList[i])


    if (language_input==1):
        for i in range(0, len(filterRequirementList), 1):
            if ("Arabic" in filterRequirementList[i]):
                indexResult.append(i)
        for i in range(0, len(indexResult), 1):
            result.append(programNameList[indexResult[i]])
    elif (language_input==2):
        for i in range(0, len(filterRequirementList), 1):
            if ("Chinese" in filterRequirementList[i]):
                indexResult.append(i)
        for i in range(0, len(indexResult), 1):
            result.append(programNameList[indexResult[i]])
    elif (language_input==3):
        for i in range(0, len(filterRequirementList), 1):
            if ("Czech" in filterRequirementList[i]):
                indexResult.append(i)
        for i in range(0, len(indexResult), 1):
            result.append(programNameList[indexResult[i]])
    elif (language_input==4):
        for i in range(0, len(filterRequirementList), 1):
            if ("Dutch" in filterRequirementList[i]):
                indexResult.append(i)
        for i in range(0, len(indexResult), 1):
            result.append(programNameList[indexResult[i]])
    elif (language_input==5):
        for i in range(0, len(filterRequirementList), 1):
            if ("French" in filterRequirementList[i]):
                indexResult.append(i)
        for i in range(0, len(indexResult), 1):
            result.append(programNameList[indexResult[i]])
    elif (language_input==6):
        for i in range(0, len(filterRequirementList), 1):
            if ("German" in filterRequirementList[i]):
                indexResult.append(i)
        for i in range(0, len(indexResult), 1):
            result.append(programNameList[indexResult[i]])
    elif (language_input==7):
        for i in range(0, len(filterRequirementList), 1):
            if ("Italian" in filterRequirementList[i]):
                indexResult.append(i)
        for i in range(0, len(indexResult), 1):
            result.append(programNameList[indexResult[i]])
    elif (language_input==8):
        for i in range(0, len(filterRequirementList), 1):
            if ("Japanese" in filterRequirementList[i]):
                indexResult.append(i)
        for i in range(0, len(indexResult), 1):
            result.append(programNameList[indexResult[i]])
    elif (language_input==9):
        for i in range(0, len(filterRequirementList), 1):
            if ("Korean" in filterRequirementList[i]):
                indexResult.append(i)
        for i in range(0, len(indexResult), 1):
            result.append(programNameList[indexResult[i]])
    elif (language_input==10):
        for i in range(0, len(filterRequirementList), 1):
            if ("Portuguese" in filterRequirementList[i]):
                indexResult.append(i)
        for i in range(0, len(indexResult), 1):
            result.append(programNameList[indexResult[i]])
    elif (language_input==11):
        for i in range(0, len(filterRequirementList), 1):
            if ("Spanish" in filterRequirementList[i]):
                indexResult.append(i)
        for i in range(0, len(indexResult), 1):
            result.append(programNameList[indexResult[i]])


    if (len(result))> 10:
        return result[0:9]
    elif (len(result)==0):
        return ["There are no matches."]
    else:
        return result

  



