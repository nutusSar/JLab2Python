<h1>Jupyter Lab to Python Converter (and Back!)</h1>

<p>This project provides a pair of scripts to convert between Jupyter Lab notebooks and Python scripts, and back. The converter is designed to be used with the Jupyter Lab notebook interface.</p>

<h2>Files</h2>
<ul>
    <li><code>JLab2PythonConverter.ipynb</code>: a Jupyter Lab notebook that contains the code for converting Jupyter Lab notebooks to Python scripts.</li>
    <li><code>JLab2PythonConverter.py</code>: a Python script generated from the JLab2PythonConverter.ipynb notebook.</li>
    <li><code>Python2JLabConverter.ipynb</code>: a Jupyter Lab notebook that contains the code for converting Python scripts to Jupyter Lab notebooks.</li>
    <li><code>Python2JLabConverter.py</code>: a Python script generated from the Python2JLabConverter.ipynb notebook.</li>
</ul>
    
<h2>Installation</h2>

<p>To get started with the converter, you can either download the code from GitHub, or clone the repository using Git. Here are the steps to use the converter:</p>

<ol>
    <li>Download the repository as a ZIP file or clone it using Git:</li>
    <pre><code>git clone https://github.com/nutusSar/JLab2Python-AND-Python2JLab.git</code></pre>
</ol>

<p>This will install the converter and all its required dependencies. Please note that you can use Jupyter Lab or raw Python to use this converter.</p>

<h2>Usage</h2>
<p>The project includes two notebooks and their corresponding Python scripts:</p>

<ul>
    <li><code>JLab2PythonConverter.ipynb</code> and <code>JLab2PythonConverter.py</code>: These files contain the code for converting Jupyter Lab notebooks to Python scripts.</li>
    <li><code>Python2JLabConverter.ipynb</code> and <code>Python2JLabConverter.py</code>: These files contain the code for converting Python scripts to Jupyter Lab notebooks.</li>
</ul>

<p>To use the converter, you can call the main functions <code>ipynb2py</code> and <code>py2ipynb</code>. Here's an example of how to convert a list of Jupyter Lab notebooks to Python scripts:</p>

<pre><code>from JLab2PythonConverter import ipynb2py

docs = ['notebook1.ipynb', 'notebook2.ipynb', 'notebook3.ipynb']
ipynb2py(docs)
</code></pre>

<p>This will create Python scripts in the same directories as the notebooks, with the same names as the notebooks but with the <code>.py</code> extension.</p>

<p>To convert a list of Python scripts to Jupyter Lab notebooks, you can use the following code:</p>

<pre><code>from Python2JLabConverter import py2ipynb

docs = ['script1.py', 'script2.py', 'script3.py']
py2ipynb(docs)
</code></pre>

<p>This will create Jupyter Lab notebooks in the same directories as the original scripts, with the same names as the scripts but with the <code>.ipynb</code> extension.</p>

<p>Please note that the converter files are Python scripts, not Python modules, so they cannot be installed directly using PIP or Conda.</p>

<h2>Contributing</h2>
<p>Contributions are welcome! If you find a bug or have a feature request, please open an issue on the project's GitHub page. If you'd like to contribute code, please submit a pull request with your changes.</p>
