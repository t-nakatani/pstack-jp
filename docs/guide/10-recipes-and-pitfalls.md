<a id="recipes-and-pitfalls"></a>

# レシピと落とし穴

プロンプトはコピーする価値がありますが、誰もが一度は犯す間違いです。独自のパスとフィニッシュ条件を交換します。レシピは意図的に非公式になっています。これが実際に入力される方法であり、スキルは意図を適切に読み取ります。

![ロボットがレシピボックスから調理する間、彼女は完成した料理を試食します。カウンターの上には、/how、/tdd、/loop と書かれたカードがピンで留められています。](./images/recipes.jpg)

<a id="understand-an-unfamiliar-subsystem"></a>

## 馴染みのないサブシステムを理解する

```text
use /how first to understand how this initialization works. then use /why to figure out why it broke recently.
```

メカニックが第一、歴史が二番目。各スキルのレポートには、検索したソースが示されるため、答えの根拠がわかります。

<a id="restate-a-noisy-report-before-touching-code"></a>

## コードに触れる前にノイズの多いレポートを再表示する

```text
/poteto-mode read this thread. restate the underlying issue in your own words, in plain english. don't change any code yet.
```

再記述に誤読があり、修正するには 1 つのメッセージが必要です。エージェントが独自の理論を述べるまでは、自分の理論を胸に秘めておいてください。

<a id="prototype-before-you-pick"></a>

## 選ぶ前のプロトタイプ

```text
/poteto-mode prototype a few options for the settings layout. put them behind a switcher and send me screenshots of each.
```

説明ではなく、実行されるものから選択します。エージェントは、途中で独自のレイアウトとタイミングの質問に答えます。

<a id="turn-a-settled-design-into-a-plan"></a>

## 固まったデザインを計画に変える

```text
/poteto-mode turn this design into a plan. small verifiable PRs, each with its own proof.
```

デザインが固まってから質問してください。プランは成果物であり、それを実行するプレイブックに名前を付けます。

<a id="get-a-second-opinion-on-a-design"></a>

## 設計についてのセカンドオピニオンを得る

```text
ask /arena for a second opinion on this thread and our approach
```

現在のデザインはいくつかの候補の中の 1 つとなり、合成により、パネルがより良いものを見つけたか、または既存のものを確認したかがわかります。高価な契約の前に、安価な保険を。

<a id="check-independent-slices-in-parallel"></a>

## 独立したスライスを並列でチェックする

```text
/swarm check every package under packages/ against its check.sh. one worker per package. one report.
```

各ワーカーは 1 つのパッケージを所有します。親はすべてのスライスを待機し、生のワーカー ダンプの代わりに 1 つの `PASS`、`ISSUES`、または `BLOCKED` レポートを返します。

<a id="review-a-branch-skeptically"></a>

## ブランチを懐疑的にレビューする

```text
/interrogate the whole branch, but skeptically. don't change anything yet. no nitpicks unless it's an actual bug or regression in behavior.
```

修飾子は実際に機能します。 「まだ何も変更しない」と読み取り専用に保ち、細かいルールによってノイズが事前にフィルターされるため、`Act on` の結果は時間をかけて調べる価値があります。

<a id="fix-a-bug-through-a-failing-test"></a>

## 失敗したテストを通じてバグを修正する

```text
/poteto-mode repro the duplicate write first. if there's a cheap test path, /tdd it. then fix and rerun.
```

「安価なテスト パスがあるかどうか」が重要です。脆弱なモックを使用してテストを強制することは、実際のコマンドを実行することよりも効果が低いことが証明されており、プレイブックではそう言うことが許可されています。

<a id="repro-and-fix-a-report-with-proof"></a>

## 証拠付きレポートを再現して修正する

```text
/poteto-mode repro this with /verify-<app>. if it repros on main, fix it and show me a video as proof.
```

「メインで再現する場合」を使用すると、バグがすでに解消されているときに実行を早期に停止できます。ビデオでは、差分を読む前に修正を確認できます。

<a id="vet-a-number-before-you-post-it"></a>

## 投稿する前に番号を精査してください

```text
/benchmark-checklist vet this 40% speedup before it goes in the pr description
```

実行回数、範囲、および回数の制限によって、速くなったり遅くなったり、測定可能な差がなかったり、決定的ではなかったりします。

<a id="stop-correcting-the-same-mistake"></a>

## 同じ間違いを訂正するのはやめてください

```text
/correct agents keep adding new config flags without registering them in the schema
```

修正はアーキテクチャ、タイプ、lint、またはテストとしてリポジトリに配置されるため、次のエージェントが間違いを犯すことはありません。

<a id="ask-how-without-starting-the-work"></a>

