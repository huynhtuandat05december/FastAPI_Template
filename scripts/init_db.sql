-- user table
CREATE TABLE public."user" (
	id serial4 NOT NULL,
	created_at timestamptz NOT NULL,
	updated_at timestamptz NOT NULL DEFAULT now(),
	is_deleted bool NOT NULL DEFAULT false,
	uuid uuid NOT NULL DEFAULT uuid_generate_v4(),
	first_name varchar(255) NOT NULL,
	last_name varchar(255) NOT NULL,
	email varchar(255) NOT NULL,
	"role" varchar(20) NOT NULL,
	status_code varchar(20) NOT NULL,
	password_hash varchar(255) NOT NULL,
	CONSTRAINT user_pk PRIMARY KEY (id),
	CONSTRAINT user_un UNIQUE (uuid),
	CONSTRAINT user_unique_email UNIQUE (email)
);
