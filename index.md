---
layout: default
---

# Ship Segmentation for Kaggle's Ship Detection Challenge

This post follows my development of a dense ship segmenter for a recent Kaggle challenge.  The basic pipeline consists of a ship/noship CNN followed by a Unet and some post-processing. The results.

# Exploring the First-Link Taxonomy of Wikipedia

An interesting property of Wikipedia is that each page's first-link often goes to its immediate superset.  For example, 'poker' first-links to 'card game' and 'card game' first-links to 'game', etc.  Where do all these first-links go?  And what does the first-link taxonomy of Wikipedia look like?

# Satellite Image Classification on the fMoW Dataset

This post documents the use of CNNs for satellite image classification on The Functional Map of the World dataset. I look at fine-tuning, the effect of sample size distribution, and the effect of adding spatial context.

# Reinforcement Learning IRL

This is post describes an Arduino robot that learns to crawl using Q-learning.  Included is a video/tutorial showing the robot in action.

# Discovering Class-Hierarchies by Clustering Confusion Matrices

This is an example showing how class hierarchies can be discovered by applying spectral clustering to a confusion matrix.

# Artificial Life, Neural Nets, and Genetic Algorithms

Can neural nets control Artificial Life agents?  Can genetic algorithms optimize such neural nets?  In this post a GA called Enforced Subpopulations is implemented to show that _yes_ GAs can optimize NNs, and _yes_ NNs can effectively control AL agents.

# Solving Threes

Threes is a dice game definitely worth knowing.  Do _you_ know how to play Threes?  Do _you_ know how to win at Threes?  Here I explain the rules of Threes and use backward induction to find its optimal policy.





Text can be **bold**, _italic_, or ~~strikethrough~~.

[Link to another page](./another-page.html).

There should be whitespace between paragraphs.

There should be whitespace between paragraphs. We recommend including a README, or a file with information about your project.

# Header 1

This is a normal paragraph following a header. GitHub is a code hosting platform for version control and collaboration. It lets you and others work together on projects from anywhere.

## Header 2

> This is a blockquote following a header.
>
> When something is important enough, you do it even if the odds are not in your favor.

### Header 3

```js
// Javascript code with syntax highlighting.
var fun = function lang(l) {
  dateformat.i18n = require('./lang/' + l)
  return true;
}
```

```ruby
# Ruby code with syntax highlighting
GitHubPages::Dependencies.gems.each do |gem, version|
  s.add_dependency(gem, "= #{version}")
end
```

#### Header 4

*   This is an unordered list following a header.
*   This is an unordered list following a header.
*   This is an unordered list following a header.

##### Header 5

1.  This is an ordered list following a header.
2.  This is an ordered list following a header.
3.  This is an ordered list following a header.

###### Header 6

| head1        | head two          | three |
|:-------------|:------------------|:------|
| ok           | good swedish fish | nice  |
| out of stock | good and plenty   | nice  |
| ok           | good `oreos`      | hmm   |
| ok           | good `zoute` drop | yumm  |

### There's a horizontal rule below this.

* * *

### Here is an unordered list:

*   Item foo
*   Item bar
*   Item baz
*   Item zip

### And an ordered list:

1.  Item one
1.  Item two
1.  Item three
1.  Item four

### And a nested list:

- level 1 item
  - level 2 item
  - level 2 item
    - level 3 item
    - level 3 item
- level 1 item
  - level 2 item
  - level 2 item
  - level 2 item
- level 1 item
  - level 2 item
  - level 2 item
- level 1 item

### Small image

![Octocat](https://assets-cdn.github.com/images/icons/emoji/octocat.png)

### Large image

![Branching](https://guides.github.com/activities/hello-world/branching.png)


### Definition lists can be used with HTML syntax.

<dl>
<dt>Name</dt>
<dd>Godzilla</dd>
<dt>Born</dt>
<dd>1952</dd>
<dt>Birthplace</dt>
<dd>Japan</dd>
<dt>Color</dt>
<dd>Green</dd>
</dl>

```
Long, single-line code blocks should not wrap. They should horizontally scroll if they are too long. This line should be long enough to demonstrate this.
```

```
The final element.
```
