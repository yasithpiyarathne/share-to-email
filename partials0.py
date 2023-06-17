from functools import partial

import permissions
import code_blocks
import sheets
import config

list_permissions = partial(permissions.list_permissions, service=code_blocks.drive, file_id=config.SHARED_FOLDER_ID)
get_sheet_data = partial(sheets.get_sheet_data, code_blocks.sheet, config.DATA_SHEET_ID, config.DATA_SHEET_TITLE)

get_readable_users = partial(code_blocks.get_readable_users, list_permissions())
get_submited_users = partial(code_blocks.get_submited_users, get_sheet_data())
grant_read = partial(permissions.create_permission, service=code_blocks.drive, file_id=config.SHARED_FOLDER_ID)
