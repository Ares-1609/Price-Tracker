<h1>🛍️ Price Tracker & Deal Notifier</h1>

<p>
  An intelligent web app that helps users track product prices on Amazon and Flipkart and get
  <strong>instant email alerts</strong> when the price drops below their target!<br>
  Built with <code>React</code>, <code>Flask</code>, and <code>web scraping</code>, this tool is perfect for bargain hunters and smart shoppers.
</p>

---

<h2>📸 Demo</h2>

<p>
  <img src="https://your-screenshot-link-here.com" alt="App UI" width="600"/>
</p>
<em>Add a screenshot or Loom demo link here</em>

---

<h2>✨ Features</h2>

<ul>
  <li>🎯 Track any product using its Amazon/Flipkart URL</li>
  <li>📉 Set a target price and wait for the price to drop</li>
  <li>📬 Get an email when a deal is found</li>
  <li>💻 Beautiful modern UI built with plain CSS</li>
  <li>🔐 Secure <code>.env</code> config for your credentials</li>
</ul>

---

<h2>🧱 Tech Stack</h2>

<table>
  <thead>
    <tr>
      <th>Frontend</th>
      <th>Backend</th>
      <th>Others</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>React</td>
      <td>Flask</td>
      <td>SMTP (Gmail)</td>
    </tr>
    <tr>
      <td>Axios</td>
      <td>BeautifulSoup</td>
      <td>python-dotenv</td>
    </tr>
    <tr>
      <td>CSS</td>
      <td>Requests</td>
      <td>Git & GitHub</td>
    </tr>
  </tbody>
</table>

---

<h2>🚀 How to Run Locally</h2>

<h3>🧰 Prerequisites</h3>

<ul>
  <li>Python 3.10+ and pip</li>
  <li>Node.js and npm</li>
  <li>Gmail account with <strong>App Password</strong></li>
</ul>

---

<h3>⚙️ 1. Clone the Repository</h3>

```bash
git clone https://github.com/Ares-1609/Price-Tracker.git
cd Price-Tracker
```

---

<h3>🖥️ 2. Backend Setup</h3>

```bash
cd backend
python -m venv venv
venv\Scripts\activate  # or source venv/bin/activate on Mac/Linux
pip install -r requirements.txt
```

Create a <code>.env</code> file inside <code>backend/</code>:

```
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
```

Then:

```bash
python app.py
```

---

<h3>🌐 3. Frontend Setup</h3>

```bash
cd ../frontend
npm install
npm start
```

Visit: <a href="http://localhost:3000" target="_blank">http://localhost:3000</a>

---

<h2>📦 Folder Structure</h2>

```text
Price-Tracker/
├── backend/
│   ├── app.py
│   ├── scraper.py
│   ├── emailer.py
│   ├── .env
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   └── components/TrackerForm.js
│   └── package.json
└── README.md
```

---

<h2>📧 Email Notification</h2>

<p>
  You'll receive an email <strong>instantly</strong> when the current price drops to your set target.<br>
  Uses <code>smtplib</code> with secure Gmail App Passwords.
</p>

---

<h2>🔐 Security Notes</h2>

<ul>
  <li>❌ Do <strong>not</strong> push your <code>.env</code> file to GitHub</li>
  <li>✅ Use <code>.gitignore</code> to protect secrets</li>
  <li>☁️ Store SMTP config as environment variables in production</li>
</ul>

---

<h2>🎯 Future Enhancements</h2>

<ul>
  <li>📦 Price history charts</li>
  <li>🔔 Push/browser notifications</li>
  <li>🧠 AI-based price prediction</li>
  <li>📱 Mobile PWA support</li>
</ul>

---

<h2>🤝 Contributing</h2>

Feel free to fork, improve, or open issues! Pull requests are welcome ❤️

---

<h2>📄 License</h2>

MIT License — free to use and modify.

---

<h2>🧑‍💻 Made with 💙 by <a href="https://github.com/Ares-1609" target="_blank">Rakshit Awadhiya</a></h2>
