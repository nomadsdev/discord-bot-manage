# Discord Bot Management 
 
## Overview 
This project is a Discord bot designed to manage server operations such as clearing channels, sending mass messages, and kicking members. It uses the `discord.py` library to interact with the Discord API and is built to automate various administrative tasks in a Discord server. 
 
## Features 
- **Clear Server:** Deletes all channels and kicks all members (except the bot itself). 
- **Mass Messaging:** Sends bulk messages to multiple channels. 
- **Server Management:** Provides commands to manage the server in bulk, such as creating channels and sending messages. 
 
## Installation 
1. **Clone the repository:** 
 
   ```bash 
   git clone https://github.com/nomadsdev/discord-bot-manage.git 
   cd discord-bot-manage 
   ``` 

3. **Install the required packages:** 
 
   ```bash 
   pip install discord.py 
   ``` 
 
4. **Configure the bot:** 
 
   - Open the `discord.py` file. 
   - Replace `'YOUR_BOT_TOKEN_HERE'` with your actual Discord bot token. 
 
## Usage 
1. **Run the bot:** 
 
   ```bash 
   python discord.py 
   ``` 
 
2. **Available Commands:** 
 
   - `!pro`: Clears the server, creates 12 channels, and sends 5 messages to each channel. 
   - `!pros`: Creates 20 channels and sends 10 messages to each channel. 
   - `!pross`: Creates 20 channels and sends 10 messages to each channel, then calls `!proleak`. 
   - `!pross`: Creates 40 channels and sends 10 messages to each channel. 
   - `!mess`: Sends "@everyone" message 40 times to the channel where the command is invoked. 
   - `!kickall`: Kicks all members from the server except the bot. 
 
## Contact 
For support or inquiries, please contact us at [support@jmmentertainenmt.com](mailto:support@jmmentertainenmt.com). 
 
## License 
This project is licensed under the MIT License
