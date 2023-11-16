CREATE TABLE flask_template.users
(
    id serial NOT NULL,
    email_id character varying(45) NOT NULL,
    password text NOT NULL,
    mobile_no character varying(10) NOT NULL,
    first_name character varying(45) NOT NULL,
    middle_name character varying(45),
    last_name character varying(45) NOT NULL,
    username character varying(8) NOT NULL,
    account_creation_date bigint NOT NULL,
    account_status character varying(20) NOT NULL,
    last_login_date bigint,
    profile_pic character varying(100),
    date_of_birth date,
    address1 character varying(45),
    address2 character varying(45),
    address3 character varying(45),
    city character varying(20),
    state character varying(20),
    country character varying(20),
    pin_code integer,
    theme character varying(5) NOT NULL,
    last_password_reset_date bigint,
    last_password_change_date bigint,
    role character varying(15) NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT email_id_pk UNIQUE (email_id),
    CONSTRAINT mobile_no_pk UNIQUE (mobile_no)
);

ALTER TABLE IF EXISTS public.users
    OWNER to postgres;