""" -wsl
python3 make_json.py --dir [DIR]
"""

import json, subprocess, glob, os, sys, argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dir", required=True, help="문제 디렉토리")
    parser.add_argument("--solution", help="정답 실행 파일 경로 (기본: <dir>/solution)")
    parser.add_argument("--inputs", help="입력 파일 디렉토리 (기본: <dir>/input)")
    parser.add_argument("--output", help="결과 JSON 경로 (기본: <dir>/data.json)")
    parser.add_argument("--timeout", type=float, default=5.0)
    args = parser.parse_args()

    solution = os.path.abspath(args.solution or os.path.join(args.dir, "solution"))
    inputs   = args.inputs  or os.path.join(args.dir, "input")
    output   = args.output  or os.path.join(args.dir, "data.json")

    input_files = sorted(glob.glob(os.path.join(inputs, "*.txt")))
    if not input_files:
        print(f"[!] no input: {inputs}", file=sys.stderr)
        sys.exit(1)

    data = []
    for path in input_files:
        with open(path) as f:
            inp = f.read()
        res = subprocess.run(
            [solution], input=inp,
            capture_output=True, text=True, timeout=args.timeout,
        )
        if res.returncode != 0:
            print(f"[!] {path} run failed: {res.stderr}", file=sys.stderr)
            continue
        data.append({
            "input": inp.rstrip("\n"),
            "expected_output": res.stdout.rstrip("\n"),
        })

    with open(output, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"[+] {len(data)} saved. → {output}")

if __name__ == "__main__":
    main()