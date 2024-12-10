# Git Automation Tool

Git Automation Tool is a Python-based tool designed to simplify the management of Git and GitHub repositories automatically. This tool is highly beneficial for developers who frequently work with Git repositories, as it saves time on manual tasks such as GitHub CLI installation, authentication, repository creation, and commit/push management.

![Git-Automation-Tool Jenderal92](https://github.com/user-attachments/assets/2a37499d-d4d3-4a0e-9cae-2b64e14c878e)


## Features

- **GitHub CLI Installation**  
  - Checks if GitHub CLI (gh) is installed.  
  - Automatically installs GitHub CLI if not available (supports Linux, macOS, Windows, and Termux).  

- **Authentication to GitHub**  
  - Authenticates using a Personal Access Token (PAT) for secure access.  

- **GitHub Repository Creation**  
  - Creates a new GitHub repository with customizable descriptions.  

- **Local Repository Initialization**  
  - Initializes a local directory as a Git repository.  
  - Adds a remote URL to the created GitHub repository.  

- **Automatic Commit and Push**  
  - Adds all files to the staging area.  
  - Creates an initial commit and pushes it to the main branch.  


## How to Use

1. **Install Python**  
   Ensure Python 2.7 is installed. You can download it from the official website: [Python](https://www.python.org).

2. **Install Required Module**  
   Run the command: `pip install requests`.

3. **Add Your GitHub Token**  
   Save your GitHub Personal Access Token (PAT) in a file named `token.txt` in the same directory as the tool.

4. **Run the Tool**  
   Execute the script using the command: `python git_push.py`.

5. **Follow the Instructions**  
   Complete the setup and automation steps via the terminal.

## How to Generate a GitHub Token

1. **Log in to Your GitHub Account**  
   Go to [GitHub](https://github.com/) and log in.

2. **Access Developer Settings**  
   - Click your profile icon in the top-right corner.  
   - Select **Settings** > **Developer settings** > **Personal access tokens > Tokens (classic)**.

3. **Generate a New Token**  
   - Click **Generate new token > Generate new token (classic)**.  
   - Provide a description for your token, e.g., "Git Automation Tool".  
   - Choose the token duration (e.g., 30 or 60 days).

4. **Select Permissions**  
   - Enable the following permissions:  
     - **repo**: Access to private and public repositories.  
     - **workflow**: Access GitHub Actions (if needed).  
     - **delete_repo** (optional): Allow repository deletion.  
   - Click **Generate token**.

5. **Save the Token**  
   - Copy the generated token immediately, as it won’t be shown again.  
   - Save it in the `token.txt` file.
