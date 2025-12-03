import { execSync } from "node:child_process";
import { readFileSync, readdirSync } from "node:fs";
import { join } from "node:path";

export interface PythonSolution {
  filename: string;
  code: string;
  output: string;
}

export function loadPythonSolutions(path: string): PythonSolution[] {
  const files = readdirSync(path).filter((f) => f.endsWith(".py"));

  return files.map((filename) => {
    const fullPath = join(path, filename);
    const code = readFileSync(fullPath, "utf8");

    let output = "";
    try {
      output = execSync(`python3 "${fullPath}"`, { encoding: "utf8" });
    } catch (err) {
      output = "⚠️ Error running script:\n" + err;
    }

    return { filename, code, output };
  });
}
