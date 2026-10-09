<a id="understand-the-code-before-changing-it"></a>

# コードを変更する前にコードを理解する

理解できないコードを編集すると、微妙なリグレッションが発生する可能性があり、それはあなただけでなくエージェントにも当てはまります。通常、エージェントは 2 つの方法のいずれかで失敗します。彼らはあなたが望んでいることを読み違えているか、仕事を正しく行うためのコンテキストを持っていません。 [プロンプトの内容](./02-poteto-mode.md#what-goes-in-a-prompt) は最初の処理を行います。このページでは 2 番目について説明します。

pstack には 4 つの方法があります。 `/how` はコードが現在何をしているかを説明しています。 `/why` は、そのような形状になった理由を掘り下げます。 `/teach` は両方を 1 つの説明にまとめています。 `/recall` は、トピックに関する独自の最近のコンテキストを再構築します。それぞれのエージェントは、確認できる言葉でエージェント自身を説明します。そうすることで、自分よりもコードをよく知っているエージェントを監督することができます。

![ロボットが事件ファイルを取り出す間、刑事は虫眼鏡で機械の設計図を調べます。彼女の背後にある証拠ボードには、/how と /why の下に手がかりがリンクされています。](./images/understanding.jpg)

<a id="start-with-a-read-only-investigation"></a>

## 読み取り専用の調査から開始する

原因が不明な場合は、修正ではなく所見を求めてください。

```text
/poteto-mode investigate why background jobs time out every few hours. give me what we know, what data you used, and your best hypotheses. don't change any code yet.
```

「まだコードを変更しないでください」は、これを [調査プレイブック](../../skills/poteto-mode/playbooks/investigation.md) にルーティングします。 `/how` を実行し、動機に関する質問に対して `/why` を追加し、引用された説明を返します。オプションの選択については、トレードオフ テーブルを含む推奨事項が返されます。 「どのようなデータを使用したか」を尋ねることで、エージェントは証拠と推測を区別するようになります。調査結果が修正を示している場合は、新しいタスクとして修正を開始します。

<a id="trace-behavior-with-how"></a>

## `/how` による動作のトレース

```text
/how do we dedupe notifications? is there an n+1 when we look up subscribers?
```

実際に抱いている質問をしてください。 [`/how`](../../skills/how/SKILL.md) はコードを読み取り、サブシステムにオンボーディングする上級エンジニアのレベルで、ランタイム フロー、キー タイプ、および非自明な部分について回答します。大規模なサブシステムの場合、最初に 2 ～ 4 つの読み取り専用エクスプローラーがファンアウトされます。狭い質問の場合は、読んで説明するだけです。

<a id="dig-up-history-with-why"></a>

## `/why` で履歴を掘り出す

```text
/why was the retry limit set to five? does the reason still hold?
```

[`/why`](../../skills/why/SKILL.md) は未解決事件の刑事のように働きます。これはソース管理から始まり、問題追跡ツール、長文ドキュメント、チーム チャット、可観測性、エラー追跡、分析など、MCP が公開するあらゆる証拠カテゴリをすべて並行してクエリします。報告書はすべてを引用し、直接証拠を推論から分離し、記録が薄い場合には「そうである」と述べている。 「誰も理由を書き留めなかった」ということ自体が答えであるため、null の結果も報告されます。

二人は自然に構成されます。 `do why first then how` は、歴史が混乱を説明しているのではないかと疑う場合に最適なプロンプトです。

<a id="actually-understand-it-with-teach"></a>

## 実は`/teach`でわかる

```text
/teach me how this PR changes retries. convince me it fixes the cause and not the symptom.
```

[`/teach`](../../skills/teach/SKILL.md) は、概要が十分でない場合に使用します。 `/how` と `/why` を実行し (そのうちの 1 つだけを小さな変更として)、結果を図ごとに構築するわかりやすい説明に織り込みます。 「納得させて」という構図は盗む価値がある。それは説明をツアーの代わりにあなたが突くことができる議論に変えます。

これはエージェント自身の選択にも適用されます。

```text
/teach me why you implemented it this way and not with a queue. what did you trade off, and why?
```

教えることは、あなたと同じようにエージェントにも役立ちます。自分の仕事を説明しなければならないエージェントは、自信を持って述べて先に進むのではなく、コードを読み、それぞれの主張を証拠で裏付けなければなりません。

<a id="rebuild-your-own-context-with-recall"></a>

## `/recall` を使用して独自のコンテキストを再構築します

```text
/recall catch me up on the export work from last week
```

[`/recall`](../../skills/recall/SKILL.md) は、あなた自身の最近のチャットと共有記録 (問題、以前の修正、まだ発生しているエラー) をマイニングし、現状と今後の状況についての概要を返します。古いチャットには、新しいエージェントに欠けているコンテキストが保持されているため、最初に古いトピックをロードして古いトピックで新しい作業を開始し、次に新しい入力を渡します。

```text
/recall my work on the virtualized list from yesterday, then read this bug report.
```

特定のチャットを再開したい場合は、`/recall` ではなく、以下のセッション ピックアップ プレイブックを使用します。

<a id="take-over-prior-work-with-session-pickup"></a>

## セッションピックアップで以前の作業を引き継ぎます

別のエージェント (または先週あなた) が飛行中に支店を離れたとき:

```text
/poteto-mode take over this branch. read the decision log, figure out what's done, and continue from there. don't redo finished work.
```

[セッション ピックアップ プレイブック](../../skills/poteto-mode/playbooks/session-pickup.md) は、以前の証跡を信頼できるものとして扱います。すべてを最初から再導出するのではなく、分岐状態と決定を再構築し、再開ポイントに名前を付け、元の目標に対して継承されたクレームを検証します。

**落とし穴:** 「エージェントはとにかくコードを読み取る」ため、このページのスキルをスキップしないでください。トレースされたモデルを使用せずに編集を開始したエージェントは、最初に考えられる箇所で症状を修正する傾向があります。 `/how` 最初のバグは 2 番目のバグよりも安価です。

次: [変更を設計](./04-design.md)。
