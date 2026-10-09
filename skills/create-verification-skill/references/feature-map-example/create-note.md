<a id="create-a-note"></a>

# メモを作成する

メモの作成では、ユーザーはブラウザまたは CLI からタイトル付きメモを保存し、未完成の下書きをキャンセルし、保存されたメモを 2 番目のユーザー向けビューから確認できます。

<a id="sub-features"></a>

## サブ機能

- `create-open` は、ブラウザーの各エントリ ポイントから空のエディターを開きます。
- `create-save` はタイトルと本文を保持します。
- `create-cancel` は未完成のブラウザーの下書きを破棄します。
- `create-cli` は端末から同じノート形状を作成します。

<a id="how-to-get-to-it-user-pov"></a>

## アクセス方法 (ユーザー視点)

- ブラウザのツールバーで `New note` ボタンを選択します。
- フォーカスが編集可能なフィールドの外にあるときに、ブラウザで `n` を押します。
- ターミナルで `notes create --title <title> --body <body>` を実行します。

<a id="driving-it-with-control-notes"></a>

## コントロールノートで操作する

前提条件:

- Notes は `http://127.0.0.1:4173` で正常です。
- `Release checklist` というタイトルのメモはありません。
- `control-notes doctor` は、予期される URL と使い捨てデータ ディレクトリを報告します。

- **エディターを開きます。** `New note` を選択します。 `control-notes browser click --role button --name "New note"` を実行します。 `Note editor` という名前のフォームが `Title` テキストボックスにフォーカスされて表示されます。
- **内容を入力してください。** タイトルと本文を入力します。 `control-notes browser fill --role textbox --name "Title" --value "Release checklist"` と `control-notes browser fill --role textbox --name "Body" --value "Tag and publish"` を実行します。 `Save note` ボタンが有効になります。
- **メモを保存します。** `Save note` を選択します。 `control-notes browser click --role button --name "Save note"` を実行します。 `Note saved` というステータスが表示され、見出しには `Release checklist` が表示されます。
- **永続性を確認します。** メモ リストに戻り、メモを再度開きます。 `control-notes browser click --role link --name "All notes"` と `control-notes browser click --role link --name "Release checklist"` を実行します。エディターには両方の保存された値が表示されます。
- **下書きをキャンセルします。** 新しいメモを開き、`Discard me` と入力し、`Cancel` を選択します。 `control-notes browser click --role button --name "New note"`、`control-notes browser fill --role textbox --name "Title" --value "Discard me"`、および `control-notes browser click --role button --name "Cancel"` を実行します。メモ リストが返されますが、`Discard me` リンクはありません。
- **CLI エントリ。** 2 番目のメモを作成します。 `control-notes cli -- notes create --title "CLI note" --body "Created from terminal" --format json` を実行します。終了コード `0` と標準出力には、新しいノート ID とタイトルが含まれています。
- **証明** `All notes` から保存した両方のメモを再度開きます。 `control-notes browser snapshot --aria --path artifacts/create-note/list.aria.txt` および `control-notes browser screenshot --path artifacts/create-note/list.png` を実行します。アーティファクトには `Release checklist` と `CLI note` が表示されます。

<a id="gotchas"></a>

## 留意点

- テキストボックスにフォーカスがあるときに `n` を押すと、新しいエディターを開く代わりに文字が入力されます。
- タイトルは保存時にトリミングされます。ドラフト入力値ではなく、レンダリングされたタイトルをアサートします。
- 保存ステータスだけでは証拠としては不十分です。リストからメモを再度開きます。
- フィクスチャのクリーンアップ中に `Release checklist` と `CLI note` を削除しますが、プルーフ アーティファクトは保持します。
