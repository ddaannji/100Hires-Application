from pathlib import Path
import re

from youtube_transcript_api import YouTubeTranscriptApi


VIDEOS = [
    {
        "expert": "Jeremy Chatelaine",
        "slug": "jeremy-chatelaine",
        "channel": "Jeremy Chatelaine",
        "title": "Proven Cold Email Structure That Gets Replies (7 Steps)",
        "video_id": "wFzoXKha4gQ",
        "upload_date": "2025-08-27",
        "url": "https://www.youtube.com/watch?v=wFzoXKha4gQ",
        "query": "Jeremy Chatelaine QuickMail cold outreach",
    },
    {
        "expert": "Jack Reamer",
        "slug": "jack-reamer",
        "channel": "Charles Cormier Podcast - Founder Wisdom",
        "title": "copywriting with salesbread founder jack reamer",
        "video_id": "9_Isu6MNlio",
        "upload_date": "2024-06-28",
        "url": "https://www.youtube.com/watch?v=9_Isu6MNlio",
        "query": "Jack Reamer SalesBread cold outreach",
    },
    {
        "expert": "Alex Vacca",
        "slug": "alex-vacca",
        "channel": "Alex Vacca",
        "title": "The Best Cold Email Strategy for 2026",
        "video_id": "90ZFgqRSErg",
        "upload_date": "2026-01-27",
        "url": "https://www.youtube.com/watch?v=90ZFgqRSErg",
        "query": "Alex Vacca ColdIQ cold email",
    },
    {
        "expert": "Eric Nowoslawski",
        "slug": "eric-nowoslawski",
        "channel": "Eric Nowoslawski",
        "title": "I sent 10,000,000 cold emails, here's what works in 2025",
        "video_id": "cfpLJqkmB6I",
        "upload_date": "2025-11-11",
        "url": "https://www.youtube.com/watch?v=cfpLJqkmB6I",
        "query": "Eric Nowoslawski Growth Engine cold email",
    },
    {
        "expert": "Patrick Spychalski",
        "slug": "patrick-spychalski",
        "channel": "Patrick Spychalski",
        "title": "How To Write Great Email Copy",
        "video_id": "BGmZ0cdJjDc",
        "upload_date": "2024-02-21",
        "url": "https://www.youtube.com/watch?v=BGmZ0cdJjDc",
        "query": "Patrick Spychalski The Kiln cold email",
    },
    {
        "expert": "Patrick Dang",
        "slug": "patrick-dang",
        "channel": "Patrick Dang",
        "title": "How to Master COLD EMAIL in 7 Minutes",
        "video_id": "ZEoKxFJpw_E",
        "upload_date": "2024-06-20",
        "url": "https://www.youtube.com/watch?v=ZEoKxFJpw_E",
        "query": "Patrick Dang cold email",
    },
    {
        "expert": "Samantha McKenna",
        "slug": "samantha-mckenna",
        "channel": "Apollo",
        "title": "Complete COLD EMAIL COURSE And It's 100% FREE",
        "video_id": "H5zsGa9FeuI",
        "upload_date": "2024-10-23",
        "url": "https://www.youtube.com/watch?v=H5zsGa9FeuI",
        "query": "Samantha McKenna Show Me You Know Me cold email",
    },
    {
        "expert": "Yurii Veremchuk",
        "slug": "yurii-veremchuk",
        "channel": "Woodpecker.co",
        "title": "How to master cold email in 6 minutes (step-by-step guide)",
        "video_id": "8Fo8nsfNZxQ",
        "upload_date": "2024-06-27",
        "url": "https://www.youtube.com/watch?v=8Fo8nsfNZxQ",
        "query": "Yurii Veremchuk Woodpecker cold email",
    },
    {
        "expert": "Jay Feldman",
        "slug": "jay-feldman",
        "channel": "HighLevel",
        "title": "Spotlight Session - Dr. Jay Feldman - Supercharging Your Agency with Cold Email Mastery",
        "video_id": "cZeF9OdC-fk",
        "upload_date": "2025-01-17",
        "url": "https://www.youtube.com/watch?v=cZeF9OdC-fk",
        "query": "Jay Feldman cold email agency",
    },
    {
        "expert": "Matthew Lucero",
        "slug": "matthew-lucero",
        "channel": "Matt Lucero",
        "title": "How To Book 30 Sales Calls Per Month Using Cold Email",
        "video_id": "hz6AC0p3GXc",
        "upload_date": "2023-07-20",
        "url": "https://www.youtube.com/watch?v=hz6AC0p3GXc",
        "query": "Matthew Lucero SaaS cold email",
    },
]


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def format_timestamp(seconds: float) -> str:
    total = int(seconds)
    hours = total // 3600
    minutes = (total % 3600) // 60
    secs = total % 60
    if hours:
        return f"{hours:02d}:{minutes:02d}:{secs:02d}"
    return f"{minutes:02d}:{secs:02d}"


def build_index(root: Path, rows: list[str]) -> None:
    lines = [
        "# YouTube Transcripts",
        "",
        "Public YouTube transcripts collected on 2026-04-02 with `youtube-transcript-api`.",
        "",
        "Each expert folder contains one selected transcript markdown file with metadata and timestamped text.",
        "",
        "| Expert | Upload Date | Video | Transcript |",
        "|---|---|---|---|",
    ]
    lines.extend(rows)
    (root / "README.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_transcripts() -> None:
    repo_root = Path(__file__).resolve().parents[1]
    transcripts_root = repo_root / "research" / "youtube-transcripts"
    transcripts_root.mkdir(parents=True, exist_ok=True)

    api = YouTubeTranscriptApi()
    index_rows = []

    for video in VIDEOS:
        transcript = api.fetch(video["video_id"], languages=["en"])
        expert_dir = transcripts_root / video["slug"]
        expert_dir.mkdir(parents=True, exist_ok=True)

        filename = f"{video['upload_date']}-{slugify(video['title'])}-{video['video_id']}.md"
        output_path = expert_dir / filename

        lines = [
            f"# {video['title']}",
            "",
            f"- Expert: {video['expert']}",
            f"- Channel: {video['channel']}",
            f"- Upload date: {video['upload_date']}",
            f"- Video URL: {video['url']}",
            f"- Search query used: `{video['query']}`",
            f"- Video ID: `{video['video_id']}`",
            "",
            "## Transcript",
            "",
        ]

        for item in transcript:
            lines.append(f"[{format_timestamp(item.start)}] {item.text}")

        output_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        rel_path = output_path.relative_to(transcripts_root)
        index_rows.append(
            f"| {video['expert']} | {video['upload_date']} | {video['title']} | [{rel_path}]({rel_path.as_posix()}) |"
        )

    build_index(transcripts_root, index_rows)


if __name__ == "__main__":
    write_transcripts()
