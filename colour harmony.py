import streamlit as st

# ---- AW BRAND CONFIG ----
st.set_page_config(
    page_title="AW Colour Harmony Tool",
    page_icon="🎯",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ---- AW LOGO ----
st.image("https://your-logo-url.com/aw-logo.png", width=140)  # Replace with your AW logo image URL

# ---- HEADLINE ----
st.markdown(
    "<h2 style='text-align: center; color: #8B0000;'>AW Colour Harmony Evaluator</h2>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align: center; color: #D4AF37;'>Unlock your contrast. Weaponize your palette.</p><hr>",
    unsafe_allow_html=True
)

# ---- USER INPUTS ----
undertone = st.selectbox("What is your undertone?", ["warm", "cool", "neutral"])
skin_tone = st.selectbox("What is your skin tone?", ["light", "medium/tan", "dark"])
hair_colour = st.selectbox("What is your hair colour?", ["blonde", "white", "brown", "dark brown", "auburn", "black"])
eye_colour = st.selectbox("What is your eye colour?", ["blue", "green", "hazel", "brown", "dark brown", "gray"])


def get_colour_profile(skin_tone, undertone, hair_colour, eye_colour):
    light_eyes = ['blue', 'green', 'gray']
    dark_eyes = ['brown', 'dark brown', 'hazel']
    light_hair = ['blonde', 'white']
    dark_hair = ['brown', 'dark brown', 'auburn', 'black']

    # Contrast logic
    if skin_tone == 'light':
        if hair_colour in dark_hair and eye_colour in light_eyes:
            contrast = 'High Contrast'
        elif hair_colour in light_hair and eye_colour in light_eyes:
            contrast = 'Low Contrast'
        else:
            contrast = 'Medium Contrast'
    elif skin_tone == 'medium/tan':
        if hair_colour in dark_hair and eye_colour in light_eyes:
            contrast = 'High Contrast'
        else:
            contrast = 'Medium Contrast'
    elif skin_tone == 'dark':
        if hair_colour in light_hair and eye_colour in light_eyes:
            contrast = 'High Contrast'
        else:
            contrast = 'Medium-High Contrast'
    else:
        contrast = 'Unknown'

    # Palette logic
    warm_palette = [
        "Cream", "Camel", "Caramel", "Beige", "Nude",
        "Tan", "Mocha", "Coffee", "Brown", "Olive", "Khaki", "Army"
    ]
    cool_palette = [
        "White", "Ivory", "Light Blue", "Marine", "Navy",
        "Dusty Pink", "Taupe", "Gray", "Charcoal", "Black", "Light Gray"
    ]
    neutral_palette = [
        "Stone", "Greige", "Muted Olive", "Ash", "Slate", "Earth Grey",
        "Saddle Brown", "Faded Navy", "Sand", "Muted Charcoal"
    ]

    if undertone == 'warm':
        best = warm_palette
        worst = ["Icy Blue", "Charcoal", "Black", "Marine", "Light Blue"]
    elif undertone == 'cool':
        best = cool_palette
        worst = ["Camel", "Caramel", "Mustard", "Olive", "Army"]
    else:  # neutral
        best = neutral_palette
        worst = ["Neon tones", "High saturation colours", "Over-bright whites"]

    return contrast, best, worst


# ---- BUTTON + RESULTS ----
if st.button("💡 Show My Colour Profile"):
    contrast, best, worst = get_colour_profile(skin_tone, undertone, hair_colour, eye_colour)

    st.markdown(f"### 🎯 Recommended Contrast Level: `{contrast}`")
    st.markdown("#### ✅ Best Colour Families:")
    st.write(" · ".join(best))

    st.markdown("#### 🚫 Colours to Avoid:")
    st.write(" · ".join(worst))

    st.markdown("<hr><p style='color:#8B0000;'>This tool is part of the AW Aesthetic Course. Master your image, dominate the room.</p>", unsafe_allow_html=True)
