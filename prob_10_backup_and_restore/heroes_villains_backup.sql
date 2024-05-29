BEGIN TRANSACTION;
CREATE TABLE arch_nemesis(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            hero_id INTEGER NOT NULL,
            villain_id INTEGER NOT NULL,
            FOREIGN KEY(hero_id) REFERENCES heroes(hero_id)
            FOREIGN KEY(villain_id) REFERENCES villains(villain_id)
        );
INSERT INTO "arch_nemesis" VALUES(1,1,1);
INSERT INTO "arch_nemesis" VALUES(2,2,2);
INSERT INTO "arch_nemesis" VALUES(3,3,3);
INSERT INTO "arch_nemesis" VALUES(4,4,4);
CREATE TABLE heroes (
            hero_id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            release_date INTEGER NOT NULL,
            hero_name TEXT NOT NULL,
            powers TEXT NOT NULL
        );
INSERT INTO "heroes" VALUES(2,'Barry','Allan',1940,'The Flash','Superspeed, Lightning Manipulation, Speed Force');
INSERT INTO "heroes" VALUES(3,'Tony','Stark',1963,'Ironman','NEW, RANDOM, POWERS, !');
INSERT INTO "heroes" VALUES(4,'Peter','Parker',1962,'Spiderman','Super Sence, Spiderweb, athletic');
CREATE TABLE villains(
            villain_id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            release_date INTEGER NOT NULL,
            villain_name TEXT NOT NULL,
            powers TEXT NOT NULL
        );
INSERT INTO "villains" VALUES(1,'Arthur','Fleck',2019,'Joker','Master Manipulator, Chemical Engineer, Master Planner');
INSERT INTO "villains" VALUES(2,'Eobard','Thawne',1963,'Reverse Flash','Negative Speed Force, Superspeed, Lightning Manipulation');
INSERT INTO "villains" VALUES(3,'Gene','Kahn',1964,'Mandarin','Genius-level Intellect, Master of Martial Arts, Expert Strategist and Tactician');
INSERT INTO "villains" VALUES(4,'Norman','Osborn',1964,'Green Goblin','Superhuman Strength, Superhuman Speed, Superhuman Refelexes');
CREATE INDEX idx_release_date
            ON
                heroes (release_date)
            
            ;
DELETE FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence" VALUES('heroes',4);
INSERT INTO "sqlite_sequence" VALUES('villains',4);
INSERT INTO "sqlite_sequence" VALUES('arch_nemesis',4);
COMMIT;
