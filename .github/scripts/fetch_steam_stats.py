import requests
import os

# Fetch Steam API key and Steam ID from environment variables
api_key = os.getenv('STEAM_WEB_API_KEY')
steam_id = os.getenv('STEAM_ID')

# Function to fetch Steam Workshop stats
def fetch_workshop_stats(api_key, steam_id):
    # Make a request to the Steam Workshop API endpoint
    response = requests.get(f'https://api.steampowered.com/ISteamRemoteStorage/GetPublishedFileDetails/v1/?key={api_key}&steamid={steam_id}')
    data = response.json()

    # Extract workshop stats (total likes, subscribers, views, etc.)
    # Process the data as needed
    workshop_stats = data.get('response', {}).get('publishedfiledetails', [])

    # Example: Calculating total likes, subscribers, and views
    total_likes = sum(item.get('consumer_app_usage', 0) for item in workshop_stats)
    total_subscribers = sum(item.get('subscriptions', 0) for item in workshop_stats)
    total_views = sum(item.get('views', 0) for item in workshop_stats)

    return total_likes, total_subscribers, total_views

# Function to fetch Steam achievements
def fetch_achievements(api_key, steam_id):
    # Make a request to the Steam User Stats API endpoint
    response = requests.get(f'https://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v1/?key={api_key}&steamid={steam_id}')
    data = response.json()

    # Extract and process achievements data
    achievements = data.get('playerstats', {}).get('achievements', [])

    # Example: Counting total achievements unlocked
    total_achievements = len(achievements)

    return total_achievements

# Function to fetch games owned
def fetch_games_owned(api_key, steam_id):
    # Make a request to the Steam Player Service API endpoint
    response = requests.get(f'https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/?key={api_key}&steamid={steam_id}&include_played_free_games=1')
    data = response.json()

    # Extract and process games owned data
    games_owned = data.get('response', {}).get('games', [])

    return games_owned

# Function to fetch Steam Year In Review data
def fetch_year_in_review(api_key, steam_id):
    # Make a request to the appropriate Steam API endpoint for Year In Review data
    # Add your implementation here if available

    # Year In Review data
    year_in_review_data = {}

    return year_in_review_data

# Function to update README.md with fetched data
def update_readme(workshop_stats, total_achievements, games_owned, year_in_review_data):
    # Example: Update README.md with fetched data
    with open('README.md', 'w') as f:
        f.write(f"# Steam Stats\n\n")
        f.write(f"## Workshop Stats\n")
        f.write(f"Total Likes: {workshop_stats[0]}\n")
        f.write(f"Total Subscribers: {workshop_stats[1]}\n")
        f.write(f"Total Views: {workshop_stats[2]}\n\n")
        f.write(f"## Achievements\n")
        f.write(f"Total Achievements: {total_achievements}\n\n")
        f.write(f"## Games Owned\n")
        for game in games_owned:
            f.write(f"- {game['name']}\n")
        f.write(f"\n")

        f.write(f"## Year In Review\n")
        # Add Year In Review data here if available

if __name__ == "__main__":
    # Fetch Steam API key and Steam ID from environment variables
    api_key = os.getenv('STEAM_API_KEY')
    steam_id = os.getenv('STEAM_ID')

    if api_key and steam_id:
        # Fetch data from Steam API
        workshop_stats = fetch_workshop_stats(api_key, steam_id)
        total_achievements = fetch_achievements(api_key, steam_id)
        games_owned = fetch_games_owned(api_key, steam_id)
        year_in_review_data = fetch_year_in_review(api_key, steam_id)

        # Update README.md with fetched data
        update_readme(workshop_stats, total_achievements, games_owned, year_in_review_data)

        print("Steam stats updated successfully.")
    else:
        print("Steam API key or Steam ID is missing.")
