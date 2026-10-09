# pstack-jp — P-STACK 日本語版

[poteto（Lauren Tan）](https://github.com/poteto) による [P-STACK](https://github.com/cursor/plugins/tree/ccb5507cec1546dc88135c1139c811e6c59115ba/pstack) の非公式日本語訳です。原作者、Cursor、SpaceXAIによる公式の日本語版ではありません。

少ないコードで高い品質を実現するための、エージェントの開発原則と作業手順を日本語で読めます。README、利用ガイド、スキル、参照資料、プレイブック、エージェント定義、任意のBenny自動化パックを翻訳しています。

| 内容 | 件数 |
| --- | ---: |
| 翻訳したMarkdown文書 | 131 |
| スキル（原則を含む） | 51 |
| 開発原則 | 24 |
| プレイブック | 23 |
| Benny自動化パックのスキル | 3 |
| 利用ガイド | 10章＋目次 |

## 日本語で読む

[利用ガイド](docs/guide/README.md) から順に読めます。[poteto-mode](skills/poteto-mode/SKILL.md) が全体の入口です。以下には原作者のREADMEの訳を掲載しており、一人称の「私」は原作者を指します。

## 日本語スキルを取り込む

Agent Skillsのインストーラーを使う場合は、次を実行します。

```bash
bunx skills add t-nakatani/pstack-jp
```

必要なスキルと取り込み先を選びます。内容の確認だけなら次を使います。

```bash
bunx skills add t-nakatani/pstack-jp --list
```

これは原版のCursor向け手順を翻訳したものです。Task、モデル名、設定パス、cursor-team-kitなどの依存先は原版のままです。選択した実行環境で、対応する機能とモデルが利用できるか確認してください。

以下の原版READMEやガイドにある「/add-plugin pstack」は、公式の英語版をインストールするコマンドです。日本語版を取り込む場合は、上記のこのリポジトリの指定を使います。Cursorプラグインの識別名はpstack-jp、各スキルの識別名は原版と同じです。

## 翻訳と出典

- 翻訳元：cursor/plugins 内の pstack、バージョン 0.15.15。
- 翻訳元コミット：ccb5507cec1546dc88135c1139c811e6c59115ba（2026年10月9日取得）。
- Google Translateで下訳を作成し、README、原則の説明、型と境界の重要な箇所などを編集しています。全文章の人手による校閲は完了していません。訳が不自然な箇所や意味が曖昧な箇所は原文も確認してください。
- コマンド、パス、コード例、機械が読む識別子、実行スクリプト、画像は原版を保持しています。画像内の英語とコードブロック内の英語プロンプト例も保持しています。技術的な意味を守るため、一部の用語は英語で残しています。
- 英語原文の全ファイルは [原文アーカイブ](upstream/pstack-en.tar.gz) に、出典とSHA-256は [source.json](upstream/source.json) に保存しています。
- 構造の検証は「python3 tools/verify_translation.py」で実行します。これは翻訳漏れ、コード・リンク・識別子の変更を検出するもので、訳の意味や実行環境の互換性を保証するものではありません。
- 原作の著作権表示を保持しています。配布条件は [MIT License](LICENSE) に従います。

誤訳の修正はIssueやPRで歓迎します。更新時は翻訳元コミットを固定し、原文アーカイブと日本語訳を一緒に更新してください。

---

<!-- BEGIN UPSTREAM TRANSLATION -->
<a id="pstack"></a>

# pstack

私は [poteto](https://x.com/poteto) です。社長でもCEOでもありませんが、Meta、Netflix、Cursorで何百万行ものコードに携わってきました。Reactのコアチームにも所属し、React Compilerの開発と保守に取り組んでいます。

AIは質の低いコードを作りすぎる。そう感じる人が増えています。私も同感です。雑なコードを書く人を20人集めたチームのように開発したくはありません。品質を伴わない生産量は、私の目標ではありません。速く進みたいなら、まず深く取り組んでください。

**pstackが私の答えです。** ここにあるのは、私がCursorで高品質なコードを届けるために毎日使っているスキルです。Cursorを本物のエンジニアリングチームに変えます。目標はコード行数の最大化ではありません。むしろ逆です。pstackは、より少ないコードで、より高い品質を実現するためのものです。

**pstackは安心して並列化するための基盤です。** 1つのエージェントに深く取り組ませ、品質と検証可能性を信頼できるようになれば、自信を持って並列化できます。`poteto-mode` を使って複数のエージェントを起動し、それぞれが厳密なエンジニアリング原則に沿って働くことを任せられます。

**Cursorでは各モデルの強みを組み合わせられます。** 最先端のモデルにも、それぞれ得意と不得意があります。pstackでは好きなモデルを使ってください。私のスキルの多くも、モデルごとの強みを生かすために、複数のモデルを使うワークフローを採用しています。

フォークして、改良して、自分のものにしてください。PRも歓迎します。

<a id="install"></a>

## インストール

```bash
/add-plugin pstack
```

<a id="get-started"></a>

## 使い始める

2 つのステップ:

1. [`/setup-pstack`](./skills/setup-pstack/SKILL.md) を実行し、推論予算を選択して、必要なモデルを選択します。
2. 厳密さが必要な作業を行う場合は常に [`/poteto-mode`](./skills/poteto-mode/SKILL.md) を使用してください。

ここは初めてですか? [pstack ガイド](./docs/guide/README.md) では、セットアップ、プロンプト、検証、夜間の実行に至るまで、最初の実際のタスクを順を追って説明します。行き詰まっていますか、またはどのスキルが適しているかわかりませんか? [`/poteto-help`](./skills/poteto-help/SKILL.md) に問い合わせてください。

基本はこれだけです。ほかのスキルは状況に応じて使うもので、モードが必要な場面で呼び出します。初期設定では、機能開発・リファクタリング・バグ修正・性能改善・hillclimbのコード作業をGrokに、最も難しい変更、文章、判断をOpus 5.5に割り当てます。標準のレビューパネルはOpus 5.5 / Grokです。[`/setup-pstack`](./skills/setup-pstack/SKILL.md) で変更できます。

<a id="usage"></a>

## 使い方

タスクの開始時に [`/poteto-mode`](./skills/poteto-mode/SKILL.md) を使います。依頼を読み、適したプレイブックを選び、各段階で必要なスキルを実行します。

<a id="just-use-poteto-mode"></a>

### [`/poteto-mode`](./skills/poteto-mode/SKILL.md) から始める

このスキルがメインのショートカットです。エージェントに厳密なエンジニアリング作業をしてもらう必要があるときは常にこれを使用します。 23 の プレイブック が付属しています。

```
/poteto-mode this pr has a subtle bug where the scroll drifts every 750ms even when idle. repro
first, then fix and verify.
```

```
/poteto-mode i'm going to bed. land the stack even if ci flakes. i want everything merged by
morning.
```

<details>
<summary>23 のプレイブック</summary>

| プレイブック | 用 |
|---|---|
| [調査](./skills/poteto-mode/playbooks/investigation.md) | 読み取り専用の質問です。 x はどのように機能するのか、y はなぜこのように構築されたのか、確かですか。 |
| [バグ修正](./skills/poteto-mode/playbooks/bug-fix.md) | は欠陥を再現し、その根本原因を特定し、実行時の証拠を使用して修正します。 |
| [パフォーマンス](./skills/poteto-mode/playbooks/perf-issue.md) | は測定された遅さをトレースし、ベースラインに対して改善します。 |
| [ヒルクライム](./skills/poteto-mode/playbooks/hillclimb.md) | は、目標に対する 1 つの指標の科学的な改善を継続し、測定前/後の測定と受け入れられた勝利ごとに 1 つのコミットを使用して仮説をループしました。 |
| [ランタイムフォレンジック](./skills/poteto-mode/playbooks/runtime-forensics.md) | は、計測器からライブ症状 (リーク、アイドル CPU スピン、グリッチ) を診断します。 |
| [トレースフォレンジック](./skills/poteto-mode/playbooks/trace-forensics.md) | は、キャプチャされたプロファイリング アーティファクト (cpuprofile、トレース、スピンダンプ、ヒープ スナップショット) を診断します。 |
| [機能](./skills/poteto-mode/playbooks/feature.md) | 名前付きデータ形状から構築された新しい動作または変更された動作。 |
| [リファクタリング](./skills/poteto-mode/playbooks/refactoring.md) | 構造または形状に対する動作を維持する変更。 |
| [プロトタイプ](./skills/poteto-mode/playbooks/prototype.md) | 設計や動作に関する決定を安価に行うため、またはそれを観察することで経験的な分岐点を解決するための、使い捨てのスケッチ。 |
| [ビジュアルパリティ](./skills/poteto-mode/playbooks/visual-parity.md) | 2 つの実装間のピクセル単位での UI の同等性。 |
| [スキルの作成](./skills/poteto-mode/playbooks/authoring-a-skill.md) | SKILL.md の作成または編集。 |
| [評価](./skills/poteto-mode/playbooks/eval.md) | スキルまたはプロンプトの変更がエージェントの動作にどのような影響を与えるかを盲検でテストします。 |
| [ベビーシッター](./skills/poteto-mode/playbooks/babysit.md) | pr またはスタックをマージ準備完了に駆動します: 競合、レビュー スレッド、ci。 |
| [リリース](./skills/poteto-mode/playbooks/shipping.md) | はグリーン スタックを個別に検証し、デフォルトでは github を通じて、または可能な場合はオリジンを通じて、連続した検証済みの実行をボトムアップで実行します。 |
| [自律実行](./skills/poteto-mode/playbooks/autonomous-run.md) | は、長いタスクを停止することなく完了まで推進します。 |
| [オーケストレーション](./skills/poteto-mode/playbooks/orchestrate.md) | 1 人のコーディネーター チャットに引き渡された継続的なプロジェクト: 複数日に渡る、多数の積み重ねられた PR、サブエージェントのフリート。 |
| [自動操縦フル](./skills/poteto-mode/playbooks/autopilot-full.md) | 独立した PR を実行して、PR ごとに 1 人の所有者とマージし、コードの準備ができた段階から各ラウンドでルート swarm の判定を下します。 |
| [自動操縦スタック](./skills/poteto-mode/playbooks/autopilot-stack.md) | は、オペレーターがレビューして着陸できるように、1 つの線形ベース ブランチ スタックを構築および検証します。 |
| [セッションピックアップ](./skills/poteto-mode/playbooks/session-pickup.md) | 前のエージェントの実行中の作業を再開または引き継ぎます。 |
| [安全に一時停止](./skills/poteto-mode/playbooks/pause-safely.md) | 実行中の作業を完全に一時停止して、後で再開できるようにします。 |
| [多段階計画](./skills/poteto-mode/playbooks/multi-phase-plan.md) | フェーズまたはスタックされた PR にまたがる作業。 |
| [ワークツリーのクリーンアップ](./skills/poteto-mode/playbooks/worktree-cleanup.md) | は、安全ゲート付きで、マージまたは放棄されたワークツリーと古い iOS シミュレーターをプルーニングすることでディスクを再利用します。 |
| [広告を開く](./skills/poteto-mode/playbooks/opening-a-pr.md) | 従来のコミット タイトルとブリーフィング スタイルの本文を持つ、小さな順序付けされたコミットから準備ができた PR を開きます。他のすべての プレイブック の最後に呼び出されます。 |

</details>



呼び出すと、次のように動きます。

1. タスクを [プレイブック](./skills/poteto-mode/playbooks/) に対応付け、手順をそのまま先頭に写したToDoリストを作ります。
2. 各手順に進むと、必要なスキルを呼び出します。
3. 利用者と保守担当者の視点で、AI特有の不自然な言い回しを除いた返答を書きます。

完全なルールとプレイブックは [`skills/poteto-mode/SKILL.md`](./skills/poteto-mode/SKILL.md) にあります。

ターンを超えて [`/poteto-mode`](./skills/poteto-mode/SKILL.md) を維持するには、`/` メニューから選択し、Enter の代わりに Option+Enter (Mac) または Alt+Enter (Windows) を押します。これにより、[カスタム モード](https://cursor.com/docs/skills) となり、Cursorがエージェント ウィンドウと CLI で提供されます。毎ターンコンテキスト内に留まり、プレイブックが一致する場合やタスクに厳密さが必要な場合には自動的に適用され、それ以外の場合は邪魔になりません。単純に入力すると、1 つのメッセージにのみ添付されます。そう言ってオプトアウトするか、モードを終了してオフにします。

[`/poteto-mode`](./skills/poteto-mode/SKILL.md) は、Cursorの `/loop` コマンドと非常によく連携します。厳密さを犠牲にすることなく、Cursorを長時間動作させることができます。

<a id="skills"></a>

## スキル

[`/poteto-mode`](./skills/poteto-mode/SKILL.md) は、ステップで必要なときにこれらのほとんどを実行します (`how`、`why`、`architect`、`arena`、`swarm`、`interrogate`、 `unslop`、`no-comments`、`technical-writing`、`tdd`、および原則)。以下の表は、直接必要な場合のものです。

```
/how do we cancel runs? do we have an n+1 when we look up every run to cancel?
```

```
/interrogate review this pr.
```

<details>
<summary>すべてのスキル</summary>

| スキル | の場合に使用します。 |
|---|---|
| [`/poteto-mode`](./skills/poteto-mode/SKILL.md) | 複雑なタスクの標準の入口。依頼に合うプレイブックを選びます。 |
| [`/poteto-help`](./skills/poteto-help/SKILL.md) | 初めて使うときや、スキル・プレイブック・原則の選択に迷うとき。目的を聞き取り、必要な説明と入力例を示します。`/poteto-help` と入力した場合だけ動作します。 |
| [`/how`](./skills/how/SKILL.md) | サブシステムの動作と構造を理解したいとき。 |
| [`/why`](./skills/why/SKILL.md) | なぜその設計になったか知りたいとき。利用可能なMCPを探し、コード履歴、課題、文書、チャット、監視、エラー、分析基盤を並行して調べます。 |
| [`/recall`](./skills/recall/SKILL.md) | 作業の開始や再開時に、会話履歴と共有記録から直近の文脈を復元し、現状を簡潔に整理したいとき。 |
| [`/blast-radius`](./skills/blast-radius/SKILL.md) | 小さく見える変更の影響範囲を知りたいとき。安全性を支える事実を、実行したコードで確かめます。 |
| [`/architect`](./skills/architect/SKILL.md) | 関数の境界を越えるコードを書く前に、呼び出し方、型、モジュール構成を決めたいとき。 |
| [`/arena`](./skills/arena/SKILL.md) | 同じ課題を複数のエージェントに並行して試させ、各案の良い部分を組み合わせたいとき。 |
| [`/swarm`](./skills/swarm/SKILL.md) | 異なる範囲の分担や同じ課題の競争を並行して進め、1つの報告にまとめたいとき。 |
| [`/interrogate`](./skills/interrogate/SKILL.md) | 差分を異なるモデルに批判的に検証させ、コード品質も厳しく見直したいとき。 |
| [`/automate-me`](./skills/automate-me/SKILL.md) | 実際の作業履歴から、自分専用の `-mode` スキルを作りたいとき。 |
| [`/make-bot-ui`](./skills/make-bot-ui/SKILL.md) | ボタンからWebhookでGrok Botを起こすページやダッシュボードを作りたいとき。送信キーの受け渡しとTailscaleも扱います。 |
| [`/setup-pstack`](./skills/setup-pstack/SKILL.md) | 役割ごとに使うモデルを選びたいとき。利用可能なモデルを調べ、設定ルールを書きます。 |
| [`/reflect`](./skills/reflect/SKILL.md) | 長い作業が完了し、学んだ進め方をスキルの変更として残したいとき。 |
| [`/correct`](./skills/correct/SKILL.md) | 同じ間違いを繰り返し訂正しているとき。履歴から分類し、設計、型、lint・CI、テスト、文書の順に強い仕組みで防ぎます。規則と強制手段の対応表を保ちます。 |
| [`/teach`](./skills/teach/SKILL.md) | 変更やサブシステムを実際に理解したいとき。howとwhyを実行し、図を積み重ねて説明します。 |
| [`/tdd`](./skills/tdd/SKILL.md) | 安価なローカルテストが可能なバグ修正。失敗するテストを先に書いてから直します。 |
| [`/benchmark-checklist`](./skills/benchmark-checklist/SKILL.md) | 高速化や性能劣化を測ったとき。制約要因、設定、エラー、繰り返し測定、全体への影響を確認してから報告や判断に使います。 |
| [`/no-comments`](./skills/no-comments/SKILL.md) | レビュー前にコメントを見直したいとき。Comment Sickoを起動し、採用する指摘を直し、制約をコードに表す方法を提案します。 |
| [`/typescript-best-practices`](./skills/typescript-best-practices/SKILL.md) | TypeScriptの読み書き。型システムの原則を具体的な構文に落とし込みます。 |
| [`/figure-it-out`](./skills/figure-it-out/SKILL.md) | 同梱のプレイブックが合わないとき。厳密で検証可能な専用プレイブックを設計します。 |
| [`/show-me-your-work`](./skills/show-me-your-work/SKILL.md) | レビューできる判断記録を残したいとき。コミット可能なTSVに記録します。 |
| [`/create-verification-skill`](./skills/create-verification-skill/SKILL.md) | アプリの動作をスクリプトで証明する方法がないとき。言語やプラットフォームを問わず、機能マップ付きの検証スキルを作ります。 |
| [`/maintain-verification-skill`](./skills/maintain-verification-skill/SKILL.md) | 検証スキルの機能マップが実装とずれたとき。コード調査と1回の実機確認を行い、証明できた修正を最大1つのPRにまとめます。 |
| [`/unslop`](./skills/unslop/SKILL.md) | 文章からAI特有の不自然な表現を取り除きたいとき。 |
| [`/bro`](./skills/bro/SKILL.md) | 直前のメッセージを、専門用語を避けた平易な言葉で言い直したいとき。 |
| [`/technical-writing`](./skills/technical-writing/SKILL.md) | 文書、RFC、README、PR説明、コミットメッセージを書くとき。Diátaxis、Googleの開発者向け文章規約、STE、Global Englishを組み合わせます。 |

</details>



<a id="examples"></a>

### 使用例

ほとんどの場合、タスクの開始時に [`/poteto-mode`](./skills/poteto-mode/SKILL.md) と入力して、プレイブックにルーティングします。他のスキルはステップで必要に応じて発動します。私が直接連絡を取ったものもいくつかあります。


<details>
<summary>すべての例</summary>

```
bug fix:           /poteto-mode this pr has a subtle bug where the scroll drifts every 750ms even
                   when idle. repro first, then fix and verify.
perf:              /poteto-mode a big list takes a second or two to load even though we virtualize.
                   run a cpu trace and tell me why.
feature:           /poteto-mode build a small feature behind a feature flag. verify it really works.
prototype:         /poteto-mode build two prototypes of the markdown renderer so we can compare.
                   spawn an agent for each.
multi-phase:       /poteto-mode open source these skills as a plugin. nothing internal leaks, work
                   in a temp dir, show me the dependency graph first.
overnight run:     /poteto-mode i'm going to bed. land the stack even if ci flakes. i want
                   everything merged by morning.
babysit:           /poteto-mode check on pr 123. anything outstanding?
visual parity:     /poteto-mode the row spacing is too tall when this flag is on. the second image
                   is correct. repro and fix until it matches.
figure it out:     /poteto-mode i'm stepping away. migrate every caller from the synchronous store
                   to the new async one, keeping behavior identical. i want to trust it was done
                   right when i'm back.
how:               /how do we cancel runs? do we have an n+1 when we look up every run to cancel?
why:               /why is this feature flag not on yet?
architect:         design this instrumentation to be high signal with no false positives. /architect
                   this first.
arena:             /arena take my prompt to the arena verbatim. i want to compare their proposals
                   with yours.
swarm:             /swarm check every package under packages/ against its check.sh. one worker per
                   package. one report.
interrogate:       /interrogate review this pr.
tdd:               /tdd implement
unslop:            can we unslop and tighten the new changes?
reflect:           /reflect that took too long. capture what we learned so the next run doesn't
                   repeat it.
correct:           /correct
show-me-your-work: /show-me-your-work keep a decision trail i can review when i'm back.
automate-me:       /automate-me
help:              /poteto-help which skill should i use to review this branch?
```

</details>

<a id="the-poteto-agent-and-comment-sicko-subagents"></a>

## `poteto-agent` とComment Sickoのサブエージェント

pstack には、私のスタイルをエンドツーエンドで実行するサブエージェントも同梱されています。 [`subagent_type: "poteto-agent"`](./agents/poteto-agent.md) 経由で親エージェントから生成します。作業を実行する前に、インライン原則インデックスを含む `poteto-mode` を完全に読み取ります。 `generalPurpose` を置き換えると、その読み取りがスキップされ、ドリフトします。

[`/poteto-mode`](./skills/poteto-mode/SKILL.md) と [`subagent_type: "poteto-agent"`](./agents/poteto-agent.md) は同じラッパーを介してルーティングされます。

pstack には、読み取り専用のコメント レビュアーである [Comment Sicko](./agents/comment-sicko.md) も同梱されており、`subagent_type: "Comment Sicko"` として利用できます。通常は、直接ではなく [`/no-comments`](./skills/no-comments/SKILL.md) を通じて呼び出します。

<a id="principles"></a>

## 原則

24 の短いスキル、それぞれ 1 つの原則。 `poteto-mode` はそれらにインラインでインデックスを作成し、タスクの開始時にそのインデックスを読み取ります。スタンドアロン ファイルが存在するため、他のスキルは名前で原則を参照でき、インデックスはそれぞれの完全なルールを指すことができます。

<details>
<summary>24 原則すべて</summary>

| 原理 | グループ | ルール |
|---|---|---|
| [遅延プロトコル](./skills/principle-laziness-protocol/SKILL.md) | コア | リファクタリングや変更量の判断に使います。削除を優先し、問題を解決する最小の変更を選びます。 |
| [基礎的な考え方](./skills/principle-foundational-thinking/SKILL.md) | コア | ロジックを書く前に、主要な型とデータ構造、基盤整備と機能開発の順序、並行実行主体が共有するものを決めます。データ構造を整え、後続のコードを明快にします。 |
| [第一原理からの再設計](./skills/principle-redesign-from-first-principles/SKILL.md) | コア | 既存の設計に新しい要件を組み込むときに使います。後付けせず、その要件が最初から存在した前提で設計し直します。 |
| [施設への攻撃](./skills/principle-attack-the-premise/SKILL.md) | コア | 同じ前提に基づく修正が2回以上、同じ検証で失敗したときに使います。次の修正の前に、どの実行主体に偏りがあるか集計し、修正を重ねる前に前提を疑います。 |
| [加算する前に減算](./skills/principle-subtract-before-you-add/SKILL.md) | コア | 追加・リファクタリング・書き直しの順序を決めるときに使います。不要なコード、重複する検証、内容のない参照を先に削り、単純になった基盤の上に構築します。 |
| [リーダー負荷の最小化](./skills/principle-minimize-reader-load/SKILL.md) | コア | 追いづらいコードの設計やレビューに使います。問いから答えまでの層と、読み手が覚える必要のある隠れた状態を数え、単一の呼び出し元しかないラッパーをまとめ、変更可能な状態の範囲を狭めます。 |
| [結果重視の実行](./skills/principle-outcome-oriented-execution/SKILL.md) | コア | 段階の境界が明確な書き直しや移行に使います。目標のアーキテクチャへ収束させ、一時的な互換コードで途中の状態を維持しようとしません。 |
| [体験初](./skills/principle-experience-first/SKILL.md) | コア | 製品・UX・機能範囲のトレードオフに使います。実装の都合より利用者の満足を優先し、粗い機能を増やすより少数の磨かれた機能を届けます。 |
| [設計スペースを使い果たす](./skills/principle-exhaust-the-design-space/SKILL.md) | コア | コードベースに前例のないUI操作や設計判断に使います。競合する2〜3案のプロトタイプを作り、並べて比較してから決めます。 |
| [レバーの構築](./skills/principle-build-the-lever/SKILL.md) | コア | 大量の作業に限らず、単純でない編集・移行・分析・検証に使います。手作業の代わりに、作業を実行または証明するcodemod、スクリプト、生成器、共通スキルを作ります。レビュー担当者が再実行できる道具を成果物にします。 |
| [ドメインのモデル](./skills/principle-model-the-domain/SKILL.md) | アーキテクチャ | 状態を持つ処理や、分岐やデータ構造の前提が複数ファイルに散らばるコードに使います。条件分岐を散在させず、ドメインをデータ構造に表します。 |
| [境界-規律](./skills/principle-boundary-discipline/SKILL.md) | アーキテクチャ | 検証・エラー処理・フレームワークとの接続に使います。CLI、設定、ネットワーク、外部APIなどの境界に防御処理を集め、内部の型を信頼し、業務ロジックを純粋関数に置きます。 |
| [タイプ-システム-専門分野](./skills/principle-type-system-discipline/SKILL.md) | アーキテクチャ | 型や関数シグネチャの設計、静的型付け言語の実装に使います。不正な状態を表現できなくし、意味の異なるプリミティブを区別し、外部データを境界で解析します。コンパイラを欺かず、すべてのバリアントを処理し、正本となるスキーマから型を導出します。 |
| [操作を冪等にする](./skills/principle-make-operations-idempotent/SKILL.md) | アーキテクチャ | クラッシュ・再起動・再試行を伴うコマンド、ライフサイクル操作、処理ループに使います。前回の実行が途中で止まっていても、同じ最終状態へ収束させます。 |
| [呼び出し元を移行し、レガシー API を削除](./skills/principle-migrate-callers-then-delete-legacy-apis/SKILL.md) | アーキテクチャ | 旧APIの呼び出し元が残る状態で新しい内部APIを導入するときに使います。互換層を残さず、同じ移行で呼び出し側を更新して旧APIを削除します。 |
| [シリアル化前の分離共有状態](./skills/principle-separate-before-serializing-shared-state/SKILL.md) | アーキテクチャ | 並行する実行主体が同じファイル、ブランチ、キー、状態に書き込む可能性があるときに使います。まず共有をなくし、単一の共有書き込み先が本当に必要な場合だけ構造で直列化します。 |
| [動作確認](./skills/principle-prove-it-works/SKILL.md) | 検証 | 作業を完了したと宣言する前に使います。機能の実行、実際の値、差分などの実物を確認し、代理指標・自己申告・コンパイル成功だけで判断しません。 |
| [根本原因の修正](./skills/principle-fix-root-causes/SKILL.md) | 検証 | デバッグに使います。まず再現し、根本原因に届くまで理由を問い、症状の発生源で修正します。クラッシュを隠すだけのnilチェックを追加しません。 |
| [シーケンス検証可能なユニット](./skills/principle-sequence-verifiable-units/SKILL.md) | 検証 | 複数段階の作業、移行、同種の編集、コミットやPRの積み重ねに使います。それぞれが検証可能な状態で終わる小さな単位に分け、次へ進む前に確認し、順序そのものがレビュー担当者に根拠を示すようにします。 |
| [実装ではないテスト動作](./skills/principle-test-behavior-not-implementation/SKILL.md) | 検証 | テストの作成・変更・維持に使います。利用者と同じ呼び出し方で、観測する結果を具体的な期待値と比較します。インポートした関数がすべてundefinedを返しても通るテストは、アサーションを書き直すか削除します。 |
| [番号の説明](./skills/principle-explain-the-number/SKILL.md) | 検証 | 高速化・性能劣化・スループット・遅延・評価結果など、測定した数値を信頼、報告、利用する前に使います。制約要因を特定し、意図した処理以外を測っている可能性を証拠で排除します。 |
| [コンテキストウィンドウのガード](./skills/principle-guard-the-context-window/SKILL.md) | 代表団 | 大量の出力、長いファイル、読み直し、並列作業の計画でコンテキストが埋まるときに使います。大きな内容はサブエージェントに渡し、メインチャットには生データではなく要約を残します。 |
| [決して人間をブロックしない](./skills/principle-never-block-on-the-human/SKILL.md) | 代表団 | 取り消せる作業で「実行してよいか」と聞きたくなったときに使います。実行して結果を示し、必要なら人が後から軌道修正できるようにします。取り返しのつかない操作は確認します。 |
| [構造内のレッスンをエンコード](./skills/principle-encode-lessons-in-structure/SKILL.md) | メタ | 同じ指示を2度書いたり、繰り返す修正に気づいたときに使います。説明文を増やす代わりに、lint、メタデータ、実行時チェック、スクリプトに規則を組み込みます。 |

</details>

<a id="not-shipped-here"></a>

## 同梱されていない機能

`poteto-mode` が参照しているもののバンドルされていないもの:

- `/deslop` および `deslop` スキルは `cursor-team-kit` プラグインに同梱されています。
- `control-cli` (CLI および TUI 用) および `control-ui` (ブラウザ、Electron、Web 用) も `cursor-team-kit` でリリースされます。
- `/create-skill` はCursor組み込みです。Cursorには組み込みの `/babysit` も同梱されています。 `poteto-mode` 内では、[ベビーシット プレイブック](./skills/poteto-mode/playbooks/babysit.md) が pr-status リクエストに優先します。

フルセットが必要な場合は、pstack と一緒に `cursor-team-kit` をインストールします。

<a id="why-are-there-no-planning-skills"></a>

## 計画用スキルがない理由

Cursorには、pstackと組み合わせて使える優れた計画モードがすでにあります。ただ、個人的には計画そのものを重視していません。最良の仕様はコードです。計画を作りたい場合は [`/poteto-mode`](./skills/poteto-mode/SKILL.md) が対応しますが、標準の動作ではありません。

<a id="make-it-yours"></a>

## 自分のスタイルに合わせる

`poteto-mode` が私のスタイルです。まさにそれを望んでいないかもしれません。

タイプ [`/automate-me`](./skills/automate-me/SKILL.md)。最近のトランスクリプトをマイニングし、実際の作業方法から `<your-name>-mode` スキルを作成し、その下の pstack を経由します。 pstack をベースとして保持し、最終的には `poteto-mode` と並行して独自のルーティング スキルを使用することになります。

モデルも構成可能です。 [`/setup-pstack`](./skills/setup-pstack/SKILL.md) と入力します。ユーザーがアクセスできるモデルを検出し、各役割 (コード、判断、レビューパネル) をモデルにマッピングする、常に適用される小さなルールを作成します。すべてのスキルはそれを読み取り、ルールが存在しない場合は適切なデフォルトに戻るため、必要なものだけをオーバーライドできます。

デフォルトが変更されると、変更前に作成されたルールによって古いデフォルトが固定されます。これらの役割行を削除するか、ファイルを削除してから、`/setup-pstack` を再度実行してください。再実行では、モデルがデフォルトと異なるロールはすべて保持されます。

<a id="automations"></a>

## 自動化

pstack には、休止状態の [benny automation Pack](./automations/benny/) も同梱されています。 benny はスラック問題レポートをトリアージし、実際の UI 証拠を使用して確認されたバグを再現して修正します。そのファイルはスラッシュスキルとして登録されていません。

を設定するには、[`FOR_AGENTS.md`](./automations/benny/FOR_AGENTS.md) にCursorを合わせます。セットアップはパックを `.cursor/automations/benny/` のターゲット リポジトリにコピーし、そこで共有スキル用に pstack を有効にし、コピーされたパックの外部にユーザー構成を保持します。

<a id="license"></a>

## ライセンス

MIT
