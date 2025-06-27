
import streamlit as st
import requests
from streamlit_extras.colored_header import colored_header
from streamlit_extras.mention import mention
import pandas as pd
import plotly.express as px
from streamlit_lottie import st_lottie
import json
from urllib.parse import unquote

st.set_page_config(
    page_title="GitHub Profile Analyzer",
    page_icon="🐙",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items=None
)

# --- Custom CSS for beautiful UI ---
st.markdown(
    """
    <style>
    body, .stApp {
        background: #e9e4f0 !important;
        font-family: 'Poppins', 'Segoe UI', 'Roboto', sans-serif;
    }
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        background: none !important;
        box-shadow: none !important;
    }
    .css-1v0mbdj, .stButton>button {
        background: linear-gradient(90deg, #7f7fd5 0%, #e0c3fc 100%) !important;
        color: #fff !important;
        border: none !important;
        border-radius: 14px !important;
        font-weight: 700 !important;
        letter-spacing: 0.5px;
        box-shadow: 0 2px 12px rgba(127, 127, 213, 0.13);
        transition: 0.2s;
        cursor: pointer;
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #e0c3fc 0%, #7f7fd5 100%) !important;
        color: #fff !important;
        transform: scale(1.08);
        box-shadow: 0 4px 18px rgba(127, 127, 213, 0.18);
    }
    .profile-card {
        background: rgba(255,255,255,0.96);
        border-radius: 22px;
        box-shadow: 0 6px 32px rgba(127, 127, 213, 0.13);
        padding: 2.2rem 1.7rem;
        margin-bottom: 2.2rem;
        transition: box-shadow 0.2s;
    }
    .profile-card:hover {
        box-shadow: 0 12px 40px rgba(127, 127, 213, 0.18);
    }
    .stat-card {
        background: rgba(255,255,255,0.93);
        border-radius: 16px;
        padding: 1.3rem 1.1rem;
        margin-bottom: 1.7rem;
        box-shadow: 0 2px 10px rgba(127, 127, 213, 0.09);
    }
    .lang-badge {
        display: inline-block;
        background: linear-gradient(90deg, #e0c3fc 0%, #b7baff 100%);
        color: #7f7fd5;
        border-radius: 10px;
        padding: 0.35em 1em;
        margin: 0.2em 0.4em 0.2em 0;
        font-size: 1.05em;
        font-weight: 600;
        box-shadow: 0 1px 6px rgba(127, 127, 213, 0.10);
        border: 1px solid #b7baff;
    }
    .top-repo-card {
        background: rgba(255,255,255,0.92);
        border-radius: 18px;
        padding: 1.3em 1.3em 1.1em 1.3em;
        margin-bottom: 1.2em;
        box-shadow: 0 4px 18px rgba(127, 127, 213, 0.10);
        border: none;
        transition: box-shadow 0.2s, transform 0.2s;
    }
    .top-repo-card:hover {
        box-shadow: 0 12px 32px rgba(127, 127, 213, 0.16);
        transform: translateY(-2px) scale(1.02);
    }
    .stPlotlyChart>div>div>svg {
        border-radius: 18px;
        background: rgba(255,255,255,0.97);
        box-shadow: 0 2px 10px rgba(127, 127, 213, 0.09);
    }
    </style>
    """,
    unsafe_allow_html=True
)




# ...existing code...

# Lottie animation loader
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code == 200:
        return r.json()
    return None

# Lottie animation (GitHub)
lottie_github = load_lottie_url("https://assets2.lottiefiles.com/packages/lf20_3rwasyjy.json")

with st.sidebar:
    st.image("https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png", width=60)
    st.title("GitHub Analyzer")
    st.markdown("""
    Enter a GitHub username to see a beautiful profile summary, stats, and more!
    
    - Built with [Streamlit](https://streamlit.io)
    - Powered by GitHub API
    """)


st_lottie(lottie_github, height=120, key="github-lottie")
colored_header("GitHub Profile Analyzer", description="Analyze any public GitHub profile in seconds!", color_name="violet-70")

