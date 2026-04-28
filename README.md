Podcast Episode Analytics Simulator
This project simulates how podcast platforms track listener engagement and episode performance.
It uses fictional analytics data to demonstrate how retention, drop‑off points, and clip‑worthy moments can be analysed programmatically.
This is a safe, public demonstration of the kind of thinking that goes into evaluating podcast performance — without using any real data.


flowchart TD

    A[Fake Analytics JSON] --> B[Analysis Script]
    B --> C[Retention Summary]
    B --> D[Clip Suggestions]
    C --> E[Markdown Report]
    D --> E


podcast-analytics-simulator/
│
├── data/
│   ├── episode1.json
│
├── scripts/
│   ├── analyze_episode.py
│
└── README.md
