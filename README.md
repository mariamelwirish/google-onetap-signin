# Google One Tap Sign-In

A Django demo project implementing Google One Tap authentication, allowing users to sign in with their Google account via a one-click popup.


## Installation

1. Clone the repo

```bash
git clone https://github.com/mariamelwirish/google-onetap-signin.git
cd google-onetap-signin
```

2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Create a `.env` file in the root directory

```
GOOGLE_CLIENT_ID=your_google_client_id_here
```

5. Run migrations

```bash
python manage.py migrate
```

6. Start the server

```bash
python manage.py runserver
```

7. Visit `http://127.0.0.1:8000/accounts/login/`

