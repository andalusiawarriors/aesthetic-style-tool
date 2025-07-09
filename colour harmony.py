def get_colour_profile(skin_tone, undertone, hair_colour, eye_colour):
    # Determine contrast type
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

    # Determine colour palette
    warm_palette = [
        "Cream", "Camel", "Caramel", "Beige", "Nude",
        "Tan", "Mocha", "Coffee", "Brown", "Olive", "Khaki", "Army"
    ]

    cool_palette = [
        "White", "Ivory", "Light Blue", "Marine", "Navy",
        "Dusty Pink", "Taupe", "Gray", "Charcoal", "Black", "Light Gray"
    ]

    if undertone == 'warm':
        best_colours = warm_palette
        worst_colours = ["Icy Blue", "Charcoal", "Black", "Marine", "Light Blue"]
    elif undertone == 'cool':
        best_colours = cool_palette
        worst_colours = ["Camel", "Caramel", "Mustard", "Olive", "Army"]
    else:
        best_colours = []
        worst_colours = []

    return {
        "contrast": contrast,
        "best": best_colours,
        "worst": worst_colours
    }

# --- USER INTERFACE ---
print("═══════════════════════════════════════")
print("🧠  AESTHETIC COLOUR HARMONY CALCULATOR")
print("═══════════════════════════════════════\n")

undertone = input("→ What is your undertone? (warm / cool): ").strip().lower()
skin_tone = input("→ What is your skin tone? (light / medium/tan / dark): ").strip().lower()
hair_colour = input("→ What is your hair colour? (blonde / white / brown / dark brown / auburn / black): ").strip().lower()
eye_colour = input("→ What is your eye colour? (blue / green / hazel / brown / dark brown / gray): ").strip().lower()

print("\n🎯 Analyzing your visual profile...")
print("───────────────────────────────────────")

profile = get_colour_profile(skin_tone, undertone, hair_colour, eye_colour)

print(f"\n🧩 RECOMMENDED CONTRAST LEVEL: {profile['contrast']}")
print("\n✅ BEST COLOURS FOR YOUR PROFILE:")
print("   " + " · ".join(profile["best"]))

print("\n🚫 COLOURS TO AVOID:")
print("   " + " · ".join(profile["worst"]))

print("\n🔗 Harmonise colour. Build presence. Every fit starts here.")
print("═══════════════════════════════════════")
