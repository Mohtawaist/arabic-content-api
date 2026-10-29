/*!
 * mohtawaist-api — عميل Arabic Content Intelligence API
 * الاستخدام:
 *   const mw = require('mohtawaist-api')('mw_live_...')
 *   const r = await mw.analyze({ text: 'مقال عربي...', keyword: 'المحتوى' })
 */
'use strict';

const BASE = 'https://mohtawaist.com';

function client(apiKey, options) {
  const base = (options && options.base) || BASE;
  const timeout = (options && options.timeout) || 20000;

  async function call(path, body) {
    const ctrl = new AbortController();
    const t = setTimeout(() => ctrl.abort(), timeout);
    try {
      const res = await fetch(base + path, {
        method: body ? 'POST' : 'GET',
        headers: {
          'Content-Type': 'application/json',
          'X-API-Key': apiKey,
          'User-Agent': 'mohtawaist-api-node/1.0'
        },
        body: body ? JSON.stringify(body) : undefined,
        signal: ctrl.signal
      });
      const quota = {
        limit: res.headers.get('x-quota-limit'),
        remaining: res.headers.get('x-quota-remaining'),
        reset: res.headers.get('x-quota-reset')
      };
      const data = await res.json();
      if (!res.ok) {
        const err = new Error((data && data.error) || ('HTTP ' + res.status));
        err.status = res.status; err.body = data; throw err;
      }
      return Object.assign({}, data, { quota });
    } finally { clearTimeout(t); }
  }

  return {
    analyze: (payload) => call('/api/v1/analyze', payload),
    slug: (payload) => call('/api/v1/slug', payload),
    keywords: (payload) => call('/api/v1/keywords', payload),
    readability: (payload) => call('/api/v1/readability', payload),
    health: () => call('/api/v1/health')
  };
}

module.exports = client;
module.exports.default = client;
