-- Generated by Oracle SQL Developer Data Modeler 24.3.0.240.1210
--   at:        2024-12-24 20:12:58 CET
--   site:      Oracle Database 21c
--   type:      Oracle Database 21c



DROP TABLE hotelska_soba CASCADE CONSTRAINTS;

DROP TABLE knjiga CASCADE CONSTRAINTS;

DROP TABLE naucni_program CASCADE CONSTRAINTS;

DROP TABLE odeljenje CASCADE CONSTRAINTS;

DROP TABLE oprema CASCADE CONSTRAINTS;

DROP TABLE osoba CASCADE CONSTRAINTS;

DROP TABLE pozvan_na CASCADE CONSTRAINTS;

DROP TABLE radna_prostorija CASCADE CONSTRAINTS;

DROP TABLE rukovodi CASCADE CONSTRAINTS;

DROP TABLE seminar CASCADE CONSTRAINTS;

-- predefined type, no DDL - MDSYS.SDO_GEOMETRY

-- predefined type, no DDL - XMLTYPE

CREATE TABLE hotelska_soba (
    br_sob INTEGER NOT NULL,
    kap    INTEGER NOT NULL,
    ter    CHAR(1) NOT NULL,
    ren    VARCHAR2(100 CHAR)
);

ALTER TABLE hotelska_soba ADD CONSTRAINT hotelska_soba_pk PRIMARY KEY ( br_sob );

CREATE TABLE knjiga (
    id_k     INTEGER NOT NULL,
    naz      VARCHAR2(50 CHAR) NOT NULL,
    god      INTEGER NOT NULL,
    izd      VARCHAR2(50 CHAR) NOT NULL,
    aut      VARCHAR2(50 CHAR) NOT NULL,
    osoba_id INTEGER
);

ALTER TABLE knjiga ADD CONSTRAINT knjiga_pk PRIMARY KEY ( id_k );

CREATE TABLE naucni_program (
    id_prog INTEGER NOT NULL,
    naz     VARCHAR2(50 BYTE),
    id_od   INTEGER
);

ALTER TABLE naucni_program ADD CONSTRAINT naucni_program_pk PRIMARY KEY ( id_prog );

CREATE TABLE odeljenje (
    id_od INTEGER NOT NULL,
    naz   VARCHAR2(50 BYTE)
);

ALTER TABLE odeljenje ADD CONSTRAINT odeljenje_pk PRIMARY KEY ( id_od );

CREATE TABLE oprema (
    id_op    INTEGER NOT NULL,
    naz      INTEGER,
    max_kol  INTEGER,
    osoba_id INTEGER,
    id_sem   INTEGER,
    id_prog  INTEGER
);

ALTER TABLE oprema ADD CONSTRAINT oprema_pk PRIMARY KEY ( id_op );

CREATE TABLE osoba (
    id     INTEGER NOT NULL,
    jmbg   CHAR(13 CHAR) NOT NULL,
    ime    VARCHAR2(50 CHAR) NOT NULL,
    prz    VARCHAR2(50 CHAR) NOT NULL,
    br_tel VARCHAR2(20 CHAR) NOT NULL,
    email  VARCHAR2(50 CHAR) NOT NULL,
    tip    VARCHAR2(10 CHAR) NOT NULL,
    br_sob INTEGER,
    uloga  VARCHAR2(10 CHAR),
    sef    INTEGER
);

ALTER TABLE osoba ADD CONSTRAINT osoba_pk PRIMARY KEY ( id );

CREATE TABLE pozvan_na (
    id_sem   INTEGER NOT NULL,
    id_prog  INTEGER NOT NULL,
    osoba_id INTEGER NOT NULL
);

ALTER TABLE pozvan_na
    ADD CONSTRAINT pozvan_na_pk PRIMARY KEY ( id_sem,
                                              id_prog,
                                              osoba_id );

CREATE TABLE radna_prostorija (
    id_rp   INTEGER NOT NULL,
    naz     VARCHAR2(50 BYTE),
    lok     VARCHAR2(50 BYTE),
    tip     VARCHAR2(10 BYTE),
    id_prog INTEGER
);

ALTER TABLE radna_prostorija ADD CONSTRAINT radna_prostorija_pk PRIMARY KEY ( id_rp );

CREATE TABLE rukovodi (
    osoba_id INTEGER NOT NULL,
    id_prog  INTEGER NOT NULL,
    upr      CHAR(1)
);

