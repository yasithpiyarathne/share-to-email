def get_readable_users(data_list):
    email_mapper = lambda user:user['emailAddress']
    reading_filter = lambda user:user['role']=='reader'
    return list(map(email_mapper, filter(reading_filter, data_list)))


def get_submited_users(data_list):
    email_mapper = lambda user:user['email']
    return list(map(email_mapper, data_list))

# def grant_access_from_partial(core):
#     submitted_users = core.get_submited_users()
#     print(submitted_users)
#     users_with_access = core.get_readable_users()
#     print(users_with_access)
#     users_without_access = [user for user in submitted_users if user not in users_with_access]
#     print(users_without_access)

#     successful = list()
#     unsuccessful = list()

#     for user in users_without_access:
#         try:
#             core.grant_read(user)
#             successful.append(user)
#         except HttpError as err:
#             unsuccessful.append((user, err.reason))

#     return successful, unsuccessful