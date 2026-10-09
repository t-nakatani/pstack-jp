<a id="benny"></a>

# ベニー

benny は、slack 問題レポート用に 2 つのCursor自動化を提供します。 1 人が各レポートを優先順位付けします。もう 1 つは確認されたバグを再現し、小さな修正草案を準備する可能性があります。

このディレクトリ内のファイルは、休止状態のセットアップおよびオートメーション ソースです。スラッシュスキルとしては登場しません。

<a id="set-it-up"></a>

## セットアップしてください

1. Cursorを [`FOR_AGENTS.md`](./FOR_AGENTS.md) にポイントし、ターゲット リポジトリに名前を付けます。
2. セットアップにより、このディレクトリ全体が `.cursor/automations/benny/` のターゲットにマージされます。ローカルの編集を上書きするのではなく、宛先のみのファイルを保存し、競合を確認する必要があります。
3. セットアップで、共有依存関係のターゲット リポジトリの `.cursor/settings.json` で pstack を有効にします。

```json
{
	"plugins": {
		"pstack": { "enabled": true }
	}
}
```

4. は、ユーザー所有の構成をコピーされたパックの外 (`.cursor/benny/` など) に保持します。 [`configuration.example.yaml`](./templates/configuration.example.yaml) および [`feature-map.example.md`](./skills/reproduce-and-fix-issues/references/feature-map.example.md) を適応させます。
5. いずれかの自動化を有効にする前に、`.cursor/settings.json`、`.cursor/automations/benny/`、およびシークレットなしの構成をコミットしてください。
6. は、新しいオートメーションのドラフトをそれぞれレビューするか、エディターで既存のオートメーションを更新します。次に、無害なテスト レポートを送信し、すべてのソース チャネルの投稿が元のスレッドに残っていることを確認します。
