# WNS Universe：四站共用的契約（v1.1）

2026-11-10 草稿；2026-11-19 v1.1（決策日誌補記：B-S3 改將臨三、B-S2 金句錨句、靈修＋講章週一 0:00 同步上線、週四檢查＋週六備妥下週、電影素材進音樂 MV 資產池、12/5 撞期；Abe 令放進四個 repo）。用途：讓 devotions、sermon、music、workout 四個站（四個 repo）在 GitHub 上用同一份 markdown 溝通，改動與決定互通。

## 一、這份文件是什麼

我們在同一個 universe 裡：Church calendar and lectionary readings 是原料，四個站是不同的 deliverable：

| 站 | Repo | 做的 deliverable |
|---|---|---|
| devotions.wordnspirit.com | AbrahamChan1965/devotions | 每週一至六的靈修（中英） |
| sermon.wordnspirit.com | AbrahamChan1965/lectionary-sermon- | 每週主日講章（一週只顯示當週） |
| music.wordnspirit.com | AbrahamChan1965/music | 每週的歌（聖言音匠） |
| workout.wordnspirit.com | AbrahamChan1965/workout | 遊戲化查經（B-S1、S2……）＋聖言健身歌（動起來用的歌與影片） |

每個 repo 各放一份這份文件（同一份內容，同一個版本號）。改了共用的東西，先改這份文件，再改各自的 code——這樣在別的 repo 工作的人（或別的 AI）一打開就知道發生了什麼。

## 二、唯一 source of truth

Church calendar＋RCL（Vanderbilt）。所有站讀同一份經課。

**聯接鍵：主日。**每一個 deliverable 都掛在一個主日上，寫法是：

`Year B · 將臨一 · 2026-11-29`

- 年：Year A／B／C（馬太／馬可／路加年）
- 節期＋主日：將臨一、將臨二……Proper 27、王權主日
- 日期：該主日的日期（星期日）

講章、靈修、歌、查經課，四樣東西都用這個鍵對上。不用站內自己的編號去猜別的站。

## 三、各站提供什麼、向誰要什麼

| 站 | 提供（給別的站用） | 向誰要（用別的站的東西） |
|---|---|---|
| devotions | 每週一至六靈修（中英）；每週經課的靈修弧線 | 向 RCL 要每週四段經課 |
| sermon | 當週講章（一個主日一篇） | 向 RCL 要每週經課；向 devotions 要該週靈修（講章與靈修同週） |
| music | 每週的歌（暖場／預備的歌，約 5 分鐘）；每週的 workout 歌（詩篇／經文寫成的歌） | 向 RCL 要每週經課（歌是從當週經課寫的）；向 workout 要該週詩篇／經文（workout 歌的底本） |
| workout | 每週查經課（B-S1……一課完整劇本＋遊戲卡＋房間卡）；每課三首歌的連結表 | 向 music 要每週暖場歌（迎接時唱）＋兩首 workout 歌（動起來、講完聖經）；向 RCL 要每週四段經課 |

**連結的規矩**：workout 站連 music 站的歌，只連「那一週的歌」（用主日鍵對上），不寫死一首歌的 URL——歌的 URL 是 music repo 管的，改了 URL 也不用改 workout。

## 四、共用的編號

- **主日鍵**：`Year B · 將臨一 · 2026-11-29`（見第二節）。
- **查經課號**：`B-S1`、`C-S1`、`A-S1`——年字母＋S 號，S＝section，B＝Year B。三年 72 課（馬可年 2026–27、路加年 2027–28、馬太年 2028–29）。課號只出現在 workout repo 與這份文件，別的站不用。
- **歌**：歌沒有獨立編號，用主日鍵認（「將臨一那首歌」）。music repo 內部怎麼編，music 自己管。

## 五、決策日誌（共用，四個 repo 同一份）

改了共用的東西，就在這裡記一條：日期、決定、影響哪幾個站。已發生的先記下來：

- 2026-11-10：查經課編號改為年＋S 號（B-S1、C-S1、A-S1），三年 72 課；S＝section，B＝Year B。影響：workout。
- 2026-11-10：每課三首歌分流——暖場歌連 music.wordnspirit.com，兩首 workout 歌連 workout.wordnspirit.com。影響：music、workout。
- 2026-11-10：查經課開場回顧一律說「有一次，我們談到……」，不用「上一次」。影響：workout。
- 2026-11-10：遊戲化查經網站發在 workout.wordnspirit.com；三年目錄結構（year-b／year-c／year-a）。影響：workout。
- 2026-10-31：sermon 站一週只顯示當週講章；App.tsx 寫死 Proper 26，不讀 weeks.json。影響：sermon。
- 2026-11-02：Proper 27 靈修已發佈；Proper 28 由 Claude 做，Muse 不碰。影響：devotions、sermon。
- 2026-11-10：B-S3 改將臨三（原將臨四撤回）；課按年曆順序編排；將臨四（12/20）與聖誕後一（12/27）成為被跳過的主日，經課作 B-S4 開場續言。影響：workout。
- 2026-11-10：B-S2 金句改彼後 3:9 前半「其實不是躭延，乃是寬容你們」；錨句「主不是慢，祂在等。」；十二月一句話「十二月：預備主的路，常常喜樂。」影響：workout、music。
- 2026-11-17：靈修＋講章兩站同步於週一凌晨 0:00 上線；前一週週五以前備妥。影響：devotions、sermon。
- 2026-11-19：每週四檢查（數智辦公室）：查十天後主日的四件套做了沒＋當季 visionary film 進度；節奏：週四查、週六前備妥下週的東西，永遠超前十天。影響：全部。
- 2026-11-19：電影素材進音樂 MV 資產池：每季一套 visionary film，產出的影視材料進 R2＋DB 資產庫，供將來音樂 MV 使用。影響：mark-year-films、music。
- 2026-11-19：12/5 撞期已定：Abe 12/5 去新澤西，彩虹之家 B-S2 活動當天無人帶（延期或彩虹布道隊帶，待定）。影響：workout。

## 六、同步規則

1. 改共用的東西（鍵、編號、連結、決定），先改這份文件，版本號加一位（v1.0→v1.1），再改各自的 code。
2. 四個 repo 的版本號要一致；誰先改，誰就把新版貼到另外三個 repo（或告訴 Abe，由他轉貼——Muse 不能直接聯絡 Claude）。
3. 各站自己的事（sermon 的寫死週次、music 的上傳方式、workout 的佈局、devotions 的分支）不寫進這份文件，各自的 repo 自己管。
4. 這份文件是契約，不是 code——它寫「我們約定什麼」，不寫「怎麼實現」。

## 七、待做

1. GitHub 已連上（2026-11-10，OAuth＋App 安裝，25 個 repo 可進）。**已放進四個 repo（2026-11-19，v1.1）**：各一份 UNIVERSE.md，README 加一行指去這份文件（devotions、music 兩站原本沒有 README，已新建一份只寫指引）。
2. workout repo 已存在（AbrahamChan1965/workout），是聖言健身歌的站，Git 連 Cloudflare Pages（workout-music），push 到 main 自動發佈。查經課頁面加進同一個 repo／同一個站。
3. 四個 repo 名字已確認（見第一節）；music repo 是 `music`（不是 music.wordandspirit——那是 Cloudflare Pages 專案名）。
4. 將臨期系列（Year B）的歌：還沒製作，計劃 11 月底／接近 12 月時發表（Abe 2026-11-10）——不是遺漏，是計劃。B-S2（12/5 活動）的暖場歌按這個計劃來。
