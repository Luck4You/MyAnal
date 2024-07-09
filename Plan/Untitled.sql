CREATE TABLE "Purchase" (
  "Purchase_ID" integer PRIMARY KEY,
  "Purchase_date" datetime,
  "Purchase_name" varchar,
  "User_id" integer,
  "Adress" varchar
);

CREATE TABLE "dict_product_type" (
  "dict_product_type_ID" integer PRIMARY KEY,
  "dict_product_type_name" varchar
);

CREATE TABLE "Products" (
  "Product_ID" integer PRIMARY KEY,
  "Product_name" varchar,
  "price_full" decimal,
  "quantity" decimal,
  "price_sum" decimal,
  "Purchases_ID" integer,
  "Shop_name" varchar,
  "Product_type" integer
);

CREATE TABLE "User" (
  "User_ID" integer PRIMARY KEY,
  "Purchase_date" datetime,
  "Purchase_name" varchar,
  "User_id" integer
);

ALTER TABLE "Products" ADD FOREIGN KEY ("Purchases_ID") REFERENCES "Purchase" ("Purchase_ID");

ALTER TABLE "Purchase" ADD FOREIGN KEY ("User_id") REFERENCES "User" ("User_id");

ALTER TABLE "dict_product_type" ADD FOREIGN KEY ("dict_product_type_ID") REFERENCES "Products" ("Product_type");
