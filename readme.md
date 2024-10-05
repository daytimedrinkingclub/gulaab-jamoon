# Gulaabjamoon

- A hotel listing and experince booking web page
- sampledomain.com/<hotelname>
  - based on the hotel name and city we need to fetch the experiences related data and showcase it

## Tech Stack

- Python Flask with jinja 2 templating engine
- supabase database


## Folder structure for the project
```bash
- app/
    - static/
    - templates/
        - base.html
        - main/
            - landing_page.html # extends the base
            - experience_details.html # extends the base
            - booking_page.html # extends the base
    - routes/
        - __init__.py
        - main.py # will contain the route that will bring the data from the database to render the webpage
    - services/
        - __init__.py
        - supabase_service.py
    - config.py
    - supabase_config.py
    - run.py # to run the flask app
    - requirements.txt

```