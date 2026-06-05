# WhatsApp Appointment Reminders App

A minimal, professional Django app to schedule appointments and send WhatsApp reminders via Twilio Sandbox.

## Features
- **Single Page Interface**: Simple form to book appointments.
- **Live Dashboard**: Table showing all scheduled appointments and their notification status.
- **Immediate Confirmation**: Sends a WhatsApp message as soon as an appointment is booked.
- **Automated Reminders**: Management command to send reminders for appointments occurring within the next hour.
- **Neon PostgreSQL Ready**: Configured to use Neon via `DATABASE_URL`.

## Tech Stack
- Django
- PostgreSQL (via Neon)
- Twilio (WhatsApp Sandbox)
- Plain HTML/CSS

## Setup Instructions

1. **Clone & Install Dependencies**
   ```bash
   # Create a virtual environment
   python -m venv venv
   # Activate it (Windows)
   .\venv\Scripts\activate
   # Install requirements
   pip install -r requirements.txt
   ```

2. **Configure Environment Variables**
   Rename `.env.template` to `.env` (or update the existing `.env`) and fill in your details:
   - `DATABASE_URL`: Your Neon PostgreSQL connection string.
   - `TWILIO_ACCOUNT_SID`: From Twilio Console.
   - `TWILIO_AUTH_TOKEN`: From Twilio Console.
   - `TWILIO_WHATSAPP_FROM`: Your Twilio Sandbox WhatsApp number (e.g., `whatsapp:+14155238886`).
   - `TWILIO_CONTENT_SID`: Optional, for Twilio templates if used.

3. **Database Migrations**
   ```bash
   python manage.py migrate
   ```

4. **Run the App**
   ```bash
   python manage.py runserver
   ```
   Visit `http://127.0.0.1:8000` in your browser.

## Sending Automated Reminders
To send reminders for appointments in the next hour, run the following command periodically (e.g., every 15-30 minutes via Cron):
```bash
python manage.py send_reminders
```

## Production Notes
- Set `DEBUG=False` in `.env`.
- Ensure `ALLOWED_HOSTS` includes your production domain.
- Use a real Twilio WhatsApp Sender (not sandbox) for production use cases.
