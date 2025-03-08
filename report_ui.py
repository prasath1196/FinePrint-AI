def report_markdown(extracted_data):
    html_content = f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Terms of Service Report</title>
            <style>
                body {{
                    font-family: 'Arial', sans-serif;
                    background-color: #f9f9f9;
                    margin: 0;
                    padding: 20px;
                }}
                .container {{
                    max-width: 900px;
                    margin: auto;
                    background: #ffffff;
                    padding: 25px;
                    border-radius: 10px;
                    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
                }}
                h1 {{
                    text-align: center;
                    color: #d9534f;
                    border-bottom: 3px solid #d9534f;
                    padding-bottom: 12px;
                    margin-bottom: 20px;
                }}
                h2 {{
                    color: #5a5a5a;
                    padding-top: 15px;
                    margin-bottom: 5px;
                }}
                .insight {{
                    background-color: #fdf7f7;
                    border-left: 6px solid #d9534f;
                    padding: 12px;
                    margin: 15px 0;
                    border-radius: 5px;
                    transition: transform 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
                }}
                .insight:hover {{
                    transform: scale(1.02);
                    box-shadow: 0 3px 8px rgba(0, 0, 0, 0.15);
                }}
                .insight strong {{
                    color: #d9534f;
                }}
                .icon {{
                    font-size: 18px;
                    margin-right: 8px;
                }}
                .footer {{
                    text-align: center;
                    padding: 10px;
                    margin-top: 20px;
                    font-size: 14px;
                    color: #666;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Terms of Service Insights</h1>
                
                <h2>🏢 Company</h2>
                <div class="insight"><span class="icon">🏛️</span> <strong>{extracted_data['company']}</strong></div>
                
                <h2>💰 Hidden Fees</h2>
                <div class="insight"><span class="icon">⚠️</span> <strong>{extracted_data['hidden_fees']}</strong></div>
                
                <h2>🔐 Data Privacy</h2>
                <div class="insight"><span class="icon">🔍</span> <strong>{extracted_data['data_privacy']}</strong></div>
                
                <h2>📝 Content Ownership</h2>
                <div class="insight"><span class="icon">📑</span> <strong>{extracted_data['content_ownership']}</strong></div>
                
                <h2>⛔ Account Bans</h2>
                <div class="insight"><span class="icon">🚫</span> <strong>{extracted_data['account_bans']}</strong></div>
                
                <h2>⚖️ Legal Disputes</h2>
                <div class="insight"><span class="icon">⚠️</span> <strong>{extracted_data['legal_disputes']}</strong></div>

                <div class="footer">
                    🔄 Report generated automatically by AI | <strong>Stay Informed, Stay Secure.</strong>
                </div>
            </div>
        </body>
        </html>"""
    return html_content