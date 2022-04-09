# DROP TABLES

songplay_table_drop = "Drop table if exists songplay;"
user_table_drop = "Drop table if exists users;"
song_table_drop = "Drop table if exists song;"
artist_table_drop = "Drop table if exists artist;"
time_table_drop = "Drop table if exists time;"

# CREATE TABLEStimestamp, user ID, level, song ID, artist ID, session ID, location, and user agent

songplay_table_create = ("""create table if not exists songplay(songplay_id Serial Not null, start_time timestamp, user_id varchar, level varchar, song_id int, artist_id int, session_id int, location varchar, user_agent varchar, primary key (songplay_id)
""")

user_table_create = ("""create table if not exists users ( user_id varchar not null, first_name varchar, last_name varchar, gender varchar,level varchar, primary key (user_id)
""")

song_table_create = ("""create table if not exists song(song_id varchar not null, title varchar, artist_id varchar, year int, duration real, primary key (song_id)
""")

artist_table_create = ("""create table if not exists artist(artist_id not null varchar, name varchar, location varchar, latitude real, longitude real, primary key (artist_id)
""")

time_table_create = (""" create table if not exists time(start_time timestamp, hour int, day int, week int, month int, year int, weekday int)
""")

# INSERT RECORDS

songplay_table_insert = ("""
""")

user_table_insert = ("""
""")

song_table_insert = ("""
""")

artist_table_insert = ("""
""")


time_table_insert = ("""
""")

# FIND SONGS

song_select = ("""Select s.song_id,s.artist_id from song s inner join artist a on a.artist_id=s.artist_id where s.title=%s and a.name=%s and s.duration=%s
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]