## 作業を開始せずに方法を尋ねる

```text
/poteto-help how do i get poteto-mode to stay on every turn?
```

回答、送信プロンプト、およびソースへのリンクが表示されます。そのプロンプトを送信するまでは何も実行されません。

<a id="keep-a-run-honest-while-youre-away"></a>

## 外出中も正直に走りましょう

```text
im going to bed, keep going autonomously until every fixture passes. do not stop. keep a decision log i can audit in the morning.
```

契約書の全文は [オーバーナイト ページ](./07-overnight.md) にあります。タスクと終了条件がすでに会話に含まれている場合は、短い形式が機能します。

<a id="redirect-a-drifting-run"></a>

## ドリフト走行をリダイレクトする

ステアリング プロンプトは 1 行です。

```text
i said the goal is to repro. i did not ask for a fix yet.
```

```text
apply prove it works. show me the real output, not the build log.
```

```text
/unslop that, no emdashes
```

これ以上の言葉が必要になることはほとんどありません。正しい名前が必要です。[原則ページ](./08-principles.md) が語彙です。

<a id="get-the-reply-in-plain-words"></a>

## わかりやすい言葉で返事をもらう

```text
/bro
```

これがプロンプト全体です。 [`/bro`](../../skills/bro/SKILL.md) は、専門用語を使わずに、人間が別の人間と話しているように最後のメッセージを言い換えています。返信が技術的に完全であるにもかかわらず、その内容がまだわからない場合に使用します。

<a id="the-pitfalls"></a>

## 落とし穴

- **プロンプトでスキルを列挙します。** 「use /how then /architect then /arena」は、プレイブックのすでにシーケンスされているステップの順序を変更します。目標と制約を述べます。スキルに名前を付けるのは、デフォルトを上書きする場合のみです。
- **曖昧な終了条件。** 「改善する」と `/loop` には何もチェックできません。成功するか失敗する可能性があるコマンドまたはアーティファクトを指定します。
- **原因に関するあなたの理論を説明します。** エージェントは、あなたが指した場所を検索します。まず問題を再説明してもらい、それからあなたの予感を共有してください。
- **最初のデザインを取得します。** 1 回の試行で、モデルが考えた最初の形状に固定されます。プロトタイプまたは `/architect` を要求し、証拠から選択します。
- **抽象的な計画を磨き上げる。** コードの背後にない計画を敵対的にレビューすると、決して起こらないリスクが生み出されます。プロトタイプで未解決の疑問を解決し、構築されたものをレビューします。
- **1 つのワークツリー内の並列エージェント。** 相互に上書きされ、差分は考古学的なものになります。それらをクラウド エージェントとして実行するか、「試行ごとに独自のワークツリー」と言います。
- **ループを信頼する前のループ。** ループ自体の動作を検証できないループは、未チェックの動作を高速化するだけです。まず検証スキルを機能させてください。
- **精査されていない番号を信頼する** ウォーム キャッシュやスキップされたコード パスは、高速化を装う可能性があります。数値がどこかに行く前に `/benchmark-checklist` を実行してください。
- **同じ間違いを手動で修正します。** チャットで修正すると、1 回の実行に役立ちます。 `/correct` はリポジトリを修正し、その後の実行が繰り返されないようにする。
- **カバレッジには `/arena` を使用します。** `/arena` は 1 つのデザインまたはコード概要を繰り返し、ベースを選択して最良の部分を接ぎ木します。 `/swarm` は、スライスまたは宣言されたレースアームを分割し、1 つのレポートに集約します。
- **すべてのレビュー コメントを受け付けます。** ボットと人間の両方が、実際の捕獲情報とノイズを 1 つのリストに記録します。 `/interrogate` は、結果を実行バケットと理由付きの却下バケットに分類し、どちらの方法でもオーバーライドできます。
- **`auto` をモデル スラグとして扱います。** `auto` および `inherit-parent` は、「サブエージェントが親チャット モデルを継承するようにモデル フィールドを省略する」ことを意味します。 [セットアップ](./01-setup.md) は役割をカバーします。
- **グリーン ビルドの成功を報告します。** ビルドはコンパイルできることを証明します。実際のコマンド、フロー、保存された値、またはプロファイルを要求し、応答で証拠が得られることを期待します。
- **フリーハンドで `SKILL.md` を作成します。** [スキル プレイブックの作成または変更](../../skills/poteto-mode/playbooks/authoring-a-skill.md) を通じてルーティングして、検証とレビューが行われるようにします。

それがガイドです。先にスキップした場合は、[setup](./01-setup.md) に戻り、実際のタスクを 1 つ実行します。習慣は読むことでではなく、使用することで定着します。

[ガイドインデックス](./README.md) に戻ります。
