#!/usr/bin/env python3
"""music.wordnspirit.com pilot build v2 — TEXT-ONLY design (Abe, 2026-10-22).
Branding: 陳曉東｜聖言音匠工作室. No 基督燈台事工 on this site; footer points
to devotions.wordnspirit.com. No images anywhere (Suno cover art removed);
typography only. Media served locally via symlinks for preview; in
production the videos live on R2 (media.wordnspirit.com).
"""
import json, os, html

ROOT = os.path.dirname(os.path.abspath(__file__))
PILOT = os.path.join(ROOT, "..", "music-pilot", "think-on-these-things")
SITE = os.path.join(ROOT, "site")

song = json.load(open(os.path.join(PILOT, "song.json"), encoding="utf-8"))
SLUG = song["slug"]

SECTION_LABELS = {
    "Verse 1": "主歌", "Verse 2": "主歌二", "Pre-Chorus": "導歌",
    "Chorus": "副歌", "Bridge": "橋段",
}

def lyrics_html(raw: str) -> str:
    out, cur_head, cur_lines = [], None, []
    def flush():
        if cur_head is not None:
            label = SECTION_LABELS.get(cur_head, cur_head)
            body = "<br>\n".join(html.escape(l) for l in cur_lines if l.strip())
            out.append(f'<section class="lyr"><h3>{html.escape(label)}</h3><p>{body}</p></section>')
    for line in raw.split("\n"):
        line = line.strip()
        if line.startswith("[") and line.endswith("]"):
            flush(); cur_head = line[1:-1]; cur_lines = []
        else:
            cur_lines.append(line)
    flush()
    return "\n".join(out)

def dur_fmt(sec: float) -> str:
    m, s = divmod(int(round(sec)), 60)
    return f"{m}:{s:02d}"

CSS = """
:root{--gold:#c9a227;--purple:#8b6fd8;--purple-d:#5b2a86;--ink:#f2ead8;--dim:#a99f8a;--bg:#0a0a0a;--line:#2a251c}
*{margin:0;padding:0;box-sizing:border-box}
body{background:var(--bg);color:var(--ink);font-family:"Noto Sans CJK TC","PingFang TC","Microsoft JhengHei",sans-serif;line-height:1.8}
a{color:var(--gold)}
header{border-bottom:2px solid var(--gold);padding:30px 20px 20px;text-align:center}
.brand{font-family:"Noto Serif CJK TC",serif;font-size:30px;letter-spacing:.18em;color:var(--ink);font-weight:700}
.brand .gold{color:var(--gold)}
.brand small{display:block;font-family:"Noto Sans CJK TC",sans-serif;font-size:11px;letter-spacing:.55em;color:var(--dim);margin-top:8px;font-weight:400}
main{max-width:820px;margin:0 auto;padding:34px 22px 64px}
.tagline{text-align:center;color:var(--dim);font-size:16.5px;margin-bottom:40px;font-family:"Noto Serif CJK TC",serif}
h2.sec{font-family:"Noto Serif CJK TC",serif;color:var(--gold);font-size:21px;letter-spacing:.25em;border-bottom:1px solid var(--line);padding-bottom:8px;margin:40px 0 18px}
.index-row{display:flex;align-items:baseline;gap:18px;padding:20px 4px;border-bottom:1px solid var(--line);text-decoration:none;color:var(--ink)}
.index-row .no{font-family:"Noto Serif CJK TC",serif;color:var(--purple);font-size:15px;letter-spacing:.2em}
.index-row .t{font-family:"Noto Serif CJK TC",serif;font-size:25px}
.index-row .m{margin-left:auto;color:var(--dim);font-size:14px;text-align:right;white-space:nowrap}
.index-row:hover .t{color:var(--gold)}
.note{color:var(--dim);font-size:15px}
.kicker{text-align:center;color:var(--purple);letter-spacing:.45em;font-size:13px;margin-bottom:10px}
h1.song{font-family:"Noto Serif CJK TC",serif;font-size:44px;color:var(--gold);text-align:center;margin:6px 0 6px;letter-spacing:.06em}
.sub{text-align:center;color:var(--dim);margin-bottom:10px;font-size:15px}
.scripture{text-align:center;font-family:"Noto Serif CJK TC",serif;border-top:1px solid var(--purple-d);border-bottom:1px solid var(--purple-d);padding:16px 12px;margin:24px 0 8px;font-size:17.5px}
audio{width:100%;margin:8px 0 4px}
video{width:100%;background:#000;border:1px solid var(--line)}
.qbar{margin:12px 0 4px;font-size:14px;color:var(--dim)}
.qbar button{background:transparent;color:var(--ink);border:1px solid var(--purple-d);padding:6px 16px;margin-right:8px;cursor:pointer;font-size:14px;font-family:inherit}
.qbar button.on{border-color:var(--gold);color:var(--gold)}
.hint{font-size:13px;color:var(--dim)}
.lyr{margin-bottom:22px}
.lyr h3{color:var(--purple);font-size:14px;letter-spacing:.35em;margin-bottom:5px;font-weight:400}
.lyr p{font-size:17px}
.back{display:inline-block;margin-top:34px;color:var(--dim);text-decoration:none;font-size:14.5px}
footer{border-top:2px solid var(--gold);text-align:center;color:var(--dim);padding:22px 20px;font-size:14.5px;line-height:1.9}
footer .fb{font-family:"Noto Serif CJK TC",serif;color:var(--ink);letter-spacing:.15em}
@media(max-width:600px){.brand{font-size:21px;letter-spacing:.1em}h1.song{font-size:32px}.index-row .t{font-size:21px}.index-row .m{font-size:12.5px}}
"""

