<a id="multi-phase-or-multi-pr-plan"></a>

### マルチフェーズまたはマルチ PR プラン

**あなたはコードではなくプランを所有します。計画は、所有者がボックスごとに実行するチェックリストであり、オペレーターは証拠に基づいて監査します。** 計画は成果物です。実装しないでください。

1. 変更が 1 つまたは 2 つのファイルであり、明らかなアプローチである場合は、計画をスキップしてください。そう言ってやめてください。
2. 執筆する前にプロトタイプによって未解決の質問を解決してください。それぞれに対して `playbooks/prototype.md` を実行します。付録 A のブランチ、SHA、およびスクリーンショットを保管しておいてください。オペレータに尋ねるのは、実行によって解決できない製品または優先順位の問い合わせについてのみにしてください。オプションを与えます (**人間をブロックしない** 原則スキル)。
3. `subagent_type: "poteto-agent"` とサブエージェント セクションに基づく明示的なモデル (**コンテキスト ウィンドウの保護** 原則スキル) を使用してサブエージェント内を探索します。それぞれがファイル ポインタ、規則、テスト コマンド、およびエントリ ポイントを返します。インラインダンプはありません。
4. 以下のスケルトンを計画ファイルにコピーし、すべてのプレースホルダーを埋めます。オペレーターがパスに名前を付けない限り、エージェント ストアの `docs/` の下にファイルを書き込みます。すべての見出しとすべてのサブブロックを、示されている順序に保ちます。 PR ごとに 1 つのセクション。 1 つの PR は、独自の証拠を持つ 1 つの変更です (**sequence-verifiable-units** 原則スキル)。 **この読み方**で実行プレイブックに名前を付けます。 `playbooks/autopilot-stack.md` の最後にあるルールに従って、`playbooks/autopilot-full.md` と `playbooks/autopilot-stack.md` のいずれかを選択します。常駐プログラムには `playbooks/orchestrate.md` かかります。
5. `/technical-writing` の下に完全に書き込み、次に `/unslop` を書き込みます。本体は1つのDiátaxisモード、ハウツーです。付録には説明と参考資料が含まれています。各見出しにはタスクまたは結果が記載されています。長いダッシュはありません。文中にコロンはありません。
6. `node pstack/skills/poteto-mode/scripts/check-plan.mjs <plan.md>` を実行し、出力されるすべての行を修正します (**encode-lessons-in-structure** の原則スキル)。
7. 手を戻します。プランのパスとスクリプトの出力をポストして、停止します。実行は、プラン名に指定された実行プレイブックの下で、オペレーターの明示的な実行によって開始されます。

**検証。** テストだけでは十分な検証とはなりません。 PR は、そのユニット、ライブ、パフォーマンス ボックスがすべてチェックされている場合にのみ検証されます (**prove-it-works** 原則スキル)。その文が検証ルールです。すべての検証ブロックはそれとともに開きます。ライブブロックは必須です。 PR ヘッドの 10 レーンは、`swarm workers` モデル (デフォルト `grok-4.7-xhigh-fast`) の **swarm** スキルに従って、制御スキルを通じて実際のサーフェスを駆動します。各レーンは、具体的なシナリオ、保存されるスクリーンショット、およびそのパス述語を含む 1 つのボックスです。 1 つのレーンは **体幹に対する回帰レーン** です。体幹と頭に対して同じ耐荷重シナリオを実行します。トランクにその機能がない場合、レーンはその事実を記録し、トランクの結果を作成する代わりに、diff が追加する動作に加えて、ユーザーが待機する最終状態をゲートします。パフォーマンス ゲートは両面です。トランクとヘッドの両方が名前付きメトリックを生成する必要があります。トランクにその機能がない場合は、差分によって追加される作業を分離し、その作業とユーザーが待機するエンドツーエンドの状態に対する絶対的な予算を設定します。異なるシナリオ間の比率を主張しないでください。 perf ブロックは、メトリック、インターリーブ プローブ、最初に測定されたトランク ベースライン、および失敗した番号を持つルールに名前を付けます。インタラクションを変更する PR はレビューゲートされます。オペレーターは、結合する前にスクリーンショットとビデオを使用してチャットでそれを確認します。インタラクションを変更しない PR は `**Review gate.** None. <PR id> is not review-gated.` を書き込み、その下にボックスは書き込みません。

**コントロールスキル** 面で選択します。ブラウザ、Electron、Web UI は `cursor-team-kit` から `control-ui` を使用します。 CLI と TUI は、`cursor-team-kit` から `control-cli` を使用します。ネイティブ モバイルは、リポジトリが持つシミュレータ駆動スキルをすべて使用します。 2 つのサーフェスに触れた PR は両方のレーンを取得します。コントロールスキルのない路面は付録 C ではリスクであり、そのライブブロックは依然として各レーンがどのように走行するかを示しています。

