#!/usr/bin/env python3
"""日本語版と同梱の上流スナップショットの構造を照合する。標準ライブラリのみ。"""
from pathlib import Path
from collections import Counter
import hashlib,json,re,tarfile,sys
ROOT=Path(__file__).resolve().parents[1]

def fences(text):
 blocks=[];active=None;block=[]
 for line in text.splitlines(keepends=True):
  m=re.match(r'^\s*(`{3,}|~{3,})',line)
  if active:
   block.append(line)
   if m and m[1][0]==active[0] and len(m[1])>=active[1]:
    blocks.append(''.join(block));active=None;block=[]
  elif m:active=(m[1][0],len(m[1]));block=[line]
 if active:raise ValueError('閉じていないコードブロック')
 return blocks

def inline(text):
 for block in fences(text):text=text.replace(block,'')
 return Counter(re.findall(r'`+[^`\n]+`+',text))

def frontmatter(text):
 if not text.startswith('---\n'):return None
 return text.split('---',2)[1]

def main():
 meta=json.loads((ROOT/'upstream/source.json').read_text())
 archive=ROOT/meta['snapshot']
 assert hashlib.sha256(archive.read_bytes()).hexdigest()==meta['snapshot_sha256'],'原文アーカイブのSHA-256が一致しません'
 errors=[];md_count=skill_count=playbook_count=0
 with tarfile.open(archive,'r:gz') as tar:
  for member in tar.getmembers():
   if not member.isfile():continue
   path=Path(member.name).relative_to('pstack');target=ROOT/path
   if not target.is_file():errors.append(f'{path}: ファイルがありません');continue
   original=tar.extractfile(member).read()
   if path.suffix!='.md':
    if str(path)!='.cursor-plugin/plugin.json' and target.read_bytes()!=original:errors.append(f'{path}: 翻訳対象外のファイルが変更されています')
    continue
   md_count+=1;skill_count+=path.name=='SKILL.md';playbook_count+='playbooks' in path.parts
   en=original.decode();ja=target.read_text()
   if path.name=='README.md' and len(path.parts)==1:
    ja=ja.split('<!-- BEGIN UPSTREAM TRANSLATION -->\n',1)[-1]
   if en==ja:errors.append(f'{path}: 未翻訳です')
   if not re.search(r'[ぁ-んァ-ヶ一-龯]',ja):errors.append(f'{path}: 日本語の説明がありません')
   if re.search(r'__PSTACK_|ZXQ\d+QXZ',ja):errors.append(f'{path}: 翻訳用のプレースホルダーが残っています')
   try:
    if fences(en)!=fences(ja):errors.append(f'{path}: コードブロックが原文と一致しません')
    if inline(en)!=inline(ja):errors.append(f'{path}: インラインコードが原文と一致しません')
   except ValueError as e:errors.append(f'{path}: {e}')
   for link,count in Counter(re.findall(r'\]\(([^\n]*?)\)',en)).items():
    if ja.count(']('+link+')')!=count:errors.append(f'{path}: リンク先が変わっています: {link}')
   ef,jf=frontmatter(en),frontmatter(ja)
   if ef:
    if not jf:errors.append(f'{path}: YAMLフロントマターがありません');continue
    for field in ['name','disable-model-invocation','model','tools','color']:
     em=re.search(r'^'+field+r':.*$',ef,re.M);jm=re.search(r'^'+field+r':.*$',jf,re.M)
     if bool(em)!=bool(jm) or em and em[0]!=jm[0]:errors.append(f'{path}: {field} が変更されています')
    dm=re.search(r'^description:\s*(.*)$',jf,re.M)
    ed=re.search(r'^description:\s*(.*)$',ef,re.M)
    if ed and ed[1].startswith(('>', '|')) and (not dm or dm[1]!=ed[1]):errors.append(f'{path}: description のYAML折り返し形式が変更されています')
    if dm and dm[1].startswith('"'):
     try:json.loads(dm[1])
     except json.JSONDecodeError:errors.append(f'{path}: description の引用符が不正です')
 manifest=json.loads((ROOT/'.cursor-plugin/plugin.json').read_text())
 assert manifest['name']=='pstack-jp'
 assert manifest['author']['name']=='Lauren Tan'
 assert manifest['license']=='MIT'
 print(f'Markdown {md_count}件 / SKILL.md {skill_count}件 / プレイブック {playbook_count}件を照合')
 if errors:
  print('\n'.join(errors));return 1
 print('PASS: 原文アーカイブ、全訳の存在、コード、リンク先、識別子、ライセンスを確認')
 return 0
if __name__=='__main__':sys.exit(main())
