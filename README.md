# Game Recharge Price Comparison API

This is a Flask-based API that scrapes game recharge prices (diamonds, UC) from Codashop and SEAGM.

## Deploying on Render
1. Push this repo to GitHub.
2. On Render.com:
   - Create **New Web Service**
   - Connect to GitHub repo
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
3. Deploy!

## API Endpoints
- `GET /prices?game=mobile_legends`
- `GET /prices?game=free_fire`
- `GET /prices?game=pubg_mobile`
- `GET /all`

## Usage in Blogger
```html
<div id="price-data"></div>
<script>
  fetch("https://YOUR-RENDER-URL/prices?game=free_fire")
    .then(r => r.json())
    .then(data => {
      let html = "<ul>";
      data.forEach(item => html += `<li>${item.amount} — ${item.price} (${item.vendor})</li>`);
      html += "</ul>";
      document.getElementById("price-data").innerHTML = html;
    });
</script>