````markdown
# <Program> plan

<Under ten lines. What changes, for whom, the rule the program enforces, and the PR ids in order.>

## How to read this

One box is one unit of work. Every box names the evidence that checks it. A nested box is a sub-step of the box above it. Check a box only when its evidence exists, a file, a log line, a screenshot, a test run, or a SHA. The body is a how-to. The appendices explain and record.

The program runs `pstack/skills/poteto-mode/playbooks/<execution playbook>.md`. <Who merges, and which PR ids are the operator's items that stop at merge-ready.>

Tests alone are not sufficient verification. A PR is verified only when its unit, live, and perf boxes are all checked.

## Program checklist

### Arm the program

- [ ] State the protocol and this plan to the operator, then stop. Start execution only on the operator's explicit go.
- [ ] Read these from trunk at program start. Re-read them at every tick.
  - [ ] `git show origin/main:pstack/skills/poteto-mode/playbooks/<execution playbook>.md`
  - [ ] `git show origin/main:pstack/skills/swarm/SKILL.md`
  - [ ] `git show origin/main:<control skill path>`
  - [ ] `git show origin/main:pstack/skills/poteto-mode/playbooks/opening-a-pr.md`
  - [ ] `git show origin/main:pstack/skills/<each other leaf skill the program uses>`
- [ ] On the operator's go, arm the audit tick as `/loop 1h` with the tick prompt below. Never leave the cadence to memory.
- [ ] Use this tick prompt, verbatim. "Re-read the execution playbook from trunk. Audit the operation against it and fix drift in this tick. Probe every active lane and judge progress by side effects only. Stand down a stuck lane and dispatch its replacement now. Then post a short status message to the operator in chat only when the audit found a tracked change that no earlier status message reported, such as a PR opened, a code-ready head, a round launched or closed, a verdict, a merge, a stuck agent and the action taken, a blocker added or cleared, or a decision only the operator can make. Name every such change and nothing else. Do not repeat a table, the merged list, or an unchanged blocker. If the audit found none, end the turn with no reply text. Either way, log this tick's row in your decision trail. The row names the items reported, or none."
- [ ] On the operator's hold or stand-down, send every owner a zero-writes order at once.

### Spawn owners

- [ ] Spawn one owner per PR with the full lifecycle the execution playbook names.
- [ ] Follow this dependency graph. Start dependent work only after its parent merges, or base it on the parent branch when the execution playbook stacks.
  - [ ] <PR id> and <PR id> are independent and first. Both branch from `main`.
  - [ ] <PR id> after <PR id>.
- [ ] Hold the file boundaries. <PR id or class> touches only `<glob>`.
- [ ] Hold the review gate. <PR ids> change an interaction. They wait for the operator's review in chat with screenshots and a video before merge.

### PR mechanics, for every PR

- [ ] Resolve the forge once. Default to `gh`; if `command -v origin` succeeds and Origin can resolve the repository, use `origin pr` for every PR operation. Record any fallback to `gh`. Never require `gt`.
- [ ] Open the PR ready, never draft, per **Opening a PR**. Use the run's built-in PR tool when it has one, else `origin pr create --status open --base <base-branch>` or `gh pr create --base <base-branch>` according to the resolved forge. A stack child targets its parent branch.
- [ ] Run the repo's lint and typecheck once before the PR-facing push. Push with hooks on.
- [ ] Run `/deslop` before each commit and `/no-comments` before review.
- [ ] Triage every Bugbot and security-reviewer comment per `../references/bugbot-triage.md`.
- [ ] Rebase onto current trunk before the code-ready report and babysit. Keep that merge base in fix rounds. Rebase again only at merge prep, on a `git merge-tree` conflict with trunk, or on a CI failure that comes from a change on trunk.

### Verdict and merge, for every PR

- [ ] At the code-ready head SHA and at each later push that changes the patch, run the swarm per `pstack/skills/swarm/SKILL.md`. One gates lane. The ten live lanes from the PR's **Verify, live** block. The perf lane from its **Verify, perf** block. Two or more audit lanes, each with its own focus, that read the diff and the receipts and distrust the PR body. The root audits the receipts in the merge-ready report before the verdict.
- [ ] Clean only when every lane is `PASS`. Findings go back to the owner, including a defect that a lane filed as a note. A new head gets a fresh swarm and a fresh verdict, except for results that stay valid under the patch-id rule in `playbooks/shipping.md`.
- [ ] <The merge or append rule from the execution playbook, with the patch-id rule from `playbooks/shipping.md`.>

