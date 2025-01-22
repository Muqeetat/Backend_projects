import argparse
import requests
from collections import defaultdict

def fetch_github_activity(username):
    """
    Fetch and display the recent activity of a specified GitHub user, grouping and summarizing similar events.
    """
    # GitHub API URL for fetching user events
    url = f"https://api.github.com/users/{username}/events"
    
    # Headers to specify API version and content type
    headers = {
        "Accept": "application/vnd.github.v3+json",  # Specify the version of the API
    }
    
    try:
        # Fetch data from GitHub API with a timeout of 10 seconds
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 200:
            # Parse the JSON response into Python objects (list of events)
            events = response.json()
            if events:
                # Dictionary to group events by repository and type
                # Example: {"repo_name": {"Pushed commits": 5, "Starred": 2}}
                activity_summary = defaultdict(lambda: defaultdict(int))
                
                for event in events[:50]:  # Limit to the 50 most recent events
                    repo_name = event["repo"]["name"]  # Get the repository name
                    
                    if event["type"] == "PushEvent":
                        # Count the number of commits in the push event
                        # calculates the number of commits in that list by using the len() function
                        commit_count = len(event["payload"]["commits"])
                        activity_summary[repo_name]["Pushed commits"] += commit_count
                    elif event["type"] == "IssuesEvent":
                        # Count issue-related events and capture the action performed
                        action = event["payload"]["action"].capitalize()
                        activity_summary[repo_name][f"{action} issues"] += 1
                    elif event["type"] == "WatchEvent":
                        # Count starred events
                        activity_summary[repo_name]["Starred"] += 1
                    elif event["type"] == "ForkEvent":
                        # Count fork events
                        activity_summary[repo_name]["Forked"] += 1
                    elif event["type"] == "PullRequestEvent":
                        # Count pull request events and capture the action performed
                        action = event["payload"]["action"].capitalize()
                        activity_summary[repo_name][f"{action} pull requests"] += 1
                    elif event["type"] == "CreateEvent":
                        # Count create events
                        activity_summary[repo_name]["CreateEvent"] += 1
                
                # Display the summarized activity
                print("Recent activity summary:")
                for repo, actions in activity_summary.items():
                    for action, count in actions.items():
                        # Print each action with its count and repository name
                        print(f"- {count} {action} in {repo}")
            else:
                # If no events are found, notify the user
                print(f"No recent activity found for user '{username}'.")
        elif response.status_code == 404:
            # Handle user not found error
            print(f"Error: User '{username}' not found on GitHub.")
        elif response.status_code == 403:
            # Handle rate limit error
            print("Error: Rate limit exceeded. Please try again later.")
        else:
            # Handle other HTTP errors
            print(f"Error: Failed to fetch data. HTTP Status Code: {response.status_code}")
            print(f"Message: {response.json().get('message', 'No error message provided.')}")
    except requests.exceptions.RequestException as e:
        # Handle network-related errors, such as connection issues
        print(f"Error: Unable to connect to the GitHub API. Details: {e}")

def main():
    """
    Main function to handle command-line arguments and fetch activity.
    """
    # Set up argument parser to accept a GitHub username as input
    parser = argparse.ArgumentParser(description="Fetch recent GitHub activity for a user.")
    
    # Add a positional argument for the GitHub username
    parser.add_argument(
        "username",  # Argument name
        type=str,  # Data type
        help="The GitHub username whose recent activity you want to fetch."  # Help description
    )
    
    # Parse command-line arguments into a Namespace object
    args = parser.parse_args()
    
    # Fetch and display activity for the provided username
    fetch_github_activity(args.username)

if __name__ == "__main__":
    main()  # Entry point for the script
