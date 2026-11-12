#!/usr/bin/env python3
"""VSEVENTYFIVE owner-scoped chart worker; Python stdlib only."""
import base64, json, os, time, urllib.request, urllib.error
URL = os.environ.get('V75_URL', '').rstrip('/')
KEY = os.environ.get('V75_API_KEY', '')
OLLAMA = os.environ.get('OLLAMA_URL', 'http://localhost:11434').rstrip('/')
MODEL = os.environ.get('OLLAMA_MODEL', 'qwen2.5vl:7b')
def request(url, data=None, worker=False):
    headers = {'Content-Type': 'application/json'}
    if worker: headers.update({'X-Api-Key': KEY, 'X-Worker-Name': MODEL})
    req = urllib.request.Request(url, None if data is None else json.dumps(data).encode(), headers)
    with urllib.request.urlopen(req, timeout=600) as response: return json.load(response)
def main():
    if not URL.startswith('https://') or not KEY: raise SystemExit('Set V75_URL (published HTTPS address) and V75_API_KEY before starting.')
    while True:
        try:
            queue = request(URL + '/api/public/reviews/queue?limit=1&claim=1&include_prompt=1', worker=True)
            for review in queue['reviews']:
                try:
                    images = []
                    for key in ('image_url', 'context_image_url'):
                        if review.get(key):
                            with urllib.request.urlopen(review[key], timeout=60) as image: images.append(base64.b64encode(image.read()).decode())
                    context = {k:v for k,v in review.items() if k not in ('image_url', 'context_image_url')}
                    result = request(OLLAMA + '/api/chat', {'model': MODEL, 'stream': False, 'format': queue['output_schema'], 'messages': [{'role': 'system', 'content': queue['system_prompt']}, {'role': 'user', 'content': 'Audit this chart. Return JSON only. Context: ' + json.dumps(context), 'images': images}]})
                    content = result['message']['content'].strip()
                    if content.startswith('```'): content = content.split('\n',1)[1].rsplit('```',1)[0]
                    request(URL + '/api/public/reviews/' + review['id'] + '/verdict', {'evaluation': json.loads(content), 'worker_name': MODEL}, worker=True)
                    print('Audit submitted:', review['id'])
                except Exception:
                    request(URL + '/api/public/reviews/' + review['id'] + '/verdict', {'error': 'Local worker evaluation failed. Check Ollama and retry from the desk.'}, worker=True)
                    print('Local evaluation failed; review marked failed.')
        except urllib.error.HTTPError as error:
            if error.code in (401,403): raise SystemExit('Worker key rejected. Generate a new active key.')
            print('Queue unavailable; waiting before next check.')
        except Exception: print('Connection unavailable; waiting before next check.')
        time.sleep(10)
if __name__ == '__main__':
    try: main()
    except KeyboardInterrupt: print('Worker stopped.')
