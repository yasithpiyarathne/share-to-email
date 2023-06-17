def list_permissions(service, file_id):
    permissions = list()
    params = dict(
        fileId=file_id,
        pageSize=100,
        fields="nextPageToken, permissions(emailAddress, role)"
    )
    while True:
        res = service.permissions().list(**params).execute()
        permissions.extend(res['permissions'])
        if 'nextPageToken' in res:
            params['pageToken'] = res['nextPageToken']
        else:
            break
    return permissions


def create_permission(email, service, file_id, role='reader'):
    message = '''
    Thnak you for filling our Mini Project servay form.
    You can access the drive content using this link
    https://drive.google.com/drive/folders/1EcXcXXltAJ-t_mhOtk4Kfb-rtAtSywtC?usp=sharing
    '''
    return service.permissions().create(
        fileId=file_id,
        body=dict(type='user', role=role, emailAddress=email, sendNotificationEmail=True, emailMessage=message)
    ).execute()