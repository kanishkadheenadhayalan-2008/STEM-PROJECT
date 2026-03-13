import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="Shakespeare Story Explorer", page_icon="📜")

st.title("📜 Shakespeare Story Explorer – Hidden Word Game")

menu = st.sidebar.selectbox(
    "Menu",
    ["Story Explorer","Find Shakespeare Words","Translator","Leaderboard"]
)

if "score" not in st.session_state:
    st.session_state.score = 0

if "leaderboard" not in st.session_state:
    st.session_state.leaderboard = []

# ---------------- STORIES ----------------

if menu == "Story Explorer":

    story = st.selectbox(
        "Choose Story",
        ["Romeo and Juliet","Hamlet","Macbeth"]
    )

    if story=="Romeo and Juliet":

        st.header("Romeo and Juliet")

        st.write("""
In Verona two families fight for many years.
Romeo from the Montague family meets Juliet from the Capulet family.

They fall in love secretly.

Romeo says:
**"Thou art the sun that lights my world."**

They marry secretly hoping their love will end the family fight.

However tragedy occurs and both lovers die.
Their deaths finally bring peace to their families.
""")

    elif story=="Hamlet":

        st.header("Hamlet")

        st.write("""
Prince Hamlet learns that his uncle Claudius killed his father.

The ghost tells Hamlet the truth.

Hamlet says he **hath** a duty to take revenge.

He pretends to be mad while planning justice.

In the end a tragic duel happens and many characters die.
""")

    elif story=="Macbeth":

        st.header("Macbeth")

        st.write("""
Macbeth is a brave warrior.

Three witches predict he will become king.

Encouraged by Lady Macbeth he murders King Duncan.

Macbeth **doth** become king but guilt destroys him.

Finally he is defeated in battle.
""")

# ---------------- WORD GAME ----------------

elif menu=="Find Shakespeare Words":

    st.header("Find the Meaning of Shakespeare Words")

    level = st.selectbox("Choose Level",list(range(1,11)))

    questions = [
    ("Thou",["You","King","Enemy"],"You"),
    ("Thee",["You","Run","Eat"],"You"),
    ("Thy",["Your","His","Their"],"Your"),
    ("Hath",["Has","Had","Will"],"Has"),
    ("Doth",["Does","Did","Done"],"Does"),
    ("Wilt",["Will","Run","Eat"],"Will"),
    ("Art",["Are","Run","Write"],"Are"),
    ("Dost",["Does","Did","Do"],"Does"),
    ("Wherefore",["Why","Where","When"],"Why"),
    ("Anon",["Soon","Yesterday","Never"],"Soon")
    ]

    answers=[]

    for i,q in enumerate(questions):

        ans = st.radio(
        f"Q{i+1}: What is the meaning of '{q[0]}' ?",
        q[1],
        key=f"{level}_{i}"
        )

        answers.append(ans)

    if st.button("Submit Level"):

        score=0

        for i,q in enumerate(questions):
            if answers[i]==q[2]:
                score+=1

        st.session_state.score=score

        st.success(f"Level {level} Score: {score}/10")

# ---------------- TRANSLATOR ----------------

elif menu=="Translator":

    st.header("Modern English → Shakespeare Style")

    text = st.text_input("Enter sentence")

    if st.button("Translate"):

        translation=text.lower()

        translation=translation.replace("you","thou")
        translation=translation.replace("your","thy")
        translation=translation.replace("are","art")
        translation=translation.replace("have","hast")
        translation=translation.replace("has","hath")
        translation=translation.replace("does","doth")
        translation=translation.replace("before","ere")
        translation=translation.replace("soon","anon")

        st.subheader("Shakespeare Version")
        st.success(translation)

# ---------------- LEADERBOARD ----------------

elif menu=="Leaderboard":

    st.header("Leaderboard")

    name=st.text_input("Enter your name")

    if st.button("Save Score"):

        st.session_state.leaderboard.append({
        "Name":name,
        "Score":st.session_state.score
        })

    if st.session_state.leaderboard:

        df=pd.DataFrame(st.session_state.leaderboard)


        st.table(df)
