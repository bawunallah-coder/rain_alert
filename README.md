# Rain Alert System

An automated rain alert system that checks weather forecasts and sends email notifications to recipients when rain is expected. Perfect for reminding friends and family to bring umbrellas!

# Features

- **Automated Weather Monitoring**: Checks weather forecast every 3 hours via GitHub Actions
- **Email Notifications**: Sends alerts to multiple recipients when rain is predicted
- **OpenWeatherMap Integration**: Uses real-time weather API for accurate forecasts
- **Environment Variables**: Secure handling of sensitive data (API keys, email credentials)
- **Flexible Location**: Easily change forecast location via environment variables
- **CSV-Based Distribution List**: Simple email list management

## Prerequisites

- GitHub account with repository access
- [OpenWeatherMap API Key](https://openweathermap.org/api) (free tier available)
- Gmail account with [App Password enabled](https://support.google.com/accounts/answer/185833)
- Python 3.7+ (for local testing)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/bawunallah-coder/rain_alert.git
cd rain_alert
```

### 2. Set Up Environment Variables

Create a `.env` file in the root directory:

```bash
cp .env.example .env
```

Edit `.env` with your configuration:

```env
EMAIL=your_email@gmail.com
PASSWORD=your_app_password
WEATHER_API_KEY=your_openweathermap_api_key
LATITUDE=12.268583
LONGITUDE=6.554311
```

### 3. Configure Email Recipients

Edit `emails.csv` to add your recipients:

```csv
email,name
recipient1@example.com,John Doe
recipient2@example.com,Jane Smith
```

### 4. GitHub Secrets Setup (for GitHub Actions)

Add these secrets to your GitHub repository:

1. Go to **Settings** → **Secrets and variables** → **Actions**
2. Add the following secrets:
   - `EMAIL`: Your Gmail address
   - `PASSWORD`: Your Gmail app password
   - `WEATHER_API_KEY`: Your OpenWeatherMap API key

Optionally add:
   - `LATITUDE`: Location latitude (default: 12.268583)
   - `LONGITUDE`: Location longitude (default: 6.554311)

### 5. Local Testing (Optional)

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the script locally:

```bash
python main.py
```

##  How It Works

1. **Scheduled Trigger**: GitHub Actions runs the workflow every 3 hours (configurable via `rain_alert.yml`)
2. **Weather Check**: Fetches 12-hour forecast using OpenWeatherMap API
3. **Rain Detection**: Checks if weather ID < 700 (indicates rain/snow/thunderstorm)
4. **Email Send**: If rain detected, sends alert email to all recipients in `emails.csv`
5. **Logging**: Prints confirmation for each email sent

## File Structure

```
rain_alert/
├── main.py                 # Main script logic
├── emails.csv              # Email recipients list
├── rain_alert.yml          # GitHub Actions workflow
├── requirements.txt        # Python dependencies
├── .env.example            # Environment variables template
├── .gitignore              # Git ignore rules
└── README.md               # This file
```

## Security Best Practices

- ✅ Uses environment variables for sensitive data
- ✅ Gmail app passwords (not account password)
- ✅ `.env` file excluded from version control
- ✅ API keys stored as GitHub Secrets
- ✅ No hardcoded credentials in code

##  Configuration

### Change Forecast Interval

Edit `rain_alert.yml` line 5:

```yaml
- cron: "0 */3 * * *"   # Change to desired interval (default: every 3 hours)
```

Common cron expressions:
- `"0 * * * *"` - Every hour
- `"0 */6 * * *"` - Every 6 hours
- `"0 9 * * *"` - Daily at 9 AM UTC

### Change Location

Option 1: Add environment variables in GitHub Secrets
Option 2: Edit `.env` file with new coordinates

Find coordinates at [Google Maps](https://maps.google.com) or [GeoNames](https://www.geonames.org/)

## 📚 API Reference

### OpenWeatherMap Weather Codes

- **< 200**: Thunderstorm
- **200-299**: Thunderstorm with rain/snow
- **300-399**: Drizzle
- **400-499**: Rain
- **500-599**: Snow
- **600-699**: Rain/Snow mix
- **700-799**: Mist/Fog (No alert)
- **800**: Clear
- **801-809**: Clouds

## Troubleshooting

| Issue | Solution |
|-------|----------|
| "Email sent to..." not showing | Check GitHub Actions logs in your repository |
| Gmail login failed | Ensure app password is correct (not regular password) |
| API key error | Verify OpenWeatherMap API key is active |
| No emails sent despite rain | Check if weather ID < 700 for your location |

## License

This project is open source and available.

## Contributing

Feel free to fork, modify, and submit pull requests!

## Author

[bawunallah-coder](https://github.com/bawunallah-coder)
bawunallah@gmail.com
09134883826
Yusuf Bello Shiitu

## Contact

For questions or issues, please open a GitHub issue or contact the author.

---

**Last Updated**: June 2026
