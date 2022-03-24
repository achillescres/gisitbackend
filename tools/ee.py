def auth(service_account, json_key_path):
    try:
        import ee

        credentials = ee.ServiceAccountCredentials(service_account, json_key_path)
        ee.Initialize(credentials)

        print('Successful auth')
    except Exception as e:
        print('Auth error')
        print(e)


def fires():
    pass