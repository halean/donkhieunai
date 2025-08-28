To run:
1) Get a github account
2) Go to codespaces (free 30hour a month), after that...
3) <img width="1675" height="1451" alt="image" src="https://github.com/user-attachments/assets/c9c287fa-44cf-4e27-80fc-d65ec685c065" />
4) Create code space (take about 5-10 minutes, to avoid this, set up your own dev environment, then pip install requirements.txt; then sh download_db.sh)
6) run: export open_ai_token=<SECRET_TOKEN> (contact for a ready made one)
7) run: uvicorn main:app --host 0.0.0.0 --port 3000 --loop asyncio (first time: take a few mins to download models, after that: should be faster)
8) ctrl-click on the link to test out the app
9) modify code and experiment, have fun!
