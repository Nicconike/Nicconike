# Import necessary modules
import requests
import os

def fetch_steam_stats(api_key, steam_id):
    response = requests.get(f'https://api.steampowered.com/ISteamUserStats/GetPlayerSummaries/v2/?key={api_key}&steamids={steam_id}')
    data = response.json()
    if 'players' in data['response']:
        username = data['response']['players'][0].get('personaname', 'Unknown')
        state = data['response']['players'][0].get('personastate', 'Unknown')
        return username, state
    else:
        return None, None

def update_readme(username, state):
    # Read the content of README.md file
    with open('README.md', 'r') as file:
        readme_content = file.read()

    # Find the start and end positions of the placeholder
    start_placeholder = "<!-- STEAM_STATS_START -->"
    end_placeholder = "<!-- STEAM_STATS_END -->"
    start_index = readme_content.find(start_placeholder)
    end_index = readme_content.find(end_placeholder)

    # Replace the placeholder with the fetched Steam stats
    if start_index != -1 and end_index != -1:
        updated_content = readme_content[:start_index + len(start_placeholder)] + f"\n\nUsername: {username}\nState: {state}\n\n" + readme_content[end_index:]

        # Write the updated content back to README.md file
        with open('README.md', 'w') as file:
            file.write(updated_content)
        print("Steam stats updated successfully.")
    else:
        print("Failed to find placeholder in README.md file.")

if __name__ == "__main__":
    api_key = os.getenv('STEAM_API_KEY')
    steam_id = os.getenv('STEAM_ID')
    if api_key and steam_id:
        username, state = fetch_steam_stats(api_key, steam_id)
        if username and state:
            update_readme(username, state)
        else:
            print("Failed to fetch Steam stats.")
    else:
        print("Steam API key or Steam ID is missing.")
