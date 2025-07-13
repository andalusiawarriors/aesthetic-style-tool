import streamlit as st

# ---- PAGE CONFIG ----
st.set_page_config(
    page_title="AW Colour Harmony Tool",
    page_icon="🎯",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ---- CENTERED LOGO ----
st.markdown(
    """
    <div style="display: flex; justify-content: center; padding-bottom: 10px;">
        <img src="https://raw.githubusercontent.com/andalusiawarriors/aesthetic-style-tool/refs/heads/main/ICON.png" width="140">
    </div>
    """,
    unsafe_allow_html=True
)

# ---- HEADLINE ----
st.markdown(
    "<h2 style='text-align: center;'>AW Colour Harmony Evaluator</h2>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align: center;'>Unlock your contrast. Weaponize your palette.</p><hr>",
    unsafe_allow_html=True
)

# ---- USER INPUTS ----
undertone = st.selectbox("What is your undertone?", ["warm", "cool", "neutral"])
skin_tone = st.selectbox("What is your skin tone?", ["light", "medium/tan", "dark"])
hair_colour = st.selectbox("What is your hair colour?", ["blonde", "white", "brown", "dark brown", "auburn", "black"])
eye_colour = st.selectbox("What is your eye colour?", ["blue", "green", "hazel", "brown", "dark brown", "gray"])

# ---- LOGIC FUNCTION ----
def get_colour_profile(skin_tone, undertone, hair_colour, eye_colour):
    light_eyes = ['blue', 'green', 'gray']
    dark_eyes = ['brown', 'dark brown', 'hazel']
    light_hair = ['blonde', 'white']
    dark_hair = ['brown', 'dark brown', 'auburn', 'black']

    # Determine contrast
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

    # Define colour palettes
    warm_palette = [
        "Cream", "Camel", "Caramel", "Beige", "Nude",
        "Tan", "Mocha", "Coffee", "Brown", "Olive", "Khaki", "Army"
    ]
    cool_palette = [
        "White", "Ivory", "Light Blue", "Marine", "Navy",
        "Dusty Pink", "Taupe", "Gray", "Charcoal", "Black", "Light Gray"
    ]
    neutral_palette = [
        "Stone", "Greige", "Ash", "Slate", "Earth Grey",
        "Muted Olive", "Faded Navy", "Taupe", "Sand", "Muted Charcoal"
    ]

    # Match palettes and principles
    if undertone == 'warm':
        best = warm_palette
        worst = ["Icy Neutrals", "Charcoal", "Jet Black", "Marine", "Sapphire", "Cool Lavender", "Cobalt", "Slate", " Dusty rose", "Taupe (blue-based)"]
        principle = ["Wear colours that feel like the sun touched them (red-based neutrals and yellow-based neutrals). If it looks good under golden light, it’ll look good on you."]
    elif undertone == 'cool':
        best = cool_palette
        worst = ["Camel", "Caramel", "Mustard", "Olive", "Khaki", "Beige", "Sand", "Army Green", "Brown", "Warm taupes"]
        principle = ["Blue-based neutrals like will sharpen your features, while red-based and yellow-based neutrals will clash with your skin and flatten your face."]
    elif undertone == 'neutral':
        best = neutral_palette
        worst = ["Jet black", "Stark white", "Neon beige", "Silver grey", "Pale khaki"]
        principle = ["Wear colours that feel like weathered stone, faded shadow, or earth at dusk - nothing loud, nothing pale, just perfectly muted. If it looks balanced in both golden and silver light, it’ll look balanced on you."]
    else:
        best = []
        worst = []
        principle = []
   
    return contrast, best, worst

# ---- RESULTS ----
if st.button("💡 Show My Colour Profile"):
    contrast, best, worst, principle = get_colour_profile(skin_tone, undertone, hair_colour, eye_colour)

    st.markdown(f"### 🎯 Contrast Level: `{contrast}`")
    st.markdown(f"🟡 Undertone: **{undertone.capitalize()}**")
    
    st.markdown("#### Principle:")
    st.write(principle)
    
    st.markdown("#### ✅ Best Neutral Colours:")
    st.write(" · ".join(best))

    st.markdown("#### 🚫 Neutral Colours to Avoid:")
    st.write(" · ".join(worst))

    st.markdown("<hr><p style='color:#8B0000;'>This tool is part of the AW Aesthetic Course. Master your image, then dominate the room.</p>", unsafe_allow_html=True)


