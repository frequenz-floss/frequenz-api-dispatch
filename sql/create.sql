-- (Re)create database (uncomment if needed)

/*
DROP DATABASE IF EXISTS dispatch;

CREATE DATABASE dispatch
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'en_US.utf8'
    LC_CTYPE = 'en_US.utf8'
    TABLESPACE = pg_default
    CONNECTION_LIMIT = -1;
*/

\c dispatch

CREATE SCHEMA IF NOT EXISTS dispatch
    AUTHORIZATION postgres;

-- Custom domains and types used in the schema

CREATE TYPE dispatch."dispatch_status" AS ENUM (
    'ACTIVE',
    'INACTIVE',
    'SIMULATED'
);

--- Types of dispatch that can be requested
CREATE TABLE dispatch."dispatch_type"(
    "id" BIGSERIAL NOT NULL,
    "type" VARCHAR(64) NOT NULL
);
ALTER TABLE dispatch."dispatch_type"
    ADD PRIMARY KEY("id");
CREATE UNIQUE INDEX "dispatch_type_unique_index"
    ON dispatch."dispatch_type"("type");

--- Individual dispatches for specific locations and time intervals
CREATE TABLE dispatch."dispatch"(
    "id" BIGSERIAL NOT NULL,
    "microgrid_id" BIGINT NOT NULL,  -- cross-ref to another DB
    "dispatch_type_id" BIGINT NOT NULL,
    "start_time" TIMESTAMP(0) WITH TIME ZONE NOT NULL,
    "end_time" TIMESTAMP(0) WITH TIME ZONE NOT NULL
);
ALTER TABLE dispatch."dispatch"
    ADD PRIMARY KEY("id");
ALTER TABLE dispatch."dispatch"
    ADD CONSTRAINT "dispatch_dispatch_type_id_foreign"
        FOREIGN KEY("dispatch_type_id")
        REFERENCES dispatch."dispatch_type"("id");
CREATE UNIQUE INDEX "dispatch_unique_index"
    ON dispatch."dispatch"(
        "microgrid_id",
        "dispatch_type_id",
        "start_time",
        "end_time"
    );

--- Modifications to the settings for individual dispatches
CREATE TABLE dispatch."dispatch_modification"(
    "id" BIGSERIAL NOT NULL,
    "create_time" TIMESTAMP WITH TIME zone NOT NULL DEFAULT current_timestamp,
    "dispatch_id" BIGINT NOT NULL,
    "status" dispatch."dispatch_status" NOT NULL,
    "settings" JSON NULL  -- contents determined by dispatch type
);
ALTER TABLE dispatch."dispatch_modification"
    ADD PRIMARY KEY("id");
ALTER TABLE dispatch."dispatch_modification"
    ADD CONSTRAINT "dispatch_modification_dispatch_id_foreign"
        FOREIGN KEY("dispatch_id")
        REFERENCES dispatch."dispatch"("id");
