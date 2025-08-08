# Game Recharge Price Comparison API

A Flask-based backend that scrapes diamond/UC prices from multiple gaming recharge sites and returns them as JSON.

## Deployment Steps
1. Fork or download this repository.
2. Create a new GitHub repo and push this code.
3. Go to [Render](https://render.com), create a new **Web Service**.
4. Connect to your GitHub repo.
5. Set `Build Command` to: pip install -r requirements.txt
6. Set `Start Command` to: gunicorn app:app
7. 7. Deploy.
8. Use the API in Blogger via JavaScript AJAX.

## Example API Endpoints
- `/prices?game=mobile_legends`
- `/prices?game=free_fire`
- `/prices?game=pubg`
- `/all`
