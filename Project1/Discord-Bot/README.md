#Project 1

- Setup 
  - How did you get API token ?
     I got the API token by creating a bot that for the application I created in Discord. After, I created my sever I addded the bot to the server. Then I went to the bot section   of my apllication and found the token section. I then copied the token. 
    
  - Where did you put the API token ?
    I put the API token in a file called .env. I had to use the code provided in the Discord Bot guide to get it to work.
    Example: 
   `# .env
    DISCORD_TOKEN={your-bot-token}
    DISCORD_GUILD={your-guild-name}`
    Note: Had to use `git rm --cached filename` before putting .env on Github. If not the token would be killed by Discord.
    
  - What packages needed to be installed to run the code?
    -  `pip3 install -U discord.py`
    -  `pip3 install -U python-dotenv`
    -  Also had to install both python3 and pip3. Could not use regular python kept getting syntax error when I tried running the code.

- Usage 
  - Commands I can type into Discord 
  Hello! How are you.
  What bear is best? (Office Tv show)
  
  - Response by Bot 
 Hi, I'm great. How are you.

