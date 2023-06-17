from oauth2client.service_account import ServiceAccountCredentials 
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build

import config

credentials = ServiceAccountCredentials.from_json_keyfile_name(config.SERVICE_KEY_PATH, [config.SCOPE])

drive = build('drive', 'v3', credentials=credentials)
sheet = build('sheets', 'v4', credentials=credentials)

def get_readable_users(data_list):
    email_mapper = lambda user:user['emailAddress']
    reading_filter = lambda user:user['role']=='reader'
    return list(map(email_mapper, filter(reading_filter, data_list)))


def get_submited_users(data_list):
    email_mapper = lambda user:user['email']
    return list(map(email_mapper, data_list))

def grant_access_from_partial(core):
    submitted_users = core.get_submited_users()
    users_with_access = core.get_readable_users()
    users_without_access = [user for user in submitted_users if user not in users_with_access]

    successful = list()
    unsuccessful = list()

    for user in users_without_access:
        try:
            core.grant_read(user)
            successful.append(user)
        except HttpError as err:
            unsuccessful.append((user, err.reason))

    return successful, unsuccessful