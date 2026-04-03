# transits.py - Current Planetary Transits Calculator

import swisseph as swe
from datetime import datetime, timedelta
import pytz

# Vedic Astrology uses Lahiri Ayanamsa
swe.set_sid_mode(swe.SIDM_LAHIRI)

RASHIS = [
    'Mesha (Aries)', 'Vrishabha (Taurus)', 'Mithuna (Gemini)',
    'Karka (Cancer)', 'Simha (Leo)', 'Kanya (Virgo)',
    'Tula (Libra)', 'Vrishchika (Scorpio)', 'Dhanu (Sagittarius)',
    'Makara (Capricorn)', 'Kumbha (Aquarius)', 'Meena (Pisces)'
]

PLANETS = {
    'Sun': swe.SUN,
    'Moon': swe.MOON,
    'Mars': swe.MARS,
    'Mercury': swe.MERCURY,
    'Jupiter': swe.JUPITER,
    'Venus': swe.VENUS,
    'Saturn': swe.SATURN,
    'Rahu': swe.TRUE_NODE
}

# Average transit durations (approximate)
TRANSIT_DURATIONS = {
    'Sun': 30,      # 1 month per sign
    'Moon': 2.25,   # 2.25 days per sign
    'Mars': 45,     # 1.5 months per sign
    'Mercury': 25,  # ~25 days per sign (can vary due to retrogrades)
    'Venus': 25,    # ~25 days per sign
    'Jupiter': 365, # ~1 year per sign
    'Saturn': 912,  # ~2.5 years per sign
    'Rahu': -548    # ~1.5 years per sign (retrograde, so negative)
}


def get_julian_day(dt):
    """Convert datetime to Julian Day"""
    return swe.julday(dt.year, dt.month, dt.day, 
                     dt.hour + dt.minute/60.0 + dt.second/3600.0)


def get_sidereal_position(jd, planet_id):
    """Get sidereal (Vedic) position of a planet"""
    result = swe.calc_ut(jd, planet_id, swe.FLG_SIDEREAL)
    longitude = result[0][0]
    return longitude


def get_rashi(longitude):
    """Convert longitude to Rashi (sign)"""
    rashi_num = int(longitude / 30) % 12
    return RASHIS[rashi_num]


def get_rashi_number(longitude):
    """Get rashi number (0-11)"""
    return int(longitude / 30) % 12


def get_house_number_whole_sign(planet_longitude, ascendant_longitude):
    """Calculate house number using Whole Sign House system"""
    asc_rashi = get_rashi_number(ascendant_longitude)
    planet_rashi = get_rashi_number(planet_longitude)
    house = ((planet_rashi - asc_rashi) % 12) + 1
    return house


def find_sign_change_date(planet_id, current_jd, direction='forward'):
    """
    Find when a planet changes signs
    direction: 'forward' or 'backward'
    """
    current_pos = get_sidereal_position(current_jd, planet_id)
    current_sign = int(current_pos / 30)
    
    # Binary search for sign change
    if direction == 'forward':
        # Search up to 3 years ahead
        low_jd = current_jd
        high_jd = current_jd + (3 * 365)
        
        while high_jd - low_jd > 0.1:  # Within ~2.4 hours
            mid_jd = (low_jd + high_jd) / 2
            mid_pos = get_sidereal_position(mid_jd, planet_id)
            mid_sign = int(mid_pos / 30)
            
            if mid_sign == current_sign:
                low_jd = mid_jd
            else:
                high_jd = mid_jd
        
        return high_jd
    else:
        # Search up to 3 years backward
        low_jd = current_jd - (3 * 365)
        high_jd = current_jd
        
        while high_jd - low_jd > 0.1:
            mid_jd = (low_jd + high_jd) / 2
            mid_pos = get_sidereal_position(mid_jd, planet_id)
            mid_sign = int(mid_pos / 30)
            
            if mid_sign == current_sign:
                high_jd = mid_jd
            else:
                low_jd = mid_jd
        
        return low_jd


