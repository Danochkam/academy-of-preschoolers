# 🎓 Academy of Preschoolers

**Educational Telegram Bot | Python · aiogram**

Academy of Preschoolers is a Telegram bot I developed independently to help Russian-speaking parents in Kazakhstan explore an early-learning program for children aged 4–6. The program offers **135 educational video lessons** covering early reading, logical thinking, attention, safety, hygiene, and school readiness.

**My role:** Independent Developer  
**Technologies:** Python, aiogram, Telegram Bot API

## Features

- `/start` command introduces the program and its learning objectives.
- Inline buttons guide users to a sample lesson and subscription pricing.
- A sample lesson video can be sent directly through Telegram (when provided locally).
- Parents can access subscription details and a manager contact link.
- The interface is in Russian to serve the intended audience.

## How it works

The application uses an **aiogram dispatcher** with message and callback-query handlers. A `/start` message displays the main menu. Selecting an inline button triggers the corresponding handler, which sends a response or a sample video.

## Screenshots

The screenshots retain the original Russian-language interface.

### Welcome screen
![Bot welcome screen](welcome-screen.jpg)

### Program overview
![Program description](program-overview.jpg)

### Interactive menu
![Bot interactive menu](interactive-menu.jpg)

### Pricing and support
![Subscription prices and contact](pricing-and-support.jpg)

## Run locally

1. Install **Python 3.10+** and download this repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Copy `.env.example` to `.env` and place your **new, private** BotFather token in `TELEGRAM_BOT_TOKEN`.
4. Optionally configure `MANAGER_WHATSAPP_URL` and `PAYMENT_INSTRUCTIONS` in `.env` with the relevant person's permission.
5. If you own or have permission to share a demo lesson, save it as `video.mp4` in the project folder. Otherwise, the bot displays a fallback message.
6. Start the application:
   ```bash
   python bot.py
   ```

**Security and privacy:** The Telegram token, private contacts, payment information, and copyrighted lesson videos are deliberately excluded from the public repository. The `.env` file is ignored by Git.

## Project background

I built this bot as an independent programming project, applying Python and aiogram to an educational use case. I implemented its navigation, message handlers, and sample-lesson functionality, and debugged the bot during development.
