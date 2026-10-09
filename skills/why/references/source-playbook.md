<a id="source-playbooks"></a>

# ソース プレイブック

Why スキルは、利用可能な証拠カテゴリごとに 1 人の調査員を生成し、それぞれが以下の単一のソース固有のプレイブックを読み取ります。プレイブックは、一般的な MCP の具体的な例です。同じカテゴリ内の別の MCP にそれらを適応させます。

| カテゴリ | プレイブック | ドキュメント化された MCP の例 |
|---|---|---|
|ソース管理履歴 | [`code-archaeology.md`](./sources/code-archaeology.md) | git、`gh` |
| 問題 / チケットトラッカー | [`linear.md`](./sources/linear.md) | リニア (Jira、GitHub の問題、プレーン、ショートカットに適応) |
| 長い形式の文書 | [`notion.md`](./sources/notion.md) | Notion (Confluence、Google ドキュメント、Coda に適応) |
| リアルタイムのチームチャット | [`slack.md`](./sources/slack.md) | Slack (Discord、Microsoft Teams、Mattermost に適応) |
| インフラストラクチャの可観測性 | [`datadog.md`](./sources/datadog.md) | Datadog (New Relic、Honeycomb、Grafana、Splunk に適応) |
| エラー/例外の追跡 | [`sentry.md`](./sources/sentry.md) | セントリー (ロールバー、バグスナッグ、エアブレーキに適応) |
| 製品分析ウェアハウス | [`databricks.md`](./sources/databricks.md) | Databricks SQL (Snowflake、BigQuery、ClickHouse、dbt に適応) |

横断的:

- [`incident-postmortem.md`](./sources/incident-postmortem.md)。ターゲット コードが防御的であると思われる場合 (null チェック、再試行、タイムアウト、レート制限、機能フラグ、出力ガード、OOM ハンドラー)、これを追加します。
