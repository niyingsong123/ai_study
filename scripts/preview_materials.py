"""Render source PDF title pages for archival QA, without modifying PDFs."""
import concurrent.futures, json, math, subprocess
from pathlib import Path
from PIL import Image, ImageDraw, ImageOps

ROOT=Path(__file__).resolve().parents[1]
CACHE=ROOT/'tmp'/'materials-20261002'
PREVIEW=CACHE/'previews';PREVIEW.mkdir(exist_ok=True)
POPLER=Path(r'C:\Users\niyingsong\.cache\codex-runtimes\codex-primary-runtime\dependencies\native\poppler\Library\bin')
payload=json.loads((ROOT/'original_file'/'acquisition-20261002.json').read_text(encoding='utf-8'))
jobs=[(r,f) for r in payload['records'] if r['status'].startswith('archived') for f in r['files'] if f['path'].endswith('.pdf')]

def render(job):
    row,file=job
    target=PREVIEW/Path(file['path']).stem
    cmd=[str(POPLER/'pdftoppm.exe'),'-f','1','-l','1','-singlefile','-scale-to','900','-png',str(ROOT/file['path']),str(target)]
    result=subprocess.run(cmd,capture_output=True,text=True,encoding='utf-8',errors='replace')
    return dict(source_id=row['source_id'],path=file['path'],png=str(target.with_suffix('.png')),rendered=result.returncode==0,
                rendered_pages=[1],visually_reviewed=False,error=result.stderr if result.returncode else '')

with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool: records=list(pool.map(render,jobs))
successful=[r for r in records if r['rendered']]
sheets=[]
for index in range(math.ceil(len(successful)/9)):
    canvas=Image.new('RGB',(1320,1920),'#e6e8eb');draw=ImageDraw.Draw(canvas)
    for slot,record in enumerate(successful[index*9:index*9+9]):
        x=(slot%3)*440;y=(slot//3)*640
        draw.text((x+10,y+6),record['source_id']+' / PDF page 1',fill='black')
        with Image.open(record['png']) as source:
            thumb=ImageOps.contain(source.convert('RGB'),(420,600))
            canvas.paste(thumb,(x+10+(420-thumb.width)//2,y+30))
        record['contact_sheet']=index+1
    path=PREVIEW/f'contact-{index+1:02d}.png';canvas.save(path);sheets.append(str(path))

(CACHE/'pdf-preview-checks.json').write_text(json.dumps(dict(records=records,contact_sheets=sheets),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(pdfs=len(jobs),rendered=len(successful),sheets=sheets,errors=[r for r in records if not r['rendered']]),ensure_ascii=False))
