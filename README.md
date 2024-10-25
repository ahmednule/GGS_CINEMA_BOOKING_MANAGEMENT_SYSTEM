## Garden City Cinema Booking Management System

This web application allows users to book movie tickets online effortlessly. Browse movies, select showtimes, reserve seats, and manage your bookings—all from the comfort of your home. Enjoy a streamlined movie-booking experience with our user-friendly platform.

## Features

- **Comprehensive Movie Listings:** Explore detailed movie information, including genre, rating, duration, and synopsis.
- **Flexible Showtime Selection:** Choose your preferred time slot from available showtimes for each movie.
- **Interactive Seat Reservation:** Select your ideal seats from an interactive seating chart.
- **Secure User Authentication:** Register and log in securely to manage your bookings with ease.
- **Booking History:** Track past and upcoming bookings conveniently.
- **Dedicated Admin Panel:** Manage movie listings, showtimes, and bookings from a comprehensive admin interface.

## Technology Stack

- **Frontend:** HTML, CSS, JavaScript (Bootstrap for styling)
- **Backend:** Django (Python)
- **Database:** SQLite or PostgreSQL (choose the one used)
- **Deployment:** [Specify deployment platform, e.g., Heroku, Vercel]

## Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/ahmednule/GGS_CINEMA_BOOKING_MANAGEMENT_SYSTEM.git
    cd  GGS_CINEMA_BOOKING_MANAGEMENT_SYSTEM
    cd GGsCinema
    ```

2. **Set Up Virtual Environment**

    Create a virtual environment:

    ```bash
    python3 -m venv env
    ```

    Activate the virtual environment:

    On Windows:

    ```bash
    env\Scripts\activate
    ```

    On macOS/Linux:

    ```bash
    source env/bin/activate
    ```

3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure the Database**
    #optional

    ```bash
    python manage.py migrate
    ```

5. **Create a Superuser**
     #optional

    ```bash
    python manage.py createsuperuser
    ```

6. **Run the Development Server**

    ```bash
    python manage.py runserver
    ```

7. **Access the Application**

    Open your web browser and navigate to:
    ```
    http://localhost:8000
    ```

## Usage

- **Browse Movies:** Explore the movie listings and find the perfect film for your next cinema adventure.
- **Select a Movie:** Click on a movie to view its details and available showtimes.
- **Choose a Showtime:** Pick the most convenient time slot for your schedule.
- **Reserve Seats:** Select your preferred seats from the interactive seating chart.
- **Complete the Booking:** Log in to manage your bookings and view your booking confirmation.

## Contributing

We welcome your contributions! Fork the repository and submit a pull request to share your improvements. For significant changes, please open an issue for discussion beforehand.

## License

This project is licensed under the **Nairobi Technical Training Institute** license.

## Contact

For any inquiries, please contact **Nancy Maina** at [nancymaina@gmail.com](mailto:nancymaina@gmail.com).

**Repository:** [https://github.com/ahmednule/GGS_CINEMA_BOOKING_MANAGEMENT_SYSTEM.git](https://github.com/ahmednule/GGS_CINEMA_BOOKING_MANAGEMENT_SYSTEM.git)