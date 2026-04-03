from flask import Flask, request, jsonify
from flask_cors import CORS
import swisseph as swe
from datetime import datetime
import pytz
from vedic_data import get_nakshatra_info, get_rashi_info
from transits import get_current_transits, get_transit_insights
from dasha import calculate_mahadasha_periods, get_current_dasha, calculate_antardasha, get_dasha_interpretation
from daily_predictions import get_daily_predictions
from horoscope_summary import generate_horoscope_summary
import os

app = Flask(__name__)
CORS(app)

# Vedic Astrology uses Lahiri Ayanamsa (sidereal zodiac)
swe.set_sid_mode(swe.SIDM_LAHIRI)

# Rashi names (12 zodiac signs in Vedic astrology)
RASHIS = [
    'Mesha (Aries)', 'Vrishabha (Taurus)', 'Mithuna (Gemini)',
    'Karka (Cancer)', 'Simha (Leo)', 'Kanya (Virgo)',
    'Tula (Libra)', 'Vrishchika (Scorpio)', 'Dhanu (Sagittarius)',
    'Makara (Capricorn)', 'Kumbha (Aquarius)', 'Meena (Pisces)'
]

# Nakshatra names (27 lunar mansions)
NAKSHATRAS = [
    'Ashwini', 'Bharani', 'Krittika', 'Rohini', 'Mrigashira', 'Ardra',
    'Punarvasu', 'Pushya', 'Ashlesha', 'Magha', 'Purva Phalguni',
    'Uttara Phalguni', 'Hasta', 'Chitra', 'Swati', 'Vishakha',
    'Anuradha', 'Jyeshtha', 'Mula', 'Purva Ashadha', 'Uttara Ashadha',
    'Shravana', 'Dhanishta', 'Shatabhisha', 'Purva Bhadrapada',
    'Uttara Bhadrapada', 'Revati'
]

# Planet IDs for Swiss Ephemeris
PLANETS = {
    'Sun': swe.SUN,
    'Moon': swe.MOON,
    'Mars': swe.MARS,
    'Mercury': swe.MERCURY,
    'Jupiter': swe.JUPITER,
    'Venus': swe.VENUS,
    'Saturn': swe.SATURN,
    'Rahu': swe.TRUE_NODE,
    'Ketu': None
}


def convert_to_utc(year, month, day, hour, minute, timezone_str='Asia/Kolkata'):
    """Convert local time to UTC"""
    tz = pytz.timezone(timezone_str)
    local_time = tz.localize(datetime(year, month, day, hour, minute))
    utc_time = local_time.astimezone(pytz.UTC)
    
    return (utc_time.year, utc_time.month, utc_time.day, 
            utc_time.hour, utc_time.minute + utc_time.second/60.0)


def get_julian_day(year, month, day, hour_decimal):
    """Convert date/time to Julian Day"""
    jd = swe.julday(year, month, day, hour_decimal)
    return jd


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


def get_nakshatra(longitude):
    """Convert longitude to Nakshatra"""
    nakshatra_num = int(longitude / 13.333333) % 27
    pada = int((longitude % 13.333333) / 3.333333) + 1
    return NAKSHATRAS[nakshatra_num], pada


def calculate_ascendant(jd, latitude, longitude):
    """Calculate Lagna (Ascendant) using proper house calculation"""
    # Calculate houses using Placidus system
    cusps, ascmc = swe.houses(jd, latitude, longitude, b'P')
    
    # Ascendant is ascmc[0]
    asc_longitude = ascmc[0]
    
    # Apply ayanamsa to get sidereal position
    ayanamsa = swe.get_ayanamsa_ut(jd)
    asc_sidereal = (asc_longitude - ayanamsa) % 360
    
    return asc_sidereal


def get_house_number_whole_sign(planet_longitude, ascendant_longitude):
    """
    Calculate house number using Whole Sign House system (Vedic standard)
    
    In Whole Sign:
    - Each house = one complete sign (30 degrees)
    - House 1 starts at the sign where Ascendant is located
    - House 2 is the next sign, etc.
    """
    # Get the rashi (sign) of the ascendant
    asc_rashi = get_rashi_number(ascendant_longitude)
    
    # Get the rashi (sign) of the planet
    planet_rashi = get_rashi_number(planet_longitude)
    
    # Calculate house number (1-12)
    # House 1 = rashi where ascendant is
    # House 2 = next rashi, etc.
    house = ((planet_rashi - asc_rashi) % 12) + 1
    
    return house


