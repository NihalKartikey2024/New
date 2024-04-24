import streamlit as st
st.set_page_config(
    page_title="My Page Title",
    initial_sidebar_state="auto",
    menu_items=None
)

from streamlit_option_menu import option_menu
import Home, cp, aboutus, contactus, Search_any, top_books

# Create an instance of the app 
class MultiApp():

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        with st.sidebar:
            app = option_menu(
                menu_title='Menu',
                options=['Home', 'Books', 'Top_50_books', 'Search', 'About Us', 'Contact Us'],
                icons=['house-fill', 'search', 'trophy-fill', 'search', 'info-circle-fill'],
                menu_icon='cast',
                default_index=1,
                styles={
                    "container": {"padding": "5!important", "background-color": '#FF6864'},
                    "icon": {"color": "white", "font-size": "23px"},
                    "nav-link": {"color": "#EDF4F2", "font-size": "20px", "text-align": "left", "margin": "0px",
                                "--hover-color": "#C4DFE6"},
                    "nav-link-selected": {"background-color": "#31473A"}, }
            )

        if app == "Home":
            Home.app()
        elif app == "Books":
            cp.app()
        elif app == "Top_50_books":
            top_books.app()
        elif app == "Search":
            Search_any.app()
        elif app == "About Us":
            aboutus.app()
        elif app == 'Contact Us':
            contactus.app()

multi_app = MultiApp()

multi_app.add_app("Home", Home.app)
multi_app.add_app("Account", cp.app)
multi_app.add_app("About Us", aboutus.app)
multi_app.add_app("Contact Us", contactus.app)
multi_app.add_app("Top_50_books", top_books.app)
multi_app.add_app("Search", Search_any.app)

multi_app.run()
