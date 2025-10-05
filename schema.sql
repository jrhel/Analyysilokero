CREATE TABLE User (
  id integer PRIMARY KEY,
  username TEXT UNIQUE,
  password_hash TEXT
);

CREATE TABLE Analysis (
  id integer PRIMARY KEY,
  question TEXT,
  admin integer,
  FOREIGN KEY (admin) REFERENCES User(id)
);

CREATE TABLE Hypothesis (
  id integer PRIMARY KEY,
  claim TEXT,
  analysis_id integer,
  FOREIGN KEY (analysis_id) REFERENCES Analysis(id)
);

CREATE TABLE Evidence (
  id integer PRIMARY KEY,
  observation TEXT,
  source TEXT,
  analysis_id integer,
  FOREIGN KEY (analysis_id) REFERENCES Analysis(id)
);

CREATE TABLE Analysis_User (
  id integer PRIMARY KEY,
  user_id integer,
  analysis_id integer,
  FOREIGN KEY (user_id) REFERENCES User(id),
  FOREIGN KEY (analysis_id) REFERENCES Analysis(id)
);
