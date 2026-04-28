import smtplib
import csv
import os
from email.message import EmailMessage


EMAIL_ADDRESS = "abc@gmail.com"
EMAIL_PASSWORD = "abcdefghijklmnop"
CERTIFICATE_FOLDER = "certificates"
CSV_FILE = "participants.csv"

LOGO_URL = "https://raw.githubusercontent.com/swayking007/codechef-wce-assets/main/Logo.png"

def send_certificate(name, receiver_email, certificate_file):
    name = name.strip()
    receiver_email = receiver_email.strip()
    certificate_file = certificate_file.strip()

    # Skip invalid rows
    if not receiver_email or not certificate_file:
        print(f"⚠️ Skipping invalid row for '{name}'")
        return
    
    msg = EmailMessage()
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = receiver_email
    msg["Subject"] = "🎉 Certificate of Participation – CookBook 3.0"

    msg.set_content("Please view this email in HTML format.")

    msg.add_alternative(f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <style>
            body {{
                background-color: #f4f6f8;
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
            }}
            .container {{
                max-width: 600px;
                margin: auto;
                background-color: #ffffff;
                border-radius: 12px;
                overflow: hidden;
                box-shadow: 0 6px 15px rgba(0,0,0,0.1);
            }}
            .header {{
                background: linear-gradient(90deg, #5a00ff, #ff8c00);
                padding: 25px;
                text-align: center;
                color: white;
            }}
            .header img {{
                max-width: 90px;
                margin-bottom: 10px;
            }}
            .header h1 {{
                margin: 5px 0 0;
                font-size: 26px;
            }}
            .content {{
                padding: 35px;
                text-align: center;
                color: #333;
            }}
            .content h2 {{
                color: #5a00ff;
            }}
            .content p {{
                font-size: 16px;
                line-height: 1.7;
                margin-bottom: 15px;
            }}
            .cert-icon {{
                font-size: 42px;
                margin: 20px 0;
            }}
            .btn {{
                display: inline-block;
                margin: 12px 6px;
                padding: 13px 24px;
                text-decoration: none;
                color: #ffffff !important;
                border-radius: 26px;
                font-size: 15px;
                font-weight: bold;
                border: 2px solid rgba(0,0,0,0.15);
                box-shadow: 0 4px 8px rgba(0,0,0,0.18);
            }}

            .btn-site {{
                background-color: #4b00d6;
            }}
            .btn-whatsapp {{
                background-color: #25D366;
            }}
            .footer {{
                background-color: #f0f0f0;
                padding: 18px;
                text-align: center;
                font-size: 14px;
                color: #555;
            }}
        </style>
    </head>

    <body>
        <div class="container">

            <div class="header">
                <img src="{LOGO_URL}" alt="CodeChef WCE Chapter Logo">
                <h1>CookBook 3.0</h1>
            </div>

            <div class="content">
                <h2>Dear {name},</h2>

                <p><b>You helped make the event truly special ✨</b></p>

                <p>
                    We sincerely appreciate your enthusiastic participation in
                    <b>CookBook 3.0</b>. Your curiosity, problem-solving spirit,
                    and active involvement contributed greatly to the success
                    of the event.
                </p>

                <p>
                    This certificate stands as a token of appreciation for your
                    interest in learning, collaboration, and competitive programming.
                </p>

                <p>
                    We look forward to your continued participation in future events!
                </p>

                <a class="btn btn-site" href="https://codechef-wce-chapter.org/" target="_blank">
                    🌐 Visit Our Website
                </a>

                <a class="btn btn-whatsapp" href="https://chat.whatsapp.com/DGAc2WiYg6l73plsa1cPNL" target="_blank">
                    💬 Join WhatsApp Community
                </a>
            </div>

            <div class="footer">
                Best Regards,<br>
                <b>CodeChef WCE Chapter</b>
            </div>

        </div>
    </body>
    </html>
    """, subtype="html")

    cert_path = os.path.join(CERTIFICATE_FOLDER, certificate_file)

    if not os.path.exists(cert_path):
        print(f"❌ Certificate not found: {certificate_file}")
        return

    with open(cert_path, "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype="application",
            subtype="pdf",
            filename=certificate_file
        )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)

    print(f"✅ Email sent to {name} ({receiver_email})")


with open(CSV_FILE, newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        send_certificate(row["name"], row["email"], row["certificate"])
