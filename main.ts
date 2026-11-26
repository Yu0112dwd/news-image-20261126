// Entry program for news-image-20261126 (Node 22, stdlib only).
//
// The repository holds the finished picture, entry.png: a newspaper
// front page summing up Thursday 26 November 2026, drawn by draw.py.
// This program only validates that picture against the gate and
// copies it to the output directory the grader reads.
//
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const MAX_BYTES = 1048576;
const MAX_SIDE = 1024;
const PNG_SIG = [0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a];

function fail(message) {
  throw new Error(message);
}

function checkPng(data) {
  if (data.length < 24) fail("entry.png is too short to be a PNG");
  for (let i = 0; i < PNG_SIG.length; i += 1) {
    if (data[i] !== PNG_SIG[i]) fail("entry.png does not start with the PNG signature");
  }
  if (data.length > MAX_BYTES) {
    fail(`entry.png is ${data.length} bytes, over the ${MAX_BYTES} byte limit`);
  }
  const w = data.readUInt32BE(16);
  const h = data.readUInt32BE(20);
  if (w > MAX_SIDE || h > MAX_SIDE) {
    fail(`entry.png is ${w}x${h}, over the ${MAX_SIDE}x${MAX_SIDE} limit`);
  }
  return { w, h };
}

const root = dirname(fileURLToPath(import.meta.url));
const image = readFileSync(join(root, "entry.png"));
const { w, h } = checkPng(image);

const destDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
mkdirSync(destDir, { recursive: true });
const dest = join(destDir, "entry.png");
writeFileSync(dest, image);

// The grader runs this program twice and both runs must produce the
// same bytes, so verify the written copy matches the source exactly.
const written = readFileSync(dest);
if (!written.equals(image)) fail("the output copy differs from entry.png");
console.log(`OK: wrote entry.png (${image.length} bytes, ${w}x${h})`);
