<a id="typescript-patterns"></a>

# TypeScript パターン

`SKILL.md` の各ルールのコード例。基礎となる原則は言語に依存しません。 **type-system-discipline** および **boundary-discipline** の原則スキルを参照してください。

<a id="branded-types"></a>

## ブランドのタイプ

プリミティブをブランド化し、混同できないようにします。境界で一度検証します。ダウンストリーム コードはその型を信頼します。

```ts
type AgentId = string & { readonly __brand: "AgentId" };

function parseAgentId(input: string): AgentId {
  if (!isUUID(input)) throw new Error(`Invalid agent id: ${input}`);
  return input as AgentId;
}

function focusAgent(id: AgentId): void {
  /* input is trusted */
}
```

`readonly __brand: 'X'` 形状と一致します。新しい慣例を考え出さないでください。

<a id="discriminated-unions"></a>

## 判別可能なユニオン

リテラルの判別式を使用したモデル バリアント。すべてのバリアントはフィールド名を共有し、各バリアントの値は一意であるため、不可能なコンボを表現することはできません。

```ts
// Don't. Boolean + optionals lets contradictory states exist.
type DiffState = { loading: boolean; diff?: GitDiff; error?: string };

// Do. Only valid states exist.
type DiffState =
  | { kind: "loading" }
  | { kind: "ready"; diff: GitDiff }
  | { kind: "error"; error: string };
```

識別名 (`kind`、`type`、`tag`) を 1 つ選択し、それを使用します。

<a id="constructive-modeling"></a>

## 建設的なモデリング

実行時チェックでルーズな型を制限するのではなく、すべて正当な部分から型を構築します。

空ではない、可変個引数タプル経由:

```ts
type NonEmpty<T> = [T, ...T[]];

// Don't: T[] plus a length check every caller must repeat
function pickWinner(entries: string[]): string {
  if (entries.length === 0) throw new Error("no entries");
  return entries[Math.floor(Math.random() * entries.length)];
}

// Do: an empty value of the type can't exist
function pickWinner(entries: NonEmpty<string>): string {
  return entries[Math.floor(Math.random() * entries.length)];
}
```

プレーンの`T[]`が到着したところで、ガードで1回狭めます。ファクトは次の型で伝わります。

```ts
const isNonEmpty = <T>(arr: T[]): arr is NonEmpty<T> => arr.length > 0;
```

偶数の長さ、ペア:

```ts
type Pairs<T> = [T, T][];
```

時間範囲 (開始時間と継続時間):

```ts
// Don't: a comment holds the invariant
type TimeRange = { start: Date; end: Date }; // start <= end

// Do: a negative range can't be written; derive end when needed
type TimeRange = { start: Date; durationMs: number };
```

`durationMs` は単純な数値にしておきます。反射的にではなく、期間が予想される場所に生の数値を渡すことができる場合にのみ、(ブランド型ごとに) ブランド化します。不良状態を構築不可能にする表現を選択し、必要な読み取り値をその上に公開します (`pairs.flat()`、`rangeEnd()` ヘルパー)。

<a id="simplest-total-type"></a>

## 最もシンプルなトータルタイプ

全てを強化する必要はありません。すべての操作が合計された場合は、`T[]` を保持します。

```ts
const sum = (xs: number[]) => xs.reduce((a, b) => a + b, 0); // [] is 0, fine
```

ルースタイプは使用現場で嘘を強いられる場合に強化します。伝えられる内容は、`!`、`arr[0] as T`、および「決して発生してはならない」スローです。

```ts
// Don't: partiality smuggled past the compiler
function newestSession(sessions: Session[]): Session {
  return sessions.at(0)!;
}

// Do: strengthen the input; the assertion disappears
function newestSession(sessions: NonEmpty<Session>): Session {
  return sessions[0];
}
```

結果を `Session | undefined` に弱めることは、もう 1 つの全体的な特徴です。

<a id="unknown-over-any"></a>

## `unknown` が `any` を超えました

外部データは常に `unknown` です。使用前に狭くしてください。

```ts
// Don't
function handle(input: any) {
  return input.foo.bar;
}

// Do
function handle(input: unknown) {
  if (typeof input === "object" && input !== null && "foo" in input) {
    // narrowed; compiler verifies access
  }
}
```

外部ソースには、RPC ペイロード、`JSON.parse`、`postMessage`、IPC、ファイルの内容、環境変数、データベースの結果が含まれます。

<a id="schemas-before-hand-rolled-guards"></a>

## ハンドロールガード前のスキーマ

外部データのプロパティごとの型ガードを作成する前に、リポジトリのランタイム スキーマ ライブラリと既存のスキーマを探してください。 1 つのスキーマが独自の検証を行い、そこから TypeScript 型を派生させます。バラバラになる可能性のあるスキーマ、重複したインターフェイス、およびガードを維持しないでください。

```ts
import { z } from "zod";

const UserSchema = z.object({
  id: z.string().uuid(),
  role: z.enum(["admin", "member"]),
});

type User = z.infer<typeof UserSchema>;

function parseUser(input: unknown): User {
  return UserSchema.parse(input);
}
```

分岐の失敗が予想される場合は、`safeParse` を使用します。リポジトリが別のスキーマ ライブラリを使用する場合は、同等の推論ヘルパーを使用します。 1 つのガードに新しいスキーマ依存関係を追加しないでください。このルールでは、コードベースがすでに信頼しているスキーマ システムが優先されます。

<a id="no-as-casts"></a>

## `as` キャストはありません

