#from apiclient.discovery import build
#
#client_secrets = 'client_secrets.json'
#
#service = build('')

from googleapiclient import discovery
from oauth2client.client import GoogleCredentials
import argparse
import pprint
import httplib2
import urllib.request

pp = pprint.PrettyPrinter(indent=4)
def printer(stuff):
    return pp.pprint(stuff)


# [START get_vision_service]
DISCOVERY_URL='https://{api}.googleapis.com/$discovery/rest?version={apiVersion}'

def get_vision_service():
    credentials = GoogleCredentials.get_application_default()
    return discovery.build('vision', 'v1', credentials=credentials,
                            discoveryServiceUrl=DISCOVERY_URL)
# [END get_vision_service]


# [START identify_image]
def identify_image(gcs_uri, max_results=4):
    """Uses the Vision API to identify the given image

    Args:
        gcs_uri: A uri of the form: gs://bucket/object

    Returns:
        An array of dicts with information about the picture..
    """
    batch_request = [{
        'image': {
            'source': {
                'gcs_image_uri': gcs_uri
            }
        },
        'features': [{
            'type': 'LABEL_DETECTION',
            'maxResults': max_results,
        }]
    }]

    service = get_vision_service()
    request = service.images().annotate(body={
        'requests': batch_request,
        })
    response = request.execute()

    return response['responses'][0].get('labelAnnotations', None)
# [END identify_image]


# [START main]
def main(gcs_uri):
    if gcs_uri[:5] != 'gs://':
        raise Exception('Image uri must be of the form gs://bucket/object')
    annotations = identify_image(gcs_uri)
    if not annotations:
        print('No landmark identified')
    else:
        print('\n'.join(annotation['description'] for annotation in annotations))
# [END main]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
            description='Identifies the given image.')
    parser.add_argument(
            'gcs_uri', help=('The google Cloud Storage uri to the image to identify'
                ', of the form: gs://bucket_Name/object_name.jpg'))
    args = parser.parse_args()

    main(args.gcs_uri)
