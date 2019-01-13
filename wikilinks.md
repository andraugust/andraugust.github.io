---
layout: default
---

# Exploring the First-Link Taxonomy of Wikipedia

<br />
<center><img src="../wikilinks/Banner.png" /></center>
<br />

Wikipedia articles often begin with a sentence of the form "<em>\<current article\> is a \<link\></em>".  For example, the article for <a href="https://en.wikipedia.org/wiki/Dog" target="\_blank">dog</a> begins with "The domestic dog is a member of the genus canis...", the first link being 'canis'.  Similarly the article for <a href="https://en.wikipedia.org/wiki/Canis" target="\_blank">canis</a> begins with "Canis is a genus of...", the first link being genus.  Genus links to taxonomic, taxonomic links to science, science links to knowledge, etc.

So where do these first links eventually go?  It turns out that many of them lead to Philosophy, an interesting result that stems from the use of is-a's.  First-links usually go to what might be called the immediate superclass of a current page, so the more first links clicked the more abstract pages become until a very abstract page like Philosophy is reached.

To see what the taxonomy looks like I decided to make an interactive network visualizer.  The dataset of links came from applying a regex to <a href="https://www.mediawiki.org/wiki/API:Main_page">Wikipedia API</a> responses and the visualization uses a javascript library called <a href="http://visjs.org/">visjs</a>.

The entire network has about 5M nodes (pages) each with one directed edge (first link) pointing out of it.  There are many disconnected subgraphs, usually of size 2 or 3, due due to deviations from the is-a protocol or because a page has no links in its first paragraph (a deadend).  Most nodes belong to a very small number of giant subgraphs.  The two biggest subgraphs contain 4M and 0.15M nodes (the third biggest has about 0.08M).

Unfortunately it's hard to visualize networks this big in-browser, so I removed nodes that don't have parents--those on the perimeter.  I did this twice, reducing the networks to about 70k and 4k pages.

The second largest disconnected subgraph (originally 0.15M, now 4k) is shown below.  Click the image to interact with it.

<center><a href="../wikilinks/net4k/net.html"><img src="../wikilinks/net4k.png" /></a></center>
<br />
<center>The second largest component in Wikipedia's page taxonomy.  Click to view the interactive version.</center>
<br />

The network layout was determined through a force-directed physics technique.  Each edge exerts a damped spring force on its adjacent nodes and all nodes exert a long-range attractive force like gravity on each other.  In addition there's a short-range repelling force that prevents nodes from forming a 'black hole'.

Nodes are initialized arbitrarily on the perimeter of a circle and the physics simulation steps until a stopping condition is satisfied.  I stopped the simulation when the fastest node became slower than a threshold (another option is to wait until the change in average speed is less than a threshold).

The 70k network is shown below.  It's much slower to load compared to the 4k network, but still do-able.

<center><a href="../wikilinks/net70k/net.html"><img src="../wikilinks/net70k.png" /></a></center>
<br />
<center>The largest component in Wikipedia's page taxonomy.  Click to view the interactive version.</center>
<br />

If you want to download a network you can do so by opening the one you want in a new tab and then run the following commands in the javascript console: `network.storePositions(); var nodeList = data.nodes.get(data); copy(nodeList);`, this saves the network as a json formatted string to the clipboard.  To save the clipboard contents to a file open a terminal and do `$ pbpaste > mynetwork.json`.

Necessarily both networks converge to a limit cycle.  The 4k network converges to _Mathematics_ → _Quantity_ → _Magnitude_ → _Mathematics_ and the 90k network converges to what's shown below:
<br />
<center><img src="../wikilinks/loop.png" style="height:60%; width:60%"></center>
<br />
<center>Clicking first-links repeatedly will lead to this limit cycle for about 90% of pages.</center>
<br />

In the '\<subset\> is a \<superset\>' analogy these nine nodes in union comprise the most abstract set. Combined they contain about 90% of pages, forming what might be called the base of Wikipedia's tree of knowledge. (Or at least the base of _English_ Wikipedia's tree of knowledge.  For an interesting analysis on the variation in attractor across countries, see reference [2].)

Attractor members differ in the number of pages leading to them.  The table below shows the fraction of pages leading to each attractor node.  We'll call this the node's _abstractness_.  Knowledge has a much higher abstractness than Philosophy, so even though several first-link accounts have focused on Philosophy it seems more appropriate to focus on Knowledge.

| Page Name | Abstractness |
|:----------:|:------------:|
| Knowledge | 0.59 |
| Philosophy | 0.30 |
| Fact | 0.08 |
| Education | 0.02 |
| Argument | <0.01 |
| Logic | <0.01 |
| Learning | <0.01 |
| Axiom | <0.01 |
| Premise | <0.01 |

Here's the abstractness distribution of the un-trimmed giant component.  The distribution is approximately linear on a log-log scale suggesting a power law relationship.
<br />
<center><img src="../wikilinks/abstractness_dist.png" style="height:70%; width:70%"></center>
<br />
We can also look at the distribution over distances to the center attractor.  The average distance is about 10, though nearly all pages are closer than 30, the really far out pages take about 50 clicks.  Far out pages tend to be events linking to the same event a year before/after it.  For example _23rd_Parliament_of_Ontario_ links to _22nd_Parliament_of_Ontario_ links to _21st_Parliament_of_Ontario_, etc.  Some aren't like this though, for example _Mugain_ and _Clothru_ (mythological Irish characters) are at a distance of 41.
<br />
<center><img src="../wikilinks/distance_to_center.png" style="height:70%; width:70%"></center>
<br />

That's all for now.  I highly recommend reading reference [2] for a look at how taxonomy structures vary across cultures. Have fun!

### Notes
1. Due to the continuous editing of Wikipedia (and of first links in particular) the networks shown here will be different from what they would be today.  The current dataset comes from June 2017.
2. The 4k attractor shows that Meaning_of_life → Instrumental_and_intrinsic_value → Dichotomy → Partition_of_a_set → Mathematics → Quantity → Magnitude_(mathematics) → Mathematics.  Could it be argued that the meaning of life is a subset of mathematics?  I wouldn't read into it :)

### References
1. Wikipedia's own article called "Getting to Philosophy": <a href="https://en.wikipedia.org/wiki/Wikipedia:Getting_to_Philosophy">link</a>
2. An article on arXiv about how first-link structure varies across cultures: <a href="https://arxiv.org/pdf/1708.05368.pdf">link</a>
3. A dynamic taxonomy visualizer: <a href="https://xefer.com/wikipedia">link</a>

{% include disqus.html %}
