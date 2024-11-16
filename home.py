import streamlit as st

# if "logged_in" not in st.session_state:
#     st.session_state.logged_in = False

# def login():
#     if st.button("Log in"):
#         st.session_state.logged_in = True
#         st.rerun()

# def logout():
#     if st.button("Log out"):
#         st.session_state.logged_in = False
#         st.rerun()

# login_page = st.Page(login, title="Log in", icon=":material/login:")
# logout_page = st.Page(logout, title="Log out", icon=":material/logout:")

dashboard = st.Page(
    "pages/dashboard.py", title="Dashboard", icon=":material/dashboard:", default=True
)
# bugs = st.Page("app.py", title="Bug reports", icon=":material/bug_report:")
# alerts = st.Page(
#     "app.py", title="System alerts", icon=":material/notification_important:"
# )

# search = st.Page("home.py", title="Search", icon=":material/search:")
# history = st.Page("app.py", title="History", icon=":material/history:")

# if st.session_state.logged_in:
pg = st.navigation(
    {
        "Home": [dashboard]
    }
)
# else:
# pg = st.navigation([login_page])

pg.run()