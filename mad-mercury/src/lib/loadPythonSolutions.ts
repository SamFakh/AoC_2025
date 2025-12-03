import { execSync } from "node:child_process";
import { readFileSync, readdirSync } from "node:fs";
import { fileURLToPath } from "node:url";
import { dirname, join } from "node:path";

export interface PythonSolution {
  filename: string;
  code: string;
  output: string;
  timeMs: number;
}

export function loadPythonSolutions(folderName: string): PythonSolution[] {
  // Resolve absolute location of this file
  const thisFile = fileURLToPath(import.meta.url);
  const thisDir = dirname(thisFile);

  // Path to AoC_2025 directory
  const projectRoot = join(thisDir, "..");

  // Final directory containing Python scripts
  const fullDir = join(projectRoot, folderName);

  const files = readdirSync(fullDir).filter((f) => f.endsWith(".py"));

  return files.map((filename) => {
    const fullPath = join(fullDir, filename);
    const code = readFileSync(fullPath, "utf8");

    let output = "";
    let timeMs = 0;

    try {
      const start = performance.now();
      output = execSync(`python3 "${fullPath}"`, { encoding: "utf8" });
      timeMs = performance.now() - start;
    } catch (err) {
      output = "⚠️ Error running script:\n" + err;
    }

    return { filename, code, output, timeMs };
  });
}
