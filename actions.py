# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"
from __future__ import print_function
from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals


from typing import Any, Text, Dict, List
from rasa.constants import DEFAULT_DATA_PATH
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from rasa_sdk.events import SlotSet


class ActionWeather(Action):

    def name(self) -> Text:
        return "action_weather_api"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        city = tracker.latest_message['text']
        temp = int(Weather(city)['temp']-273)
        dispatcher.utter_template("utter_temp", tracker, temp=temp)

        return []


class ActionQuestion(Action):

    def name(self) -> Text:
        return "action_question"

    def run(self, dispatcher: CollectingDispatcher,

            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        import pickle
        import os.path
        from googleapiclient.discovery import build
        from google_auth_oauthlib.flow import InstalledAppFlow
        from google.auth.transport.requests import Request
        import logging

        logging.getLogger('googleapicliet.discovery_cache').setLevel(logging.ERROR)

        SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']

        creds = None
        if os.path.exists('tokene.pickle'):
            with open('tokene.pickle', 'rb') as token:
                creds = pickle.load(token)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)

            with open('tokene.pickle', 'wb') as token:
                pickle.dump(creds, token)

        service = build('drive', 'v3', credentials=creds)

        question = tracker.get_slot("document")
        dispatcher.utter_message(
            'Sure, Here it is , please refer below documents for %s .  Hope it helps!' % (question))
        page_token = None
        i = 1
        while i < 6:
            response = service.files().list(
                q='(fullText contains \'{0}\' and name contains \'{0}\')'.format(question, question),
                spaces='drive',
                fields='nextPageToken, files(id, name)',
                pageSize='1',
                pageToken=page_token).execute()
            for file in response.get('files', []):
                dispatcher.utter_message('please visit the link https://drive.google.com/open?id=%s' % (file.get('id')))

            page_token = response.get('nextPageToken', None)
            if page_token is None:
                break
            i += 1

        return []





class ActionEmail(Action):

    def name(self) -> Text:
        return "action_send_email"

    def run(self, dispatcher, tracker, domain):
        # Get user's email id
        to_emails = tracker.get_slot('email')


        import base64
        from email.mime.text import MIMEText
        from email.mime.image import MIMEImage
        from email.mime.multipart import MIMEMultipart
        from email.mime.audio import MIMEAudio
        from email.mime.base import MIMEBase
        import mimetypes
        import pickle
        import os.path
        from apiclient import errors
        from googleapiclient.discovery import build
        from google_auth_oauthlib.flow import InstalledAppFlow
        from google.auth.transport.requests import Request

        # If modifying these scopes, delete the file token.pickle.
        SCOPES = ['https://mail.google.com/']

        def get_service():
            creds = None
            # The file token.pickle stores the user's access and refresh tokens, and is
            # created automatically when the authorization flow completes for the first
            # time.
            if os.path.exists('token.pickle'):
                with open('token.pickle', 'rb') as token:
                    creds = pickle.load(token)
            # If there are no (valid) credentials available, let the user log in.
            if not creds or not creds.valid:
                if creds and creds.expired and creds.refresh_token:
                    creds.refresh(Request())
                else:
                    flow = InstalledAppFlow.from_client_secrets_file(
                        'credential.json', SCOPES)
                    creds = flow.run_local_server(port=0)
                # Save the credentials for the next run
                with open('token.pickle', 'wb') as token:
                    pickle.dump(creds, token)

            service = build('gmail', 'v1', credentials=creds)

            return service

        def send_message(service, user_id, message):
            try:
                message = service.users().messages().send(userId=user_id,
                                                          body=message).execute()

                print('Message Id: {}'.format(message['id']))

                return message
            except Exception as e:
                print('An error occurred: {}'.format(e))
                return None

        def create_message_with_attachment(
                sender,
                to,
                subject,
                message_text,
                file,
        ):

            message = MIMEMultipart()
            message['to'] = to
            message['from'] = sender
            message['subject'] = subject

            msg = MIMEText(message_text)
            message.attach(msg)

            (content_type, encoding) = mimetypes.guess_type(file)

            if content_type is None or encoding is not None:
                content_type = 'application/octet-stream'

            (main_type, sub_type) = content_type.split('/', 1)

            if main_type == 'text':
                with open(file, 'rb') as f:
                    msg = MIMEText(f.read().decode('utf-8'), _subtype=sub_type)

            elif main_type == 'image':
                with open(file, 'rb') as f:
                    msg = MIMEImage(f.read(), _subtype=sub_type)

            elif main_type == 'audio':
                with open(file, 'rb') as f:
                    msg = MIMEAudio(f.read(), _subtype=sub_type)

            else:
                with open(file, 'rb') as f:
                    msg = MIMEBase(main_type, sub_type)
                    msg.set_payload(f.read())

            filename = os.path.basename(file)
            msg.add_header('Content-Disposition', 'attachment',
                           filename=filename)
            message.attach(msg)

            raw_message = \
                base64.urlsafe_b64encode(message.as_string().encode('utf-8'))
            return {'raw': raw_message.decode('utf-8')}

        if __name__ == "__main__":
            service = get_service()
            user_id = 'me'
            tos = "eshaan201@gmail.com"
            msg = create_message_with_attachment('eshaan201@gmail.com', tos,
                                                 'this is the subject line so be happy',
                                                 'This is the message body i am happy', './happy.txt')
            send_message(service, user_id, msg)




