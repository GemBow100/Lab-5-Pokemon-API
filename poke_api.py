'''
Library for interacting with the PokeAPI.
https://pokeapi.co/
'''
import requests

POKE_API_URL = 'https://pokeapi.co/api/v2/pokemon/'


def main():
    # Test out the get_pokemon_info() function
    # Use breakpoints to view returned dictionary
    pokemon_info = get_pokemon_info("Rockruff")
    print(pokemon_info, end='\n\n')


def get_pokemon_info(poke_name):
    """Gets information about a specified Pokemon from the PokeAPI.

    Args:
        pokemon_name (str): Pokemon name (or Pokedex number)

    Returns:
        dict: Dictionary of Pokemon information, if successful. Otherwise None.
    """
    #Clean the Pokemon name parameter
    poke_name = str(poke_name).strip().lower()

    url = 'https://pokeapi.co/api/v2/pokemon/'
    resp_msg = requests. get(f"{url}{poke_name}")
    print(resp_msg.url)

    #If the GET request was successful, convert the JSON-formatted message body text to a dictionary and return it
    if resp_msg.status_code == requests.codes.ok:
            print(f'Request Succesful!')
            return resp_msg.json()
    #If the GET request failed, print the error reason and return None
    else: 
            print(f'Request failed.')
            print(f'Status code: {resp_msg.status_code} ({resp_msg.reason})')
            return
    
    
        
    
    return None

if __name__ == '__main__':
    main()