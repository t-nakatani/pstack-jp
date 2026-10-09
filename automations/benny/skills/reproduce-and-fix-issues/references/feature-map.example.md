<a id="feature-map-example"></a>

# 機能マップの例

Benny が再現できるすべてのユーザー向け機能をマップします。アプリを実行する前に、関連するセクションをお読みください。このマップはユーザーの視点で保管してください。ここで内部情報と現在のコード パスを凍結するのではなく、実行時に検出します。

このファイルを `.cursor/automations/benny/` の外部 (たとえば `.cursor/benny/feature-map.md`) にコピーし、そのコピーに `control.feature_map_path` を設定します。パックの更新によって上書きされてはなりません。

<a id="per-feature-template"></a>

## 機能ごとのテンプレート

<a id="feature-name"></a>

### `<feature name>`

`<one-line user-visible purpose>`

<a id="how-a-user-gets-there"></a>

#### ユーザーがそこに到達する方法

- クリックパス: `<screen> -> <menu, tab, or panel> -> <control>`
- キーボード ショートカット: `<shortcut or none>`

<a id="how-the-control-adapter-drives-it"></a>

#### 制御アダプターによる駆動方法

- `<adapter action>` と `<inputs>` は `<visible result>` でなければなりません。
- リセット: `<how the adapter returns to a fresh state>`。

<a id="stable-selectors"></a>

#### 安定したセレクター

- `<role and accessible name>`
- `<ARIA relationship>`
- `<data-component or purpose-named data attribute>`

生成された CSS クラスや StyleX クラス、動的ハッシュ、子インデックス、または脆弱な DOM 位置は決して使用しないでください。

<a id="states-to-exercise"></a>

#### 行使する国家

- デフォルト、ホバー、フォーカス表示、アクティブ、無効
- 読み込み中、空、エラー
- 選択、開い、展開
- `<relevant feature-specific variants>`

該当しない状態にマークを付けます。

<a id="preconditions-and-setup"></a>

#### 前提条件とセットアップ

- 認証: `<account state>`
- データ: `<fixture>`
- 権限: `<role>`
- フラグ: `<flag or none>`
- サービス: `<required availability>`

<a id="evidence-and-cross-check"></a>

#### 証拠とクロスチェック

- スクリーンショット: `<app identity, feature, and discriminating state>`
- ビデオ: `<entry path, interaction, and final state>`
- クロスチェック: `<read-only state or value that confirms the UI>`

<a id="gotchas"></a>

#### 留意点

- `<known dead end or wrong surface>`
- `<safe environment translation>`

<a id="fictional-example"></a>

## 架空の例

これらの機能は、架空のタスク アプリに属します。これらは例であり、Benny の必須機能ではありません。

<a id="sign-in"></a>

### サインイン

ユーザーがタスク アプリに入ることができるようにします。

<a id="how-a-user-gets-there"></a>

#### ユーザーがそこに到達する方法

- アプリを開き、`Sign in` を選択します。近道はありません。

<a id="how-the-control-adapter-drives-it"></a>

#### 制御アダプターによる駆動方法

- `open_app`、`click Sign in`、`fill credentials`、および `click Continue` は項目リストを開く必要があります。
- サインアウトして破棄セッションをクリアすることでリセットします。

<a id="stable-selectors"></a>

#### 安定したセレクター

- ボタン `Sign in`、テキストボックス `Email` および `Password`、`data-component="sign-in-form"`

<a id="states-to-exercise"></a>

#### 行使する州

- デフォルト、フォーカス表示、送信中、無効、読み込み中、エラー

<a id="preconditions-and-setup"></a>

#### 前提条件とセットアップ

- 使い捨てアカウントと利用可能な認証サービス

<a id="evidence-and-cross-check"></a>

#### 証拠とクロスチェック

- 項目リストを通じてランディング ページを記録します。読み取り専用のセッション状態を確認します。

<a id="gotchas"></a>

#### 留意事項

- マーケティング ページは間違った表面です。認証サービスが欠落しているとブロックになります。

<a id="item-list-and-detail"></a>

### アイテムリストと詳細

ユーザーがアイテムを参照してアイテムを開くことができるようにします。

<a id="how-a-user-gets-there"></a>

#### ユーザーがそこに到達する方法

- [`Items`] タブを開き、行を選択します。

<a id="how-the-control-adapter-drives-it"></a>

#### 制御アダプターによる駆動方法

