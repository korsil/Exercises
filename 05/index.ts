import { createInterface } from "readline/promises";
const sqlite3 = require("sqlite3").verbose();
const db = new sqlite3.Database("db.sqlite3");

// This could also be included in the SQL table as constraints
const NAME_LENGTH_CONSTRAINT = 25;
const AGE_MIN = 0;
const AGE_MAX = 150;

const rl = createInterface({
  input: process.stdin,
  output: process.stdout,
});

function sanitizeName(in_name: string) {
  var name = in_name.trim();
  return name.slice(0, NAME_LENGTH_CONSTRAINT);
}

function sanitizeAge(in_age: number) {
  if (!Number.isInteger(in_age)) {
    throw new Error("Invalid age");
  }

  if (in_age > AGE_MAX) {
    throw new Error("Even ducks don't live that long");
  }

  if (in_age < AGE_MIN) {
    throw new Error("Even ducks don't start from negative");
  }

  return in_age;
}

function transformInput(in_name: unknown, in_age: unknown) {
  const name = sanitizeName(String(in_name));
  const age = sanitizeAge(Number(in_age));
  return { name, age };
}

async function getNameAndAge() {
  const name = await rl.question("What is your name? ");
  const age = Number(await rl.question("What is your age? "));

  rl.close();
  return { name, age };
}

const { name: rawName, age: rawAge } = await getNameAndAge();

const { name, age } = transformInput(rawName, rawAge);

const sql = `INSERT INTO people(name, age) VALUES(?, ?)`;

db.run(sql, [name, age]);

db.close();