def get_planet_positions(jd, ascendant_longitude):
    """Get all planet positions with Whole Sign house assignments"""
    positions = {}
    
    for planet_name, planet_id in PLANETS.items():
        if planet_name == 'Ketu':
            # Ketu is 180° opposite Rahu
            rahu_pos = positions['Rahu']['longitude']
            ketu_pos = (rahu_pos + 180) % 360
            positions['Ketu'] = {
                'longitude': ketu_pos,
                'rashi': get_rashi(ketu_pos),
                'house': get_house_number_whole_sign(ketu_pos, ascendant_longitude)
            }
        else:
            longitude = get_sidereal_position(jd, planet_id)
            positions[planet_name] = {
                'longitude': longitude,
                'rashi': get_rashi(longitude),
                'house': get_house_number_whole_sign(longitude, ascendant_longitude)
            }
    
    return positions


@app.route('/calculate', methods=['POST'])
def calculate_kundli():
    """
    Main endpoint to calculate Kundli using Whole Sign Houses (Vedic standard)
    """
    try:
        data = request.json
        
        # Extract birth details
        year = data['year']
        month = data['month']
        day = data['day']
        hour = data['hour']
        minute = data['minute']
        latitude = data['latitude']
        longitude = data['longitude']
        timezone = data.get('timezone', 'Asia/Kolkata')
        
        print(f"\n{'='*60}")
        print(f"CALCULATING KUNDLI")
        print(f"{'='*60}")
        print(f"Birth: {year}-{month:02d}-{day:02d} {hour:02d}:{minute:02d}")
        print(f"Place: {latitude}, {longitude}")
        print(f"Timezone: {timezone}")
        
        # Convert to UTC
        utc_year, utc_month, utc_day, utc_hour, utc_minute = convert_to_utc(
            year, month, day, hour, minute, timezone
        )
        
        # Calculate Julian Day
        jd = get_julian_day(utc_year, utc_month, utc_day, utc_hour + utc_minute/60.0)
        
        print(f"\nJulian Day: {jd}")
        
        # Get Moon position (for Rashi)
        moon_longitude = get_sidereal_position(jd, swe.MOON)
        rashi = get_rashi(moon_longitude)
        nakshatra, pada = get_nakshatra(moon_longitude)
        
        print(f"\nMoon: {moon_longitude:.2f}° -> {rashi}, {nakshatra} (Pada {pada})")
        
        # Calculate Ascendant (Lagna)
        asc_longitude = calculate_ascendant(jd, latitude, longitude)
        lagna = get_rashi(asc_longitude)
        
        print(f"Ascendant: {asc_longitude:.2f}° -> {lagna}")
        print(f"\nUsing WHOLE SIGN HOUSES (Vedic standard)")
        print(f"House 1 starts at: {lagna}")
        
        # Get all planet positions with Whole Sign house assignments
        planet_positions = get_planet_positions(jd, asc_longitude)
        
        # Print planet positions for debugging
        print(f"\n{'Planet':<10} {'Longitude':<12} {'Rashi':<20} {'House'}")
        print(f"{'-'*60}")
        for planet, data in sorted(planet_positions.items(), key=lambda x: x[1]['house']):
            print(f"{planet:<10} {data['longitude']:>8.2f}° {data['rashi']:<20} House {data['house']}")
        
        print(f"{'='*60}\n")
        
        # Get extended nakshatra and rashi information
        nakshatra_info = get_nakshatra_info(nakshatra)
        rashi_info = get_rashi_info(rashi)

        # Prepare response
        result = {
            'success': True,
            'birthDetails': {
                'date': f'{day}/{month}/{year}',
                'time': f'{hour:02d}:{minute:02d}',
                'latitude': latitude,
                'longitude': longitude,
                'timezone': timezone
            },
            'rashi': rashi,
            'nakshatra': f'{nakshatra} (Pada {pada})',
            'lagna': lagna,
            'planets': planet_positions,
            'ascendantDegree': round(asc_longitude, 2),
            'houseSystem': 'Whole Sign (Vedic)',
            
            # Extended nakshatra details
            'nakshatraDetails': {
                'name': nakshatra,
                'pada': pada,
                'rulingPlanet': nakshatra_info.get('lord', 'Unknown'),
                'deity': nakshatra_info.get('deity', 'Unknown'),
                'symbol': nakshatra_info.get('symbol', 'Unknown'),
                'quality': nakshatra_info.get('quality', 'Unknown'),
                'luckyNumber': nakshatra_info.get('lucky_number', []),
                'luckyColor': nakshatra_info.get('lucky_color', []),
                'luckyDay': nakshatra_info.get('lucky_day', 'Unknown'),
                'luckyGem': nakshatra_info.get('lucky_gem', 'Unknown'),
                'metal': nakshatra_info.get('metal', 'Unknown')
            },
            
            # Extended rashi details
            'rashiDetails': {
                'name': rashi,
                'element': rashi_info.get('element', 'Unknown'),
                'quality': rashi_info.get('quality', 'Unknown'),
                'rulingPlanet': rashi_info.get('lord', 'Unknown'),
                'nature': rashi_info.get('nature', 'Unknown'),
                'luckyNumber': rashi_info.get('lucky_number', []),
                'luckyColor': rashi_info.get('lucky_color', []),
                'luckyDay': rashi_info.get('lucky_day', 'Unknown'),
                'luckyGem': rashi_info.get('lucky_gem', 'Unknown'),
                'metal': rashi_info.get('metal', 'Unknown'),
                'bodyPart': rashi_info.get('body_part', 'Unknown'),
                'strengths': rashi_info.get('strengths', []),
                'weaknesses': rashi_info.get('weaknesses', [])
            }
        }

        print(f"\n>>> SENDING ascendantDegree: {result['ascendantDegree']}")
        print(f">>> Full result keys: {list(result.keys())}\n") 
        # Get current transits
        current_transits = get_current_transits(asc_longitude, timezone)
        transit_insights = get_transit_insights(current_transits, rashi)

        result['currentTransits'] = current_transits
        result['transitInsights'] = transit_insights

                # Calculate Vimshottari Dasha
        birth_date_str = f"{day}/{month}/{year}"
        mahadashas = calculate_mahadasha_periods(birth_date_str, moon_longitude, timezone)
        current_dasha = get_current_dasha(mahadashas, timezone=timezone)

        # Add interpretation to current dasha
        if current_dasha:
            current_dasha['interpretation'] = get_dasha_interpretation(current_dasha['planet'])
            
            # Calculate Antardashas for current Mahadasha
            antardashas = calculate_antardasha(
                current_dasha['planet'],
                current_dasha['startDate'],
                current_dasha['years'],
                timezone
            )
            current_dasha['antardashas'] = antardashas

        result['mahadashas'] = mahadashas
        result['currentDasha'] = current_dasha

                # Generate daily predictions
        daily_predictions = get_daily_predictions(
            rashi, 
            current_transits, 
            nakshatra_info.get('lord', 'Unknown'),
            timezone
        )

        # Generate complete horoscope summary
        horoscope_summary = generate_horoscope_summary(
            rashi=rashi,
            nakshatra=nakshatra,
            lagna=lagna,
            nakshatra_lord=nakshatra_info.get('lord', 'Unknown'),
            rashi_lord=rashi_info.get('lord', 'Unknown'),
            planets=planet_positions,
            current_dasha=current_dasha,
            rashi_details=rashi_info,
            nakshatra_details=nakshatra_info
        )

        result['dailyPredictions'] = daily_predictions
        result['horoscopeSummary'] = horoscope_summary

        return jsonify(result), 200
        
    except Exception as e:
        print(f"\nERROR: {str(e)}")
        import traceback
        traceback.print_exc()
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400


@app.route('/health', methods=['GET'])
def health_check():
    """Simple health check endpoint"""
    return jsonify({'status': 'running', 'houseSystem': 'Whole Sign (Vedic)'}), 200


if __name__ == '__main__':
    print("\n" + "="*60)
    print("VEDIC ASTROLOGY CALCULATOR")
    print("Using Whole Sign House System (Vedic Standard)")
    print("="*60 + "\n")
    app.run(host='0.0.0.0', port=5000, debug=True)
    if __name__ == '__main__':
        port = int(os.environ.get('PORT', 5000))
        print("\n" + "="*60)
        print("VEDIC ASTROLOGY CALCULATOR")
        print("Using Whole Sign House System (Vedic Standard)")
        print(f"Running on port {port}")
        print("="*60 + "\n")
        app.run(host='0.0.0.0', port=port, debug=False)