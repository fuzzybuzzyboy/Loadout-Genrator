try:
    from chatgptverify import scrape_brawlers
    from colorama import Fore, Style # Fore, Style # styles: BRIGHT, NORMAL, DIM. Fore.WHITE, Style.RESET_ALL (EXAMPLE: Fore.GREEN + Style.BRIGHT + "a")
    import random, colorama, json
    colorama.init(autoreset=True)
    scrape_brawlers()
    data = json.load(open("data.json", "r", encoding="utf-8"))

    def brawler(team_size: int = 3):
        response = {}

        all_brawlers = [
            (area, brawler)
            for area, brawlers in data.items()
            for brawler in brawlers
        ]

        # Check for any brawlers with missing gadgets or starpowers
        for area, brawler in all_brawlers:
            g = data[area][brawler].get("Gadgets", [])
            s = data[area][brawler].get("Starpowers", [])
            if not g or not s:
                print(f"⚠️ {brawler} in {area} has missing data: Gadgets={g}, Starpowers={s}")


        team_size = min(team_size, len(all_brawlers))
        selected = random.sample(all_brawlers, k=team_size)

        for area, brawler in selected:
            gadget = random.choice(data[area][brawler]["Gadgets"])
            starpower = random.choice(data[area][brawler]["Starpowers"])
            response[brawler] = {
                "Gadget": gadget,
                "Starpower": starpower,
                "Rarity": area  # 👈 this is the important part
            }

        return response


    import streamlit as st
    st.set_page_config('Team generator', layout='wide')
    st.markdown('<h1 style="text-align: center;">Brawl stars team generator</h1>', unsafe_allow_html=True)
    cols = st.columns(2, vertical_alignment='bottom')
    team = cols[0].segmented_control('How many teammates are you?', [1, 2, 3, 4, 5], default=3, help='Required.', width="stretch")
    if team is not None:
        if cols[1].button("Generate Again", type="primary", use_container_width=True):
            st.rerun()
        gen = brawler(team)
        #print(gen.items())
        for brawler_name, info in gen.items():
            st.divider()
            cols = st.columns(2, gap="large")
            cols[0].markdown(f"## **{brawler_name}** ({info['Rarity']})")
            import os
            image_path = f"images/{brawler_name}.png"
            if os.path.exists(image_path):
                cols[1].image(image_path, width=190)
            else:
                cols[1].warning(f"Image not found for {brawler_name} (how??)")
                print(f"Image not found for {brawler_name} at {image_path} (how???)")
            cols[0].write(f":green[Gadget]: {info['Gadget']}")
            cols[0].write(f":orange[Starpower]: {info['Starpower']}")
    else:
        cols[1].button("Generate Again", type="primary", use_container_width=True, disabled=True)
        st.divider()
        st.warning("Pick a team size to start.", icon=":material/warning:")#, width=221)
except ModuleNotFoundError as e:
	ModuleMissing = str(e)
	ModuleMissing = ModuleMissing.split("'")
	ModuleMissing = ModuleMissing[1]
	exit(f'Module not found: {e}\nPlease (pip) install {ModuleMissing}')
