
-- SEQUENCE: public.check_id_seq

-- DROP SEQUENCE IF EXISTS public.check_id_seq;

CREATE SEQUENCE IF NOT EXISTS public.check_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

ALTER SEQUENCE public.check_id_seq
    OWNER TO postgres;

CREATE TABLE IF NOT EXISTS public."check"
(
    id integer NOT NULL DEFAULT nextval('check_id_seq'::regclass),
    type character varying(255) COLLATE pg_catalog."default",
    date timestamp without time zone,
    uuid character varying COLLATE pg_catalog."default",
    is_active boolean,
    CONSTRAINT check_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public."check"
    OWNER to postgres;
-- Index: ix_check_uuid

-- DROP INDEX IF EXISTS public.ix_check_uuid;

CREATE UNIQUE INDEX IF NOT EXISTS ix_check_uuid
    ON public."check" USING btree
    (uuid COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;


-- SEQUENCE: public.check_line_id_seq
-- DROP SEQUENCE IF EXISTS public.check_line_id_seq;

CREATE SEQUENCE IF NOT EXISTS public.check_line_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

ALTER SEQUENCE public.check_line_id_seq
    OWNER TO postgres;

-- Table: public.check_line

-- DROP TABLE IF EXISTS public.check_line;

CREATE TABLE IF NOT EXISTS public.check_line
(
    id integer NOT NULL DEFAULT nextval('check_line_id_seq'::regclass),
    item_no character varying COLLATE pg_catalog."default",
    qty integer,
    description character varying COLLATE pg_catalog."default",
    check_id integer,
    CONSTRAINT check_line_pkey PRIMARY KEY (id),
    CONSTRAINT check_line_check_id_fkey FOREIGN KEY (check_id)
        REFERENCES public."check" (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.check_line
    OWNER to postgres;
-- Index: ix_check_line_description

-- DROP INDEX IF EXISTS public.ix_check_line_description;

CREATE INDEX IF NOT EXISTS ix_check_line_description
    ON public.check_line USING btree
    (description COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;
-- Index: ix_check_line_item_no

-- DROP INDEX IF EXISTS public.ix_check_line_item_no;

CREATE INDEX IF NOT EXISTS ix_check_line_item_no
    ON public.check_line USING btree
    (item_no COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;



-- packing


CREATE SEQUENCE IF NOT EXISTS public.packing_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

ALTER SEQUENCE public.packing_id_seq
    OWNER TO postgres;

CREATE TABLE IF NOT EXISTS public.packing
(
    id integer NOT NULL DEFAULT nextval('packing_id_seq'::regclass),
    type character varying(255) COLLATE pg_catalog."default",
    date timestamp without time zone,
    uuid character varying COLLATE pg_catalog."default",
    is_active boolean,
    CONSTRAINT packing_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.packing
    OWNER to postgres;


CREATE UNIQUE INDEX IF NOT EXISTS ix_packing_uuid
    ON public.packing USING btree
    (uuid COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;


CREATE SEQUENCE IF NOT EXISTS public.packing_line_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

ALTER SEQUENCE public.packing_line_id_seq
    OWNER TO postgres;



CREATE TABLE IF NOT EXISTS public.packing_line
(
    id integer NOT NULL DEFAULT nextval('packing_line_id_seq'::regclass),
    item_no character varying COLLATE pg_catalog."default",
    qty integer,
    description character varying COLLATE pg_catalog."default",
    packing_id integer,
    CONSTRAINT packing_line_pkey PRIMARY KEY (id),
    CONSTRAINT packing_line_packing_id_fkey FOREIGN KEY (packing_id)
        REFERENCES public.packing (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.packing_line
    OWNER to postgres;


CREATE INDEX IF NOT EXISTS ix_packing_line_description
    ON public.packing_line USING btree
    (description COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;


CREATE INDEX IF NOT EXISTS ix_packing_line_item_no
    ON public.packing_line USING btree
    (item_no COLLATE pg_catalog."default" ASC NULLS LAST)
    TABLESPACE pg_default;
