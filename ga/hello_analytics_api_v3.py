import sys
import unicodedata

# import the Auth Helper class
import hello_analytics_api_v3_auth

from apiclient.errors import HttpError
from oauth2client.client import AccessTokenRefreshError

def main(argv):
  # Step 1. Get an analytics service object.
  service = hello_analytics_api_v3_auth.initialize_service()

  try:
    # Step 2. Get the user's first profile ID.
    profile_id = get_first_profile_id(service)

    if profile_id:
      # Step 3. Query the Core Reporting API.
      results = get_results(service, profile_id)

      # Step 4. Output the results.
      print_results(results)

  except TypeError, error:
    # Handle errors in constructing a query.
    print ('There was an error in constructing your query : %s' % error)

  except HttpError, error:
    # Handle API errors.
    print ('Arg, there was an API error : %s : %s' %
           (error.resp.status, error._get_reason()))

  except AccessTokenRefreshError:
    # Handle Auth errors.
    print ('The credentials have been revoked or expired, please re-run '
           'the application to re-authorize')

def get_first_profile_id(service):
  # Get a list of all Google Analytics accounts for this user
  accounts = service.management().accounts().list().execute()

  if accounts.get('items'):
    # Get the first Google Analytics account
    firstAccountId = accounts.get('items')[0].get('id')

    # Get a list of all the Web Properties for the first account
    webproperties = service.management().webproperties().list(accountId=firstAccountId).execute()

    if webproperties.get('items'):
      # Get the first Web Property ID
      firstWebpropertyId = webproperties.get('items')[0].get('id')

      # Get a list of all Views (Profiles) for the first Web Property of the first Account
      profiles = service.management().profiles().list(
          accountId=firstAccountId,
          webPropertyId=firstWebpropertyId).execute()

      if profiles.get('items'):
        # return the first View (Profile) ID
        return profiles.get('items')[0].get('id')

  return None
start = 1
def get_results(service, profile_id):
  global start
  # Use the Analytics Service Object to query the Core Reporting API
  return service.data().ga().get(
      ids='ga:' + profile_id,
      start_date='2012-03-03',
      end_date='2014-03-03',
      dimensions = 'ga:landingPagePath',
      # start-index = 1000,
      start_index=start,
      sort= '-ga:sessions',
      metrics='ga:sessions,ga:bounces').execute()

# def unicode_convertor(lis):
#   full = []
  
#   # for i in lis: 
#   #   temp = []
#   #   for j in i: 
#   #     temp = temp.append(str(j))
#   #   full.append(temp)
#   # return full

def print_results(results):
  global start
  # Print data nicely for the user.
  while results:
    t = results.get('rows')
    print results.get('totalResults'), 
    print '\n'
    f = open('fdf.csv', 'a')
    for i in t:      
      for j in i: 
        
        try:
          f.write(j)
        except: 
          f.write(unicodedata.normalize('NFKD', j).encode('ascii','ignore'))
        f.write(',')
      f.write('\n')
    start += 1000
    f.close()
    print start
    main(sys.argv)

    


  else:
    print 'No results found'



if __name__ == '__main__':
  main(sys.argv)