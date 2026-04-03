# dasha.py - Vimshottari Dasha Calculator

from datetime import datetime, timedelta
import pytz

# Vimshottari Dasha System - 120 years total cycle
# Each planet rules for a specific number of years

DASHA_YEARS = {
    'Ketu': 7,
    'Venus': 20,
    'Sun': 6,
    'Moon': 10,
    'Mars': 7,
    'Rahu': 18,
    'Jupiter': 16,
    'Saturn': 19,
    'Mercury': 17
}

# Order of Mahadasha lords (starting from Ketu)
DASHA_ORDER = ['Ketu', 'Venus', 'Sun', 'Moon', 'Mars', 'Rahu', 'Jupiter', 'Saturn', 'Mercury']

# Nakshatra to starting Dasha lord mapping
NAKSHATRA_LORDS = {
    'Ashwini': 'Ketu',
    'Bharani': 'Venus',
    'Krittika': 'Sun',
    'Rohini': 'Moon',
    'Mrigashira': 'Mars',
    'Ardra': 'Rahu',
    'Punarvasu': 'Jupiter',
    'Pushya': 'Saturn',
    'Ashlesha': 'Mercury',
    'Magha': 'Ketu',
    'Purva Phalguni': 'Venus',
    'Uttara Phalguni': 'Sun',
    'Hasta': 'Moon',
    'Chitra': 'Mars',
    'Swati': 'Rahu',
    'Vishakha': 'Jupiter',
    'Anuradha': 'Saturn',
    'Jyeshtha': 'Mercury',
    'Mula': 'Ketu',
    'Purva Ashadha': 'Venus',
    'Uttara Ashadha': 'Sun',
    'Shravana': 'Moon',
    'Dhanishta': 'Mars',
    'Shatabhisha': 'Rahu',
    'Purva Bhadrapada': 'Jupiter',
    'Uttara Bhadrapada': 'Saturn',
    'Revati': 'Mercury'
}


def calculate_balance_of_dasha(moon_longitude):
    """
    Calculate how much of the birth nakshatra's dasha period is already completed
    Returns: (nakshatra_name, ruling_planet, balance_in_years)
    """
    # Each nakshatra = 13.333... degrees (360/27)
    nakshatra_span = 360 / 27
    
    # Find which nakshatra (0-26)
    nakshatra_num = int(moon_longitude / nakshatra_span)
    
    # Position within the nakshatra (0 to 13.333...)
    position_in_nakshatra = moon_longitude % nakshatra_span
    
    # Fraction of nakshatra completed
    fraction_completed = position_in_nakshatra / nakshatra_span
    
    # Get nakshatra name and lord
    nakshatras = list(NAKSHATRA_LORDS.keys())
    nakshatra_name = nakshatras[nakshatra_num]
    lord = NAKSHATRA_LORDS[nakshatra_name]
    
    # Total years for this lord's dasha
    total_years = DASHA_YEARS[lord]
    
    # Years already completed (not yet lived)
    years_completed = total_years * fraction_completed
    
    # Balance remaining to be lived at birth
    balance_years = total_years - years_completed
    
    return nakshatra_name, lord, balance_years


def calculate_mahadasha_periods(birth_date, moon_longitude, timezone='Asia/Kolkata'):
    """
    Calculate all Mahadasha periods from birth
    Returns list of dasha periods with start/end dates
    """
    tz = pytz.timezone(timezone)
    
    # If birth_date is string, convert to datetime
    if isinstance(birth_date, str):
        birth_date = datetime.strptime(birth_date, '%d/%m/%Y')
    
    # Make timezone-aware
    if birth_date.tzinfo is None:
        birth_date = tz.localize(birth_date)
    
    # Calculate balance of birth dasha
    nakshatra_name, first_lord, balance_years = calculate_balance_of_dasha(moon_longitude)
    
    # Find starting position in dasha order
    start_index = DASHA_ORDER.index(first_lord)
    
    dashas = []
    current_date = birth_date
    
    # First dasha (balance period)
    end_date = current_date + timedelta(days=balance_years * 365.25)
    dashas.append({
        'planet': first_lord,
        'startDate': current_date.strftime('%d %B %Y'),
        'endDate': end_date.strftime('%d %B %Y'),
        'years': round(balance_years, 2),
        'isBalance': True
    })
    current_date = end_date
    
    # Remaining dashas (full periods)
    for i in range(1, len(DASHA_ORDER)):
        lord_index = (start_index + i) % len(DASHA_ORDER)
        lord = DASHA_ORDER[lord_index]
        years = DASHA_YEARS[lord]
        
        end_date = current_date + timedelta(days=years * 365.25)
        dashas.append({
            'planet': lord,
            'startDate': current_date.strftime('%d %B %Y'),
            'endDate': end_date.strftime('%d %B %Y'),
            'years': years,
            'isBalance': False
        })
        current_date = end_date
        
        # Calculate for next 100 years only
        if (end_date - birth_date).days > (100 * 365.25):
            break
    
    return dashas


