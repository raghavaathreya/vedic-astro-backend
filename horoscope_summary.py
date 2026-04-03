# horoscope_summary.py - Complete Horoscope Summary Generator

def generate_horoscope_summary(
    rashi, nakshatra, lagna, 
    nakshatra_lord, rashi_lord, 
    planets, current_dasha,
    rashi_details, nakshatra_details
):
    """
    Generate a comprehensive horoscope summary
    """
    
    summary = {
        'overview': generate_overview(rashi, nakshatra, lagna),
        'corePersonality': generate_personality_analysis(
            rashi_details, nakshatra_details, nakshatra_lord
        ),
        'lifeAreas': generate_life_areas_analysis(planets),
        'strengths': rashi_details.get('strengths', []),
        'challenges': rashi_details.get('weaknesses', []),
        'careerPredictions': generate_career_predictions(
            nakshatra_lord, rashi_lord, planets
        ),
        'relationshipPredictions': generate_relationship_predictions(
            rashi, planets
        ),
        'healthGuidance': generate_health_guidance(rashi_details),
        'currentPhase': generate_current_phase(current_dasha),
        'futureOutlook': generate_future_outlook(current_dasha, nakshatra_lord),
        'recommendations': generate_life_recommendations(
            nakshatra_lord, rashi_lord, rashi_details
        )
    }
    
    return summary


def generate_overview(rashi, nakshatra, lagna):
    """Generate basic overview"""
    return (
        f"Born under {rashi} with {nakshatra} Nakshatra and {lagna} Ascendant, "
        f"your chart reveals a unique blend of emotional depth, destiny patterns, "
        f"and life direction. This combination shapes your personality, life path, "
        f"and the lessons you're meant to learn in this lifetime."
    )


def generate_personality_analysis(rashi_details, nakshatra_details, nakshatra_lord):
    """Analyze core personality"""
    
    element = rashi_details.get('element', 'Unknown')
    quality = rashi_details.get('quality', 'Unknown')
    nakshatra_quality = nakshatra_details.get('quality', 'Unknown')
    
    return (
        f"Your core nature is influenced by the {element} element, making you {quality} "
        f"in your approach to life. The {nakshatra_lord} ruling your Nakshatra adds "
        f"qualities of {nakshatra_quality}. This creates a personality that is both "
        f"emotionally intuitive and action-oriented in pursuing life goals."
    )


def generate_life_areas_analysis(planets):
    """Analyze different life areas based on planetary positions"""
    
    areas = {}
    
    # Career (10th house planets)
    career_planets = [p for p, d in planets.items() if d['house'] == 10]
    if career_planets:
        areas['career'] = f"Strong focus on career with {', '.join(career_planets)} in 10th house. Success through hard work and recognition."
    else:
        areas['career'] = "Career growth through consistent effort and skill development."
    
    # Relationships (7th house planets)
    relationship_planets = [p for p, d in planets.items() if d['house'] == 7]
    if relationship_planets:
        areas['relationships'] = f"Relationships are significant with {', '.join(relationship_planets)} in 7th house."
    else:
        areas['relationships'] = "Balanced approach to partnerships and relationships."
    
    # Wealth (2nd and 11th house)
    wealth_planets = [p for p, d in planets.items() if d['house'] in [2, 11]]
    if wealth_planets:
        areas['wealth'] = f"Financial opportunities through {', '.join(wealth_planets)} placement."
    else:
        areas['wealth'] = "Steady financial growth through savings and planning."
    
    return areas


def generate_career_predictions(nakshatra_lord, rashi_lord, planets):
    """Generate career predictions"""
    
    career_fields = {
        'Sun': "Leadership, government, administration, entrepreneurship",
        'Moon': "Hospitality, healthcare, counseling, creative arts",
        'Mars': "Engineering, military, sports, surgery, real estate",
        'Mercury': "Business, communication, writing, technology, teaching",
        'Jupiter': "Education, law, spirituality, consultancy, finance",
        'Venus': "Arts, entertainment, luxury goods, fashion, design",
        'Saturn': "Construction, mining, labor, administration, elderly care"
    }
    
    primary_field = career_fields.get(nakshatra_lord, "Multiple fields based on skills")
    
    return {
        'suitableFields': primary_field,
        'prediction': (
            f"Your {nakshatra_lord} Nakshatra lord indicates natural affinity for {primary_field}. "
            f"Success comes through leveraging your unique skills and consistent effort."
        )
    }


def generate_relationship_predictions(rashi, planets):
    """Generate relationship predictions"""
    
    venus_house = planets.get('Venus', {}).get('house', 0)
    
    if venus_house == 7:
        return "Strong potential for harmonious partnerships. Marriage brings happiness and growth."
    elif venus_house == 1:
        return "Charismatic personality attracts good relationships. Focus on balance in partnerships."
    elif venus_house in [4, 10]:
        return "Relationships blend with family or career. Partner may be from professional circles."
    else:
        return "Relationships develop naturally. Focus on communication and mutual understanding."


def generate_health_guidance(rashi_details):
    """Generate health guidance based on rashi"""
    
    body_part = rashi_details.get('bodyPart', 'overall health')
    
    return (
        f"Pay special attention to {body_part}. Regular exercise, balanced diet, "
        f"and stress management are key to maintaining good health. "
        f"Preventive care is better than cure."
    )


def generate_current_phase(current_dasha):
    """Analyze current dasha phase"""
    
    if not current_dasha:
        return "Currently in a transitional phase. Focus on building foundations."
    
    planet = current_dasha.get('planet', 'Unknown')
    years_remaining = current_dasha.get('yearsRemaining', 0)
    
    return (
        f"Currently in {planet} Mahadasha with {years_remaining} years remaining. "
        f"This period shapes your experiences and opportunities significantly."
    )


def generate_future_outlook(current_dasha, nakshatra_lord):
    """Generate future predictions"""
    
    return (
        f"The coming years under your current planetary period will bring opportunities "
        f"aligned with {nakshatra_lord}'s energy. Focus on long-term goals, maintain discipline, "
        f"and stay open to learning. Major life changes are possible in the next 2-3 years."
    )


def generate_life_recommendations(nakshatra_lord, rashi_lord, rashi_details):
    """Generate personalized life recommendations"""
    
    recommendations = []
    
    # Based on nakshatra lord
    nakshatra_advice = {
        'Sun': "Develop leadership skills and confidence. Take responsibility.",
        'Moon': "Practice emotional intelligence and intuition. Care for mental health.",
        'Mars': "Channel energy productively. Learn patience with aggression.",
        'Mercury': "Enhance communication skills. Focus on continuous learning.",
        'Jupiter': "Expand knowledge and wisdom. Practice generosity.",
        'Venus': "Cultivate relationships and artistic expression. Seek balance.",
        'Saturn': "Build discipline and long-term planning. Honor commitments."
    }
    
    recommendations.append(nakshatra_advice.get(nakshatra_lord, "Stay focused on growth."))
    
    # Based on rashi element
    element = rashi_details.get('element', '')
    if element == 'Fire':
        recommendations.append("Channel your passionate energy into productive goals.")
    elif element == 'Earth':
        recommendations.append("Build practical foundations for long-term success.")
    elif element == 'Air':
        recommendations.append("Use your communication skills to build connections.")
    elif element == 'Water':
        recommendations.append("Trust your intuition while staying grounded.")
    
    # General advice
    recommendations.append("Practice daily meditation or mindfulness for mental clarity.")
    recommendations.append("Maintain work-life balance for overall wellbeing.")
    recommendations.append("Build strong relationships with family and mentors.")
    
    return recommendations