import re

def normalize(title):
    title = title.lower()
    title = title.replace("’", "'")
    title = re.sub(r"\s*:\s*", ":", title)
    title = re.sub(r"\s+", " ", title)
    return title.strip()

def merge_unique_by_name(existing, new):
    seen = {normalize(g.get("title")) for g in existing if "title" in g}
    for key in new:
        print(key)
        for g in new[key]:
            name = g.get("title")
            if name and normalize(name) not in seen:
                existing.append(g)
                seen.add(name)
    