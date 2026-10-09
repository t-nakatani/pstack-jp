<a id="code-archaeology-git--in-repo"></a>

# コード考古学 (git + インリポジトリ)

<a id="what-this-source-contains"></a>

## このソースの内容

- コミット履歴 (メッセージ、日付、作成者、差分)
- PR の説明、レビュー コメント、ディスカッション スレッド (`gh` 経由)
- インライン コード コメント、TODO、FIXME、非推奨ノート
- ADR (アーキテクチャ決定レコード) (リポジトリに保存されている場合)
- テスト。名前とアサーションは、多くの場合、変更の動機となったエッジケースをエンコードしています。
- 同じコミットで変更された関連ファイル (同時変更シグナル)
- CHANGELOG エントリ、リポジトリ内のリリース ノート
- コミット メッセージおよび PR ボディに記載されている問題/チケット ID

最も信頼できるソースであり、コードに直接関連付けられており、最も完全です。リポジトリを通過したものはすべてここにあるはずです。

<a id="how-to-search-it"></a>

## 検索方法

シード コミット リストを展開します。

```bash
# Full history of the file through renames
git log --follow --oneline -- <file>

# Pickaxe: commits that added or removed this exact text
git log -S '<exact_string_from_code>' -- <file>

# Or for patterns:
git log -G '<regex>' -- <file>

# Who wrote each line and when
git blame -L <start>,<end> <file>

# The full diff of a specific commit
git show <hash>

# Commits between two points affecting this file
git log <old>..<new> -p -- <file>
```

実質的なコミットごとに、PR コンテキストをプルします。

```bash
# Find the PR number from the merge commit or branch
git log -1 --format=%B <hash>

# Full PR context: body, review comments, linked issues
gh pr view <number> --json title,body,author,createdAt,mergedAt,labels,closingIssuesReferences,comments,reviews,files

# The --json reviews and comments fields are where the real signal is
```

帯域外ドキュメントを探します。

```bash
# ADRs often live in docs/adr/ or similar
rg -l -i 'architecture.decision' --glob '*.md'

# TODOs and FIXMEs near the target
rg -n -C2 '(TODO|FIXME|HACK|XXX|NOTE)' <target_file>

# Related tests. Names often encode the "why"
rg -l '<symbol>' --glob '*test*'
```

<a id="what-good-evidence-looks-like-here"></a>

## 良い証拠は次のとおりです

- 単なる変更ではなく、解決される問題を説明する PR 説明 (「これにより、X の原因となったページネーションのバグが修正されます」)
- 代替案が議論された長いレビュー スレッド
- 非自明な制約を説明するターゲット行の近くのインライン コメント
- コードを動機付けるエッジケースを明らかにする `test_handles_edge_case_when_X` という名前のテスト
- チケットまたはインシデント ID を参照するコミット メッセージ
- ユーザーに表示される根拠を要約した CHANGELOG エントリ

<a id="common-pitfalls"></a>

## よくある落とし穴

- **フラットランドのスカッシュマージ。** リポジトリが PR をスカッシュすると、ブランチ履歴内の個々のコミットが失われます。 PR 本文とコメントに戻ります。
- **誤解を招くコミット メッセージ。** 「小規模なリファクタリング」により、意図的な動作の変更が隠蔽される場合があります。メッセージではなく差分を見てください。
- **カルト崇拝のパターン。** 作成者は理由を理解せずにパターンをコピーした可能性があります。パターンがコードベースの以前に発生したかどうかを確認し、*その* コミットを調査します。
- **ボットのコミットと自動マージ。** 通常、Dependabot、Renovate、および自動化されたバックポートには動機がありません。意図を見つけようとするときはそれらをスキップしてください。
- **コードを意図の証拠として扱う** コード自体は、その存在理由の証拠ではありません。証拠はコミットメッセージ、PR、コメント、テスト、ドキュメントから得られます。意図の証拠として「関数の名前は X です」と引用しないでください。

<a id="what-to-return"></a>

## 返すもの

質問に関連するすべてのコミット/PR/コメント:
- 正確なテキスト (引用)
- ハッシュ / PR 番号 / ファイル:行
- 作成者と日付
- 直接的（質問に明示的に対処している）か状況的なものか
