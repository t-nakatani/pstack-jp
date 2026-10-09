<a id="routing-map-example"></a>

# ルーティングマップの例

このファイルを `.cursor/automations/benny/` の外 (たとえば `.cursor/benny/routing.md`) にコピーし、すべてのプレースホルダーを置き換えます。コピーに `routing.map_path` を指定します。パックの更新によって上書きされてはなりません。

トリアージ スキルはこれをデータとして扱います。ルートには、レポートまたは原因追跡からの証拠が必要です。キーワード一致だけでは十分ではありません。

```yaml
routes:
  - name: "billing-example"
    match:
      product_areas:
        - "billing-area-placeholder"
      code_paths:
        - "billing-code-path-placeholder"
      error_signatures:
        - "billing-error-placeholder"
    destination:
      slack_channel: "billing-channel-placeholder"
      tracker_team: "billing-team-placeholder"
    owners:
      - "billing-owner-placeholder"
    allow_feature_owner_ping: false

  - name: "desktop-example"
    match:
      product_areas:
        - "desktop-area-placeholder"
      code_paths:
        - "desktop-code-path-placeholder"
      error_signatures:
        - "desktop-error-placeholder"
    destination:
      slack_channel: "desktop-channel-placeholder"
      tracker_team: "desktop-team-placeholder"
    owners:
      - "desktop-owner-placeholder"
    allow_feature_owner_ping: false

fallback:
  destination: ""
  owners: []
  allow_feature_owner_ping: false

ping_policy:
  default: "off"
  allow:
    - "configured-feature-owner"
    - "confirmed-regression-author"
  deny:
    - "broad-on-call-group"
    - "unverified-owner"
```

<a id="rules"></a>

## ルール

- 1 つのチームが一致しないレポートをすべて受け入れる場合を除き、`fallback.destination` は空のままにしておきます。
- 安定した製品領域、コード パス、およびエラー署名を使用します。
- パブリック コピーにプライベート データを含めないでください。
- 公開されるサンプルに生のユーザー ID またはチャネル ID を貼り付けないでください。
- 対象チームが同意するまで、機能所有者の ping をオフにしておきます。
- リルートはレポーターにどこへ行くべきかを伝えます。自動化がクロスポストされることはありません。
