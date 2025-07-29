# Timezones Are Hard

> “What time works for you?”  
> "Uh… let me just look up what time 3pm EST is in my city… again."

Welcome to Tui-Zone.

## What Is This?

This is the app I built out of *pure frustration*, a (c)lifeline for anyone who’s ever:

- Missed a meeting because they thought PST stood for Perpetual Scheduling Trauma.
- Scheduled a call at 3am because "I thought you meant c u next YOUR Tuesday."
- Said “UTC is the truth” and then immediately looked up a converter.
– Debated whether DST is a global conspiracy… or just a Queensland cow protection policy (moo 🐄)

If you’ve ever tried to arrange a meeting across 4+ timezones, you know:  
**time isn’t real.** Or at least it’s not consistently configured across the globe.

## The Problem With Time

Time is relentless. It never stops, never pauses, never gives you a breather.  
You can argue about calendars, daylight saving, or whether it’s “Tuesday there already?” 
but time just keeps marching on utterly indifferent to your confusion.

You can't reason with it.  
You can't fight it.  
You can only try to *compute* it... and maybe build an app to help.

## Why I Built This

Every global team conversation turns into a philosophical debate about “what time even *is*.” So I snapped. I built this app to:

- Visualise who’s theoretically awake *right now*, breakfast is cultural bullying.
- Avoid the nightmare of DST shifts half-hour zones and regions that just said “nah” to time rules (looking at you... Adelaide).
- Help me *stop asking the AI what UTC+3 is* every single day, so it stops learning my primal routines.

## Tech Stack

- Python, because whatever. 
- A cli of some sort, I think most computers come with that these days.
- Text editor, vi vi vi 🤘


## Known Issues

- Time remains linear and irreversible.  
- We can’t stop meetings at 6am only inform you of them.
- Philosophical dread not included but highly likely.


## Installing

```
cd ~/
git clone https://github.com/benzies/tui-zone-compare.git
python3 -m venv Tui-Zone
source Tui-Zone/bin/activate
python3 -m pip install rich pytz tomli
python tz-view-config.py
```

## Configuration
```
vi config.toml
```

Find whatever timezone you want to see using this https://en.wikipedia.org/wiki/List_of_tz_database_time_zones


