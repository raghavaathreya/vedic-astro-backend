# daily_predictions.py - Daily Predictions based on Current Transits

from datetime import datetime
import pytz

def get_weekday_lord(weekday):
    """Get ruling planet for each day of the week"""
    day_lords = {
        0: 'Moon',      # Monday
        1: 'Mars',      # Tuesday
        2: 'Mercury',   # Wednesday
        3: 'Jupiter',   # Thursday
        4: 'Venus',     # Friday
        5: 'Saturn',    # Saturday
        6: 'Sun'        # Sunday
    }
    return day_lords.get(weekday, 'Sun')


def get_daily_predictions(birth_rashi, current_transits, nakshatra_lord, timezone='Asia/Kolkata'):
    """
    Generate daily predictions based on:
    - Day of the week and its ruling planet
    - Current moon position relative to birth rashi
    - Current transits affecting the birth chart
    """
    tz = pytz.timezone(timezone)
    today = datetime.now(tz)
    
    weekday = today.weekday()
    day_lord = get_weekday_lord(weekday)
    day_name = today.strftime('%A')
    date_str = today.strftime('%d %B %Y')
    
    # Get current moon position
    moon_transit = current_transits.get('Moon', {})
    moon_rashi = moon_transit.get('rashi', 'Unknown')
    moon_house = moon_transit.get('house', 0)
    
    # Calculate moon's relationship to birth rashi
    rashi_list = [
        'Mesha (Aries)', 'Vrishabha (Taurus)', 'Mithuna (Gemini)',
        'Karka (Cancer)', 'Simha (Leo)', 'Kanya (Virgo)',
        'Tula (Libra)', 'Vrishchika (Scorpio)', 'Dhanu (Sagittarius)',
        'Makara (Capricorn)', 'Kumbha (Aquarius)', 'Meena (Pisces)'
    ]
    
    try:
        birth_rashi_num = rashi_list.index(birth_rashi)
        moon_rashi_num = rashi_list.index(moon_rashi)
        moon_position = ((moon_rashi_num - birth_rashi_num) % 12) + 1
    except ValueError:
        moon_position = 1
    
    # Generate predictions
    predictions = {
        'date': date_str,
        'day': day_name,
        'dayLord': day_lord,
        'moonSign': moon_rashi,
        'moonHouse': moon_house,
        'summary': generate_daily_summary(day_lord, moon_position, nakshatra_lord),
        'dos': generate_daily_dos(day_lord, moon_position),
        'donts': generate_daily_donts(day_lord, moon_position),
        'luckyTime': get_lucky_time(day_lord),
        'luckyColor': get_lucky_color(day_lord),
        'luckyNumber': get_lucky_number(day_lord)
    }
    
    return predictions


def generate_daily_summary(day_lord, moon_position, nakshatra_lord):
    """Generate daily summary based on day lord and moon position"""
    
    # Moon position interpretations
    moon_effects = {
        1: "You may feel energetic and confident today.",
        2: "Focus on financial matters and family stability.",
        3: "Good day for communication and short travels.",
        4: "Emotional day, spend time with loved ones.",
        5: "Creative energy is high, express yourself.",
        6: "Health and work require attention today.",
        7: "Partnerships and relationships in focus.",
        8: "Deep transformation or unexpected changes possible.",
        9: "Spiritual growth and learning opportunities.",
        10: "Career and public recognition highlighted.",
        11: "Networking and social connections favored.",
        12: "Introspection and rest recommended."
    }
    
    base_summary = moon_effects.get(moon_position, "A balanced day ahead.")
    
    # Add day lord influence
    day_influences = {
        'Sun': "Leadership qualities shine today.",
        'Moon': "Emotions and intuition guide you.",
        'Mars': "Action and courage are your strengths.",
        'Mercury': "Communication and intellect are sharp.",
        'Jupiter': "Wisdom and expansion opportunities arise.",
        'Venus': "Love, beauty, and harmony surround you.",
        'Saturn': "Discipline and patience bring rewards."
    }
    
    day_influence = day_influences.get(day_lord, "")
    
    return f"{base_summary} {day_influence}"


