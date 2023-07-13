## NBA Stat Track

NbaStatTrack is a Python-based sports-oriented application designed to retrieve player information and display season averages for the latest 2022 season. The application interacts with the BallDontLie API to fetch player data and showcase relevant statistics.

<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExYzdoZXhqMXdjZmVnODZwdWhmM3NiY2xmdjRmazNzMHRqbDB6aHgyNyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/EZgnl4SE0pxaiSXE4i/giphy.gif" alt="NBA stat track overview" height="100%" />

## Optimizations

1. Add testing to ensure the two APIs being called work as intended.
2. Add more layers to this project such as the ability to get player averages from any season.

## Steps when building: 

1. Setup the project utilizing Python
2. Pseudocoded what I wanted to do in JavaScript(Make an API request based on user input and send the JSON information back to our user in some sort of clean format).
3. Researched Python syntax to implement what I wanted to do above. 

## Libraries/Tools used

1. Python
2. Tabulate
3. Requests
4. BallDontLie API

## How to Run

1. Download the repository to your local machine
2. Locate the folder and navigate to it using your terminal or command prompt.
3. Download the necessary dependencies using: pip3 install requests tabulate
3. Run the following command to start the application: python3 api.py
4. When prompted, enter the name of the player you are looking for, including any spaces between the first and last name.
5. The application will fetch the player's information and display their season averages.

Please ensure that you have Python 3 installed on your machine and that the necessary dependencies are available. Feel free to modify the command if your Python executable is named differently (python, python3, etc.).
