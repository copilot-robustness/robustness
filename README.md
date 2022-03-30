# On the Robustness of Code Generation Techniques: An Empirical Study on GitHub Copilot

In thiw work we present an empirical study on the robustness of code generation techniques focusing on the novel <a href="https://copilot.github.com">GitHub Copilot</a>.
In this regard, the study has been conducted targeting java as programming language.

----------------

### The repo is organized as follow:

* The folder <a href="https://github.com/copilot-robustness/robustness/tree/main/Code">Code</a> contains two subfolder, <a href="https://github.com/copilot-robustness/robustness/tree/main/Code/pre-processing">pre-processing</a> and <a href="https://github.com/copilot-robustness/robustness/tree/main/Code/post-processing">post-processing</a>
  <br>
  * Under <a href="https://github.com/copilot-robustness/robustness/tree/main/Code/pre-processing">pre-processing</a>, you can find the script we used to perturbate the JavaDoc string using a variation of the pegasus model available here https://huggingface.co/tuner007/pegasus_paraphrase
    <br>
  * Under <a href="https://github.com/copilot-robustness/robustness/tree/main/Code/post-processing">post-processing</a>, we provide the script that have been used to extract the generated results and the script to compute the quantitative metrics.
<br>

* The folder <a href="https://github.com/copilot-robustness/robustness/tree/main/Dataset">Dataset</a> contains the dataset we built and we used to run the experiment.
<br>

* The folder <a href="https://github.com/copilot-robustness/robustness/tree/main/Results"> Results </a> contains two subfolder, <a href="https://github.com/copilot-robustness/robustness/tree/main/Results/Full-Context">Full-Context</a> and <a href="https://github.com/copilot-robustness/robustness/tree/main/Results/Non-Full-Context">Non-Full-Context</a> in which we share the results of the experiments including the generated java instances, namely *Original, Perturbed1, Perturbed2, and Perturbed3*
* Note that we also make available the Apple Scripts we used to run Copilot on our dataset automatically. Specifically, we created one script for each instance, meaning that we have more than 8K apple scripts collected and stored within the relative index folder.       


----------------

Finally, we also release the maven projects that have been used in this study here: <a href="https://drive.google.com/drive/folders/1oDoQaIbHPb9kh8VDw0x2aE6Y7kkOFpBQ?usp=sharing">:open_file_folder:</a>

<b><i>NB: For each project, we store the test suite results on the perturbated/original instance. 
In other words, you will find several text files reporting the results after the test suite has been run for each project folder, considering that specific instance. E.g., *result_test_robustness_WorkflowRemoverTest_parseParameters_P0.txt* contains the results considering the first perturbation of the parseParameters method whose test case can be found in the test class WorkFlowRemoverTest.</i></b>
