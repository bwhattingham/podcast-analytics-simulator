import argparse
import subprocess
import sys

def main():
    parser = argparse.ArgumentParser(description="Podcast Analytics CLI Tool")

    parser.add_argument("--episode", nargs=1, help="Analyze a single episode JSON file")
    parser.add_argument("--compare", nargs=2, help="Compare two episode JSON files")

    args = parser.parse_args()

    if args.episode:
        episode_path = args.episode[0]
        subprocess.run(["python3", "scripts/analyze_episode.py", episode_path])
        return

    if args.compare:
        ep1, ep2 = args.compare
        subprocess.run(["python3", "scripts/compare_episodes.py", ep1, ep2])
        return

    print("No valid arguments provided. Use --help for options.")

if __name__ == "__main__":
    main()
