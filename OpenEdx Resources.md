#####This file is a collection of pointers to documentation and other resources for open-edX

* [The open edx 2015 conference](http://con.openedx.org/)
* [Open EdX discussion group](https://groups.google.com/forum/#!forum/edx-code) A good place to ask questions.
* [Open edX youTube channel](https://www.youtube.com/c/OpenedX)
* [edX demo Course](https://www.edx.org/course/demox-edx-demox-1): an introduction to edX in the form of an edX xourse.
* [edX Studio](https://studio.edx.org/) - the instudtor facing tool for authoring open-EdX content.
  * [Documentation for edX studio](http://edx.readthedocs.org/projects/edx-partner-course-staff/en/latest/getting_started/get_started.html)  
    * [Working with course outline](http://edx.readthedocs.org/projects/edx-partner-course-staff/en/latest/developing_course/course_outline.html) The outline is the way in which edX combines components. The organization is hierarchical (section etc.) but only linear. I (YF) would like to find out how to organize the course as a directed graphs, where failure in some problems guides the student to a section that explains the concepts and methods needed to answer the question (for example, converging/diverging infinite sums are needed to understand expectations for distributions over the integers).
  * [Working with problem components](http://edx.readthedocs.org/projects/edx-partner-course-staff/en/latest/creating_content/create_problem.html)
  * [Problems with adaptive hints](http://edx.readthedocs.org/projects/edx-open-learning-xml/en/latest/problem-xml/problem_with_hint.html)
  * [Working with content libraries](http://edx.readthedocs.org/projects/edx-partner-course-staff/en/latest/creating_content/libraries.html)
    * [Enabling content libraries inside studio](http://edx-partner-course-staff.readthedocs.org/en/latest/exercises_tools/randomized_content_blocks.html#enable-content-libraries)
  * [Write your own grader problems](http://edx.readthedocs.org/projects/edx-partner-course-staff/en/latest/exercises_tools/custom_python.html) allows the author to insert their own python code to check the correctness of the problem or to provide hints.
  * [Overview of content experiments](http://edx.readthedocs.org/projects/edx-partner-course-staff/en/latest/content_experiments/content_experiments_overview.html) Content experiments allow the author to perform A/B tests to compare the efficacy of different problems.
  * [Math Expression Input Problems](http://edx.readthedocs.org/projects/edx-partner-course-staff/en/latest/exercises_tools/math_expression_input.html#math-expression-input) these problems are very close to the type of problems supported by webwork.
  * [Custom JavaScript Problem](http://edx.readthedocs.org/projects/edx-partner-course-staff/en/latest/exercises_tools/custom_javascript.html) A problem that uses custom javascript. Joe should check this out.
* [Extending edX](https://open.edx.org/extending-edx)
  * [XBlocks](https://open.edx.org/xblocks) is a way to break up a course into small modules that can be combined into lessons and courses and reused in different contexts.
  * [Xblocks Tutorial](http://opencraft.com/doc/edx/xblock/tutorial.html)
  * [Talk about XBlocks in open edX 2014](https://open.edx.org/videos/open-edx-xblock-tutorial-and-demos)
  * [XBlocks SDK](https://github.com/edx/xblock-sdk) This is a tool designed for creating new XBlocks.
  * [js-input](https://open.edx.org/js-input) extending open edX with javascript components.
  * [XBlocks list](https://github.com/edx/edx-platform/wiki/List-of-XBlocks) A list of currently available public XBlocks.
* [edX deployment](https://open.edx.org/deployment-options) EdX can be deployed in a developer version using Vagrant, As a full version on a local machine, or as an AMI on AWS.
* [edX architecture](https://open.edx.org/contributing-to-edx/architecture)
* [EdX code base](https://github.com/edx/)  set of github repository which, together, power open edX.
* [A guide for building and running an edX course](http://edx.readthedocs.org/projects/open-edx-building-and-running-a-course/en/named-release-cypress/)
* [Stanford open edX](http://online.stanford.edu/openedx)
<<<<<<< HEAD
* [MathJax Documentation](http://www.onemathematicalcat.org/MathJaxDocumentation/TeXSyntax.htm)

