const fs = require('fs');
const path = '/workspaces/Membrane/src/services/api.ts';
let code = fs.readFileSync(path, 'utf-8');
code = code.replace(
  `const getApiBase = () => {
  if (import.meta.env.VITE_API_URL) return import.meta.env.VITE_API_URL
  const href = window.location.href
  if (href.includes('-3000.')) return href.replace('-3000', '-8000')
  return 'http://localhost:8000'
}`,
  `const getApiBase = () => {
  if (import.meta.env.VITE_API_URL) return import.meta.env.VITE_API_URL;
  const href = window.location.href;
  if (href.includes('-5173.')) {
    const url = new URL(href);
    url.hostname = url.hostname.replace('-5173', '-8000');
    return url.origin;
  }
  if (href.includes('-3000.')) {
    const url = new URL(href);
    url.hostname = url.hostname.replace('-3000', '-8000');
    return url.origin;
  }
  return 'http://localhost:8000';
}`
);
fs.writeFileSync(path, code);
