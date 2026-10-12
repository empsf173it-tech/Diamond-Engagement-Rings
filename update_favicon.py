import os
import glob
import re

dir_path = r'e:\OfficeDownloads_\JulyWebsites\Watch_Jewellery_Showroom'
html_files = glob.glob(os.path.join(dir_path, '*.html'))

favicon_tag = '<link rel=\"icon\" type=\"image/png\" href=\"assets/images/favicon.png\">'

for file_path in html_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if favicon already exists
    if 'rel=\"icon\"' in content or 'rel=\"shortcut icon\"' in content:
        # replace existing
        content = re.sub(r'<link[^>]*rel=[\"\'](?:shortcut )?icon[\"\'][^>]*>', favicon_tag, content)
    else:
        # insert before </head>
        content = content.replace('</head>', f'    {favicon_tag}\n</head>')
        
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

print(f'Updated {len(html_files)} files.')
