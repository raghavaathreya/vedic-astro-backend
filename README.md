# Vedic Astrology Calculator - Python Backend

Astronomical calculation microservice for Vedic astrology using Swiss Ephemeris library.

## 🌟 Features

- **Precise Astronomical Calculations**: Using Swiss Ephemeris for accurate planetary positions
- **Vedic House System**: Whole Sign house system (traditional Vedic method)
- **Planetary Positions**: Sun, Moon, Mars, Mercury, Jupiter, Venus, Saturn, Rahu, Ketu
- **Nakshatra Determination**: 27 lunar mansions with pada (quarter) calculation
- **Rashi Analysis**: 12 zodiac signs with detailed interpretations
- **Dasha Calculations**: Vimshottari Mahadasha and Antardasha periods
- **Transit Analysis**: Current planetary positions and their effects
- **Daily Predictions**: Personalized guidance based on transits
- **Horoscope Summary**: Complete life analysis

## 🛠️ Tech Stack

- **Python 3.9+**
- **Flask** - Lightweight web framework
- **pyswisseph** - Swiss Ephemeris Python bindings
- **pytz** - Timezone handling
- **Flask-CORS** - Cross-origin resource sharing

## 📡 API Endpoints

### Calculate Kundli
```http
POST /calculate
Content-Type: application/json

{
  "year": 2000,
  "month": 5,
  "day": 13,
  "hour": 20,
  "minute": 30,
  "latitude": 12.9716,
  "longitude": 77.5946
}
```

**Response:**
```json
{
  "success": true,
  "rashi": "Kanya (Virgo)",
  "nakshatra": "Uttara Phalguni (Pada 3)",
  "lagna": "Vrishchika (Scorpio)",
  "ascendantDegree": 234.82,
  "planets": {
    "Sun": { "longitude": 52.4, "rashi": "Mesha (Aries)", "house": 6 },
    "Moon": { "longitude": 163.2, "rashi": "Kanya (Virgo)", "house": 11 },
    "Mars": { ... },
    ...
  },
  "nakshatraDetails": {
    "name": "Uttara Phalguni",
    "pada": 3,
    "rulingPlanet": "Sun",
    "deity": "Aryaman",
    ...
  },
  "rashiDetails": { ... },
  "currentTransits": { ... },
  "mahadashas": [ ... ],
  "currentDasha": { ... },
  "dailyPredictions": { ... },
  "horoscopeSummary": { ... }
}
```

### Health Check
```http
GET /health
```

**Response:**
```json
{
  "status": "running",
  "houseSystem": "Whole Sign (Vedic)"
}
```

## ⚙️ Environment Variables

```bash
PORT=5000  # Set automatically by Render
```

## 🚀 Local Development

### Prerequisites
- Python 3.9 or higher
- pip

### Setup

1. **Clone the repository**
```bash
git clone https://github.com/raghavaathreya/vedic-astro-backend.git
cd vedic-astro-backend
```

2. **Create virtual environment**
```bash
python -m venv venv

# On Linux/Mac:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Run the server**
```bash
python app.py
```

Server will start at `http://localhost:5000`

5. **Test the API**
```bash
curl -X POST http://localhost:5000/calculate \
  -H "Content-Type: application/json" \
  -d '{
    "year": 2000,
    "month": 5,
    "day": 13,
    "hour": 20,
    "minute": 30,
    "latitude": 12.9716,
    "longitude": 77.5946
  }'
```

## 🌐 Deployment

Deployed on **Render** with automatic deployments from GitHub.

**Production URL**: `https://vedic-astro-python.onrender.com`

### Deploy to Render
1. Connect GitHub repository
2. Build command: `pip install -r requirements.txt`
3. Start command: `python app.py`
4. Render auto-deploys on git push

**Note**: Free tier sleeps after 15 minutes of inactivity. First request after sleep takes ~30 seconds to wake up.

## 📁 Project Structure

```
vedic-astro-backend/
├── app.py                      # Main Flask application
├── vedic_data.py              # Nakshatra and Rashi reference data
├── transits.py                # Current planetary transit calculations
├── dasha.py                   # Vimshottari Dasha period calculations
├── daily_predictions.py       # Daily predictions based on transits
├── horoscope_summary.py       # Complete horoscope summary generator
├── requirements.txt           # Python dependencies
└── README.md
```

## 🔧 Key Modules

### `app.py`
Main Flask application with endpoints:
- `/calculate` - Birth chart calculation with all features
- `/health` - Service health check

### `vedic_data.py`
Comprehensive reference data:
- **27 Nakshatras**: Ruling planets, deities, qualities, symbols
- **12 Rashis**: Elements, ruling planets, characteristics, strengths/weaknesses

### `transits.py`
Current planetary positions and transit effects:
- Real-time planetary positions
- Transit house analysis
- Effect interpretations

### `dasha.py`
Vimshottari Dasha system calculations:
- Mahadasha (major periods) - 120-year cycle
- Antardasha (sub-periods)
- Balance of birth dasha
- Current dasha identification

### `daily_predictions.py`
Daily guidance generation:
- Current Moon position and house
- Planetary transit analysis
- Do's and don'ts
- Lucky colors, numbers, and times

### `horoscope_summary.py`
Comprehensive life analysis:
- Core personality traits
- Life areas focus
- Strengths and challenges
- Career predictions
- Relationship guidance
- Health recommendations
- Future outlook

## 📚 Astronomical Calculations

This service uses the **Swiss Ephemeris** library:
- **Precision**: High-accuracy planetary positions
- **Range**: Historical accuracy from 6000 BCE to 6000 CE
- **Professional Grade**: Used by astrologers worldwide
- **House System**: Whole Sign (traditional Vedic method)

### Vedic vs Western Astrology
- Uses **Sidereal Zodiac** (based on fixed stars)
- **Ayanamsa**: Lahiri ayanamsa for precession correction
- **Whole Sign Houses**: Each sign = one house (traditional Vedic)

## 🔗 Related Repository

- **Spring Boot Backend**: [vedic-astro-springboot](https://github.com/raghavaathreya/vedic-astro-springboot)

## 🌐 Live Demo

🔗 **Full Application**: [https://vedic-astro-app.netlify.app/]

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the MIT License.

## 👤 Author

**Raghav**
- GitHub: [@raghavaathreya](https://github.com/raghavaathreya)

## 🙏 Acknowledgments

- Swiss Ephemeris for astronomical calculations
- Flask framework
- pyswisseph Python bindings
- Render for free hosting
