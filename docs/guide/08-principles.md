<a id="steer-with-principle-names"></a>

# 原則名を使用したステアリング

pstack には、24 の原則が個別のスキルとして付属しています。 `/poteto-mode` は、すべてのマルチステップ タスクの開始時にインデックスを読み取り、タスクがトリガーするものを適用し、変更された決定とともに応答で適用される各原則に名前を付けます。

あなたは原則を持ち出しません。あなたは彼らの名前を使って操縦します。それぞれの名前は、エージェントがすでに読んだ完全なルールを指しているため、1 つのフレーズが指示の段落よりも正確に作業をリダイレクトします。

<a id="steering-in-practice"></a>

## ステアリングの実践

エージェントが 3 つの既存のアダプターに新しいアダプターをボルトで固定しようとしているとします。

```text
use subtract before you add. delete the obsolete adapters first, then design what's left.
```

ビルドが成功したため成功したと主張します。

```text
apply prove it works. run the real import flow and show me the written records.
```

2 つの並列試行が同じブランチに書き込もうとしているとします。

```text
separate before serializing shared state. give each attempt its own worktree, no locks.
```

各フレーズが着地するのは、その背後にあるルールが固有であるためです。エージェントは依然として、どの決定がルールを変更したかを返信で言わなければなりません。決定の背後にない原則的な引用は、適用されるのではなく名前が削除されたと伝えています。

<a id="the-24-briefly"></a>

## 24 を簡単に説明すると

基本原則によって、どれだけの量を構築するか、いつ設計を再考するかが決まります。

- [怠惰なプロトコル](../../skills/principle-laziness-protocol/SKILL.md) は削除と、問題を解決する最小限の変更を優先します。
- [基礎的な考え方](../../skills/principle-foundational-thinking/SKILL.md) は、ロジックを記述する前にコア データ構造を選択します。
- [最初の原則からの再設計](../../skills/principle-redesign-from-first-principles/SKILL.md) は、あたかも最初から存在していたかのように新しい要件を統合します。
- [前提を攻撃](../../skills/principle-attack-the-premise/SKILL.md) は、どのアクターが不均衡を保持しているかを調査した後、2 つ以上の失敗した修正が共有されているという前提に疑問を呈します。
- [追加する前に減算](../../skills/principle-subtract-before-you-add/SKILL.md) は、その上に建物を建てる前に自重を取り除きます。
- [リーダーの負荷を最小限に抑える](../../skills/principle-minimize-reader-load/SKILL.md) は、リーダーが頭の中に保持する必要があるレイヤーと非表示の状態を折りたたみます。
- [結果指向の実行](../../skills/principle-outcome-oriented-execution/SKILL.md) は、使い捨ての互換性状態を保持するのではなく、ターゲット デザインに書き換えを収束します。
- [経験優先](../../skills/principle-experience-first/SKILL.md) は、実装の利便性よりもユーザーの結果を選択します。
- [設計スペースを使い果たす](../../skills/principle-exhaust-the-design-space/SKILL.md) は、前例がない場合に 2 つまたは 3 つの競合するプロトタイプを構築します。
- [レバーの構築](../../skills/principle-build-the-lever/SKILL.md) は、作業を実行または証明するスクリプトを構築し、レビュー担当者が再実行できるようにします。エージェントが手作業で同じ作業を続ける場合は、エージェントに必要なツールやスキルを記述してもらいます。スクリプトが毎回同じ方法でステップを実行できる場合は、そのスクリプトを使用し、判断呼び出し用にエージェントを保存します。

アーキテクチャ原則により、状態、検証、互換性がどこに存在するかが決まります。

- [ドメインのモデル化](../../skills/principle-model-the-domain/SKILL.md) は、散在する条件文ではなく、繰り返しのルールを 1 つの構造でエンコードします。
- [境界規律](../../skills/principle-boundary-discipline/SKILL.md) は境界で検証し、内部型を信頼します。
- [型システム規律](../../skills/principle-type-system-discipline/SKILL.md) は、不正な状態を表現できなくなります。
- [操作を冪等にする](../../skills/principle-make-operations-idempotent/SKILL.md) は、再試行を同じ終了状態に収束させます。
- [呼び出し元を移行してからレガシー API を削除](../../skills/principle-migrate-callers-then-delete-legacy-apis/SKILL.md) は 1 つのウェーブで移行と削除を行います。
- [共有状態をシリアル化する前に分離](../../skills/principle-separate-before-serializing-shared-state/SKILL.md) は、調整を追加する前に共有を削除します。

検証原則では、何が証拠としてカウントされるかを定義します。

- [動作することを証明する](../../skills/principle-prove-it-works/SKILL.md) は、プロキシではなく実際のアーティファクトを検証します。
- [根本原因の修正](../../skills/principle-fix-root-causes/SKILL.md) は、コードを変更する前に原因を再現して追跡します。
- [作業を検証可能な単位にシーケンスする](../../skills/principle-sequence-verifiable-units/SKILL.md) は、次の単位を開始する前に、チェックで各小さな単位を終了します。
- [実装ではなくテスト動作](../../skills/principle-test-behavior-not-implementation/SKILL.md) は、ユーザーが行う方法でコードを呼び出し、リテラルの期待値をアサートし、インポートされたすべての関数が `undefined` を返した場合でも合格するテストを削除します。
- [数値の説明](../../skills/principle-explain-the-number/SKILL.md) は、測定された数値を制限するものを指定し、誰かがそれを信頼したり報告したりする前に、それが他のものを測定したことを除外します。 [`/benchmark-checklist`](../../skills/benchmark-checklist/SKILL.md) は、実際の実行から回答する 7 つの質問に変換されます。

委任の原則により、並列作業が健全に保たれます。

- [コンテキスト ウィンドウの保護](../../skills/principle-guard-the-context-window/SKILL.md) は、一括読み取りをサブエージェントにルーティングし、結果をメイン チャットに保持します。
- [決して人間をブロックしない](../../skills/principle-never-block-on-the-human/SKILL.md) は可逆的な作業を進め、結果を提示します。

そしてメタ原則が 1 つあります。

- [構造内のエンコード レッスン](../../skills/principle-encode-lessons-in-structure/SKILL.md) は、2 回繰り返したアドバイスを lint、チェック、またはスクリプトに変換します。 [`/correct`](../../skills/correct/SKILL.md) は、[Make it yours](./09-make-it-yours.md#fix-the-environment-with-correct) に示すように、リポジトリ全体に適用されます。

リストを暗記しないでください。今すぐざっと読んで、エージェントがここに名前を付けておけば阻止できそうなことをしているのを見つけたら戻ってきてください。そうやって語彙が定着していきます。

次へ: [自分のものにする](./09-make-it-yours.md)。
