# sfx-translator-assistant
Suggests Ukrainian manga sound effects for English ones, based on phonetic similarity and panel context.


## Context tags

Every sound effect gets exactly one of these six tags. Tag by what
physically makes the sound, not by how the scene feels — a punch in a
sad moment is still `impact`.

| Tag | Covers | Examples |
| --- | --- | --- |
| `impact` | Collisions, hits, explosions, things breaking | wham, bang, crash, thud |
| `motion` | Movement through space, speed, air displacement | whoosh, dash, zoom, flutter |
| `body` | Involuntary body sounds with no words in them | doki doki, gulp, pant, sniff |
| `voice` | Vocal sounds that aren't speech | gasp, mumble, giggle, scream |
| `object` | Materials and handling, texture, small noises | rustle, clink, creak, drip |
| `mood` | Atmosphere with no physical source at all | silence, sparkle, tension, gloom |

## Dataset

`data/sfx_pairs.csv` — one row per *occurrence* of a sound effect, not
per unique sound, so that frequency is preserved.

| Column | What it holds |
| --- | --- |
| `id` | Row number |
| `series` | Which manga |
| `chapter` | Chapter number |
| `panel` | Where to find it again, e.g. `p14-3` |
| `sfx_en` | The English sound effect |
| `sfx_ja` | The Japanese original, when legible. Optional |
| `sfx_ua` | My Ukrainian translation |
| `context` | One of the six tags above |
| `intensity` | My own 1–3 rating of how loud or big it is |
| `notes` | Anything worth remembering |