class ActionQuestions(Action):

    def name(self) -> Text:
        return "action_questions"

    def run(self, dispatcher: CollectingDispatcher,

            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        import pickle
        import os.path
        from googleapiclient.discovery import build
        from google_auth_oauthlib.flow import InstalledAppFlow
        from google.auth.transport.requests import Request
        import logging

        logging.getLogger('googleapicliet.discovery_cache').setLevel(logging.ERROR)

        SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']

        creds = None
        if os.path.exists('tokene.pickle'):
            with open('tokene.pickle', 'rb') as token:
                creds = pickle.load(token)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)

            with open('tokene.pickle', 'wb') as token:
                pickle.dump(creds, token)

        service = build('drive', 'v3', credentials=creds)

        question = tracker.get_slot("document")
        dispatcher.utter_message(
            ' %s ' % (question))
        page_token = None
        i = 1
        while i < 6:
            response = service.files().list(
                q='(fullText contains \'{0}\' and name contains \'{0}\')'.format(question, question),
                spaces='drive',
                fields='nextPageToken, files(id, name)',
                pageSize='1',
                pageToken=page_token).execute()
            for file in response.get('files', []):
                dispatcher.utter_message('please visit the link https://drive.google.com/open?id=%s' % (file.get('id')))

            page_token = response.get('nextPageToken', None)
            if page_token is None:
                break
            i += 1

        return []

class ActionQuestionsa(Action):

    def name(self) -> Text:
        return "action_introductory"

    def run(self, dispatcher: CollectingDispatcher,

            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        import pickle
        import os.path
        from googleapiclient.discovery import build
        from google_auth_oauthlib.flow import InstalledAppFlow
        from google.auth.transport.requests import Request
        import logging

        logging.getLogger('googleapicliet.discovery_cache').setLevel(logging.ERROR)

        SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']

        creds = None
        if os.path.exists('tokene.pickle'):
            with open('tokene.pickle', 'rb') as token:
                creds = pickle.load(token)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)

            with open('tokene.pickle', 'wb') as token:
                pickle.dump(creds, token)

        service = build('drive', 'v3', credentials=creds)

        question = "Introduction to Data Science"
        dispatcher.utter_message(
            'Please refer below documents for %s .  Hope it helps to learn data science!' % (question))
        page_token = None
        i = 1
        while i < 6:
            response = service.files().list(
                q='(fullText contains \'{0}\' and name contains \'{0}\')'.format(question, question),
                spaces='drive',
                fields='nextPageToken, files(id, name)',
                pageSize='1',
                pageToken=page_token).execute()
            for file in response.get('files', []):
                dispatcher.utter_message('please visit the link https://drive.google.com/open?id=%s' % (file.get('id')))

            page_token = response.get('nextPageToken', None)
            if page_token is None:
                break
            i += 1

        return []

class ActionML(Action):

    def name(self) -> Text:
        return "action_machine_learning"

    def run(self, dispatcher: CollectingDispatcher,

            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        import pickle
        import os.path
        from googleapiclient.discovery import build
        from google_auth_oauthlib.flow import InstalledAppFlow
        from google.auth.transport.requests import Request
        import logging

        logging.getLogger('googleapicliet.discovery_cache').setLevel(logging.ERROR)

        SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']

        creds = None
        if os.path.exists('tokene.pickle'):
            with open('tokene.pickle', 'rb') as token:
                creds = pickle.load(token)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)

            with open('tokene.pickle', 'wb') as token:
                pickle.dump(creds, token)

        service = build('drive', 'v3', credentials=creds)

        question = "Machine Learning"
        dispatcher.utter_message(
            'Please refer below documents for %s .  Hope it helps to learn data science!' % (question))
        page_token = None
        i = 1
        while i < 6:
            response = service.files().list(
                q='(fullText contains \'{0}\' and name contains \'{0}\')'.format(question, question),
                spaces='drive',
                fields='nextPageToken, files(id, name)',
                pageSize='1',
                pageToken=page_token).execute()
            for file in response.get('files', []):
                dispatcher.utter_message('please visit the link https://drive.google.com/open?id=%s' % (file.get('id')))

            page_token = response.get('nextPageToken', None)
            if page_token is None:
                break
            i += 1

        return []


class ActionDL(Action):

    def name(self) -> Text:
        return "action_deep_learning"

    def run(self, dispatcher: CollectingDispatcher,

            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        import pickle
        import os.path
        from googleapiclient.discovery import build
        from google_auth_oauthlib.flow import InstalledAppFlow
        from google.auth.transport.requests import Request
        import logging

        logging.getLogger('googleapicliet.discovery_cache').setLevel(logging.ERROR)

        SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']

        creds = None
        if os.path.exists('tokene.pickle'):
            with open('tokene.pickle', 'rb') as token:
                creds = pickle.load(token)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)

            with open('tokene.pickle', 'wb') as token:
                pickle.dump(creds, token)

        service = build('drive', 'v3', credentials=creds)

        question = "Deep Learning"
        dispatcher.utter_message(
            'Please refer below documents for %s .  Hope it helps to learn data science!' % (question))
        page_token = None
        i = 1
        while i < 6:
            response = service.files().list(
                q='(fullText contains \'{0}\' and name contains \'{0}\')'.format(question, question),
                spaces='drive',
                fields='nextPageToken, files(id, name)',
                pageSize='1',
                pageToken=page_token).execute()
            for file in response.get('files', []):
                dispatcher.utter_message('please visit the link https://drive.google.com/open?id=%s' % (file.get('id')))

            page_token = response.get('nextPageToken', None)
            if page_token is None:
                break
            i += 1

        return []

