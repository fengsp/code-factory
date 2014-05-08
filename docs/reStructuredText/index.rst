==================
 reStructuredText
==================

This is a paragraph.  It's quite
short.

    This paragraph will result in an indented block of
    text, typically used for quoting other text.

This is another one.  Inline *italics* and **bold**.  Another
``double back-quotes``.

1. number one
2. number two
3. number three

* item one
    - item one-one
    - item one-two
        + item one-two-one
        + item one-two-two
* item two
* item three

what
    Definition lists associate a term with a definition.

An example::

      Whitespace, newlines, blank lines, and all kinds of markup
        (like *this* or \this) is preserved by literal blocks.
    Lookie here, I've dropped an indentation level
    (but not far enough)

no more example

Chapter 1
=========

Section 1.1
-----------

Subsection 1.1.1
````````````````

Section 1.2
-----------

Chapter 2
=========

We have a `spider`_ here.

.. _spider: http://img3.douban.com/view/photo/photo/public/p2181844923.jpg

:copyright: (c) 2014 by fsp.
:license: BSD.

Grid table:

+------------+------------+-----------+ 
| Header 1   | Header 2   | Header 3  | 
+============+============+===========+ 
| body row 1 | column 2   | column 3  | 
+------------+------------+-----------+ 
| body row 2 | Cells may span columns.| 
+------------+------------+-----------+ 
| body row 3 | Cells may  | - Cells   | 
+------------+ span rows. | - contain | 
| body row 4 |            | - blocks. | 
+------------+------------+-----------+

Simple table:

=====  =====  ====== 
   Inputs     Output 
------------  ------ 
  A      B    A or B 
=====  =====  ====== 
False  False  False 
True   False  True 
False  True   True 
True   True   True 
=====  =====  ======
