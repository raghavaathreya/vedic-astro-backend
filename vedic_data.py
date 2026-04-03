# vedic_data.py - Traditional Vedic Astrology Reference Data

# Nakshatra data with ruling planets (lords)
NAKSHATRA_DATA = {
    "Ashwini": {
        "lord": "Ketu",
        "deity": "Ashwini Kumaras",
        "symbol": "Horse's head",
        "quality": "Quick, healing, pioneering",
        "lucky_number": [7, 9],
        "lucky_color": ["Red", "Orange"],
        "lucky_day": "Tuesday",
        "lucky_gem": "Cat's Eye",
        "metal": "Iron"
    },
    "Bharani": {
        "lord": "Venus",
        "deity": "Yama",
        "symbol": "Yoni",
        "quality": "Creative, passionate, nurturing",
        "lucky_number": [6, 9],
        "lucky_color": ["Red", "Pink"],
        "lucky_day": "Friday",
        "lucky_gem": "Diamond",
        "metal": "Silver"
    },
    "Krittika": {
        "lord": "Sun",
        "deity": "Agni",
        "symbol": "Razor",
        "quality": "Sharp, purifying, determined",
        "lucky_number": [1, 3],
        "lucky_color": ["Red", "Orange", "Gold"],
        "lucky_day": "Sunday",
        "lucky_gem": "Ruby",
        "metal": "Gold"
    },
    "Rohini": {
        "lord": "Moon",
        "deity": "Brahma",
        "symbol": "Chariot",
        "quality": "Beautiful, creative, materialistic",
        "lucky_number": [2, 7],
        "lucky_color": ["White", "Cream"],
        "lucky_day": "Monday",
        "lucky_gem": "Pearl",
        "metal": "Silver"
    },
    "Mrigashira": {
        "lord": "Mars",
        "deity": "Soma",
        "symbol": "Deer's head",
        "quality": "Curious, searching, gentle",
        "lucky_number": [9, 3],
        "lucky_color": ["Red", "Green"],
        "lucky_day": "Tuesday",
        "lucky_gem": "Coral",
        "metal": "Copper"
    },
    "Ardra": {
        "lord": "Rahu",
        "deity": "Rudra",
        "symbol": "Teardrop",
        "quality": "Transformative, intense, stormy",
        "lucky_number": [4, 8],
        "lucky_color": ["Green", "Grey"],
        "lucky_day": "Saturday",
        "lucky_gem": "Hessonite",
        "metal": "Lead"
    },
    "Punarvasu": {
        "lord": "Jupiter",
        "deity": "Aditi",
        "symbol": "Bow and quiver",
        "quality": "Optimistic, forgiving, expansive",
        "lucky_number": [3, 5],
        "lucky_color": ["Yellow", "Gold"],
        "lucky_day": "Thursday",
        "lucky_gem": "Yellow Sapphire",
        "metal": "Gold"
    },
    "Pushya": {
        "lord": "Saturn",
        "deity": "Brihaspati",
        "symbol": "Cow's udder",
        "quality": "Nurturing, protective, disciplined",
        "lucky_number": [8, 4],
        "lucky_color": ["Blue", "Black"],
        "lucky_day": "Saturday",
        "lucky_gem": "Blue Sapphire",
        "metal": "Iron"
    },
    "Ashlesha": {
        "lord": "Mercury",
        "deity": "Nagas",
        "symbol": "Coiled serpent",
        "quality": "Mystical, penetrating, cunning",
        "lucky_number": [5, 6],
        "lucky_color": ["Green", "Emerald"],
        "lucky_day": "Wednesday",
        "lucky_gem": "Emerald",
        "metal": "Bronze"
    },
    "Magha": {
        "lord": "Ketu",
        "deity": "Pitris",
        "symbol": "Royal throne",
        "quality": "Regal, traditional, authoritative",
        "lucky_number": [7, 9],
        "lucky_color": ["Red", "Gold"],
        "lucky_day": "Tuesday",
        "lucky_gem": "Cat's Eye",
        "metal": "Gold"
    },
    "Purva Phalguni": {
        "lord": "Venus",
        "deity": "Bhaga",
        "symbol": "Hammock",
        "quality": "Pleasure-seeking, artistic, generous",
        "lucky_number": [6, 9],
        "lucky_color": ["White", "Pink"],
        "lucky_day": "Friday",
        "lucky_gem": "Diamond",
        "metal": "Silver"
    },
    "Uttara Phalguni": {
        "lord": "Sun",
        "deity": "Aryaman",
        "symbol": "Bed",
        "quality": "Generous, helpful, organized",
        "lucky_number": [1, 3],
        "lucky_color": ["Gold", "Orange"],
        "lucky_day": "Sunday",
        "lucky_gem": "Ruby",
        "metal": "Gold"
    },
    "Hasta": {
        "lord": "Moon",
        "deity": "Savitar",
        "symbol": "Hand",
        "quality": "Skillful, crafty, humorous",
        "lucky_number": [2, 7],
        "lucky_color": ["White", "Light Green"],
        "lucky_day": "Monday",
        "lucky_gem": "Pearl",
        "metal": "Silver"
    },
    "Chitra": {
        "lord": "Mars",
        "deity": "Tvashtar",
        "symbol": "Bright jewel",
        "quality": "Creative, charismatic, artistic",
        "lucky_number": [9, 3],
        "lucky_color": ["Red", "Orange"],
        "lucky_day": "Tuesday",
        "lucky_gem": "Coral",
        "metal": "Copper"
    },
    "Swati": {
        "lord": "Rahu",
        "deity": "Vayu",
        "symbol": "Young sprout",
        "quality": "Independent, adaptable, gentle",
        "lucky_number": [4, 8],
        "lucky_color": ["Black", "Blue"],
        "lucky_day": "Saturday",
        "lucky_gem": "Hessonite",
        "metal": "Lead"
    },
    "Vishakha": {
        "lord": "Jupiter",
        "deity": "Indra-Agni",
        "symbol": "Triumphal arch",
        "quality": "Goal-oriented, ambitious, intense",
        "lucky_number": [3, 5],
        "lucky_color": ["Yellow", "Gold"],
        "lucky_day": "Thursday",
        "lucky_gem": "Yellow Sapphire",
        "metal": "Gold"
    },
    "Anuradha": {
        "lord": "Saturn",
        "deity": "Mitra",
        "symbol": "Lotus",
        "quality": "Devoted, balanced, harmonious",
        "lucky_number": [8, 4],
        "lucky_color": ["Blue", "Red"],
        "lucky_day": "Saturday",
        "lucky_gem": "Blue Sapphire",
        "metal": "Iron"
    },
    "Jyeshtha": {
        "lord": "Mercury",
        "deity": "Indra",
        "symbol": "Earring",
        "quality": "Protective, authoritative, secretive",
        "lucky_number": [5, 6],
        "lucky_color": ["Red", "Green"],
        "lucky_day": "Wednesday",
        "lucky_gem": "Emerald",
        "metal": "Bronze"
    },
    "Mula": {
        "lord": "Ketu",
        "deity": "Nirriti",
        "symbol": "Roots",
        "quality": "Investigative, philosophical, destructive",
        "lucky_number": [7, 9],
        "lucky_color": ["Red", "Brown"],
        "lucky_day": "Tuesday",
        "lucky_gem": "Cat's Eye",
        "metal": "Iron"
    },
    "Purva Ashadha": {
        "lord": "Venus",
        "deity": "Apas",
        "symbol": "Elephant tusk",
        "quality": "Invincible, proud, purifying",
        "lucky_number": [6, 9],
        "lucky_color": ["White", "Yellow"],
        "lucky_day": "Friday",
        "lucky_gem": "Diamond",
        "metal": "Silver"
    },
    "Uttara Ashadha": {
        "lord": "Sun",
        "deity": "Vishvadevas",
        "symbol": "Planks of a bed",
        "quality": "Righteous, grateful, leadership",
        "lucky_number": [1, 3],
        "lucky_color": ["Orange", "Gold"],
        "lucky_day": "Sunday",
        "lucky_gem": "Ruby",
        "metal": "Gold"
    },
    "Shravana": {
        "lord": "Moon",
        "deity": "Vishnu",
        "symbol": "Ear",
        "quality": "Listening, learning, connecting",
        "lucky_number": [2, 7],
        "lucky_color": ["White", "Light Blue"],
        "lucky_day": "Monday",
        "lucky_gem": "Pearl",
        "metal": "Silver"
    },
    "Dhanishta": {
        "lord": "Mars",
        "deity": "Vasus",
        "symbol": "Drum",
        "quality": "Wealthy, musical, charitable",
        "lucky_number": [9, 3],
        "lucky_color": ["Red", "Orange"],
        "lucky_day": "Tuesday",
        "lucky_gem": "Coral",
        "metal": "Copper"
    },
    "Shatabhisha": {
        "lord": "Rahu",
        "deity": "Varuna",
        "symbol": "Empty circle",
        "quality": "Healing, mysterious, solitary",
        "lucky_number": [4, 8],
        "lucky_color": ["Blue", "Green"],
        "lucky_day": "Saturday",
        "lucky_gem": "Hessonite",
        "metal": "Lead"
    },
    "Purva Bhadrapada": {
        "lord": "Jupiter",
        "deity": "Aja Ekapada",
        "symbol": "Swords",
        "quality": "Passionate, transformative, dualistic",
        "lucky_number": [3, 5],
        "lucky_color": ["Yellow", "Silver"],
        "lucky_day": "Thursday",
        "lucky_gem": "Yellow Sapphire",
        "metal": "Gold"
    },
    "Uttara Bhadrapada": {
        "lord": "Saturn",
        "deity": "Ahir Budhnya",
        "symbol": "Twin",
        "quality": "Deep, patient, mystical",
        "lucky_number": [8, 4],
        "lucky_color": ["Purple", "Black"],
        "lucky_day": "Saturday",
        "lucky_gem": "Blue Sapphire",
        "metal": "Iron"
    },
    "Revati": {
        "lord": "Mercury",
        "deity": "Pushan",
        "symbol": "Fish",
        "quality": "Prosperous, caring, wealthy",
        "lucky_number": [5, 6],
        "lucky_color": ["Brown", "Green"],
        "lucky_day": "Wednesday",
        "lucky_gem": "Emerald",
        "metal": "Bronze"
    }
}

