import streamlit as st

st.set_page_config(page_title="Aesthetic Colour Harmony Tool", layout="centered")

st.title("🧠 Aesthetic Colour Harmony Evaluator")
st.markdown("Match your contrast, tone, and best colours in under 30 seconds.")

skin_tone = st.selectbox("What is your skin tone?", ["light", "medium/tan", "dark"])
undertone = st.selectbox("What is your undertone?", ["warm", "cool"])
hair_colour = st.selectbox("What is your hair colour?", ["blonde", "white", "brown", "dark brown", "auburn", "black"])
eye_colour = st.selectbox("What is your eye colour?", ["blue", "green", "hazel", "brown", "dark brown", "gray"])

def get_colour_profile(skin_tone, undertone, hair_colour, eye_colour):
    light_eyes = ['blue', 'green', 'gray']
    dark_eyes = ['brown', 'dark brown', 'hazel']
    light_hair = ['blonde', 'white']
    dark_hair = ['brown', 'dark brown', 'auburn', 'black']

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

    warm_palette = [
        "Cream", "Camel", "Caramel", "Beige", "Nude",
        "Tan", "Mocha", "Coffee", "Brown", "Olive", "Khaki", "Army"
    ]

    cool_palette = [
        "White", "Ivory", "Light Blue", "Marine", "Navy",
        "Dusty Pink", "Taupe", "Gray", "Charcoal", "Black", "Light Gray"
    ]

    if undertone == 'warm':
        best = warm_palette
        worst = ["Icy Blue", "Charcoal", "Black", "Marine", "Light Blue"]
    else:
        best = cool_palette
        worst = ["Camel", "Caramel", "Mustard", "Olive", "Army"]

    return contrast, best, worst

if st.button("💡 Show My Colour Profile"):
    contrast, best, worst = get_colour_profile(skin_tone, undertone, hair_colour, eye_colour)
    st.subheader(f"🎯 Recommended Contrast Level: {contrast}")
    st.markdown(f"✅ **Best Colours for You:**\n- " + " · ".join(best))
    st.markdown(f"🚫 **Colours to Avoid:**\n- " + " · ".join(worst))
