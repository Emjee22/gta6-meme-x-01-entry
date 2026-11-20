// Entry point for the gta6-meme-x-01 bounty (Node 22, standard library
// only). The entry is the X post itself: this program only copies
// POST.json, which names the post's address, from the repository root to
// the output directory, where the gate reads it. Nothing it writes about
// the post is judged; the house reads the post from X.
//
// The copy is byte for byte and the program does no other I/O, so two
// runs from any working directory write identical output.
//
// Run it the way the grader does:
//   mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync, mkdirSync } from 'node:fs';
import { join } from 'node:path';

const botDir = process.env.MAKEFUN_BOT_DIR ?? '/bot';
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';

mkdirSync(outDir, { recursive: true });
try {
  copyFileSync(join(botDir, 'POST.json'), join(outDir, 'POST.json'));
} catch (err) {
  console.error(`POST.json could not be copied from ${botDir}: ${(err as Error).message}`);
  process.exit(1);
}