# Rashi (Zodiac Sign) data
RASHI_DATA = {
    "Mesha (Aries)": {
        "element": "Fire",
        "quality": "Cardinal",
        "lord": "Mars",
        "nature": "Aggressive, pioneering, energetic",
        "lucky_number": [9, 1],
        "lucky_color": ["Red", "Scarlet"],
        "lucky_day": "Tuesday",
        "lucky_gem": "Red Coral",
        "metal": "Copper",
        "body_part": "Head",
        "strengths": ["Courageous", "Determined", "Confident", "Enthusiastic"],
        "weaknesses": ["Impatient", "Moody", "Short-tempered", "Impulsive"]
    },
    "Vrishabha (Taurus)": {
        "element": "Earth",
        "quality": "Fixed",
        "lord": "Venus",
        "nature": "Stable, patient, materialistic",
        "lucky_number": [6, 5],
        "lucky_color": ["Pink", "White"],
        "lucky_day": "Friday",
        "lucky_gem": "Diamond",
        "metal": "Silver",
        "body_part": "Throat, neck",
        "strengths": ["Reliable", "Patient", "Practical", "Devoted"],
        "weaknesses": ["Stubborn", "Possessive", "Uncompromising"]
    },
    "Mithuna (Gemini)": {
        "element": "Air",
        "quality": "Mutable",
        "lord": "Mercury",
        "nature": "Communicative, versatile, curious",
        "lucky_number": [5, 3],
        "lucky_color": ["Green", "Yellow"],
        "lucky_day": "Wednesday",
        "lucky_gem": "Emerald",
        "metal": "Bronze",
        "body_part": "Shoulders, arms, lungs",
        "strengths": ["Gentle", "Affectionate", "Curious", "Adaptable"],
        "weaknesses": ["Nervous", "Inconsistent", "Indecisive"]
    },
    "Karka (Cancer)": {
        "element": "Water",
        "quality": "Cardinal",
        "lord": "Moon",
        "nature": "Emotional, nurturing, protective",
        "lucky_number": [2, 7],
        "lucky_color": ["White", "Silver"],
        "lucky_day": "Monday",
        "lucky_gem": "Pearl",
        "metal": "Silver",
        "body_part": "Chest, stomach",
        "strengths": ["Tenacious", "Highly imaginative", "Loyal", "Emotional"],
        "weaknesses": ["Moody", "Pessimistic", "Suspicious", "Insecure"]
    },
    "Simha (Leo)": {
        "element": "Fire",
        "quality": "Fixed",
        "lord": "Sun",
        "nature": "Confident, generous, leadership",
        "lucky_number": [1, 4],
        "lucky_color": ["Gold", "Orange"],
        "lucky_day": "Sunday",
        "lucky_gem": "Ruby",
        "metal": "Gold",
        "body_part": "Heart, spine",
        "strengths": ["Creative", "Passionate", "Generous", "Cheerful"],
        "weaknesses": ["Arrogant", "Stubborn", "Self-centered", "Inflexible"]
    },
    "Kanya (Virgo)": {
        "element": "Earth",
        "quality": "Mutable",
        "lord": "Mercury",
        "nature": "Analytical, practical, perfectionist",
        "lucky_number": [5, 6],
        "lucky_color": ["Green", "Grey"],
        "lucky_day": "Wednesday",
        "lucky_gem": "Emerald",
        "metal": "Bronze",
        "body_part": "Digestive system",
        "strengths": ["Loyal", "Analytical", "Kind", "Hardworking"],
        "weaknesses": ["Shy", "Worry", "Overly critical", "Perfectionist"]
    },
    "Tula (Libra)": {
        "element": "Air",
        "quality": "Cardinal",
        "lord": "Venus",
        "nature": "Balanced, diplomatic, social",
        "lucky_number": [6, 9],
        "lucky_color": ["Pink", "Light Blue"],
        "lucky_day": "Friday",
        "lucky_gem": "Diamond",
        "metal": "Silver",
        "body_part": "Kidneys, lower back",
        "strengths": ["Cooperative", "Diplomatic", "Gracious", "Fair-minded"],
        "weaknesses": ["Indecisive", "Avoids confrontations", "Self-pity"]
    },
    "Vrishchika (Scorpio)": {
        "element": "Water",
        "quality": "Fixed",
        "lord": "Mars",
        "nature": "Intense, passionate, mysterious",
        "lucky_number": [9, 18],
        "lucky_color": ["Red", "Black"],
        "lucky_day": "Tuesday",
        "lucky_gem": "Red Coral",
        "metal": "Copper",
        "body_part": "Reproductive system",
        "strengths": ["Resourceful", "Brave", "Passionate", "Stubborn"],
        "weaknesses": ["Distrusting", "Jealous", "Secretive", "Violent"]
    },
    "Dhanu (Sagittarius)": {
        "element": "Fire",
        "quality": "Mutable",
        "lord": "Jupiter",
        "nature": "Optimistic, philosophical, adventurous",
        "lucky_number": [3, 9],
        "lucky_color": ["Yellow", "Orange"],
        "lucky_day": "Thursday",
        "lucky_gem": "Yellow Sapphire",
        "metal": "Gold",
        "body_part": "Hips, thighs",
        "strengths": ["Generous", "Idealistic", "Great sense of humor"],
        "weaknesses": ["Promises more than can deliver", "Impatient"]
    },
    "Makara (Capricorn)": {
        "element": "Earth",
        "quality": "Cardinal",
        "lord": "Saturn",
        "nature": "Disciplined, ambitious, practical",
        "lucky_number": [8, 4],
        "lucky_color": ["Black", "Brown"],
        "lucky_day": "Saturday",
        "lucky_gem": "Blue Sapphire",
        "metal": "Iron",
        "body_part": "Knees, bones",
        "strengths": ["Responsible", "Disciplined", "Self-control", "Manager"],
        "weaknesses": ["Know-it-all", "Unforgiving", "Condescending"]
    },
    "Kumbha (Aquarius)": {
        "element": "Air",
        "quality": "Fixed",
        "lord": "Saturn",
        "nature": "Innovative, humanitarian, independent",
        "lucky_number": [8, 4],
        "lucky_color": ["Blue", "Turquoise"],
        "lucky_day": "Saturday",
        "lucky_gem": "Blue Sapphire",
        "metal": "Lead",
        "body_part": "Ankles, circulatory system",
        "strengths": ["Progressive", "Original", "Independent", "Humanitarian"],
        "weaknesses": ["Runs from emotional expression", "Uncompromising"]
    },
    "Meena (Pisces)": {
        "element": "Water",
        "quality": "Mutable",
        "lord": "Jupiter",
        "nature": "Compassionate, intuitive, artistic",
        "lucky_number": [3, 7],
        "lucky_color": ["Sea Green", "Purple"],
        "lucky_day": "Thursday",
        "lucky_gem": "Yellow Sapphire",
        "metal": "Tin",
        "body_part": "Feet, immune system",
        "strengths": ["Compassionate", "Artistic", "Intuitive", "Gentle"],
        "weaknesses": ["Fearful", "Overly trusting", "Sad", "Victim mentality"]
    }
}

def get_nakshatra_info(nakshatra_name):
    """Get detailed nakshatra information"""
    # Extract just the nakshatra name (remove Pada info)
    base_name = nakshatra_name.split('(')[0].strip()
    return NAKSHATRA_DATA.get(base_name, {})

def get_rashi_info(rashi_name):
    """Get detailed rashi information"""
    return RASHI_DATA.get(rashi_name, {})