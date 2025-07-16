
# GitHub Profile Analyzer 🐙

An elegant and modern Streamlit web application for analyzing any public GitHub profile in seconds.

---

## 🚀 Overview

GitHub Profile Analyzer provides a comprehensive and visually appealing dashboard to explore public GitHub profiles. Instantly view user details, repository statistics, language usage, and more—all in a beautiful, interactive interface.

---

## ✨ Features

- **Instant Profile Lookup:**
  - Enter any public GitHub username to fetch and display:
    - Profile picture, name, bio, location, company, blog, and more
    - Key stats: public repositories, followers, following, gists
    - Account creation and last update dates
    - One-click copy of the GitHub profile URL
- **Repository Insights:**
  - View the top 5 public repositories by star count, including descriptions
- **Language Analytics:**
  - Interactive pie chart visualizing languages used across repositories
- **Profile Summary:**
  - Total stars, forks, and most-used language
- **Modern UI:**
  - Custom CSS styling and Lottie animations for an engaging user experience

---

## 🛠️ Getting Started

Follow these steps to set up and run the application locally:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/NikithaKunapareddy/Github-analyzer.git
   cd Github-analyzer
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Launch the app:**
   ```bash
   streamlit run app.py
   ```

The app will open in your default browser. Enter any GitHub username to begin analysis.

---

## 📸 Screenshots

<details>
<summary>Click to expand</summary>

![Profile Example](./screenshots/profile-example.png)
![Top Repos](./screenshots/top-repos.png)

</details>

---

## 🏗️ Architecture

The GitHub Profile Analyzer is built with a modular and maintainable architecture:

- **Frontend/UI:**
  - Developed using Streamlit for rapid prototyping and interactive web interfaces.
  - Custom CSS and Lottie animations enhance user experience and visual appeal.
- **Backend/Data Layer:**
  - Utilizes the GitHub REST API to fetch user profile and repository data in real time.
  - Data is processed and transformed using Pandas for analytics and visualization.
- **Visualization:**
  - Interactive charts and graphs are rendered using Plotly for clear data presentation.
- **App Flow:**
  1. User enters a GitHub username.
  2. App fetches profile and repository data from GitHub.
  3. Data is analyzed, summarized, and visualized in the dashboard.
  4. UI displays profile details, top repositories, language usage, and summary stats.

This architecture ensures the app is fast, reliable, and easy to extend or customize.

## 🧰 Technologies Used

- [Streamlit](https://streamlit.io) — Web app framework
- [Plotly](https://plotly.com/python/) — Interactive charts
- [Pandas](https://pandas.pydata.org/) — Data manipulation
- [GitHub REST API](https://docs.github.com/en/rest) — Data source
- [Lottie Animations](https://lottiefiles.com/) — Animated graphics

---

## 🙏 Credits

- UI inspired by modern dashboard designs

---

## 🤝 Acknowledgments

- Thanks to the open-source community for libraries and inspiration.
- Special thanks to [Streamlit](https://streamlit.io), [Plotly](https://plotly.com/python/), and [LottieFiles](https://lottiefiles.com/) for their amazing tools.
- GitHub REST API for providing accessible developer data.

---

## 💬 Support

If you encounter any issues, have suggestions, or want to contribute:

- Open an [issue](https://github.com/NikithaKunapareddy/Github-analyzer/issues)
- Submit a pull request
- Contact the maintainer via [GitHub](https://github.com/NikithaKunapareddy)

If you like this project, please consider giving it a ⭐ on GitHub!

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

**Tip:** Try usernames like `torvalds`, `guido`, or your own!

---

## 👩‍💻 Author

**Nikitha Kunapareddy**  
[![GitHub](https://img.shields.io/badge/GitHub-NikithaKunapareddy-blue?logo=github)](https://github.com/NikithaKunapareddy)

Passionate software engineer and data enthusiast focused on building elegant, user-friendly web applications and data-driven dashboards. Experienced in Python, Streamlit, and modern visualization tools. Dedicated to making developer tools and analytics accessible to everyone.