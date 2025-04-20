# Supporting Independent Musicians: Building a Personalized Recommendation Engine with Interlude!


In today's music industry, independent artists face significant challenges in gaining exposure. Streaming platforms like Spotify are powerful but often prioritise mainstream content through their recommendation algorithms, leaving smaller artists in the shadows. With millions of tracks available and only limited real estate on a user's screen, algorithmic bias becomes a significant obstacle. To address this, we developed **Interlude!** — a personalized music discovery CLI application that empowers users to discover music based on their tastes while intentionally spotlighting independent creators.

---

## Understanding the Problem

The key issue lies in the **algorithmic favouritism** that shapes mainstream music discovery today. Spotify’s recommendation engine, while still effective at keeping users engaged, often reinforces popularity rather than diversity.

According to *The Verge*, Spotify’s “Discovery Mode” allows artists to trade royalties to increase their visibility, creating an uneven playing field ([The Verge, 2021](https://www.theverge.com/2021/3/25/22348429/spotify-discovery-mode-algorithm-payola-artists-music-industry)). Additionally, a study on *Medium* highlights how the vast majority of streaming revenue goes to the top percentile of artists, leaving independents with minimal earnings ([Medium, 2023](https://medium.com/music-technology/why-spotify-might-be-failing-independent-artists-9f071b8d5b6a)).

This presents the dual problem:
1. Users are limited in discovering niche or emerging artists/music they might enjoy.
2. Independent artists lack fair access to new audiences.

---

## Tackling Ethical & Technical Hurdles in Music Discovery
When creating a tool to help independent musicians get discovered, you're not just building software, you’re navigating a complex landscape of ethical choices and technical boundaries. With Interlude!, we faced both head-on.

## Ethical Considerations
### Algorithmic Bias
With most mainstream recommendation engines favor what's already trending, sidelining smaller, independent voices. We wanted Interlude! to flip that script to highlight what you love, not just what everyone else is playing.

### Data Privacy
User trust is everything. That’s why Interlude! stores user preferences locally, steering clear of cloud-based data mining or third-party storage.

### Transparency
Ever wonder why a song gets recommended to you? We believe users should be in the loop. Our system makes recommendations based solely on your own ratings and preferences—simple, transparent, and fair.

## Technical Limitations
Limited API Support for Indies

The Spotify API doesn’t explicitly tag music as “independent,” which makes indie-focused filtering tricky. This limitation inspired our idea to potentially incorporate alternative APIs like MusicBrainz or Last.fm in future versions.

### No Machine Learning (Yet)
Without machine learning, we can’t do real-time adaptive recommendations—yet. But our foundation is ready for it. Once we validate the core features, we aim to introduce ML to personalize even further.

### API Rate Limits
Like any developer using a public API, we hit speed bumps with Spotify’s rate limits. This means we have to be thoughtful about when and how often we make requests, especially when batch-processing large user libraries.

# Our Solution: Meet Interlude!
To start solving this problem, we built Interlude!, a Python-based command-line tool for music discovery and personal taste management.

With Interlude!, users can:

- Create profiles and store favorites locally (no cloud tracking!)

- Rate albums, songs, and artists they love

- Get curated new release recommendations

- View their listening profile in a clean, table-based layout

While it’s a work in progress, Interlude! is laying the groundwork for a future where indie artists can break through based on genuine listener taste, not just algorithmic trends.

---

## Reflections: Lessons Learned & Looking Ahead
Before diving into Interlude!, my experience with structured Python applications and real-world API integration was fairly limited. Most of my past work focused on smaller, isolated scripts—nothing that pulled together user interaction, data persistence, and ethical design all at once.

## What I Learned Along the Way
Working on Interlude! was a crash course in full-stack CLI development. I gained practical skills in:

 **API integration** – including OAuth setup, endpoint handling, and rate limit management using Spotify's API.

 **Modular programming** – designing clean, reusable Python classes for Users, Songs, Albums, and Artists.

 **Persistent storage** – using local JSON files to safely store user preferences without depending on the cloud.

 **CLI design** – improving user experience using libraries like prettytable, colorama, and rich.

 **Documentation & Git workflows** – writing clean docstrings, maintaining a .gitignore, and using GitHub for structured commits.

**Ethical awareness** – critically thinking about data privacy, algorithmic bias, and transparency throughout the build.

It wasn't just a technical learning experience it, deepened my understanding of how design choices impact users and creators in real with unfortunately, often unequal, ways.

## Technology Justification

| Tool/Framework       | Purpose                                                                 |
|----------------------|-------------------------------------------------------------------------|
| **Python**           | Simple syntax, strong ecosystem, ideal for CLI and API apps              |
| **Spotify API**      | Official source for music metadata, streaming links, artist info         |
| **requests/json**    | To fetch and handle HTTP + JSON responses                                |
| **prettytable/rich** | For formatted console outputs                                             |
| **colorama**         | To add color to the CLI for readability                                  |
| **Git & GitHub**     | Version control and collaboration                                        |

All dependencies are open-source and ethically licensed under MIT or Apache 2.0. This aligns with our project values: openness, transparency, and support for community-driven software.

---

## Step-by-Step Plan

### Phase 1: Research & Problem Validation
- Reviewed Spotify documentation and music industry commentary.
- Collected feedback from independent artists and listeners.

### Phase 2: Application Design
- Modular structure for maintainability (User, Album, Artist, Song modules).
- Rating system built for future learning/recommendation logic.

### Phase 3: Development
- CLI menus for user interaction.
- Local JSON file storage for account data.
- Spotify API integration for searching and browsing.

### Phase 4: Testing
- Manual testing of CLI functions.
- Validated authentication flow and API result handling.

### Phase 5: Documentation
- README with installation, usage, licensing, and ethical notes.
- In-code documentation with consistent PEP 257-style docstrings.

---

## Skills Learned

Before starting, I had limited experience working with APIs and structuring larger Python projects. Through this process, I’ve gained skills in:
- Handling API authentication and data fetching.
- Creating intuitive CLI apps with persistent storage.
- Documenting projects professionally.
- Ethical awareness in tech development.

---

## Reflections and Future Enhancements

### Challenges Faced
- Differentiating independent vs. commercial artists using Spotify alone.
- Implementing deeper personalization logic without machine learning.

### Unfinished Elements
- No direct Bandcamp or SoundCloud API integration yet.
- OAuth login not implemented; uses basic local authentication instead.

### Future Directions
- Add support for more artist platforms.
- Implement collaborative filtering using `Surprise` or `scikit-learn`.
- Create a web or mobile interface to widen accessibility.

---



## Conclusion

Interlude! is a first step toward more ethical, user-centered music discovery. It addresses a genuine industry problem by enabling music fans to find hidden gems and support indie musicians—fairly, transparently, and with purpose.

As platforms evolve, there's increasing demand for tools that blend ethical AI, transparent personalisation, and fair exposure for underrepresented artists. Interlude! sits at the intersection of these trends by prioritising user driven recommendations and offering a roadmap for ML integration. Future innovation in this space will likely be shaped by open data standards, federated learning, and artist-owned distribution platforms.


By sharing this project openly, we hope to encourage further innovation in the space and inspire others to build tools that support the creators behind the music we love.

> Check out the [GitHub](https://github.com/tshort11/ISK002-ll.git) and try Interlude! today!
