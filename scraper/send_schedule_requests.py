#!/usr/bin/env python3
"""
Automated email sender for grand rounds schedule requests.
Sends templated emails to institutional contacts requesting upcoming lectures.
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import json

# Contact list for each institution
CONTACTS = {
    "Yale School of Medicine": {
        "name": "Grand Rounds Coordinator",
        "email": "grandrounds@yale.edu",  # UPDATE WITH REAL EMAIL
        "department": "Internal Medicine"
    },
    "Massachusetts General Hospital": {
        "name": "Medical Education Office",
        "email": "mghcme@mgh.harvard.edu",
        "department": "Medicine"
    },
    "Brigham and Women's Hospital": {
        "name": "CME Office",
        "email": "PartnersCPD@partners.org",
        "department": "Medicine"
    },
    "Dartmouth Hitchcock Medical Center": {
        "name": "CME Office",
        "email": "continuing.education@hitchcock.org",
        "department": "Medicine"
    },
    "Rhode Island Hospital / Brown University": {
        "name": "Residency Program",
        "email": "imrp_rih@brown.edu",
        "department": "Internal Medicine"
    }
}

# Email configuration
SMTP_SERVER = "smtp.gmail.com"  # Change if using different provider
SMTP_PORT = 587
FROM_EMAIL = "your-email@gmail.com"  # UPDATE THIS
FROM_NAME = "New England Medical Grand Rounds"

def load_template():
    """Load the email template"""
    with open('scraper/email_request_template.txt', 'r') as f:
        return f.read()

def send_request_email(institution, contact_info, smtp_password):
    """
    Send a schedule request email to an institution
    
    Args:
        institution: Name of the institution
        contact_info: Dict with name and email
        smtp_password: SMTP password for authentication
    """
    try:
        # Load and customize template
        template = load_template()
        body = template.replace('[CONTACT_NAME]', contact_info['name'])
        body = body.replace('[YOUR_NAME]', FROM_NAME)
        
        # Create message
        msg = MIMEMultipart()
        msg['From'] = f"{FROM_NAME} <{FROM_EMAIL}>"
        msg['To'] = contact_info['email']
        msg['Subject'] = f"Grand Rounds Schedule Request - {institution}"
        
        msg.attach(MIMEText(body, 'plain'))
        
        # Send email
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(FROM_EMAIL, smtp_password)
        
        server.send_message(msg)
        server.quit()
        
        print(f"✓ Email sent to {institution} ({contact_info['email']})")
        return True
        
    except Exception as e:
        print(f"✗ Failed to send to {institution}: {e}")
        return False

def send_all_requests(smtp_password):
    """Send requests to all institutions"""
    print("Sending schedule requests to all institutions...")
    print("=" * 60)
    
    results = {
        'sent': [],
        'failed': []
    }
    
    for institution, contact in CONTACTS.items():
        success = send_request_email(institution, contact, smtp_password)
        if success:
            results['sent'].append(institution)
        else:
            results['failed'].append(institution)
    
    print("\n" + "=" * 60)
    print(f"Summary: {len(results['sent'])} sent, {len(results['failed'])} failed")
    
    return results

def parse_email_response(email_text):
    """
    Parse a filled-in email response and convert to JSON
    
    Args:
        email_text: The replied email text with filled information
        
    Returns:
        List of event dictionaries
    """
    events = []
    lines = email_text.split('\n')
    
    current_event = {}
    for line in lines:
        line = line.strip()
        if line.startswith('Date:'):
            if current_event:
                events.append(current_event)
            current_event = {'date': line.split(':', 1)[1].strip()}
        elif line.startswith('Time:'):
            current_event['time'] = line.split(':', 1)[1].strip()
        elif line.startswith('Title:'):
            current_event['title'] = line.split(':', 1)[1].strip()
        elif line.startswith('Speaker:'):
            current_event['speaker'] = line.split(':', 1)[1].strip()
        elif line.startswith('Department:'):
            current_event['department'] = line.split(':', 1)[1].strip()
        elif line.startswith('CME Available:'):
            current_event['cme_available'] = 'yes' in line.lower()
        elif line.startswith('Registration'):
            current_event['source_link'] = line.split(':', 1)[1].strip()
    
    if current_event:
        events.append(current_event)
    
    return events

if __name__ == '__main__':
    import getpass
    
    print("=" * 60)
    print("Grand Rounds Schedule Request Email Sender")
    print("=" * 60)
    print("\nThis will send emails to all institutions requesting schedules.")
    print(f"From: {FROM_EMAIL}")
    print("\nInstitutions to contact:")
    for inst in CONTACTS.keys():
        print(f"  - {inst}")
    
    print("\n" + "=" * 60)
    confirm = input("Send emails? (yes/no): ")
    
    if confirm.lower() == 'yes':
        password = getpass.getpass(f"Enter SMTP password for {FROM_EMAIL}: ")
        send_all_requests(password)
    else:
        print("Cancelled.")