def jd_to_datetime(jd, timezone='Asia/Kolkata'):
    """Convert Julian Day to datetime with timezone"""
    year, month, day, hour = swe.revjul(jd)
    dt = datetime(year, month, day, int(hour), int((hour % 1) * 60))
    # Make it timezone-aware
    tz = pytz.timezone(timezone)
    dt_aware = tz.localize(dt)
    return dt_aware


def get_current_transits(birth_ascendant_longitude, timezone='Asia/Kolkata'):
    """
    Get current planetary transits with time periods
    """
    tz = pytz.timezone(timezone)
    now = datetime.now(tz)
    current_jd = get_julian_day(now)
    
    transits = {}
    
    for planet_name, planet_id in PLANETS.items():
        # Get current position
        current_longitude = get_sidereal_position(current_jd, planet_id)
        current_rashi = get_rashi(current_longitude)
        current_house = get_house_number_whole_sign(current_longitude, birth_ascendant_longitude)
        
     
# Find when planet entered current sign
        entry_jd = find_sign_change_date(planet_id, current_jd, 'backward')
        entry_date = jd_to_datetime(entry_jd, timezone)

            # Find when planet will exit current sign
        exit_jd = find_sign_change_date(planet_id, current_jd, 'forward')
        exit_date = jd_to_datetime(exit_jd, timezone)
        
        transits[planet_name] = {
            'longitude': round(current_longitude, 2),
            'rashi': current_rashi,
            'house': current_house,
            'enteredOn': entry_date.strftime('%d %B %Y'),
            'willExitOn': exit_date.strftime('%d %B %Y'),
            'daysInSign': (exit_date - entry_date).days,
            'daysRemaining': (exit_date - now).days
        }
    
    # Calculate Ketu (180° opposite Rahu)
    rahu_data = transits['Rahu']
    ketu_longitude = (rahu_data['longitude'] + 180) % 360
    ketu_rashi = get_rashi(ketu_longitude)
    ketu_house = get_house_number_whole_sign(ketu_longitude, birth_ascendant_longitude)
    
    transits['Ketu'] = {
        'longitude': round(ketu_longitude, 2),
        'rashi': ketu_rashi,
        'house': ketu_house,
        'enteredOn': rahu_data['enteredOn'],
        'willExitOn': rahu_data['willExitOn'],
        'daysInSign': rahu_data['daysInSign'],
        'daysRemaining': rahu_data['daysRemaining']
    }
    
    return transits


def get_transit_insights(transits, birth_rashi):
    """
    Generate insights based on current transits
    """
    insights = []
    
    # Jupiter transit
    jupiter = transits.get('Jupiter', {})
    insights.append({
        'planet': 'Jupiter',
        'message': f"Jupiter is transiting through {jupiter.get('rashi', 'Unknown')} in your {jupiter.get('house', 0)} house. "
                  f"This period favors growth, learning, and expansion in areas related to this house. "
                  f"It will remain here until {jupiter.get('willExitOn', 'Unknown')}."
    })
    
    # Saturn transit
    saturn = transits.get('Saturn', {})
    insights.append({
        'planet': 'Saturn',
        'message': f"Saturn is transiting through {saturn.get('rashi', 'Unknown')} in your {saturn.get('house', 0)} house. "
                  f"This is a time for discipline, hard work, and patience in matters of this house. "
                  f"Saturn will stay here until {saturn.get('willExitOn', 'Unknown')}."
    })
    
    # Rahu-Ketu transit
    rahu = transits.get('Rahu', {})
    ketu = transits.get('Ketu', {})
    insights.append({
        'planet': 'Rahu-Ketu',
        'message': f"Rahu is in your {rahu.get('house', 0)} house and Ketu in your {ketu.get('house', 0)} house. "
                  f"This axis indicates where you're experiencing growth (Rahu) and where you need to let go (Ketu). "
                  f"This transit continues until {rahu.get('willExitOn', 'Unknown')}."
    })
    
    return insights