t = open('index.html').read()
start = t.find('<div style="padding:2.5rem 2rem;background:var(--bg);border-bottom:1px solid var(--border);">')
end = t.find('<!-- PROBLEM -->', start)
if start > 0 and end > 0:
    t = t[:start] + t[end:]
    open('index.html','w').write(t)
    print('Removed duplicate')
else:
    print(f'start={start} end={end}')
