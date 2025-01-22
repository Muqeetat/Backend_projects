
# Github User Activity

Sample solution for the [Github User Activity](https://roadmap.sh/projects/github-user-activity) challenge from [roadmap.sh](https://roadmap.sh/).

## Features

- Fetches recent GitHub events (up to 50 most recent).
- Summarizes activities such as:
  - Push events (commits)
  - Issue events (opened, closed)
  - Watch events (stars)
  - Fork events
  - Pull request events (opened, closed)
  - Create events (new repositories)
- Handles errors such as user not found, rate limit exceeded, and network issues.

## Requirements

- Python 3.x
- `requests` library (can be installed using `pip install requests`)

## Usage

### Command-Line Usage

To run the script, open a terminal or command prompt and use the following command:

```bash
python main.py <github-username>
```

Replace `<github-username>` with the GitHub username whose activity you want to fetch.

### Example

```bash
python main.py sam123
```

This will fetch the recent activity of the GitHub user `sam123`.

### Output Example

```bash
Recent activity summary:
- 5 Pushed commits in octocat/Hello-World
- 2 Starred in octocat/awesome-project
- 1 Forked in octocat/another-repo
- 3 Opened pull requests in octocat/sample-repo
```

## Error Handling

- **User Not Found**: If the specified GitHub user does not exist, the script will notify the user.
- **Rate Limit Exceeded**: If the GitHub API rate limit is exceeded, the script will inform the user and suggest waiting before trying again.
- **Network Errors**: If there are issues connecting to GitHub's API, the script will print the error details.