### Boot recipe, for every live lane

Each live lane runs on its own cloud VM at the PR head. Drive through `control-ui` or `control-cli` from `cursor-team-kit`.

- [ ] `git fetch origin <head-branch> && git checkout <head SHA>`.
- [ ] <Start the backend and the surface. Wait for ready.>
- [ ] <Deliver input only through the control skill's commands. Name the read-only diagnostics.>
- [ ] Save every screenshot to `/tmp/swarm-<pr-id>/worker-<n>/<slug>.png` and return the paths with the report.

## <Task as a verb phrase> (<PR id>)

**Depends on.** <PR id, or None.>

**Files.**

- [ ] Edit `<path>`.
- [ ] Create `<path>`.
- [ ] Delete `<path>`.

**Build.**

- [ ] <One change. Name the symbol and the file.>

**You see.**

- [ ] <One observable result, with the exact log line or screen state.>

**Verify, unit.** Tests alone are not sufficient verification. A PR is verified only when its unit, live, and perf boxes are all checked.

- [ ] <Test file and the case it gains.> Run `<command>`.

**Verify, live.** Tests alone are not sufficient verification. A PR is verified only when its unit, live, and perf boxes are all checked. Ten lanes on `<swarm workers model>` at the PR head, per the boot recipe.

- [ ] Lane 1. Regression lane against trunk. Run <the same load-bearing scenario> at trunk and head. If trunk lacks the feature, record that and gate <the behavior the diff adds plus the end state the user waits for>. Save `<slug>.png`. Pass when <predicate>.
- [ ] Lane 2. <Scenario.> Save `<slug>.png`. Pass when <predicate>.
- [ ] Lane 3. <Scenario.> Save `<slug>.png`. Pass when <predicate>.
- [ ] Lane 4. <Scenario.> Save `<slug>.png`. Pass when <predicate>.
- [ ] Lane 5. <Scenario.> Save `<slug>.png`. Pass when <predicate>.
- [ ] Lane 6. <Scenario.> Save `<slug>.png`. Pass when <predicate>.
- [ ] Lane 7. <Scenario.> Save `<slug>.png`. Pass when <predicate>.
- [ ] Lane 8. <Scenario.> Save `<slug>.png`. Pass when <predicate>.
- [ ] Lane 9. <Scenario.> Save `<slug>.png`. Pass when <predicate>.
- [ ] Lane 10. <Scenario.> Save `<slug>.png`. Pass when <predicate>.

**Verify, perf.** Tests alone are not sufficient verification. A PR is verified only when its unit, live, and perf boxes are all checked.

- [ ] Metric. <What is measured at both trunk and head. If trunk lacks the feature, also name the diff-added work and the end-to-end state the user waits for.>
- [ ] Probe. <The command or procedure, run at trunk and at the head, interleaved. Both sides must produce the metric.>
- [ ] Baseline. Record the trunk <value> first.
- [ ] Rule. <Head against trunk, with the number that fails. If the scenarios differ, add absolute budgets for the diff-added work and the user-visible end state instead of an invalid ratio.>

**Review gate.** The operator reviews before merge.

- [ ] Copy lane <n> screenshots into `<media path>/<pr-id>-review-<slug>.png`.
- [ ] Record a 30 to 60 second video of the change on a lane VM. Save it as `<media path>/<pr-id>-review.mp4`.
- [ ] Post the screenshots and the video in chat. Stop at merge-ready. Wait for the operator's click.

**Merge.**

- [ ] Root's clean verdict at the exact head SHA.
- [ ] Bugbot triage done.
- [ ] Rebased onto current trunk after the verdict, patch-id unchanged.
- [ ] <The owner squash-merges its own PR, or the root appends it to the base-branch stack and the operator lands it bottom-up.>

## Close the program

- [ ] Every box above is checked with its evidence.
- [ ] Reply to the operator with the report the execution playbook names.

## Appendix A. Prototype evidence

<Each open question a prototype answered, with the branch, the SHA, and the artifact links. Each question that stays unproven.>

## Appendix B. Alternatives rejected

<Each approach weighed and why it lost.>

## Appendix C. Risks

<Each risk with the PR it lands in and what the owner watches.>

## Appendix D. Links and reading list

<Docs to read before editing. Which PRs get `pstack/skills/how/SKILL.md` and `pstack/skills/interrogate/SKILL.md`. The trail per `pstack/skills/show-me-your-work/SKILL.md`.>
````

**返信:** プラン パス、PR ID とその依存関係、レビュー ゲート セット、プロトタイプで証明されたものと証明されていないもの、およびチェック スクリプトの出力。