username = st.text_input("🔎 Enter GitHub username:", help="Type any public GitHub username")

if username:
    with st.spinner("Fetching profile..."):
        url = f"https://api.github.com/users/{username}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            st.success(f"Profile found: {data['login']}")
            st.markdown("<div class='profile-card' style='animation: fadeIn 1.2s;'>", unsafe_allow_html=True)
            col1, col2 = st.columns([1, 3])
            with col1:
                st.image(data['avatar_url'], width=120)
                st.markdown(f"<a href='{data['html_url']}' target='_blank' style='text-decoration:none;'><button style='background:#24292f;color:white;border:none;padding:8px 16px;border-radius:8px;margin-top:8px;'>View on GitHub</button></a>", unsafe_allow_html=True)
            with col2:
                if data.get('name'):
                    st.markdown(f"<h3 style='margin-bottom:0.2em'>{data['name']}</h3>", unsafe_allow_html=True)
                if data.get('bio'):
                    st.markdown(f"<span style='color:#6c757d;'>{data['bio']}</span>", unsafe_allow_html=True)
                if data.get('location'):
                    st.markdown(f"<span style='font-size:1em;'>📍 {data['location']}</span>", unsafe_allow_html=True)
                if data.get('company'):
                    st.markdown(f"<span style='font-size:1em;'>🏢 {data['company']}</span>", unsafe_allow_html=True)
                if data.get('blog'):
                    st.markdown(f"<span style='font-size:1em;'>🔗 <a href='{data['blog']}' target='_blank'>{data['blog']}</a></span>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

            st.markdown("<div class='stat-card' style='animation: fadeIn 1.2s;'>", unsafe_allow_html=True)
            st.markdown("<h4 style='margin-bottom:1em;'>Stats</h4>", unsafe_allow_html=True)
            c1, c2, c3, c4 = st.columns(4)
            c1.metric("Public Repos", data['public_repos'], "📦")
            c2.metric("Followers", data['followers'], "👥")
            c3.metric("Following", data['following'], "➡️")
            c4.metric("Gists", data['public_gists'], "📝")
            st.markdown("</div>", unsafe_allow_html=True)

            st.markdown("<div class='stat-card' style='animation: fadeIn 1.2s;'>", unsafe_allow_html=True)
            st.markdown("<h4 style='margin-bottom:1em;'>More Info</h4>", unsafe_allow_html=True)
            more_info = []
            if data.get('created_at'):
                more_info.append(f"<b>Created at:</b> {data['created_at'][:10]}")
            if data.get('updated_at'):
                more_info.append(f"<b>Last updated:</b> {data['updated_at'][:10]}")
            if data.get('twitter_username'):
                more_info.append(f"<b>Twitter:</b> @{data['twitter_username']}")
            if data.get('email'):
                more_info.append(f"<b>Email:</b> {data['email']}")
            if more_info:
                st.markdown("<ul style='margin:0;padding-left:1.2em;'>" + "".join([f"<li>{item}</li>" for item in more_info]) + "</ul>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)
            st.info("Tip: Try famous usernames like 'torvalds', 'guido', or your own!")

            # --- Fetch Repositories ---
            repos_url = data['repos_url']
            repos_response = requests.get(repos_url)
            repos = repos_response.json() if repos_response.status_code == 200 else []

            # --- Summary Card ---
            if repos:
                total_stars = sum(r.get('stargazers_count', 0) for r in repos)
                total_forks = sum(r.get('forks_count', 0) for r in repos)
                lang_count = {}
                for repo in repos:
                    lang = repo['language']
                    if lang:
                        lang_count[lang] = lang_count.get(lang, 0) + 1
                most_used_lang = max(lang_count, key=lang_count.get) if lang_count else 'N/A'
                st.markdown(f"""
                <div class='profile-card' style='animation: fadeIn 1.2s;'>
                    <h4 style='margin-bottom:0.7em;'>✨ Profile Summary</h4>
                    <b>Total Stars:</b> ⭐ {total_stars} &nbsp; | &nbsp; <b>Total Forks:</b> 🍴 {total_forks} &nbsp; | &nbsp; <b>Most Used Language:</b> <span class='lang-badge'>{most_used_lang}</span>
                </div>
                """, unsafe_allow_html=True)

            # --- Copy GitHub URL Button ---
            import streamlit.components.v1 as components
            copy_code = f"navigator.clipboard.writeText('{data['html_url']}');"
            st.markdown("<div style='margin-bottom:1em;'></div>", unsafe_allow_html=True)
            if st.button('📋 Copy GitHub URL'):
                components.html(f"<script>{copy_code}</script>", height=0)
                st.success('GitHub URL copied to clipboard!')

            # --- Top 5 Repositories by Stars ---
            st.markdown("<h3 style='margin-bottom:0.7em; margin-top:1.5em;'>⭐ Top 5 Public Repositories (by stars)</h3>", unsafe_allow_html=True)
            if repos:
                top_repos = sorted(repos, key=lambda r: r['stargazers_count'], reverse=True)[:5]
                st.markdown("<div style='display: flex; flex-direction: column; gap: 0.5em;'>", unsafe_allow_html=True)
                for repo in top_repos:
                    st.markdown(f"""
                        <div class='top-repo-card' style='animation: fadeIn 1.2s; box-shadow: 0 4px 18px rgba(127,127,213,0.10); border: none;'>
                            <b><a href='{repo['html_url']}' target='_blank' style='color:#4b3ca7;text-decoration:none;'>{repo['name']}</a></b>
                            <span style='font-size:1.1em; margin-left:0.5em;'>⭐ {repo['stargazers_count']}</span><br>
                            <span style='color:#6c757d;'>{repo['description'] or ''}</span>
                        </div>
                    """, unsafe_allow_html=True)
                st.markdown("</div>", unsafe_allow_html=True)
            else:
                st.info("No public repositories found.")

            # --- Pie Chart of Languages Used ---
            st.markdown("<h3 style='margin-bottom:0.7em; margin-top:1.5em;'>🗂️ Languages Used (Pie Chart)</h3>", unsafe_allow_html=True)
            if repos:
                lang_count = {}
                for repo in repos:
                    lang = repo['language']
                    if lang:
                        lang_count[lang] = lang_count.get(lang, 0) + 1
                if lang_count:
                    lang_df = pd.DataFrame({
                        'Language': list(lang_count.keys()),
                        'Count': list(lang_count.values())
                    })
                    # Custom color palette for beautiful pie chart
                    custom_colors = ['#43cea2', '#185a9d', '#f8ffae', '#f7971e', '#fd5c63', '#a770ef', '#f6d365', '#fda085', '#f5576c', '#4facfe']
                    fig = px.pie(
                        lang_df,
                        names='Language',
                        values='Count',
                        title='Languages Used',
                        color_discrete_sequence=custom_colors
                    )
                    fig.update_traces(textinfo='percent+label', textfont_size=18, pull=[0.04]*len(lang_df))
                    fig.update_layout(
                        legend=dict(
                            font=dict(size=16),
                            orientation="v",
                            yanchor="middle",
                            y=0.5,
                            xanchor="left",
                            x=1.02
                        ),
                        margin=dict(t=60, b=30, l=0, r=0),
                        paper_bgcolor='rgba(0,0,0,0)',
                        plot_bgcolor='rgba(0,0,0,0)'
                    )
                    st.plotly_chart(fig, use_container_width=True)
                    st.markdown("<div style='margin-top:1em; text-align:center;'>" +
                        " ".join([f"<span class='lang-badge'>{lang}</span>" for lang in lang_count.keys()]) +
                        "</div>", unsafe_allow_html=True)
                else:
                    st.info("No language data available.")
            else:
                st.info("No language data available.")
        else:
            st.error("User not found. Please check the username and try again.")
