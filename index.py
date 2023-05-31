






# Import the necessary libraries

import requests

import bs4

import mysql.connector

# Create a connection to the MySQL database

conn = mysql.connector.connect(

    host="localhost",

    user="root",

    password="password",

    database="flashscore"

)

# Create a cursor object

cursor = conn.cursor()

# Get the latest soccer scores from FlashScore

url = "https://www.flashscore.com/soccer/"

response = requests.get(url)

soup = bs4.BeautifulSoup(response.content, "html.parser")

# Find all of the soccer matches

matches = soup.find_all("div", class_="match-container")

# For each match, get the following information:

#   - Match name

#   - Match status

#   - Match time

#   - Match score

#   - Match venue

#   - Match odds

for match in matches:

    match_name = match.find("div", class_="match-name").text

    match_status = match.find("div", class_="match-status").text

    match_time = match.find("div", class_="match-time").text

    match_score = match.find("div", class_="match-score").text

    match_venue = match.find("div", class_="match-venue").text

    match_odds = match.find("div", class_="match-odds").text

    # Insert the match information into the MySQL database

    cursor.execute("""

        INSERT INTO matches (match_name, match_status, match_time, match_score, match_venue, match_odds)

        VALUES (%s, %s, %s, %s, %s, %s)

    """, (match_name, match_status, match_time, match_score, match_venue, match_odds))

# Commit the changes to the database

conn.commit()

# Close the connection to the database

conn.close()

# Create the HTML page

html = """

<!DOCTYPE html>

<html>

<head>

    <title>FlashScore</title>

    <link rel="stylesheet" href="style.css">

</head>

<body>

    <h1>FlashScore</h1>

    <table>

        <thead>

            <tr>

                <th>Match Name</th>

                <th>Match Status</th>

                <th>Match Time</th>

                <th>Match Score</th>

                <th>Match Venue</th>

                <th>Match Odds</th>

            </tr>

        </thead>

        <tbody>

            {% for match in matches %}

                <tr>

                    <td>{{ match.match_name }}</td>

                    <td>{{ match.match_status }}</td>

                    <td>{{ match.match_time }}</td>

                    <td>{{ match.match_score }}</td>

                    <td>{{ match.match_venue }}</td>

                    <td>{{ match.match_odds }}</td>

                </tr>

            {% endfor %}

        </tbody>

    </table>

</body>

</html>

"""

# Create the CSS file

css = """

body {

    font-family: sans-serif;

}

table {

    border-collapse: collapse;

}

th, td {

    border: 1px solid black;

    padding: 10px;

}

"""

# Save the HTML and CSS files

with open("index.html", "w") as f:

    f.write(html)

with open("style.css", "w") as f:

    f.write(css)
