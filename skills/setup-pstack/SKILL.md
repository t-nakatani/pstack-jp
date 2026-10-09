---
name: setup-pstack
description: "pstackが役割ごとに使うモデルと推論予算を設定します。利用可能なモデルを調べ、スキルの初期設定を上書きする常時適用のルールを書きます。/setup-pstack、モデル設定、予算設定、モデル変更の依頼に使います。"
---

<a id="setup-pstack"></a>

# pstack のセットアップ

`~/.cursor/rules/pstack-models.mdc` を書き込みます。これは、役割ごとに pstack のモデルを設定する常に適用されるルールです。

<a id="steps"></a>

## の手順

<a id="1-detect-available-models"></a>

### 1. 利用可能なモデルの検出

このセッションで `Task` サブエージェントに渡すことができるモデル スラグを列挙します。それが信頼できる情報源です。 Cursor が、ユーザーの資格のあるモデルをリストするモデル API または CLI も公開する場合は、完全性を高めるために、それを優先します。何も検出できない場合は、アクセス権のあるスラッグを貼り付けるようにユーザーに依頼してください。利用可能であることを確認していない本物のスラッグは決して書き込まないでください。エイリアス `inherit-parent` および `auto` は、スラッグとして検出されない場合でも常に有効です。

<a id="2-load-current-state"></a>

### 2. 負荷の現在の状態

デフォルトのロールとモデルのマッピングは、以下の手順 5 に示すルール形状です。 `~/.cursor/rules/pstack-models.mdc` がすでに存在する場合は、それを読み取り、その `# budget` 行とそのロール値を現在の選択肢として扱います。それ以外の場合は、それらのデフォルトから開始してください。役割が手順 5 にない行 (`how critics` など) は、廃止された役割からのものです。落としてください。

<a id="3-budget-map-and-confirm"></a>

### 3. 予算、地図、確認

**(a) 予算を尋ねます。** 自由記述よりも質問を優先します。これら 4 つのオプションをこれらの正確なラベルで提供し、ルールが予算を記録するときに現在の予算に名前を付けます。ルールなしで、`large` がスキルのデフォルトと一致するとします。

- `unlimited — max reasoning`
- `large — xhigh reasoning`
- `medium — high reasoning`
- `small — medium reasoning`

**(b) 適用します。** スキルのデフォルトから作業テーブルを構築し、再実行時に、ファミリー、リスト、またはエイリアス (`inherit-parent`、`auto`) によって変更したロールを保持します。 `unlimited`、`large`、`medium`、および `small` は、パネル エントリを含むすべての実際のスラッグのエフォート トークンを `max`、`xhigh`、`high`、または `medium` に設定します。エフォート トークンは、ラダー `max` > `xhigh` > `high` > `medium` > `low` の最後のトークン、または後続の `fast` の前のトークンです。結果が検出されたナメクジではない場合は、同じファミリーの検出されたナメクジをターゲット以下の最高の努力で使用します。それ以外の場合は、役割を選択が必要であるとマークします。 `inherit-parent` と `auto` は変更されません。したがって、`unlimited` は `claude-opus-5-5-xhigh` を `claude-opus-5-5-max` に変換します。 Grok slugs は `xhigh` でトップアウトするため、`unlimited` ではフォールバックによって Grok は `xhigh` に設定され、`grok-4.7-xhigh-fast` はそのまま維持されます。 `large` は両方のデフォルトを維持します。 `small` は、それらを `claude-opus-5-5-medium` および `grok-4.7-medium-fast` に変換します。

**(c) 役割を表示して確認します。** すべての役割をそのモデルとともに表示し、検出されたセットにない実際のナメクジを選択が必要であるとマークします。ステップ 2 で削除された各行もリストします。そのまま受け入れるか、特定のロールを変更するかを尋ね、検出されたモデルに加えて `inherit-parent` および `auto` (どちらも意味: このロールは親チャット モデルで実行され、自動ユーザーが自動に留まる方法です) をオプションとして提供します。フリーテキストよりも質問することを好みます。パネル ロール (アリーナ ランナー、アーキテクト ランナー、尋問レビュー担当者) の場合、値はリストであり、エイリアス エントリを含むエントリごとに 1 つのサブエージェントが実行されるため、リストの長さによってカウントが設定されます。 `arena cross-judge pool` もリストですが、Arena は可能な場合、そのモデル ファミリが親の値とは異なる値を 1 つ選択します。 `swarm workers` は、レースまたは比較によってアームごとに別のモデルが割り当てられない限り、すべてのワーカーのデフォルト モデルです。

<a id="4-validate"></a>

### 4. 検証

書き込まれるすべての実際のスラッグは、検出されたセットに含まれている必要があります。 `inherit-parent` と `auto` は常に合格します。選択した本物のナメクジが利用できない場合は、立ち止まってもう一度尋ねてください。

<a id="5-write-the-rule"></a>

### 5. ルールを書く

Poteto-mode が使用するのと同じラベルを使用して、`~/.cursor/rules/pstack-models.mdc` を `alwaysApply: true` で書き込み、`# budget` 行で選択したラベルとそのターゲット エフォートを書き込み、ロールごとに 1 行を書き込みます。ファイル全体を上書きして、再実行が冪等のままになるようにします。形状:

```
---
description: pstack per-role model choices (overrides skill defaults)
alwaysApply: true
---
# pstack model configuration. One line per role. Delete a line to fall back to the skill default.
# `inherit-parent` or `auto` as a value: the role runs on the parent chat model (omit Task `model`). Alias entries in a panel list still count toward its fan-out.
# budget: large (xhigh)
feature, refactoring: grok-4.7-xhigh-fast
bug-fix: grok-4.7-xhigh-fast
perf-issue: grok-4.7-xhigh-fast
hillclimb: grok-4.7-xhigh-fast
judgment and prose: claude-opus-5-5-xhigh
hardest tasks: claude-opus-5-5-xhigh
how explorer: grok-4.7-xhigh-fast
how explainer: claude-opus-5-5-xhigh
why investigators: grok-4.7-xhigh-fast
why synthesizer: claude-opus-5-5-xhigh
reflect tooling: grok-4.7-xhigh-fast
reflect judgment, divergent, synthesizer: claude-opus-5-5-xhigh
arena runners: claude-opus-5-5-xhigh, grok-4.7-xhigh-fast
arena cross-judge pool: claude-opus-5-5-xhigh, grok-4.7-xhigh-fast
swarm workers: grok-4.7-xhigh-fast
architect runners: claude-opus-5-5-xhigh, grok-4.7-xhigh-fast
interrogate reviewers: claude-opus-5-5-xhigh, grok-4.7-xhigh-fast
```

<a id="6-confirm"></a>

### 6. 確認

ルールが作成されたことと、それが新しいセッションに適用されることをユーザーに伝えます。このスキルを再実行すると更新されます。

<a id="7-offer-a-verification-skill-optional"></a>

### 7. 検証スキルを提供する (オプション)

プロジェクトに、証明のために実際のアプリを駆動する方法 (`verify-*` スキル、または既存のハーネス) があるかどうかを確認します。そうでない場合は、「エージェントがユーザーと同じようにアプリを操作し、変更が機能することを証明できるように、プロジェクト ローカルの検証スキルが必要ですか? /create-verification-skill で生成できます。」と一度申し出てください。 「はい」の場合、`/create-verification-skill` を呼び出します (pstack がインストールされている場所 (ワークスペース、ユーザー、またはプラグイン) で解決されます)。いいえ、無理せずに先に進んでください。
