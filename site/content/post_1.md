---
title: First
date: 2019-04-15
tags: Introduktion, Planering, Budget
thumbnail: img/1.jpg
summary: First static text Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
slug: post-1
---

# H1 Test
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Nullam eget felis eget nunc lobortis mattis aliquam faucibus purus. Quis imperdiet massa tincidunt nunc pulvinar sapien et ligula ullamcorper. Volutpat commodo sed egestas egestas fringilla phasellus faucibus scelerisque. Eget aliquet nibh praesent tristique magna sit amet. Odio pellentesque diam volutpat commodo sed egestas egestas. Nec dui nunc mattis enim. Elit duis tristique sollicitudin nibh sit amet commodo nulla facilisi. <br><br> Ac ut consequat semper viverra nam libero justo laoreet. Duis at consectetur lorem donec massa sapien faucibus. Amet nulla facilisi morbi tempus iaculis urna. Maecenas sed enim ut sem viverra aliquet eget sit. Porttitor leo a diam sollicitudin. Nisl suscipit adipiscing bibendum est ultricies. Commodo ullamcorper a lacus vestibulum sed arcu non odio euismod. Et pharetra pharetra massa massa ultricies mi quis hendrerit dolor. <br> <br>Enim praesent elementum facilisis leo vel. Tempor nec feugiat nisl pretium fusce id velit ut. Diam phasellus vestibulum lorem sed risus ultricies tristique. Consequat id porta nibh venenatis cras sed felis eget.
<br><br>
Eget aliquet nibh praesent tristique magna sit amet. Odio pellentesque diam volutpat commodo sed egestas egestas. Nec dui nunc mattis enim. Elit duis tristique sollicitudin nibh sit amet commodo nulla facilisi.

<br><br> Ac ut consequat semper viverra nam libero justo laoreet. Duis at consectetur lorem donec massa sapien faucibus. Amet nulla facilisi morbi tempus iaculis urna. Maecenas sed enim ut sem viverra aliquet eget sit. Porttitor leo a diam sollicitudin. Nisl suscipit adipiscing bibendum est ultricies. Commodo ullamcorper a lacus vestibulum sed arcu non odio euismod. Et pharetra pharetra massa massa ultricies mi quis hendrerit dolor. Enim praesent elementum facilisis leo vel. Tempor nec feugiat nisl pretium fusce id velit ut. Diam phasellus vestibulum lorem sed risus ultricies tristique. Consequat id porta nibh venenatis cras sed felis eget.Eget aliquet nibh praesent tristique magna sit amet. Odio pellentesque diam volutpat commodo sed egestas egestas. Nec dui nunc mattis enim. Elit duis tristique sollicitudin nibh sit amet commodo nulla facilisi. Ac ut consequat semper viverra nam libero justo laoreet. Duis at consectetur lorem donec massa sapien faucibus. Amet nulla facilisi morbi tempus iaculis urna. Maecenas sed enim ut sem viverra aliquet eget sit. Porttitor leo a diam sollicitudin. Nisl suscipit adipiscing bibendum est ultricies. Commodo ullamcorper a lacus vestibulum sed arcu non odio euismod. Et pharetra pharetra massa massa ultricies mi quis hendrerit dolor. Enim praesent elementum facilisis leo vel. Tempor nec feugiat nisl pretium fusce id velit ut. Diam phasellus vestibulum lorem sed risus ultricies tristique. Consequat id porta nibh venenatis cras sed felis eget.

## H2 Rubrik

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Nullam eget felis eget nunc lobortis mattis aliquam faucibus purus. Quis imperdiet massa tincidunt nunc pulvinar sapien et ligula ullamcorper. Volutpat commodo sed egestas egestas fringilla phasellus faucibus scelerisque. Eget aliquet nibh praesent tristique magna sit amet. Odio pellentesque diam volutpat commodo sed egestas egestas. Nec dui nunc mattis enim. Elit duis tristique sollicitudin nibh sit amet commodo nulla facilisi. <br><br>


								niklas@arvidsson.xyz
								https://www.arvidsson.xyz 
								https://github.com/nikklas-a?tab=repositories
								+46 72 443 8236 


<br>

 Ac ut consequat semper viverra nam libero justo laoreet. Duis at consectetur lorem donec massa sapien faucibus. Amet nulla facilisi morbi tempus iaculis urna. Maecenas sed enim ut sem viverra aliquet eget sit. Porttitor leo a diam sollicitudin. Nisl suscipit adipiscing bibendum est ultricies. Commodo ullamcorper a lacus vestibulum sed arcu non odio euismod. Et pharetra pharetra massa massa ultricies mi quis hendrerit dolor. <br> <br>Enim praesent elementum facilisis leo vel. Tempor nec feugiat nisl pretium fusce id velit ut. Diam phasellus vestibulum lorem sed risus ultricies tristique. Consequat id porta nibh venenatis cras sed felis eget.

### H3 Rubrik 

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Nullam eget felis eget nunc lobortis mattis aliquam faucibus purus. Quis imperdiet massa tincidunt nunc pulvinar sapien et ligula ullamcorper. Volutpat commodo sed egestas egestas fringilla phasellus faucibus scelerisque. Eget aliquet nibh praesent tristique magna sit amet. Odio pellentesque diam volutpat commodo sed egestas egestas. Nec dui nunc mattis enim. Elit duis tristique sollicitudin nibh sit amet commodo nulla facilisi. <br><br> Ac ut consequat semper viverra nam libero justo laoreet. Duis at consectetur lorem donec massa sapien faucibus. Amet nulla facilisi morbi tempus iaculis urna. Maecenas sed enim ut sem viverra aliquet eget sit. Porttitor leo a diam sollicitudin. Nisl suscipit adipiscing bibendum est ultricies. Commodo ullamcorper a lacus vestibulum sed arcu non odio euismod. Et pharetra pharetra massa massa ultricies mi quis hendrerit 

**Exempelkod:**

<?php

function getPosts() {
	
	global $conn;
	$sql = "SELECT * FROM posts WHERE published=true";

    $result = mysqli_query($conn, $sql);

	$posts = mysqli_fetch_all($result, MYSQLI_ASSOC);

	return $posts;
    
    }

