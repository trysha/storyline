/*
 * database for storyline 
 * 
 * datatypes are sqlite simplified stuff for now
 */
DROP TABLE IF EXISTS stories;
CREATE TABLE stories (
  storyid TEXT primary key,
  title TEXT NOT NULL,
  teaser TEXT NOT NULL, 
  synopsis TEXT,
  url TEXT NOT NULL,
  date FLOAT NOT NULL,
  sequence FLOAT NOT NULL,
  nsfw BOOLEAN NOT NULL
);

DROP TABLE IF EXISTS arc_map;
CREATE TABLE arc_map (
  storyid TEXT NOT NULL,
  arcid TEXT NOT NULL,
  required BOOLEAN NOT NULL,
  sequence FLOAT NOT NULL
);

DROP TABLE IF EXISTS arcs;
CREATE TABLE arcs (
  arcid TEXT PRIMARY KEY,
  name TEXT NOT NULL
);

DROP TABLE IF EXISTS warning_map;
CREATE TABLE warning_map (
  storyid TEXT NOT NULL,
  name TEXT NOT NULL
);

DROP TABLE IF EXISTS tag_map;
CREATE TABLE tag_map (
  storyid TEXT NOT NULL,
  tagid TEXT NOT NULL
);

DROP TABLE IF EXISTS tags;
CREATE TABLE tags (
  tagid TEXT PRIMARY KEY,
  name TEXT NOT NULL
);

DROP TABLE IF EXISTS ref_map;
CREATE TABLE ref_map (
  storyid TEXT NOT NULL,
  refid TEXT NOT NULL
);

DROP TABLE IF EXISTS characters;
CREATE TABLE characters (
  characterid TEXT PRIMARY KEY,
  primary_aliasid TEXT NOT NULL,
  blurb TEXT
);

DROP TABLE IF EXISTS character_map;
CREATE TABLE character_map (
  storyid TEXT NOT NULL,
  characterid TEXT NOT NULL
);;

DROP TABLE IF EXISTS aliases;
CREATE TABLE aliases (
  characterid TEXT PRIMARY KEY,
  aliasid TEXT NOT NULL,
  name TEXT NOT NULL,
  hidden BOOLEAN NOT NULL
)
