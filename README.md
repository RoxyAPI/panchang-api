[![Panchang API](banner.png)](https://roxyapi.com/products/vedic-astrology-api)

# Panchang API

> Complete daily panchang with tithi, nakshatra, yoga, karana, rahu kaal, abhijit muhurta, and 15 auspicious windows. One key. Location-aware. Roxy Ephemeris verified against NASA JPL Horizons.

[![Get API Key](https://img.shields.io/badge/Get_API_Key-RoxyAPI-14b8a6?style=for-the-badge&logo=key&logoColor=white)](https://roxyapi.com/pricing)
[![Try Live](https://img.shields.io/badge/Try_API_Live-Free_in_browser-22c55e?style=for-the-badge&logo=swagger&logoColor=white)](https://roxyapi.com/api-reference)
[![Methodology](https://img.shields.io/badge/Methodology-NASA_JPL_verified-f59e0b?style=for-the-badge&logo=nasa&logoColor=white)](https://roxyapi.com/methodology)

[![MCP Server](https://img.shields.io/badge/MCP_Server-Streamable_HTTP-8b5cf6?style=for-the-badge&logo=anthropic&logoColor=white)](https://roxyapi.com/docs/mcp)
[![SDK](https://img.shields.io/badge/SDK-TypeScript_+_Python-3b82f6?style=for-the-badge&logo=npm&logoColor=white)](https://roxyapi.com/docs/sdk)

## What is Panchang API

The Panchang API returns a complete Hindu calendar (panchang) for any date and observer location. One call delivers all five limbs: Tithi (lunar day), Nakshatra (lunar mansion), Yoga, Karana, and Vara. It then adds sunrise, sunset, moonrise, moonset, Rahu Kaal, Yamaganda, Gulika Kaal, Abhijit Muhurta, Brahma Muhurta, Chandrabalam, Tarabalam, Varjyam, and Amrit Kalam. Powered by Roxy Ephemeris, verified against NASA JPL Horizons, and available through 10 spiritual domains in one subscription. The Remote MCP server at `https://roxyapi.com/mcp/vedic-astrology` makes the panchang API instantly usable in Claude, Cursor, or any MCP-compatible agent.

## Why this API

| Property | Value |
|----------|-------|
| Coverage | 10 spiritual domains in one subscription |
| Calculation | Roxy Ephemeris, verified against NASA JPL Horizons |
| MCP server | `https://roxyapi.com/mcp/vedic-astrology` (Streamable HTTP, no local setup) |
| SDKs | TypeScript on npm `@roxyapi/sdk`, Python on PyPI `roxy-sdk` |
| Pricing | One key, flat per call, $39 for 25K calls |
| Licensing | Personal and commercial use, including closed source apps. No AGPL or GPL entanglement. [Full terms](https://roxyapi.com/policy/license) |
| Last verified | 2026-Q2 |

## Quick start

1. Get a key at [roxyapi.com/pricing](https://roxyapi.com/pricing)
2. Pick a language below
3. Copy the snippet, run, ship

### cURL

```bash
# Step 1: geocode the city
curl -s "https://roxyapi.com/api/v2/location/search?q=New+Delhi" \
  -H "X-API-Key: $ROXY_API_KEY"

# Step 2: detailed panchang using coordinates from step 1
curl -X POST https://roxyapi.com/api/v2/vedic-astrology/panchang/detailed \
  -H "X-API-Key: $ROXY_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"date":"2026-05-03","latitude":28.6139,"longitude":77.209,"timezone":"Asia/Kolkata"}'
```

### Python

```python
import os
from roxy_sdk import create_roxy

roxy = create_roxy(os.environ["ROXY_API_KEY"])

# Step 1: geocode the city - never hardcode coordinates
loc = roxy.location.search_cities(q="New Delhi")
city = loc["cities"][0]
latitude, longitude, timezone = city["latitude"], city["longitude"], city["timezone"]

# Step 2: detailed panchang for that location
panchang = roxy.vedic_astrology.get_detailed_panchang(
    date="2026-05-03", latitude=latitude, longitude=longitude, timezone=timezone,
)
tithi = panchang["tithi"]
print(tithi["name"], tithi["paksha"], "paksha")
print("Rahu Kaal:", panchang["rahuKaal"]["start"], "to", panchang["rahuKaal"]["end"])
```

### JavaScript (Node)

```js
import { createRoxy } from '@roxyapi/sdk';

const roxy = createRoxy(process.env.ROXY_API_KEY);

// Step 1: geocode the city - never hardcode coordinates
const { data: loc } = await roxy.location.searchCities({ query: { q: 'New Delhi' } });
const { latitude, longitude, timezone } = loc.cities[0];

// Step 2: detailed panchang for that location
const { data } = await roxy.vedicAstrology.getDetailedPanchang({
  body: { date: '2026-05-03', latitude, longitude, timezone },
});
console.log(data.tithi.name, data.tithi.paksha, 'paksha');
console.log('Rahu Kaal:', data.rahuKaal.start, 'to', data.rahuKaal.end);
```

### TypeScript

```ts
import { createRoxy } from '@roxyapi/sdk';

const roxy = createRoxy(process.env.ROXY_API_KEY!);

// Step 1: geocode the city - never hardcode coordinates
const { data: loc } = await roxy.location.searchCities({ query: { q: 'New Delhi' } });
const { latitude, longitude, timezone } = loc!.cities[0];

// Step 2: detailed panchang for that location
const { data } = await roxy.vedicAstrology.getDetailedPanchang({
  body: { date: '2026-05-03', latitude, longitude, timezone },
});
console.log(data?.tithi.name, data?.tithi.paksha, 'paksha');
console.log('Rahu Kaal:', data?.rahuKaal.start, 'to', data?.rahuKaal.end);
```

## Request schema

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `date` | string | yes | Date in YYYY-MM-DD format. Panchang is calculated for this date. |
| `latitude` | number | yes | Observer latitude in decimal degrees (-90 to 90). Determines sunrise and sunset times which define day/night boundaries for muhurta calculations. |
| `longitude` | number | yes | Observer longitude in decimal degrees (-180 to 180). Affects local time calculations for sunrise, sunset, and muhurta period boundaries. |
| `timezone` | number | no | Timezone offset from UTC in decimal hours. Defaults to 5.5 (IST). Used for sunrise/sunset/moonrise/moonset search accuracy and output time formatting. |

## Response shape

```json
{
  "date": "2026-05-03",
  "vara": { "name": "Sunday", "lord": "Sun" },
  "sunrise": "2026-05-03T05:39:00",
  "sunset": "2026-05-03T18:57:00",
  "moonrise": "2026-05-03T20:15:00",
  "moonset": "2026-05-04T07:30:00",
  "tithi": {
    "number": 17,
    "name": "Dvitiya",
    "paksha": "Krishna",
    "percent": 18.38,
    "deity": "Brahma",
    "rulingPlanet": "Moon",
    "element": "Earth"
  },
  "nakshatra": {
    "number": 16,
    "name": "Vishakha",
    "lord": "Jupiter",
    "pada": 4,
    "deity": "Indra and Agni",
    "symbol": "Triumphal Arch"
  },
  "yoga": { "number": 18, "name": "Variyaana", "percent": 32.17 },
  "karana": { "number": 4, "name": "Taitil", "type": "char" },
  "rahuKaal": { "start": "2026-05-03T17:17:00", "end": "2026-05-03T18:57:00" },
  "abhijitMuhurta": { "start": "2026-05-03T11:51:00", "end": "2026-05-03T12:44:00" },
  "brahmaMuhurta": { "start": "2026-05-03T04:03:00", "end": "2026-05-03T04:51:00" },
  "chandrabalam": {
    "favorableRashis": ["Aries", "Gemini", "Virgo", "Scorpio", "Capricorn", "Aquarius"],
    "ashtamaChandraRashi": "Pisces"
  },
  "tarabalam": {
    "favorableNakshatras": ["Bharani", "Rohini", "Ardra", "Pushya"],
    "unfavorableNakshatras": ["Krittika", "Mrigashira"]
  }
}
```

| Field | Type | Description |
|-------|------|-------------|
| `date` | string | Date for which panchang is calculated. |
| `vara` | object | Hindu weekday (Vara) with name and ruling planet. Vara begins at local sunrise, not midnight. |
| `sunrise` | string | Local sunrise time. Marks the start of the Hindu day. |
| `sunset` | string | Local sunset time. Marks the transition to night muhurtas. |
| `moonrise` | string or null | Moonrise time in the requested timezone. Null if Moon does not rise on this date. |
| `moonset` | string or null | Moonset time in the requested timezone. Null if Moon does not set on this date. |
| `moonSign` | object | Moon rashi (sidereal zodiac sign) at sunrise with Sanskrit name. Determines Chandrabalam and Tarabalam. |
| `sunSign` | object | Sun rashi (sidereal zodiac sign) at sunrise with Sanskrit name. Determines the solar month (Saura Masa). |
| `sunNakshatra` | object | Nakshatra the Sun occupies: number, name, lord, pada. Sun spends ~13-14 days per nakshatra. |
| `tithi` | object | Lunar day (1-30). Includes name, paksha, percent elapsed, presiding deity, ruling planet, element. |
| `nakshatra` | object | Lunar mansion (1-27). Includes name, lord, pada (1-4), deity, symbol, characteristics. |
| `yoga` | object | Nitya Yoga (1-27) derived from combined Sun-Moon longitude. Includes name and characteristics. |
| `karana` | object | Half-tithi (changes twice per tithi). Includes name, type (Movable/Fixed), characteristics. |
| `hora` | object | Current planetary hora with ruling planet, sequence number, start and end times. |
| `rahuKaal` | object | Rahu Kaal start/end. Inauspicious period ruled by Rahu. Avoid starting new ventures. |
| `yamaganda` | object | Yamaganda start/end. Inauspicious period ruled by Yama. |
| `gulika` | object | Gulika Kaal start/end. Inauspicious period ruled by Saturn son Gulika. |
| `abhijitMuhurta` | object or null | Most auspicious ~48-minute window around solar noon. Null on Wednesdays per Muhurta Chintamani. |
| `brahmaMuhurta` | object | Sacred pre-dawn period ~96 minutes before sunrise. Best for meditation and spiritual sadhana. |
| `vijayaMuhurta` | object | Auspicious for journeys, legal proceedings, and competitions. |
| `nishitaMuhurta` | object | Sacred midnight period. Significant for Shivaratri and Janmashtami celebrations. |
| `godhuliMuhurta` | object or null | Universally auspicious 24-minute window around sunset. |
| `durMuhurta` | array | Inauspicious muhurta periods per weekday. Each period lasts ~48 minutes. |
| `varjyam` | array | Inauspicious ~96-minute nakshatra-based periods. Avoid auspicious ceremonies. |
| `amritKalam` | array | Most auspicious ~96-minute nakshatra-based periods for muhurta selection. |
| `chandrabalam` | object | Moon strength: favorable rashis and the Ashtama Chandra rashi. |
| `tarabalam` | object | Star strength via the 9-Tara system: favorable and unfavorable birth nakshatras. |
| `panchaka` | object | Active status and type when Moon transits nakshatras 23-27. |
| `bhadra` | object | Active status and timing for Vishti (Bhadra) karana. |
| `transitions` | object | Precise transition times for tithi, yoga, karana, nakshatra, and Moon sign. |

## Common use cases

| Use case | Endpoint flow |
|----------|---------------|
| Hindu calendar app | POST `/vedic-astrology/panchang/detailed` with date and user location. Display all five limbs. |
| Muhurta selection | Check `abhijitMuhurta`, `brahmaMuhurta`, `vijayaMuhurta`, `amritKalam`. Exclude `rahuKaal`, `yamaganda`, `durMuhurta`. |
| Daily astrology notification | Combine `tithi`, `nakshatra`, `vara` for a morning push notification. |
| Marriage and naming ceremonies | Check `chandrabalam`, `tarabalam`, `bhadra`, `panchaka` before selecting an auspicious time. |
| Electional astrology tools | Use `transitions` to determine precise panchang change boundaries to the minute. |
| Hindu festival dates | Feed daily tithi number into festival lookup (Purnima, Amavasya, Ekadashi) for dynamic calendar generation. |

## Related endpoints in this domain

- POST `/vedic-astrology/panchang/basic` (`getBasicPanchang`) for Tithi, Nakshatra, Yoga, Karana without time-based muhurtas
- POST `/vedic-astrology/panchang/choghadiya` (`getChoghadiya`) for 8-period day/night muhurta divisions
- POST `/vedic-astrology/panchang/hora` (`getHora`) for all 24 planetary hours with ruling planets

## Use this in your AI agent

Connect Claude, GPT, Gemini, or Cursor to RoxyAPI through the remote MCP server. No Docker. No self hosting. The full MCP tool catalog for this domain is at `https://roxyapi.com/mcp/vedic-astrology`.

```json
{
  "mcpServers": {
    "vedic-astrology": {
      "url": "https://roxyapi.com/mcp/vedic-astrology",
      "headers": { "X-API-Key": "$ROXY_API_KEY" }
    }
  }
}
```

See [docs/mcp](https://roxyapi.com/docs/mcp) for Claude Desktop, Cursor, Windsurf, VS Code, and Claude Code setup.

## For AI coding agents

This repo ships an [AGENTS.md](AGENTS.md) execution playbook. Cursor, Claude Code, Aider, Codex, Windsurf, RooCode, and Gemini CLI will pick it up automatically. Top level overview lives at [roxyapi.com/AGENTS.md](https://roxyapi.com/AGENTS.md).

## Resources

- [Methodology and gold standard tests](https://roxyapi.com/methodology) verified against NASA JPL Horizons
- [Full API reference](https://roxyapi.com/api-reference) interactive Scalar UI
- [TypeScript SDK on npm](https://www.npmjs.com/package/@roxyapi/sdk)
- [Python SDK on PyPI](https://pypi.org/project/roxy-sdk/)
- [llms.txt](https://roxyapi.com/llms.txt) full LLM citation index
- [Top level AGENTS.md](https://roxyapi.com/AGENTS.md)

## Other RoxyAPI samples

[![KP Astrology API](https://img.shields.io/badge/KP_Astrology_API-github-181717?style=flat-square&logo=github)](https://github.com/RoxyAPI/kp-astrology-api)
[![Kundli API](https://img.shields.io/badge/Kundli_API-github-181717?style=flat-square&logo=github)](https://github.com/RoxyAPI/kundli-api)
[![Dasha API](https://img.shields.io/badge/Dasha_API-github-181717?style=flat-square&logo=github)](https://github.com/RoxyAPI/dasha-api)

## License

MIT for this sample repo. See [LICENSE](LICENSE).

**Catalog licensing:** Personal and commercial use, including closed source proprietary apps. No AGPL or GPL entanglement. RoxyAPI APIs and SDKs are safe to embed in commercial products. Full terms at [roxyapi.com/policy/license](https://roxyapi.com/policy/license).

## Contact

- Site: [roxyapi.com](https://roxyapi.com)
- Status: [roxyapi.com/api-reference](https://roxyapi.com/api-reference)
