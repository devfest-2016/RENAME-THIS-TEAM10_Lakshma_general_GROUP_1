from oauth2client.contrib import gce
import httplib2

credentials = gce.AppAssertionCredentials(
    scope='https://www.googleapis.com/auth/drive.read_write')
http = credentials.authorize(httplib2.Http())
service = discovery.build('drive', 'v2', http=http)


print(http)
