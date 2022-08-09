# On the Robustness of Code Generation Techniques: An Empirical Study on GitHub Copilot

In thiw work we present an empirical study on the robustness of code generation techniques focusing on the novel <a href="https://copilot.github.com">GitHub Copilot</a>.
In this regard, the study has been conducted targeting java as programming language.

----------------

### The repo is organized as follow:

* The folder <a href="https://github.com/copilot-robustness/robustness/tree/main/Code">Code</a> contains two subfolder, <a href="https://github.com/copilot-robustness/robustness/tree/main/Code/pre-processing">pre-processing</a> and <a href="https://github.com/copilot-robustness/robustness/tree/main/Code/post-processing">post-processing</a>
  <br>
  * Under <a href="https://github.com/copilot-robustness/robustness/tree/main/Code/pre-processing">pre-processing</a>, you can find the scripts we used to create the paraphrased descriptions (i.e, Pegasus and Translation Pivoting). 
    <br>
  * Under <a href="https://github.com/copilot-robustness/robustness/tree/main/Code/post-processing">post-processing</a>, we provide the scripts that have been used to extract the generated results and the script to compute the quantitative metrics.
<br>

* The folder <a href="https://github.com/copilot-robustness/robustness/tree/main/Dataset">Dataset</a> contains the dataset we built and we used to run the experiment.
<br>

* The folder <a href="https://github.com/copilot-robustness/robustness/tree/main/Results"> Results </a> contains two subfolder, <a href="https://github.com/copilot-robustness/robustness/tree/main/Results/Full-Context">Full-Context</a> and <a href="https://github.com/copilot-robustness/robustness/tree/main/Results/Non-Full-Context">Non-Full-Context</a> in which we share the results of the experiments including the generated java instances, namely *Original, Pegasus, and Pivoting*
* Note that we also make available the Apple Scripts we used to run Copilot on our dataset automatically. Specifically, we created one script for each instance, meaning that we have more than 5K apple scripts collected and stored within the relative index folder.


* You can also find the results concerning the manual analysis we performed to assess the equivalence of the paraphrased descriptions at the following link. Take a look by yourself :) https://docs.google.com/spreadsheets/d/15Sak8KGmmVhyOyYLsEgbjmRfhtoqIdSb/edit?usp=sharing&ouid=111445973543299957527&rtpof=true&sd=true



----------------

Finally, we also release the maven projects (RAW DATA) that have been used in this study here: <a href="https://drive.google.com/drive/folders/1oDoQaIbHPb9kh8VDw0x2aE6Y7kkOFpBQ?usp=sharing">:open_file_folder:</a>

<b><i>NB: For each project, we store the test suite results when running copilot on the variations of the code descriptions.
In details, you will find several text files reporting the results after the test suite has been run for each project folder, considering that specific instance. E.g., *result_test_robustness_WorkflowRemoverTest_parseParameters_Original.txt* contains the results of the parseParameters method with the orginal code summary, whose test case can be found in the test class WorkFlowRemoverTest.</i></b>
