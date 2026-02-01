#!/usr/bin/env python3
"""
Focus Timer CLI - A simple Pomodoro timer with future Spotify integration.

Usage:
    python focus_timer.py [duration_minutes]
    
Default duration is 25 minutes (standard Pomodoro).
"""

import argparse
import sys
import time
from datetime import datetime, timedelta


def format_time(seconds: int) -> str:
    """Format seconds as MM:SS."""
    minutes = seconds // 60
    secs = seconds % 60
    return f"{minutes:02d}:{secs:02d}"


def clear_line():
    """Clear the current terminal line."""
    sys.stdout.write('\r' + ' ' * 50 + '\r')
    sys.stdout.flush()


def run_timer(duration_minutes: int, label: str = "Focus"):
    """Run a countdown timer with live display."""
    total_seconds = duration_minutes * 60
    end_time = datetime.now() + timedelta(minutes=duration_minutes)
    
    print(f"\n🍅 {label} Timer Started!")
    print(f"   Duration: {duration_minutes} minutes")
    print(f"   End time: {end_time.strftime('%H:%M:%S')}")
    print("-" * 40)
    
    try:
        for remaining in range(total_seconds, -1, -1):
            clear_line()
            progress = (total_seconds - remaining) / total_seconds
            bar_width = 30
            filled = int(bar_width * progress)
            bar = "█" * filled + "░" * (bar_width - filled)
            
            sys.stdout.write(f"\r⏱️  {format_time(remaining)} [{bar}] {int(progress * 100)}%")
            sys.stdout.flush()
            
            if remaining > 0:
                time.sleep(1)
        
        print("\n" + "-" * 40)
        print("✅ Timer complete! Great work! 🎉")
        print("\n🔔 DING DING DING!")
        
        # TODO: Add Spotify integration here
        # - Pause music when timer starts
        # - Resume/play celebration playlist when done
        
    except KeyboardInterrupt:
        clear_line()
        print("\n\n⏸️  Timer paused/cancelled.")
        remaining_mins = remaining // 60
        remaining_secs = remaining % 60
        print(f"   Time remaining: {remaining_mins}m {remaining_secs}s")
        sys.exit(0)


def main():
    parser = argparse.ArgumentParser(
        description="Focus Timer CLI - Pomodoro timer with future Spotify integration"
    )
    parser.add_argument(
        "duration",
        type=int,
        nargs="?",
        default=25,
        help="Timer duration in minutes (default: 25)"
    )
    parser.add_argument(
        "-s", "--short-break",
        action="store_true",
        help="Start a short break timer (5 minutes)"
    )
    parser.add_argument(
        "-l", "--long-break",
        action="store_true",
        help="Start a long break timer (15 minutes)"
    )
    
    args = parser.parse_args()
    
    if args.short_break:
        run_timer(5, "Short Break")
    elif args.long_break:
        run_timer(15, "Long Break")
    else:
        run_timer(args.duration, "Focus")


if __name__ == "__main__":
    main()
