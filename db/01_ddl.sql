-- DROP TABLE hotelska_soba CASCADE;

-- DROP TABLE knjiga CASCADE;

-- DROP TABLE naucni_program CASCADE;

-- DROP TABLE odeljenje CASCADE;

-- DROP TABLE oprema CASCADE;

-- DROP TABLE osoba CASCADE;

-- DROP TABLE pozvan_na CASCADE;

-- DROP TABLE radna_prostorija CASCADE;

-- DROP TABLE rukovodi CASCADE;

-- DROP TABLE seminar CASCADE;

CREATE TABLE hotelska_soba (
    br_sob SERIAL,
    kap    INTEGER NOT NULL,
    ter    BOOLEAN NOT NULL,
    ren    VARCHAR(100)
);

ALTER TABLE hotelska_soba ADD CONSTRAINT hotelska_soba_pk PRIMARY KEY ( br_sob );

CREATE TABLE knjiga (
    id_k     SERIAL,
    naz      VARCHAR(50) NOT NULL,
    god      INTEGER NOT NULL,
    izd      VARCHAR(50) NOT NULL,
    aut      VARCHAR(50) NOT NULL,
    osoba_id INTEGER
);

ALTER TABLE knjiga ADD CONSTRAINT knjiga_pk PRIMARY KEY ( id_k );

CREATE TABLE naucni_program (
    id_prog VARCHAR(10) NOT NULL,
    naz     VARCHAR(50),
    id_od   CHAR(1)
);

ALTER TABLE naucni_program ADD CONSTRAINT naucni_program_pk PRIMARY KEY ( id_prog );

CREATE TABLE odeljenje (
    id_od CHAR(1) NOT NULL,
    naz   VARCHAR(50)
);

ALTER TABLE odeljenje ADD CONSTRAINT odeljenje_pk PRIMARY KEY ( id_od );

CREATE TABLE oprema (
    id_op    SERIAL,
    naz      INTEGER,
    max_kol  INTEGER,
    osoba_id INTEGER,
    id_sem   VARCHAR(10),
    id_prog  VARCHAR(10)
);

ALTER TABLE oprema ADD CONSTRAINT oprema_pk PRIMARY KEY ( id_op );

CREATE TABLE osoba (
    id       SERIAL,
    jmbg     CHAR(13) NOT NULL,
    ime      VARCHAR(50) NOT NULL,
    prz      VARCHAR(50) NOT NULL,
    br_tel   VARCHAR(20) NOT NULL,
    email    VARCHAR(50) NOT NULL,
    tip      VARCHAR(20) NOT NULL,
    br_sob   INTEGER,
    uloga    VARCHAR(20),
    sef_id   INTEGER
);

ALTER TABLE osoba ADD CONSTRAINT osoba_pk PRIMARY KEY ( id );

CREATE TABLE pozvan_na (
    id_sem   VARCHAR(10) NOT NULL,
    id_prog  VARCHAR(10) NOT NULL,
    osoba_id INTEGER NOT NULL
);

ALTER TABLE pozvan_na
    ADD CONSTRAINT pozvan_na_pk PRIMARY KEY ( id_sem,
                                              id_prog,
                                              osoba_id );

CREATE TABLE radna_prostorija (
    id_rp   SERIAL,
    naz     VARCHAR(50),
    lok     VARCHAR(50),
    tip     VARCHAR(20),
    id_prog VARCHAR(10)
);

ALTER TABLE radna_prostorija ADD CONSTRAINT radna_prostorija_pk PRIMARY KEY ( id_rp );

CREATE TABLE rukovodi (
    osoba_id INTEGER NOT NULL,
    id_prog  VARCHAR(10) NOT NULL,
    upr      BOOLEAN NOT NULL DEFAULT FALSE
);

ALTER TABLE rukovodi ADD CONSTRAINT rukovodi_pk PRIMARY KEY ( osoba_id,
                                                              id_prog );

CREATE TABLE seminar (
    id_sem    VARCHAR(10) NOT NULL,
    dat_start DATE,
    dat_kraj  DATE,
    tip       VARCHAR(20),
    id_prog   VARCHAR(10) NOT NULL
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
    ADD CONSTRAINT osoba_fkv5 FOREIGN KEY ( sef_id )
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
