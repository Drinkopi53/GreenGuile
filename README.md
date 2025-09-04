# GreenGuile

GreenGuile is a Python lightweight solution that runs on microcontrollers to acoustically deter agricultural pests using learned predator sound patterns from local bird datasets, replacing chemical pesticides.

## Features
- Acoustic pest deterrent using predator sounds
- SMS flashing capability for remote updates
- Seasonal pattern adjustment
- Lightweight implementation for microcontrollers
- Configurable sound intervals and volume
- Time-based activation schedules

## Components
1. **Sound Generation Module** - Plays predator sound patterns to deter pests
2. **SMS Communication Module** - Handles remote commands via SMS
3. **Pattern Management System** - Manages seasonal sound patterns
4. **Configuration System** - Handles system settings and preferences

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/GreenGuile.git
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Configure the system by editing `config.json`

## Usage

Run the main application:
```
python main.py
```

### SMS Commands

- `ACTIVATE` - Turn on the pest deterrent system
- `DEACTIVATE` - Turn off the pest deterrent system
- `SEASON <season>` - Change seasonal sound patterns (spring/summer/autumn/winter)
- `STATUS` - Get system status information

### Configuration

The system can be configured through `config.json`:
- `sound_interval`: Time between sound patterns (in seconds)
- `volume`: Audio output volume (percentage)
- `active_hours`: Time range when the system is active
- `season`: Current season for sound pattern selection
- `phone_number`: Authorized phone number for SMS commands

## Hardware Requirements

- Microcontroller with Python support (e.g., Raspberry Pi)
- Audio output device (speaker)
- GSM module for SMS communication (optional in simulation)