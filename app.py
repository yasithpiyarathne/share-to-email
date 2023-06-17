from flask import Flask, render_template
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials
from googleapiclient.errors import HttpError

import config
import code_blocks
import permissions
import sheets

app = Flask(__name__)

@app.route('/')
def grant_access():
    credentials = ServiceAccountCredentials.from_json_keyfile_name(config.SERVICE_KEY_PATH, [config.SCOPE])
    sheet = build('sheets', 'v4', credentials=credentials)
    drive = build('drive', 'v3', credentials=credentials)

    submitted_users = code_blocks.get_submited_users(sheets.get_sheet_data(sheet, config.DATA_SHEET_ID, config.DATA_SHEET_TITLE))
    print(submitted_users)
    users_with_access = code_blocks.get_readable_users(permissions.list_permissions(drive, config.SHARED_FOLDER_ID))
    print(users_with_access)

    users_without_access = [user for user in submitted_users if user not in users_with_access]
    print(users_without_access)
    successful = list()
    unsuccessful = list()

    for user in users_without_access:
        if user:
            try:
                permissions.create_permission(user, drive, config.SHARED_FOLDER_ID)
                successful.append(user)
            except HttpError as err:
                unsuccessful.append((user, err.reason))
    return render_template('access_template.html', successful=successful, unsuccessful=unsuccessful)
