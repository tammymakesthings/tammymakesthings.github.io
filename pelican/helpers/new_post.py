#!/bin/env python

import sys
import os
import re
from datetime import date

parent_dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(parent_dir_path)
from pelicanconf import *

print("========================================================================")
print("                   Create new Pelican blog post v0.01                   ")
print("========================================================================")
print("")
post_title = ""
while len(post_title) == 0:
    post_title = input("Enter post title: ")
post_slug = re.sub(r'[^a-zA-Z0-9_-]', '', post_title.lower().replace(" ", "-"))
today = date.today().strftime("%Y-%m-%d")

post_filename = os.path.join(
    parent_dir_path, "content", "blog", f"{today}-{post_slug}.md")
print("Generating post in", post_filename)
with open(post_filename, "w") as f:
    f.write(f"title: {post_title}\n")
    f.write("category: misc\n")
    f.write("tags: misc\n")
    f.write("status: draft\n")
    f.write(f"date: {today}\n")
    f.write("author: Tammy\n")
print("Done.")