ALTER TABLE rukovodi ADD CONSTRAINT rukovodi_pk PRIMARY KEY ( osoba_id,
                                                              id_prog );

CREATE TABLE seminar (
    id_sem    INTEGER NOT NULL,
    dat_start DATE,
    dat_kraj  DATE,
    tip       VARCHAR2(10 BYTE),
    id_prog   INTEGER NOT NULL
);

ALTER TABLE seminar ADD CONSTRAINT seminar_pk PRIMARY KEY ( id_sem,
                                                            id_prog );

ALTER TABLE osoba
    ADD CONSTRAINT hotelska_soba_fk FOREIGN KEY ( br_sob )
        REFERENCES hotelska_soba ( br_sob );

ALTER TABLE radna_prostorija
    ADD CONSTRAINT naucni_program_fk FOREIGN KEY ( id_prog )
        REFERENCES naucni_program ( id_prog );

ALTER TABLE rukovodi
    ADD CONSTRAINT naucni_program_fkv1 FOREIGN KEY ( id_prog )
        REFERENCES naucni_program ( id_prog );

ALTER TABLE seminar
    ADD CONSTRAINT naucni_program_fkv2 FOREIGN KEY ( id_prog )
        REFERENCES naucni_program ( id_prog );

ALTER TABLE naucni_program
    ADD CONSTRAINT odeljenje_fk FOREIGN KEY ( id_od )
        REFERENCES odeljenje ( id_od );

ALTER TABLE knjiga
    ADD CONSTRAINT osoba_fk FOREIGN KEY ( osoba_id )
        REFERENCES osoba ( id );

ALTER TABLE pozvan_na
    ADD CONSTRAINT osoba_fkv1 FOREIGN KEY ( osoba_id )
        REFERENCES osoba ( id );

ALTER TABLE oprema
    ADD CONSTRAINT osoba_fkv2 FOREIGN KEY ( osoba_id )
        REFERENCES osoba ( id );

ALTER TABLE rukovodi
    ADD CONSTRAINT osoba_fkv3 FOREIGN KEY ( osoba_id )
        REFERENCES osoba ( id );

ALTER TABLE osoba
    ADD CONSTRAINT osoba_fkv5 FOREIGN KEY ( sef )
        REFERENCES osoba ( id );

ALTER TABLE pozvan_na
    ADD CONSTRAINT seminar_fk
        FOREIGN KEY ( id_sem,
                      id_prog )
            REFERENCES seminar ( id_sem,
                                 id_prog );

ALTER TABLE oprema
    ADD CONSTRAINT seminar_fkv2
        FOREIGN KEY ( id_sem,
                      id_prog )
            REFERENCES seminar ( id_sem,
                                 id_prog );



-- Oracle SQL Developer Data Modeler Summary Report:
--
-- CREATE TABLE                            10
-- CREATE INDEX                             0
-- ALTER TABLE                             22
-- CREATE VIEW                              0
-- ALTER VIEW                               0
-- CREATE PACKAGE                           0
-- CREATE PACKAGE BODY                      0
-- CREATE PROCEDURE                         0
-- CREATE FUNCTION                          0
-- CREATE TRIGGER                           0
-- ALTER TRIGGER                            0
-- CREATE COLLECTION TYPE                   0
-- CREATE STRUCTURED TYPE                   0
-- CREATE STRUCTURED TYPE BODY              0
-- CREATE CLUSTER                           0
-- CREATE CONTEXT                           0
-- CREATE DATABASE                          0
-- CREATE DIMENSION                         0
-- CREATE DIRECTORY                         0
-- CREATE DISK GROUP                        0
-- CREATE ROLE                              0
-- CREATE ROLLBACK SEGMENT                  0
-- CREATE SEQUENCE                          0
-- CREATE MATERIALIZED VIEW                 0
-- CREATE MATERIALIZED VIEW LOG             0
-- CREATE SYNONYM                           0
-- CREATE TABLESPACE                        0
-- CREATE USER                              0
--
-- DROP TABLESPACE                          0
-- DROP DATABASE                            0
--
-- REDACTION POLICY                         0
--
-- ORDS DROP SCHEMA                         0
-- ORDS ENABLE SCHEMA                       0
-- ORDS ENABLE OBJECT                       0
--
-- ERRORS                                   0
-- WARNINGS                                 0
