# Automated Email Schedule Requests

## Setup

### 1. Configure Email Settings

Edit `scraper/send_schedule_requests.py`:

```python
FROM_EMAIL = "your-email@gmail.com"  # Your email address
FROM_NAME = "Your Name"
```

### 2. Update Contact List

Add/update institutional contacts in `CONTACTS` dictionary with real email addresses.

### 3. Gmail Setup (if using Gmail)

1. Enable 2-Factor Authentication
2. Generate an App Password:
   - Go to https://myaccount.google.com/apppasswords
   - Create new app password for "Mail"
   - Save this password securely

## Usage

### Send Schedule Requests

```bash
python3 scraper/send_schedule_requests.py
```

The script will:
1. Show you which institutions will be contacted
2. Ask for confirmation
3. Request your email password
4. Send templated emails to all contacts

### Process Responses

When you receive replies:

1. Copy the filled-in text from the email
2. Save it to a file: `response_yale.txt`
3. Parse it:

```python
python3 << 'EOF'
from scraper.send_schedule_requests import parse_email_response

with open('response_yale.txt', 'r') as f:
    email_text = f.read()

events = parse_email_response(email_text)

# Add to manual_events.json
import json
with open('scraper/manual_events.json', 'r+') as f:
    data = json.load(f)
    data['events'].extend(events)
    f.seek(0)
    json.dump(data, f, indent=2)

print(f"✓ Added {len(events)} events")
EOF

# Regenerate site data
python3 -m scraper.main
```

## Email Template

The template (`scraper/email_request_template.txt`) includes:
- Easy fill-in-the-blank format
- 4 lecture slots (expandable)
- All necessary fields (date, time, speaker, title, CME info)
- Professional tone
- Clear instructions

## Automation Schedule

Recommended: Send requests monthly

```bash
# Add to crontab for monthly automation
# First Monday of each month at 9 AM:
0 9 1-7 * * [ "$(date +\%u)" -eq 1 ] && cd /path/to/grandrounds && python3 scraper/send_schedule_requests.py
```

## Contact Management

Current contacts in `CONTACTS`:
- Yale School of Medicine
- Massachusetts General Hospital  
- Brigham and Women's Hospital
- Dartmouth Hitchcock Medical Center
- Rhode Island Hospital / Brown University

Update emails as you find the right contact persons.

## Response Tracking

Create a log to track who responded:

```bash
# Track responses
echo "$(date): Sent requests to all institutions" >> scraper/email_log.txt
echo "$(date): Received response from Yale" >> scraper/email_log.txt
```

## Tips

1. **Be polite and professional** - these are busy medical educators
2. **Send monthly** - not too frequent
3. **Follow up** - if no response in 2 weeks, send gentle reminder
4. **Thank responders** - send thank you email when they reply
5. **Credit institutions** - make sure the website properly credits them
