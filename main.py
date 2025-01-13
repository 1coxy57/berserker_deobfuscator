import argparse, asyncio
from berserker import decrypt
import os, sys
import logging
import colorlog


formatter = colorlog.ColoredFormatter("%(log_color)s%(asctime)s - %(levelname)s - %(message)s")
handler = logging.StreamHandler()
handler.setFormatter(formatter)

logger = logging.getLogger()
logger.setLevel(level=logging.INFO)
logger.addHandler(handler)

async def main(file: str) -> str:
    try: 
        with open(file,'r',encoding="utf-8") as f:
            content = f.read()
            res = await decrypt(content)
            return res
    except:
        logger.error('An error occured while trying to decrypt the file')
        sys.exit(0)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog="berserker deobf by coxy57", usage="%(prog)s [options]", description="Berserker Deobfuscator")
    parser.add_argument('file',type=str,help='File you want to deobfuscate')
    args = parser.parse_args()

    if not os.path.exists(args.file):
        logger.warning('File does not exist.')
        sys.exit(0)

    try:
        result = asyncio.run(main(args.file))
        logger.log('Successfully deobfuscated and wrote to out.py')
        open('out.py','w').write(result)
    except Exception as e:
        logging.error('Error: ' + e)
        sys.exit(0)
    
