-- Table definitions for the tournament_game project.

-- Drop tournament_game database if it exists
DROP DATABASE IF EXISTS tournament_game;

-- Create Database 'tournament_game'
CREATE DATABASE tournament_game;

-- Connect to the tournament_game database
\connect tournament_game

-- Drop all tables and views if they exist
DROP TABLE IF EXISTS gamer CASCADE;
DROP TABLE IF EXISTS match CASCADE;
DROP VIEW IF EXISTS slots CASCADE;

-- Creates gamer table
CREATE TABLE gamer(
  gamer_id serial PRIMARY KEY,
  gamer_name text
);

-- Creates match table with FK to gamer
CREATE TABLE match (
  match_id serial PRIMARY KEY,
  winplayer INTEGER,
  loseplayer INTEGER,
  FOREIGN KEY(winplayer) REFERENCES gamer(gamer_id),
  FOREIGN KEY(loseplayer) REFERENCES gamer(gamer_id)
);

-- Creates a view of matches played sorted by wonplayer count
CREATE VIEW slots AS
SELECT p.gamer_id as gamer_id, p.gamer_name,
(SELECT count(*) FROM match WHERE match.winplayer = p.gamer_id) as wonplayer,
(SELECT count(*) FROM match WHERE p.gamer_id in (winplayer, loseplayer)) as played
FROM gamer p
GROUP BY p.gamer_id
ORDER BY wonplayer DESC;