def get_current_dasha(dashas, current_date=None, timezone='Asia/Kolkata'):
    """
    Find which Mahadasha is currently active
    """
    if current_date is None:
        tz = pytz.timezone(timezone)
        current_date = datetime.now(tz)
    
    for dasha in dashas:
        start = datetime.strptime(dasha['startDate'], '%d %B %Y')
        end = datetime.strptime(dasha['endDate'], '%d %B %Y')
        
        # Make timezone-aware for comparison
        tz = pytz.timezone(timezone)
        start = tz.localize(start)
        end = tz.localize(end)
        
        if start <= current_date <= end:
            # Calculate days remaining
            days_remaining = (end - current_date).days
            years_remaining = round(days_remaining / 365.25, 2)
            
            return {
                **dasha,
                'daysRemaining': days_remaining,
                'yearsRemaining': years_remaining,
                'isCurrent': True
            }
    
    return None


def calculate_antardasha(mahadasha_lord, mahadasha_start, mahadasha_years, timezone='Asia/Kolkata'):
    """
    Calculate Antardasha (sub-periods) within a Mahadasha
    """
    tz = pytz.timezone(timezone)
    
    if isinstance(mahadasha_start, str):
        mahadasha_start = datetime.strptime(mahadasha_start, '%d %B %Y')
        mahadasha_start = tz.localize(mahadasha_start)
    
    # Find the starting position for this mahadasha lord
    start_index = DASHA_ORDER.index(mahadasha_lord)
    
    antardashas = []
    current_date = mahadasha_start
    
    for i in range(len(DASHA_ORDER)):
        lord_index = (start_index + i) % len(DASHA_ORDER)
        antara_lord = DASHA_ORDER[lord_index]
        
        # Antardasha duration = (Mahadasha years × Antardasha lord years) / 120
        years = (mahadasha_years * DASHA_YEARS[antara_lord]) / 120
        
        end_date = current_date + timedelta(days=years * 365.25)
        
        antardashas.append({
            'planet': antara_lord,
            'startDate': current_date.strftime('%d %B %Y'),
            'endDate': end_date.strftime('%d %B %Y'),
            'months': round(years * 12, 1)
        })
        
        current_date = end_date
    
    return antardashas


def get_dasha_interpretation(planet):
    """
    Get general interpretation for each Mahadasha period
    """
    interpretations = {
        'Sun': "Period of authority, leadership, and recognition. Focus on career growth and self-confidence.",
        'Moon': "Time for emotional growth, family matters, and intuition. Good for creative pursuits.",
        'Mars': "Action-oriented period. Focus on courage, competition, and physical activities. Handle aggression wisely.",
        'Mercury': "Excellent for learning, communication, business, and intellectual pursuits.",
        'Jupiter': "Expansion and growth in all areas. Good for education, spirituality, and financial gains.",
        'Venus': "Period of luxury, relationships, arts, and material comforts. Good for marriage.",
        'Saturn': "Time for discipline, hard work, and patience. Rewards come through persistent effort.",
        'Rahu': "Unconventional period with sudden changes. Focus on innovation and breaking patterns.",
        'Ketu': "Spiritual growth and detachment. Time for introspection and letting go of material attachments."
    }
    
    return interpretations.get(planet, "Period of growth and learning.")