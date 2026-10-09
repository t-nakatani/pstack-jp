<a id="build-the-change-and-clean-the-diff"></a>

# 変更をビルドし、差分をクリーンアップします

ビルド プレイブックは 1 つの分野を共有します。あなたが観察したことを話して、戦略に証拠を要求させてください。このページでは、各一般的なビルド タスクのプロンプトに何を入力するかを示し、次に、差分をレビュー可能にしておくためのクリーンアップ習慣を示します。

<a id="prompt-each-build-playbook-with-what-you-know"></a>

## 知っていることを各ビルド プレイブックに入力するよう求める

バグ プロンプトには症状が示され、最初に再現が求められます。

```text
/poteto-mode this command emits two records after a retry. repro first, then fix and verify.
```

機能プロンプトには、動作と変更してはいけないものが示されます。

```text
/poteto-mode add a --json flag. text output stays byte-identical. verify both forms.
```

リファクタリング プロンプトは、構造が移動する前に動作を固定します。

```text
/poteto-mode move parsing into one module, zero behavior change. record the current output first and prove it's unchanged after.
```

パフォーマンス プロンプトには、雰囲気ではなく測定値が示されます。

```text
/poteto-mode startup takes 1.8s on this fixture. trace it, fix the measured cause, show me before and after.
```

これらのそれぞれは、プレイブック ([バグ修正](../../skills/poteto-mode/playbooks/bug-fix.md)、[機能](../../skills/poteto-mode/playbooks/feature.md)、[リファクタリング](../../skills/poteto-mode/playbooks/refactoring.md)、[パフォーマンスの問題](../../skills/poteto-mode/playbooks/perf-issue.md)) にルーティングされ、プレイブックは入力しなかった手順を提供します。つまり、修正する前に再現し、実装する前にデータ形状に名前を付け、再構築する前に動作を固定し、再構築する前にプロファイルを作成します。最適化すること。

1 つの数値を継続的に改善するには、[ヒルクライム プレイブック](../../skills/poteto-mode/playbooks/hillclimb.md) があります。メトリクス、ターゲット、試行の下限を与えると、フリーズした測定ハーネスを使用して一度に 1 つの仮説をループします。勝利を維持し、他のすべてを元に戻します。

どちらの perf プレイブック も、その番号で [`/benchmark-checklist`](../../skills/benchmark-checklist/SKILL.md) を実行します。 Perf 問題ではベースラインとその後のすべての数値が精査され、Hillclimb ではフリーズする前にハーネスが精査されます。 [検証してリリース](./06-verify-and-ship.md#vet-a-measured-number-with-benchmark-checklist) は、自分で入力する場合を示しています。

修正する前に原因を知りたい場合があります。リーク、アイドル状態の CPU スピン、視覚的な不具合などの実際の症状については、[ランタイム フォレンジック プレイブック](../../skills/poteto-mode/playbooks/runtime-forensics.md) が実行中のプロセスを計測します。すでにキャプチャしたプロファイルの場合、[トレース フォレンジック プレイブック](../../skills/poteto-mode/playbooks/trace-forensics.md) はアーティファクトを読み取り、ホット フレームをソースにマッピングします。どちらも、修正ではなく診断を返します。

```text
/poteto-mode here's a cpuprofile from the slow startup. tell me where the time goes and which source lines own it. no fix yet.
```

<a id="write-the-failing-test-first-with-tdd"></a>

## `/tdd` を使用して、失敗したテストを最初に書き込みます

バグに安価なローカル テスト パスがある場合、プロンプト全体が次の 2 語になることがあります。

```text
/tdd implement
```

文脈的にはそれで十分です。 [`/tdd`](../../skills/tdd/SKILL.md) は、意図した理由で失敗する最小のテストを作成し、次に修正を行って、テストを再実行します。テストに広範なハーネス設定または脆弱なモックが必要な場合、スキルはその旨を示し、代わりに最も近い実行可能チェックを使用します。実際のコマンドがより強力な証拠となるテストを強制しないでください。

<a id="load-the-typescript-rules-by-name"></a>

## TypeScript ルールを名前でロードします

[`typescript-best-practices`](../../skills/typescript-best-practices/SKILL.md) は、型システムの原則を具体的なルール (区別された共用体、境界での `unknown`、網羅的バリアント、スキーマ派生型) に変換します。単独では読み込まれないため、タスクが `.ts` または `.tsx` ファイルにアクセスする場合は、「`/typescript-best-practices`」と入力します。

<a id="clean-before-you-commit"></a>

## コミットする前にクリーンアップする

[PR プレイブックを開く](../../skills/poteto-mode/playbooks/opening-a-pr.md) は、各コミットの前に差分に対して `/deslop` を実行し、[`/unslop`](../../skills/unslop/SKILL.md) を PR の説明とコミット本体に適用します。 `/deslop` は pstack ではなく、`cursor-team-kit` プラグインに同梱されています。それをお持ちでない場合は、わかりやすい言葉で同じ結果を求めてください。ナレーション コメント、サポートされていないガード、無効な互換性パス、無関係な編集を削除してください。

文章の場合、`/unslop` はターゲットと追加のルールを受け取ります。

```text
/unslop the readme changes, no emdashes
```

独自の短縮表現を作成します。このスキルは、`unslop that, tighten it` のような簡潔なプロンプトから意図を適切に読み取ります。

<a id="strip-the-comments-with-no-comments"></a>

## `/no-comments` でコメントを削除します

コメントには、コメントを作成したエージェントからではなく、独自のパスが必要です。著者は、あなたが自分のコメントを擁護するのと同じように、自分のコメントを擁護します。したがって、レビューする前に、新しい目で見てください。

```text
/no-comments the diff
```

[`/no-comments`](../../skills/no-comments/SKILL.md) は、[Comment Sicko](../../agents/comment-sicko.md) を生成します。これは、ライセンス ヘッダー、パブリック API のドキュメント コメント、できないコードを説明するリンク、再形成できない外部依存関係によって強制される動作など、短い保持リストを持つ読み取り専用レビュアーです。それ以外はすべてうまくいきます。独自のコードにサプライズが含まれていても、そのようなパスは得られません。コメントはリファクタリング フラグとして返され、`/no-comments` は受け入れられるフラグを根本原因で修正します。コメントが「削除しない」という制約を要求する場合、スキルはその要求をタイプ、テスト、または lint としてエンコードすることを提案します。いずれにせよ、コメントは出ます。

分業は明確にしておく価値があります。 `/deslop` はコードから余分な部分を削除し、`/unslop` は文章を削除し、`/no-comments` はコメントを書いていないレビュー担当者にコメントを渡します。

**落とし穴:** クリーンアップはオプションのポリッシュではありません。ナレーションのコメントと防御的なデッドウェイトを含む差分は、レビュー担当者にとっては未完成であるように見え、追加のコードは次のバグが隠れている場所です。 diff が水増しされていると感じる場合は、レビューで呼び出された後ではなく、コミットする前に `deslop it` と言ってください。

次: [確認してリリース](./06-verify-and-ship.md)。