- `select_tab Items` と `click <fixture item>` で詳細が開きます。
- 詳細を閉じて選択をクリアしてリセットします。

<a id="stable-selectors"></a>

#### 安定したセレクター

- `Items` という名前のタブとリスト、フィクスチャという名前の行、`data-component="item-detail"`

<a id="states-to-exercise"></a>

#### 行使する州

- 読み込み中、空、エラー、選択済み、開いている、展開されています

<a id="preconditions-and-setup"></a>

#### 前提条件とセットアップ

- 名前付きフィクスチャ アイテム、読み取り権限、利用可能なアイテム サービス

<a id="evidence-and-cross-check"></a>

#### 証拠とクロスチェック

- 選択内容と一致する詳細タイトルを表示します。選択項目IDを確認します。

<a id="gotchas"></a>

#### 留意点

- 検索結果は似ているように見えますが、異なるパスを使用する場合があります。

<a id="item-editor"></a>

### アイテムエディター

ユーザーが項目を作成または編集できるようにします。

<a id="how-a-user-gets-there"></a>

#### ユーザーがそこに到達する方法

- 詳細から `Edit` を選択するか、リストから `New item` を選択します。

<a id="how-the-control-adapter-drives-it"></a>

#### 制御アダプターによる駆動方法

- `click Edit`、`fill <field>`、および `click Save` は詳細を更新する必要があります。
- フィクスチャを復元してリセットします。

<a id="stable-selectors"></a>

#### 安定したセレクター

- ボタン `Edit`、`New item`、`Save`、フォーム `Item editor`、ラベルにリンクされたフィールド

<a id="states-to-exercise"></a>

#### 行使する州

- デフォルト、フォーカス表示、ダーティ、検証中、無効、保存、エラー、成功

<a id="preconditions-and-setup"></a>

#### 前提条件とセットアップ

- 編集可能なフィクスチャ、書き込み権限、利用可能な保存サービス

<a id="evidence-and-cross-check"></a>

#### 証拠とクロスチェック

- 更新された詳細によるフィールドの変更を表示します。格納されている項目の値を読み取り専用で確認します。

<a id="gotchas"></a>

#### 留意点

- フォーム状態を注入しません。読み取り専用の詳細フィールドはエディターではありません。

<a id="settings"></a>

### 設定

ユーザーが個人設定を変更できるようにします。

<a id="how-a-user-gets-there"></a>

#### ユーザーがそこに到達する方法

- プロファイル メニューを開き、`Settings` を選択します。

<a id="how-the-control-adapter-drives-it"></a>

#### 制御アダプターによる駆動方法

- `open_menu Profile`、`click Settings`、および `toggle <preference>` はコントロールを更新する必要があります。
- 開始設定を復元してリセットします。

<a id="stable-selectors"></a>

#### 安定したセレクター

- ボタン `Profile`、メニュー項目 `Settings`、領域 `Settings`、目的名付きプリファレンス属性

<a id="states-to-exercise"></a>

#### 行使する州

- 閉じている、開いている、選択されている、フォーカスが表示されている、無効になっている、読み込み中、エラー

<a id="preconditions-and-setup"></a>

#### 前提条件とセットアップ

- サインインしたテスト アカウント、既知の設定、利用可能な設定サービス

<a id="evidence-and-cross-check"></a>

#### 証拠とクロスチェック

- メニュー パスと最終的なコントロール状態を表示します。設定値を読み取り専用で確認します。

<a id="gotchas"></a>

#### 留意点

- オペレーティング システムの設定は別の面です。

<a id="completeness-checklist"></a>

## 完全性チェックリスト

- 再現可能なすべてのユーザー向け機能にはセクションがあります。
- 各セクションでは、ユーザー パス、アダプター アクション、およびリセットに名前を付けます。
- セレクターは、ロール、名前、ARIA、安定したコンポーネント マーカー、または目的の名前が付けられた属性を使用します。
- 生成されたクラスまたは DOM 位置を使用するセレクターはありません。
- 関連するインタラクション、読み込み中、空、エラー、選択済み、および展開された状態がカバーされています。
- 認証、フィクスチャ、権限、フラグ、およびサービスは明示的です。
- スクリーンショット、ビデオ、および基礎となるクロスチェック要件は明示的です。
- 間違ったサーフェス、行き止まり、安全な環境の変換がリストされています。
- 実装の詳細は実行時の検出のままです。
