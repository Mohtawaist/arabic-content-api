# Arabic Content Intelligence API

**One call scores your Arabic article:** quality grade · keyword density · readability · heading structure.
Built for agencies, bloggers and content pipelines that publish Arabic daily.

> أدوات SEO العالمية لا تفهم العربية. هذا الـAPI يقيسها: درجة جودة، كثافة الكلمة، سهولة القراءة، بنية العناوين.

## Quick start

```bash
curl -X POST https://mohtawaist.com/api/v1/analyze \
  -H "Content-Type: application/json" \
  -H "X-API-Key: mw_live_xxxxxxxx" \
  -d '{"text":"نص مقالك العربي هنا...","keyword":"المحتوى"}'
```

```json
{
  "ok": true,
  "score": 78,
  "grade": "جيد",
  "keyword_density": 1.4,
  "readability": 62,
  "headings": {"h2": 6, "h3": 9},
  "quota": {"limit": 5000, "remaining": 4999}
}
```

### Python
```python
from mohtawaist import Client
r = Client("mw_live_xxx").analyze("نص عربي...", keyword="المحتوى")
```

### Node
```js
const mw = require('./client')('mw_live_xxx');
const r = await mw.analyze({ text: 'نص عربي...', keyword: 'المحتوى' });
```

## Endpoints
| Method | Path | Purpose |
|---|---|---|
| POST | `/api/v1/analyze` | تحليل شامل (درجة/كثافة/قراءة/عناوين) |
| POST | `/api/v1/slug` | توليد slug عربي نظيف |
| POST | `/api/v1/keywords` | استخراج أهم الكلمات |
| POST | `/api/v1/readability` | سهولة القراءة |
| GET | `/api/v1/health` | فحص حيّ |

## Pricing
| Plan | Calls/day | Price |
|---|---|---|
| BASIC | 500 | **Free** — [احصل على مفتاح](https://mohtawaist.com/api/free-key?utm_source=github) |
| PRO | 5,000 | $9.99/mo |
| ULTRA | 50,000 | $29.99/mo |
| MEGA | 500,000 | $79.99/mo |

Docs: https://mohtawaist.com/developers/?utm_source=github · OpenAPI: https://mohtawaist.com/openapi.json

## License
MIT © MohtaWaist
