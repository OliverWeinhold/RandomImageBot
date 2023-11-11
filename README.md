# DemoImageBot

DemoImageBot is a Telegram bot that sends random images from a specified directory and provides basic information about the bot when specific commands are used.

## Features

- Sends random images from the 'Images' directory to users.
- Provides information about the bot using specific commands.

## Prerequisites

Before you get started, make sure you have the following:

- Python 3.x installed
- Telegram bot token (replace 'YOUR_TELEGRAM_BOT_TOKEN' in the code with your actual token)

### How to get telegram bot token
If you dont have a Telegram bot token yet, you must first create the bot in Telegram using [Botfather](https://t.me/botfather):
1. Open the Telegram client and search for the user "BotFather"
2. Send the BotFather the command "/newbot" to create a new bot
3. After you have followed the BotFather's instructions, you will receive an API token. This token is the key with which you can control your bot programmatically.

## Installation

1. Clone the repository to your local machine or server:

```sh
git clone https://github.com/OliverWeinhold/DemoImageBot.git
```

2. Navigate to the project directory:

```sh
cd DemoImageBot
```

3. Install the required Python packages using pip:

```sh
pip install python-telegram-bot
```

4. Replace 'YOUR_TELEGRAM_BOT_TOKEN' with your actual Telegram bot token in the code.

## Usage

To run the bot, execute the following command within the project directory:

```sh
python main.py
```

The bot will start running, and you can interact with it on your Telegram.

## Commands

- `/start`: The bot will send a random image from the 'Images' directory.
- `/about`: The bot will provide information about itself.

You can customize the bot's behavior by modifying the code.

Detailed documentation (in German only) can be found at [oliverweinhold.de](https://oliverweinhold.de/blog/eigenen-telegram-bot-mit-python-programmieren/).

## License

This project is licensed under the [GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.html).

## Author

- [Oliver Weinhold](https://oliverweinhold.de/)

## Support

Please note that the maintenance of this code is not continuous and not guaranteed. For support, feature requests, or bug reporting, please use GitHub.


## Contributions

Contributions are welcome! Feel free to open a pull request or issue on GitHub!