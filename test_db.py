import psycopg2


# connexion = psycopg2.connect(dbname="portfolio",
#                                      user="mehdi",
#                                      host="127.0.0.1",
#                                      password="azerty"
#                                      )

connexion = psycopg2.connect("dbname='portfolio_project' user='root' host='127.0.0.1' password=''" )
