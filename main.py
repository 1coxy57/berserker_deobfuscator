import argparse, asyncio
from berserker import decrypt

async def main(file: str) -> str:
    with open(file,'r') as f:
        content = f.read()
        res = await decrypt(content)
        return res


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="berserker deobf", usage="%(prog)s [options]", description="Berserker Deobfuscator")
    parser.add_argument('file',type=str,help='File you want to deobfuscate')
    args = parser.parse_args()
    
    result = asyncio.run(main(args.file))
    print('decoded', result)
    open('out.py','w').write(result)
    
