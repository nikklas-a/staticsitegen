from markdown2 import markdown 
from jinja2 import Environment, FileSystemLoader, Template
from json import load
from urllib.parse import urlparse  
from datetime import datetime  
from datetime import date
from os import listdir
from os.path import isfile, join
import os, shutil
import json

root_path = Environment(loader=FileSystemLoader(searchpath='./'))
post_template = root_path.get_template('site/templates/post_template.html')
about_template = root_path.get_template('site/templates/about_template.html')
index_template = root_path.get_template('site/templates/index_template.html')
today = date.today()


input_file = open ('./site/notpostscontent/published.json')
json_array = json.load(input_file)
post_list = []

# Looks for all files in "site/content/"
for files in os.listdir('./site/content/'):
    file = os.path.join('./site/content/', files)
        
    # If the file is a markdown file (.md) then open them as a markdown file to use for post.        
    if file.endswith(".md"):
        
      with open(file, 'r') as post_markdown_file:
            article = markdown(
            post_markdown_file.read(),
            extras=['fenced-code-blocks', 'code-friendly', 'metadata'])
            
            print(f"Rendering post from {file}...")
        
    # If the file is a json config file (.json) then open them as a json config file to use for post
    if file.endswith(".json"):
    
     with open(file, 'r') as config_file:
        config = load(config_file)
        post_slug = config['post_slug'] #auto generate filename ([slut].html) from slug defined in config file. 

        print(f"using config file: {file}")

        #The template is the same for all posts. Use this one:
        with open('site/html/posts/' + post_slug + '.html', 'w') as output_file:
        
         output_file.write(

                post_template.render(
                    
                    title=config['title'],
                    summary=config['summary'],
                    thumbnail=config['thumbnail'],
                    author=config['author'],
                    identifier=config['identifier'],
                    url=config['url'],
                    post_slug=config['post_slug'],
                    article=article,
                    date_created = config['date_created'],
                    date_generated = today,
                    tag_1 = config['tag_1'],
                    tag_2 = config['tag_2'],
                    tag_3 = config['tag_3'],
            )
)
        print(f"Rendered html file: {output_file}")
    
#Generate index.html (feed)       
#----------------------------------------------------------
    posts = []

    for post in json_array:
   
        post = dict(
                title = post['post_title'], 
                summary = post['post_summary'], 
                date = post['date_created'],
                author = post['post_author'],
                slug = post['post_slug'],
                date_generated = today,
                
                
                )
        
        posts.append(post)

    with open('site/html/index.html', 'w+') as file:
        html = index_template.render(
            
            posts=posts,
            date_generated = today,
            feed_title = "Feed",
            
            )
        
         
        
        file.write(html)
        
        print(f"Rendering index-page.")
    

#Generate about.html  
#----------------------------------------------------------
with open('site/notpostscontent/about.md') as about_markdown_file:
    article = markdown(
        about_markdown_file.read(),
        extras=['fenced-code-blocks', 'code-friendly', 'metadata'])
    
with open('site/notpostscontent/about.json') as about_config_file:
    
    config = load(about_config_file)
    
    with open('site/html/about.html', 'w') as output_file:
  
       post_slug_full = config['post_slug']
       date_created_short = config['date_created']
       
       output_file.write(
        
        about_template.render(
            
            title = config['title'],
            thumbnail = config['thumbnail'],
            author = config['author'],
            identifier = config['identifier'],
            url = config['url'],
            post_slug = post_slug_full.replace(" ", "-"), #replaces space with -
            article = article,
            date_created = config['date_created'],
            date_generated = today,
            tag_1 = config['tag_1'],
            tag_2 = config['tag_2'],
            tag_3 = config['tag_3']
        )          
    )
       
    print("Rendering about-page.")