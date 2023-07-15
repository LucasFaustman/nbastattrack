## NBA Stat Track

The NBA Stat Track API is a Python-based sports-oriented application designed to retrieve player information and display season averages for the latest 2022 season. It interacts with the BallDontLie API to fetch player data and showcases relevant statistics. Originally built as a terminal application, it has been converted to a public-facing API utilizing Flask on the backend and Docker for hosting.

Try for yourself: https://nba-stat-track.onrender.com/player/lebron%20james

<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbjllaTF5MXJnZnNxbWxtMm12eWl2b25zMzFrcnNnNmg4OGlrZndvZCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/WadO4tgDrFPejyaHIj/giphy.gif" alt="NBA stat track overview" height="100%" />

## Optimizations

1. Add testing to ensure the APIs being called are working as intended.
2. Expand the functionality by adding more layers to the project, such as the ability to retrieve player averages from any season.
3. Add filtering capabilities.

## Steps when building: 

1. Setup the project utilizing Python
2. Pseudocoded what I wanted to do in JavaScript(Make an API request based on user input and send the JSON information back to our user in some sort of clean format).
3. Researched Python syntax to implement what I wanted to do above. 
  - Learned the syntax for:
      - Declaring variables
      - Importing dependencies
      - Using if-else statements
      - Looping
      - Array Manipulation
4. Utilized a quick start guide to build a public-facing API using Flask and Docker.
5. Created the API endpoint.
6. Implemented Models and Serializers for better data validation and maintainability.
7. Dockerized the application to enable easy deployment on Render.

## Libraries/Tools used

1. Python
2. Tabulate
3. Requests
4. BallDontLie API
5. Flask
6. Marshmellow for Object Serialization.
7. Docker

## How to Use
- To retrieve player statistics, use the following endpoint:
    - https://nba-stat-track.onrender.com/player/{player name}
- Replace {player name} with the name of the player you want to fetch statistics for, with spaces between the first and last name. For example:
  - https://nba-stat-track.onrender.com/player/lebron%20james
- This will return the player information and season averages for the specified player.

Feel free to explore the NBA Stat Track API and retrieve statistics for your favorite NBA players!

