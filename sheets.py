def get_sheet_data(service, sheet_id, data_range):
    sheet = service.spreadsheets()
    sheet_res = sheet.values().get(spreadsheetId=sheet_id,
                            range=data_range).execute()
    values:list[list] = sheet_res['values']
    headers = values.pop(0)
    data = list()
    for record in values:
        data.append({key: val for (key, val) in zip(headers, record)})
    return data