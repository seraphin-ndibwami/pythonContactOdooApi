import requests
import json
import base64


def connect_to_odoo_api(url: str, parameters: dict) -> str:
    """
    Connects to an Odoo instance using the RESTful API.
    Returns:
        str or None: The session_id from the API, or None if an error occurs.
    """
    session_url = f'{url}/web/session/authenticate'

    params = {
        'jsonrpc': '2.0',
        'method': 'call',
        'params': parameters
    }

    try:
        session_response = requests.post(session_url, json=params)
        session_response.raise_for_status()  # Raise an exception for HTTP errors

        session_data = session_response.json()

        if session_data.get('result') and session_response.cookies.get('session_id'):
            print('\n Successfully authenticated.',
                  session_response.cookies['session_id'], '\n')
            return session_response.cookies['session_id']
        else:
            print(
                f'Error: Failed to authenticate - {session_data.get("error")}')
            return None
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None


def send_data_with_files(url: str, path: str, data: dict, files: dict, headers: dict) -> dict:
    """
    Send data along with files to the specified API endpoint.
    Args:
        url (str): The base URL of the API.
        path (str): The API endpoint path.
        data (dict): The data to send in the request.
        files (dict): The files to send in the request.
        headers (dict): The headers for the request.
    Returns:
        dict: The JSON response from the API.
    """
    endpoint = f'{url}{path}'

    try:
        response = requests.post(
            endpoint, headers=headers, data=data, files=files)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None
    except json.JSONDecodeError:
        print("Failed to decode JSON response.")
        return None


def image_to_base64(image_path):
    try:
        # Ouvrir l'image à partir du chemin spécifié
        with open(image_path, "rb") as image_file:
            # Lire le contenu binaire de l'image
            image_binary = image_file.read()
            # Convertir en base64
            image_base64 = base64.b64encode(image_binary)
            # Convertir en format UTF-8 pour l'affichage
            image_base64_utf8 = image_base64.decode('utf-8')
            return image_base64_utf8
    except IOError:
        print(f"Erreur: Impossible d'ouvrir le fichier {image_path}")
        return None


if __name__ == '__main__':
    url = 'http://localhost:8888'
    path = '/reporting/detection/illegal/activity'
    print('\n\n we use http://localhost:8888 as the base URL for the API. \n')
    parameters = {
        'db': input('Enter your database name: '),
        'login': input('Enter your username: '),
        'password': input('Enter your password: '),
    }
    session_id = connect_to_odoo_api(url, parameters)
    if not session_id:
        print('\n Failed to connect to Odoo API.\n')
        exit(1)

    headers = {
        'Cookie': f"session_id={session_id}",
    }

    data = {
        'observation_category_id': '4',
        'latitude': '15.0',
        'longitude': '30.0',
    }

    files = {
        'multimedia': image_to_base64('WIN_20240520_11_48_35_Pro.png'),
    }

    response = send_data_with_files(url, path, data, files, headers)

    if response:
        print(f"\n Response received: {response} \n")
    else:
        print('No response received.')
