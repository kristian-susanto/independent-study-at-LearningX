import requests

root_url = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json'
word = 'potato'
api_key = 'ed5728e8-d4ee-4cd7-a14b-b148bb491735'
final_url = f'{root_url}/{word}?key={api_key}'

# Make the request and assign it to 'res'
res = requests.get(final_url)

# Get the definitions as JSON
definitions = res.json()

# Print each definition
for definition in definitions:
    print(definition)