すべての `as` はランタイム クラッシュの可能性があります。型システムがクレームを検証した後にのみキャストします。

```ts
import { z } from "zod";

// Don't
const user = data as User;

// Don't
function isUser(data: unknown): data is User {
  return typeof data === "object" && data !== null && "id" in data;
}

// Do
const userSchema = z.object({ id: z.string(), name: z.string() });
type User = z.infer<typeof userSchema>;

function parseUser(data: unknown): User {
  return userSchema.parse(data);
}
```

型が最初にある場合は、検証された型でバリデーターに注釈を付けます。その後、コンパイラは、その型より小さいことを証明するバリデータを拒否します。以下のオブジェクトから `name` を削除すると、割り当てはコンパイルに失敗します。

```ts
type User = { id: string; name: string };

const userSchema: z.ZodType<User> = z.object({ id: z.string(), name: z.string() });
```

既存のコードから `as` をリファクタリングするときに、TypeScript が推論できない理由を特定します。

- 判別式がありません: 1 つ追加し、判別式共用体に切り替えます。
- 幅が広すぎるソース タイプ (`Record<string, unknown>` など): 狭くします。
- 型なし境界: 形状を所有するスキーマで解析します。スキーマが存在しない場合にのみスキーマを追加します。
- まったく表現不能です: ブランドのタイプまたは `satisfies` を使用してください。

<a id="narrowing-hierarchy"></a>

## 階層の絞り込み

最善から最後の手段まで:

1. **識別共用体スイッチ / if.** コンパイラは自動的に絞り込みます。
2. **`in` 演算子.** `"key" in obj` は、そのキーを含むバリアントに絞り込みます。
3. **`typeof` / `instanceof`.** プリミティブおよびクラス インスタンス用。
4. **ユーザー定義の型ガード。** 上記だけでは不十分な場合。
5. **`as` キャスト。** 検証後のみ。

```ts
function area(s: Shape): number {
  if ("radius" in s) return Math.PI * s.radius ** 2; // narrowed to circle
  return s.width * s.height; // narrowed to rect
}
```

<a id="type-guards"></a>

## タイプガード

警備員はその主張を実際に検証する必要があります。嘘つきのガードは `as` よりも悪いです。

```ts
function isCircle(s: Shape): s is Shape & { kind: "circle" } {
  return s.kind === "circle";
}
```

可能な場合は判別式狭めを優先します。

<a id="exhaustiveness"></a>

## 徹底

デフォルトのアームでは、判別式を `never` 型のローカルに割り当てます。

```ts
// Value-returning switch
function area(s: Shape): number {
  switch (s.kind) {
    case "circle":
      return Math.PI * s.radius ** 2;
    case "rect":
      return s.width * s.height;
    default: {
      const _exhaustive: never = s;
      return _exhaustive;
    }
  }
}

// Void switch
function handle(s: Shape): void {
  switch (s.kind) {
    case "circle":
      drawCircle(s);
      break;
    case "rect":
      drawRect(s);
      break;
    default: {
      const _exhaustive: never = s;
      void _exhaustive;
    }
  }
}
```

値を返すスイッチでは return スタイル、ステートメント スイッチでは void スタイル。

<a id="satisfies-over-as"></a>

## `satisfies` が `as` を超えました

`satisfies` は、リテラル型を拡張せずに検証します。

```ts
// Don't. Widens, loses literal types.
const config = { theme: "dark", cols: 3 } as Config;

// Do. Validates AND preserves literal types.
const config = { theme: "dark", cols: 3 } satisfies Config;
// config.theme is "dark" (literal), not string
```

<a id="boundary-validation"></a>

## 境界検証

データが交差する場所を一度検証します。内部のタイプを信頼します。 **boundary-discipline**原則スキルを参照してください。

- **ワイヤ形式** (プロト、JSON-RPC): `ignoreUnknownFields` で解析するため、前方互換性のある変更によって古いクライアントが壊れることはありません。
- **永続的な JSON:** 解析の周りに try/catch を持つバージョン管理された BLOB。
- 呼び出しチェーンの奥深くでは **再検証しないでください**。

<a id="schema-derived-types"></a>

## スキーマ派生型

`.proto`、OpenAPI 仕様、GraphQL スキーマ、またはデータベースの移行によって既にシェイプが定義されている場合、それらを複製するのではなく、生成されたタイプから派生します。

```ts
// Don't. Duplicate shape, drifts when the schema changes.
type CheckSummary = {
  totalCount: number;
  checks: { name: string; status: string }[];
};
function renderChecks(s: CheckSummary) {
  /* ... */
}

// Do. Derive from the generated schema type.
import type { ChecksMessage } from "<generated module>";
function renderChecks(s: Pick<ChecksMessage, "totalCount" | "checks">) {
  /* ... */
}
```

新しいインターフェイスを作成する前に、`Pick`、`Omit`、`Parameters`、`ReturnType`、`Awaited`、`typeof` に到達してください。

<a id="object-args"></a>

## オブジェクト引数

```ts
// Don't. Swap two args, still compiles.
openFile(uri, {
  startLineNumber: 10,
  startColumn: 1,
  endLineNumber: 10,
  endColumn: 1,
});

// Do. Order-independent, self-documenting.
openFile({
  uri,
  selection: {
    startLineNumber: 10,
    startColumn: 1,
    endLineNumber: 10,
    endColumn: 1,
  },
});
```

ホット パスをスキップします: フレームごとのレンダリング、トークナイザー、パーサー、割り当てコストが重要となる緊密なループ内のすべてのもの。
