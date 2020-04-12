def estimator(data):
  """ Provide the estimate calulations based on that data received """
  #Collect required data from data imput
  impact = {}
  severeImpact = {}
  reportedCases = data['reportedCases']
  periodType = data['periodType']
  timeToElapse = data['timeToElapse']

  
  #CHALLENGE 1

  duration = get_duration_in_day(periodType, timeToElapse)
  factor = duration//3

  #For Impact
  impact['currentlyInfected'] = reportedCases * 10
  impact['infectionsByRequestedTime'] = impact['currentlyInfected'] * (2**factor)

  #For Severe Impact
  severeImpact['currentlyInfected'] = reportedCases * 50
  severeImpact['infectionsByRequestedTime'] = severeImpact['currentlyInfected']*(2**factor)


  result = {'data':data, 'impact':impact, 'severeImpact': severeImpact}

  return result

def get_duration_in_day(periodType, timeToElapse):
    """ Calculates the number of days in that period types received from the data input """

    if periodType == "days":
        return timeToElapse
    elif periodType == "weeks":
        return timeToElapse * 7
    elif periodType == "months":
        return timeToElapse * 30
    else:
        return 0



