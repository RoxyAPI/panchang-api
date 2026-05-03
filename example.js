/**
 * Panchang API example (JavaScript/Node)
 * Tithi, nakshatra, yoga, karana, rahu kaal, abhijit muhurta in one call.
 * Docs: https://roxyapi.com/api-reference
 */

import { createRoxy } from '@roxyapi/sdk';

const roxy = createRoxy(process.env.ROXY_API_KEY);

// Always geocode first. Example: roxy.location.searchCities({ query: { q: 'New Delhi' } })
const { data, error } = await roxy.vedicAstrology.getDetailedPanchang({
  body: {
    date: '2026-05-03',
    latitude: 28.6139,   // New Delhi
    longitude: 77.209,
    timezone: 5.5,       // IST
  },
});

if (error) {
  console.error('Error:', error);
  process.exit(1);
}

console.log('Date:', data.date);
console.log('Vara:', data.vara.name, '(lord:', data.vara.lord + ')');
console.log('Tithi:', data.tithi.number, data.tithi.name, data.tithi.paksha, 'paksha');
console.log('Nakshatra:', data.nakshatra.name, 'pada', data.nakshatra.pada, '(lord:', data.nakshatra.lord + ')');
console.log('Yoga:', data.yoga.name);
console.log('Karana:', data.karana.name);
console.log('Sunrise:', data.sunrise);
console.log('Sunset:', data.sunset);
console.log('Rahu Kaal:', data.rahuKaal.start, 'to', data.rahuKaal.end);
console.log('Abhijit Muhurta:', data.abhijitMuhurta ? `${data.abhijitMuhurta.start} to ${data.abhijitMuhurta.end}` : 'null (Wednesday)');
console.log('Chandrabalam favorable rashis:', data.chandrabalam.favorableRashis.join(', '));
