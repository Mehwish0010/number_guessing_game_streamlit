import random
import streamlit as st

# Streamlit UI with Styling
st.set_page_config(page_title="Number Guessing Game", page_icon="🎮", layout="centered")

st.markdown(
    """
    <style>
        body { background-color: #f0f8ff; }
        .stApp { background: linear-gradient(to right, #ff9966, #ff5e62); color: white; }
        .big-font { font-size:60px !important; font-weight: bold; text-align: center; }
        .stButton>button { background-color: #4CAF50; color: white; font-size: 18px; padding: 10px; border-radius: 8px; }
        .stNumberInput>div>div>input { font-size: 28px; text-align: center; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown("<p class='big-font'>🎮 WELCOME TO THE GAMEWORLD!</p>", unsafe_allow_html=True)
st.write("💡 **Rules:** You have **5 attempts** to guess the number between **50 and 100**. Let's play!")

# Initialize session state variables
if 'number_to_guess' not in st.session_state:
    st.session_state.number_to_guess = random.randint(50, 100)
    st.session_state.chances = 5
    st.session_state.guess_counter = 0
    st.session_state.game_over = False
    st.session_state.message = ""

# User input with styling
if not st.session_state.game_over:
    my_guess = st.number_input("🔢 Enter your guess:", min_value=50, max_value=100, step=1, format="%d")
    
    if st.button("🚀 Submit Guess"):
        st.session_state.guess_counter += 1
        
        if my_guess == st.session_state.number_to_guess:
            st.session_state.message = f"🎉 **Congratulations!** The number was **{st.session_state.number_to_guess}**. You succeeded in **{st.session_state.guess_counter}** attempts!"
            st.session_state.game_over = True
        elif st.session_state.guess_counter >= st.session_state.chances:
            st.session_state.message = f"❌ **Game Over!** The correct number was **{st.session_state.number_to_guess}**. Try again!"
            st.session_state.game_over = True
        elif my_guess < st.session_state.number_to_guess:
            st.session_state.message = "📉 **Too Low!** Try a higher number."
        elif my_guess > st.session_state.number_to_guess:
            st.session_state.message = "📈 **Too High!** Try a lower number."

# Display message
st.markdown(f"<h2 style='text-align: center; color: yellow;'>{st.session_state.message}</h2>", unsafe_allow_html=True)

# Reset game button
if st.session_state.game_over and st.button("🔄 Play Again"):
    st.session_state.number_to_guess = random.randint(50, 100)
    st.session_state.chances = 5
    st.session_state.guess_counter = 0
    st.session_state.game_over = False
    st.session_state.message = ""
