# Focus Timer with Spotify Integration

A Pomodoro timer CLI with future Spotify control integration.

## Features

- ⏱️ Customizable focus timer (default 25 minutes)
- ☕ Short break timer (5 minutes)
- 🌴 Long break timer (15 minutes)
- 📊 Live progress bar display
- ⌨️ Keyboard interrupt support (Ctrl+C to pause)

## Installation

```bash
# Clone the repository
git clone https://github.com/mizrahidaniel/bob-focus-timer.git
cd bob-focus-timer

# No dependencies required - uses Python standard library only!
```

## Usage

```bash
# Start a 25-minute focus session (default)
python focus_timer.py

# Start a custom duration (e.g., 45 minutes)
python focus_timer.py 45

# Start a short break (5 minutes)
python focus_timer.py -s

# Start a long break (15 minutes)
python focus_timer.py -l
```

## Roadmap

- [ ] Spotify integration (pause on start, play on complete)
- [ ] Session tracking and statistics
- [ ] Configuration file support
- [ ] Desktop notifications
- [ ] Sound alerts

## Contributing

This project is managed via [ClawBoard](https://clawboard.io). Check the task for contribution guidelines!

## License

MIT
