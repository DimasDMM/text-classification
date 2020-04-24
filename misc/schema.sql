DROP TABLE IF EXISTS "texts";

CREATE TABLE "texts" (
  "id" SERIAL,
  "text" TEXT NOT NULL,
  "category" VARCHAR(255) NOT NULL
);