def generate_daily_dos(day_lord, moon_position):
    """Generate daily do's based on planetary influences"""
    
    general_dos = {
        'Sun': [
            "Focus on important tasks and leadership roles",
            "Wear bright colors, especially gold or orange",
            "Practice meditation facing east in the morning"
        ],
        'Moon': [
            "Spend time near water or with family",
            "Eat cooling foods and stay hydrated",
            "Practice emotional self-care"
        ],
        'Mars': [
            "Exercise or engage in physical activities",
            "Take initiative on pending projects",
            "Channel energy into productive work"
        ],
        'Mercury': [
            "Write, communicate, and learn new things",
            "Focus on business and financial planning",
            "Network and build connections"
        ],
        'Jupiter': [
            "Study spiritual or philosophical topics",
            "Help others and practice generosity",
            "Make important decisions today"
        ],
        'Venus': [
            "Enjoy arts, music, and beauty",
            "Spend quality time in relationships",
            "Shop for luxury items or self-care"
        ],
        'Saturn': [
            "Work on long-term goals with patience",
            "Organize and structure your life",
            "Honor elders and traditions"
        ]
    }
    
    return general_dos.get(day_lord, [
        "Stay positive and focused",
        "Practice gratitude",
        "Take care of your health"
    ])


def generate_daily_donts(day_lord, moon_position):
    """Generate daily don'ts based on planetary influences"""
    
    general_donts = {
        'Sun': [
            "Avoid ego conflicts with authority figures",
            "Don't overwork or exhaust yourself",
            "Avoid starting new partnerships today"
        ],
        'Moon': [
            "Don't make emotional decisions hastily",
            "Avoid conflicts with mother or maternal figures",
            "Don't suppress your feelings"
        ],
        'Mars': [
            "Avoid arguments and aggressive behavior",
            "Don't rush into risky ventures",
            "Avoid sharp objects and accidents"
        ],
        'Mercury': [
            "Don't sign important documents without review",
            "Avoid gossip and miscommunication",
            "Don't overcommit to multiple tasks"
        ],
        'Jupiter': [
            "Avoid being overly optimistic or extravagant",
            "Don't ignore details in legal matters",
            "Avoid overindulgence in food"
        ],
        'Venus': [
            "Don't overspend on luxuries",
            "Avoid relationship conflicts",
            "Don't neglect responsibilities for pleasure"
        ],
        'Saturn': [
            "Avoid shortcuts or unethical means",
            "Don't ignore health issues",
            "Avoid laziness or procrastination"
        ]
    }
    
    return general_donts.get(day_lord, [
        "Avoid negative thinking",
        "Don't rush important decisions",
        "Avoid conflicts"
    ])


def get_lucky_time(day_lord):
    """Get auspicious time period for the day"""
    
    lucky_times = {
        'Sun': "6:00 AM - 7:30 AM",
        'Moon': "7:00 PM - 8:30 PM",
        'Mars': "6:00 AM - 7:30 AM (Tuesday)",
        'Mercury': "6:00 AM - 7:30 AM (Wednesday)",
        'Jupiter': "6:00 AM - 7:30 AM (Thursday)",
        'Venus': "7:00 AM - 8:30 AM (Friday)",
        'Saturn': "6:00 PM - 7:30 PM (Saturday)"
    }
    
    return lucky_times.get(day_lord, "Morning hours (6-8 AM)")


def get_lucky_color(day_lord):
    """Get lucky color for the day"""
    
    colors = {
        'Sun': "Gold, Orange, Red",
        'Moon': "White, Silver, Cream",
        'Mars': "Red, Orange, Maroon",
        'Mercury': "Green, Emerald",
        'Jupiter': "Yellow, Gold",
        'Venus': "White, Pink, Light Blue",
        'Saturn': "Blue, Black, Dark Green"
    }
    
    return colors.get(day_lord, "White")


def get_lucky_number(day_lord):
    """Get lucky number for the day"""
    
    numbers = {
        'Sun': [1, 10, 19],
        'Moon': [2, 11, 20],
        'Mars': [9, 18, 27],
        'Mercury': [5, 14, 23],
        'Jupiter': [3, 12, 21],
        'Venus': [6, 15, 24],
        'Saturn': [8, 17, 26]
    }
    
    return numbers.get(day_lord, [1, 5, 9])