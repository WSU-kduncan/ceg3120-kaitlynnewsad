# Project 1

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
  - Changed made to code

    Change the code so it could output different quotes then the ones provide. 
    
    The program can output two quotes.
    
  - Commands I can type into Discord 

    Right Now the code works when the user enters this:
    
    Hello! How are you.
    
    The user can input his quote if the office_quote is used:
    
    What bear is best?  (Office Tv show)
  
  - Response by Bot 
  - 
    The program will output this sentence:
    
    Hi, I'm great. How are you.
    
    If the program is using office_quotes then the program will output this:
    
    Thats a ridculous question. Its debatable. There are basically two schools of thought--  (Office Tv show)
   
 - Research
  
   - How could you have the program always running.
   
      One solution is hosting the program on a server. This would work because the server will wait for the computer/user to respond and will provide a response.
      The server will never shutdown unless a problem and the server needs to be fixed or the user needs to make chnages to the program the user is using. 
      
   - Proof of Bot and Output 
   
   ![Proof of Bot and Output](https://user-images.githubusercontent.com/56359938/150377598-418895f0-5a47-4e14-b008-4ce568b57cf3.png)
   
   - Proof of Branch and Marge
   
   ![Proof of git branch](https://user-images.githubusercontent.com/56359938/150378841-da04d788-2964-4a19-a2aa-ef76f7fa4948.png)


