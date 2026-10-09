<a id="search-notes"></a>

# 検索メモ

検索を使用すると、ユーザーはタイトルまたは本文テキストでメモを検索し、一致するメモを検査し、一致しないメモと使用できない検索を区別できます。

<a id="sub-features"></a>

## サブ機能

- `search-open` は、サポートされている各ブラウザー エントリ ポイントから検索を開きます。
- `search-match` は、ノート データを変更せずにタイトルと本文の一致を返します。
- `search-open-result` は、ノートエディターで結果を開きます。
- `search-empty` は、一致するものがないクエリの完全な空の状態を示します。
- `search-clear` はクエリを削除し、最近のメモ ビューを復元します。
- `search-cli` は、端末から同じ一致するメモを返します。

<a id="how-to-get-to-it-user-pov"></a>

## アクセス方法 (ユーザー視点)

- ブラウザのツールバーで `Search` ボタンを選択します。
- フォーカスが編集可能なフィールドの外にあるときに、ブラウザーで `/` を押します。
- ターミナルで `notes search <query>` を実行します。

<a id="driving-it-with-control-notes"></a>

## コントロールノートで操作する

前提条件:

- Notes は `http://127.0.0.1:4173` で正常です。
- 使い捨てデータ ディレクトリには、本文テキスト `Draft budget` を含む `Quarterly plan` が含まれています。
- `control-notes doctor` は、予期される URL とデータ ディレクトリを報告します。

- **ツールバーのエントリ。** `Search` ボタンを選択します。 `control-notes browser click --role button --name "Search"` を実行します。 `Search notes` という名前のダイアログが表示され、検索ボックスにフォーカスが置かれます。
- **キーボード入力。** ダイアログを閉じ、ページにフォーカスして、`/` を押します。 `control-notes browser press --key "/"` を実行します。同じダイアログが表示されますが、ページにはスラッシュが挿入されません。
- **タイトルが一致しました。** `quarterly` と入力します。 `control-notes browser fill --role searchbox --name "Search notes" --value "quarterly"` を実行します。 `Search results` リストには `Quarterly plan` が含まれていますが、`Grocery list` は含まれていません。
- **本文一致。** クエリを `budget` に置き換えます。 `control-notes browser fill --role searchbox --name "Search notes" --value "budget"` を実行します。結果 `Quarterly plan` は、本文一致の抜粋とともに表示されたままになります。
- **結果を開きます。** `Quarterly plan` を選択します。 `control-notes browser click --role link --name "Quarterly plan"` を実行します。ダイアログが閉じ、エディターの見出しに `Quarterly plan` が表示されます。
- **空の状態。** 検索を再度開き、`volcano` と入力します。 `control-notes browser fill --role searchbox --name "Search notes" --value "volcano"` を実行します。検索が完了すると、`No matching notes` というステータスが表示されます。
- **クエリをクリアします。** `Clear search` を選択します。 `control-notes browser click --role button --name "Clear search"` を実行します。検索ボックスは空で、`Recent notes` 領域が結果リストを置き換えます。
- **CLI 一致。** ターミナルから検索します。 `control-notes cli -- notes search "quarterly" --format json` を実行します。終了コード `0` と標準出力には、タイトルが `Quarterly plan` であるオブジェクトが 1 つ含まれています。
- **CLI ミス。** 存在しない値を検索します。 `control-notes cli -- notes search "volcano" --format json` を実行します。終了コード `0` と標準出力は `[]` です。
- **証明** 入力された結果の状態をキャプチャします。 `control-notes browser snapshot --aria --path artifacts/search/results.aria.txt` と `control-notes browser screenshot --path artifacts/search/results.png` を実行します。どちらのアーティファクトも、Notes、クエリ、および `Quarterly plan` を識別します。

<a id="gotchas"></a>

## 留意点

- エディターまたは検索ボックスにフォーカスがあるときに `/` を押すと、検索を開く代わりにテキストが挿入されます。
- 短いデバウンスの後に結果が更新されます。固定スリープではなく、結果リストまたは空のステータスを待ちます。
- アーカイブされたメモは、ユーザーが `Include archived` を有効にしない限り除外されます。
- CLI のデフォルトは人間が判読できる出力です。安定したアサーションには `--format json` を使用します。
- 結果を開くとブラウザの状態が変わります。別のクエリを証明する前に、検索を再度開いてください。
