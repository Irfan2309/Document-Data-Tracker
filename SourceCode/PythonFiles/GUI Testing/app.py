import streamlit as st

# Set page configuration
st.set_page_config(page_title='Login', layout='centered')
st.markdown("""
<style>
    .stButton>button {
        display: block;
        width: 100%;
        margin: 0px auto;
        border-radius: 5px;
        background-color: #4a7dff; /* Adjust the color to match your theme */
        color: white;
        border: none;
        height: 40px; /* Match the height to your inputs */
    }
</style>
""", unsafe_allow_html=True)


def get_card_style():
    return """
    <style>
        .card {
            margin: 10px 0px;
            padding: 20px;
            text-align: center;
            background-color: #333333;
            color: white;
            border-radius: 10px;
            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.15);
        }
        .card-title {
            margin-top: 10px;
            font-size: 1.25rem;
            color: #aaa;
        }
        .card-value {
            font-size: 2.5rem;
            margin-bottom: 10px;
        }
    </style>
    """

# Function to display a row of cards with the dark theme
def display_cards():
    # Inject the card style
    st.markdown(get_card_style(), unsafe_allow_html=True)

    # Card data
    card_data = [
        ("New Booking", "258"),
        ("Customers", "1,287"),
        ("New Project", "128"),
        ("Revenue", "$48,697")
    ]

    # Generate a container to hold the cards in a row
    card_container = st.container()
    with card_container:
        # Create 4 columns to hold the cards
        cols = st.columns(4)
        # For each column, create a card
        for col, data in zip(cols, card_data):
            with col:
                # Each card is a div with a class of 'card'
                st.markdown(f"""
                <div class="card">
                    <div class="card-value">{data[1]}</div>
                    <div class="card-title">{data[0]}</div>
                </div>
                """, unsafe_allow_html=True)
    
# Function to display the login form
def login_form():
    with st.container():
        col1, col2, col3 = st.columns((1, 2, 1))
        with col2:
            st.title("Login")

            # Login form
            with st.form(key='login_form'):
                email = st.text_input("Email")
                password = st.text_input("Password", type="password")
                
                # Align the login button
                submitted = st.form_submit_button("Login")
                if submitted:
                    if email == "admin@email.com" and password == "admin":
                        # Set the session state to indicate authentication success
                        st.session_state['authenticated'] = True
                        st.experimental_rerun()  # Rerun the app to update the state
                    else:
                        st.error("Invalid username or password")

# Function to display the new screen after successful login
def new_screen():
    # Sidebar layout
    with st.sidebar:
        st.title('Menu')
        st.markdown("## Dashboard")
        st.markdown("Widgets")
        st.markdown("Apps")
        st.markdown("Email")
        
        st.title('UI ELEMENTS')
        st.markdown("Basic Components")
        st.markdown("Advanced")
        st.markdown("Blank Page")

        st.title('OTIKA')
        st.markdown("Forms")
        st.markdown("Tables")
        st.markdown("Charts")
        st.markdown("Icons")

    # Main content area
    display_cards()


# # Run the appropriate screen based on authentication status
if 'authenticated' in st.session_state and st.session_state['authenticated']:
    new_screen()
else:
    login_form()



# new_screen()

