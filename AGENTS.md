# AGENTS.md for Panchang API

This repo teaches AI coding agents (Cursor, Claude Code, Aider, Codex, Windsurf, RooCode, Gemini CLI) how to use the RoxyAPI Detailed Panchang endpoint.

## Endpoint
- Method: `POST`
- URL: `https://roxyapi.com/api/v2/vedic-astrology/panchang/detailed`
- Auth: `X-API-Key` header
- Domain: `vedic-astrology` (one of 12 in the RoxyAPI catalog)
- Operation ID: `getDetailedPanchang` matches the SDK method name in camelCase
- MCP tool: `post_vedic_astrology_panchang_detailed` on `https://roxyapi.com/mcp/vedic-astrology`

## TypeScript SDK
```ts
import { createRoxy } from '@roxyapi/sdk';
const roxy = createRoxy(process.env.ROXY_API_KEY!);
const { data, error } = await roxy.vedicAstrology.getDetailedPanchang({
  body: { date: '2026-05-03', latitude: 28.6139, longitude: 77.209, timezone: 5.5 },
});
```

## Python SDK
```python
import os
from roxy_sdk import create_roxy
roxy = create_roxy(os.environ["ROXY_API_KEY"])
result = roxy.vedic_astrology.get_detailed_panchang(
    date="2026-05-03", latitude=28.6139, longitude=77.209, timezone=5.5
)
```

## Setup step (only when the endpoint requires coordinates)
Always call `GET /location/search?q={city}` first. Take `latitude`, `longitude`, `timezone` from `cities[0]` and pipe them in. Never ask the user to type coordinates.

## Request fields
- `date` (string, required): Date in YYYY-MM-DD format.
- `latitude` (number, required): Observer latitude in decimal degrees (-90 to 90). Determines sunrise/sunset times.
- `longitude` (number, required): Observer longitude in decimal degrees (-180 to 180). Affects muhurta period boundaries.
- `timezone` (number, optional, default 5.5): UTC offset in decimal hours. Pass the city utcOffset from the location endpoint for correctness outside IST.

## Response top level keys
`date`, `location`, `vara`, `sunrise`, `sunset`, `moonrise`, `moonset`, `moonSign`, `sunSign`, `sunNakshatra`, `tithi`, `nakshatra`, `yoga`, `karana`, `hora`, `rahuKaal`, `yamaganda`, `gulika`, `abhijitMuhurta`, `brahmaMuhurta`, `vijayaMuhurta`, `nishitaMuhurta`, `godhuliMuhurta`, `pratahSandhya`, `sayahnaSandhya`, `durMuhurta`, `varjyam`, `amritKalam`, `chandrabalam`, `tarabalam`, `panchaka`, `bhadra`, `transitions`

## Domain rules
- `vara` starts at local sunrise, not midnight. Pass the correct timezone offset so the weekday is determined from the correct local sunrise.
- `abhijitMuhurta` is null on Wednesdays (coincides with Dur Muhurta on that weekday per Muhurta Chintamani).
- `moonrise` and `moonset` can be null in polar regions.
- `godhuliMuhurta` is null only in polar regions where the Sun does not set.
- `tithi.number` 1-15 is Shukla Paksha (waxing), 16-30 is Krishna Paksha (waning). Purnima is 15, Amavasya is 30.
- `nakshatra.pada` is 1-4, each spanning 3 degrees 20 minutes. Useful for navamsha calculations.
- `chandrabalam.ashtamaChandraRashi` is the most inauspicious Moon position. Natives of this rashi should avoid important activities.
- All time strings are ISO 8601 in the requested timezone offset. For display, convert using the timezone value in `location.timezone`.
- `panchaka.type` is one of: Mrityu, Agni, Raja, Chora, Roga. Null when Panchaka is not active.
- `transitions` gives precise binary-search-level (~1 minute) timing for when each element changes. Use `transitions.tithi.endsAt` to know when the current tithi ends.
- All calculations are based on the sidereal zodiac (Lahiri ayanamsha), not the tropical zodiac.

## Related endpoints
- POST `/vedic-astrology/panchang/basic` (`getBasicPanchang`): Tithi, Nakshatra, Yoga, Karana without muhurtas.
- POST `/vedic-astrology/panchang/choghadiya` (`getChoghadiya`): 8 daytime and 8 nighttime muhurta periods.
- POST `/vedic-astrology/panchang/hora` (`getHora`): All 24 planetary hora periods.

## Verified
2026-Q2 against `https://roxyapi.com/api/v2/openapi.json`. Re-fetch the spec for ground truth before changing this file.

## Discovery
- Full catalog: https://roxyapi.com/AGENTS.md
- LLM index: https://roxyapi.com/llms.txt
- Methodology: https://roxyapi.com/methodology