HEADER = """<header><div class="brand">陳曉東<span class="gold">｜</span>聖言音匠工作室<small>MUSIC.WORDNSPIRIT.COM</small></div></header>"""
FOOTER = """<footer><div class="fb">陳曉東｜聖言音匠工作室</div>聖言靈禱 <a href="https://devotions.wordnspirit.com" target="_blank" rel="noopener">devotions.wordnspirit.com ↗</a></footer>"""

def page(title, desc, body, depth=0):
    p = "../" * depth
    return f"""<!DOCTYPE html>
<html lang="zh-Hant"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:type" content="website">
<link rel="stylesheet" href="{p}assets/style.css">
</head><body>{HEADER}<main>{body}</main>{FOOTER}</body></html>"""

os.makedirs(os.path.join(SITE, "assets"), exist_ok=True)
os.makedirs(os.path.join(SITE, SLUG), exist_ok=True)
os.makedirs(os.path.join(SITE, "media", SLUG), exist_ok=True)
open(os.path.join(SITE, "assets", "style.css"), "w", encoding="utf-8").write(CSS)
# drop any stale image links from v1
for stale in ("cover.jpg", "poster.jpg"):
    fp = os.path.join(SITE, "media", SLUG, stale)
    if os.path.lexists(fp): os.remove(fp)

MEDIA_MAP = {song["audio_file"]: "audio.mp3", "video-720p.mp4": "video-720p.mp4", "video-480p.mp4": "video-480p.mp4"}
for src, dst in MEDIA_MAP.items():
    link = os.path.join(SITE, "media", SLUG, dst)
    if os.path.lexists(link): os.remove(link)
    os.symlink(os.path.abspath(os.path.join(PILOT, src)), link)

M = f"media/{SLUG}"
# Production: videos are served from R2 at media.wordnspirit.com (set env
# MUSIC_VIDEO_BASE to switch the generated <video> sources to absolute URLs).
VID = os.environ.get("MUSIC_VIDEO_BASE", f"../{M}")
index_body = f"""
<p class="tagline">把聖言唱出來——獻給每一位願意聆聽的朋友。<br>點開就能聽，不用註冊，不用安裝任何軟件。</p>
<h2 class="sec">作品目錄</h2>
<a class="index-row" href="{SLUG}/">
<span class="no">01</span>
<span class="t">《{html.escape(song['title'])}》</span>
<span class="m">{html.escape(song['scripture'])}<br>詩歌 · {dur_fmt(song['duration_sec'])}</span>
</a>
"""
open(os.path.join(SITE, "index.html"), "w", encoding="utf-8").write(
    page("陳曉東｜聖言音匠工作室", "聖言音匠工作室：把聖言唱出來。點開就能聽的詩歌。", index_body))

song_body = f"""
<p class="kicker">聖言音匠工作室 · 詩歌</p>
<h1 class="song">《{html.escape(song['title'])}》</h1>
<p class="sub">經文：{html.escape(song['scripture'])} · 時長 {dur_fmt(song['duration_sec'])}</p>
<div class="scripture">「凡是真實的、可敬的、公義的、清潔的、可愛的、有美名的，若有甚麼德行，若有甚麼稱讚，這些事你們都要思念。」——腓立比書 4:8</div>

<h2 class="sec">聽歌</h2>
<audio controls preload="metadata" src="../{M}/audio.mp3"></audio>
<p class="hint">MP3 約 6.6MB，點播放即邊下載邊播；網絡慢時稍等幾秒。</p>

<h2 class="sec">看 MV</h2>
<video id="mv" controls preload="none" playsinline>
<source src="{VID}/video-720p.mp4" type="video/mp4">
</video>
<div class="qbar">畫質：
<button id="q720" class="on" onclick="setq(720)">720p 高清</button>
<button id="q480" onclick="setq(480)">480p 省流量</button>
<span class="hint">網絡慢請選 480p（約 35MB）；720p 約 80MB。</span></div>

<h2 class="sec">歌詞</h2>
{lyrics_html(song['lyrics'])}

<h2 class="sec">製作</h2>
<p class="note">詞／曲出處：腓立比書 4:8–9。製作：陳曉東・聖言音匠工作室。</p>
<a class="back" href="../">← 回作品目錄</a>
<script>
var v=document.getElementById('mv');
function setq(q){{var t=v.currentTime,p=!v.paused;
v.src='{VID}/video-'+q+'p.mp4';v.load();
document.getElementById('q720').className=q==720?'on':'';
document.getElementById('q480').className=q==480?'on':'';
v.addEventListener('loadedmetadata',function h(){{v.currentTime=t;if(p)v.play();v.removeEventListener('loadedmetadata',h);}});}}
</script>
"""
open(os.path.join(SITE, SLUG, "index.html"), "w", encoding="utf-8").write(
    page(f"《{song['title']}》｜聖言音匠工作室", f"《{song['title']}》——腓立比書 4:8–9。點開就能聽的詩歌。", song_body, depth=1))

print("built v2 (text-only):", SITE)
