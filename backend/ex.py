#!/usr/bin/python3
import requests
import sys
import codecs

# needed to display output on the web server
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())
#  pokemonEntry is a number


def dexEntry(pokemonEntry):
    url = 'https://pokeapi.co/api/v2/pokemon-species/' + \
        str(pokemonEntry) + '/'  # url that can be changed
    response = requests.get(url)  # easier to read
    convertToPython = response.json()  # converts website to a format we can use
    rightLanguage = 0
    for index in range(len(convertToPython['flavor_text_entries'])):
        if 'en' in convertToPython['flavor_text_entries'][index]['language']['name']:
            rightLanguage = index  # gets the english version
            break
    # get the dex entry
    dexEntry = convertToPython['flavor_text_entries'][rightLanguage]['flavor_text']
    return dexEntry


def pokemonName(pokemonEntry):
    url = 'https://pokeapi.co/api/v2/pokemon/' + \
        str(pokemonEntry) + '/'
    response = requests.get(url)
    convertToPython = response.json()
    dexEntry = convertToPython['forms'][0]['name']
    return dexEntry.title()


def abilities(pokemonEntry):
    url = 'https://pokeapi.co/api/v2/pokemon/' + \
        str(pokemonEntry) + '/'
    response = requests.get(url)
    convertToPython = response.json()
    abilities = convertToPython['abilities']
    ListOfAbilities = []
    for ability in range(len(abilities)):
        ListOfAbilities.append(
            abilities[ability]['ability']['name'].title().replace('-', ' '))
    return ListOfAbilities



def pokemonInfo(pokemonEntry):
    return str(pokemonEntry), pokemonName(pokemonEntry)
