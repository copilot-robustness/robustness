# On the Robustness of Code Generation Techniques: An Empirical Study on GitHub Copilot

In thiw work we present an empirical study on the robustness of code generation techniques focusing on the novel <a href="https://copilot.github.com">GitHub Copilot</a>.
In this regard, the study has been conducted targeting java as programming language.

----------------

###The repo is organized as follow:

* The folder <a href="https://github.com/copilot-robustness/robustness/tree/main/Code">Code</a> contains two subfolder, <a href="https://github.com/copilot-robustness/robustness/tree/main/Code/pre-processing">pre-processing</a> and <a href="https://github.com/copilot-robustness/robustness/tree/main/Code/post-processing">post-processing</a>
  <br>
  * Under <a href="https://github.com/copilot-robustness/robustness/tree/main/Code/pre-processing">pre-processing</a>, you can find the script we used to perturbate the JavaDoc string using a variation of the pegasus model available here https://huggingface.co/tuner007/pegasus_paraphrase
    <br>
  * Under <a href="https://github.com/copilot-robustness/robustness/tree/main/Code/post-processing">post-processing</a>, we provide the script that have been used to extract the generated results and the script to compute the quantitative metrics.
<br>

* The folder <a href="https://github.com/copilot-robustness/robustness/tree/main/Dataset">Dataset</a> contains the dataset we built and we used to run the experiment.
<br>

* The folder <a href="https://github.com/copilot-robustness/robustness/tree/main/Results"> Results </a> contains two subfolder, <a href="https://github.com/copilot-robustness/robustness/tree/main/Results/Full-Context">Full-Context</a> and <a href="https://github.com/copilot-robustness/robustness/tree/main/Results/Non-Full-Context">Non-Full-Context</a> in which we share the results of the experiments including the generated java instances, namely *Original, Perturbated1, Perturbated2, and Perturbated3*


----------------

Finally, we also release the maven projects that have been used for this study here: <a href="https://drive.google.com/drive/folders/1oDoQaIbHPb9kh8VDw0x2aE6Y7kkOFpBQ?usp=sharing">:open_file_folder:<a>  
