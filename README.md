<h1>Jupyter Lab to Python Converter</h1>
<p>This project is a Python module that works with Jupyter Lab to convert notebooks to Python scripts, and back. The converter is designed to be used with the Jupyter Lab notebook interface.</p>

<h2>Installation</h2>
<p>To install the converter, you can use pip:</p>

<pre><code>pip install jupyterlab2py</code></pre>

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

<h2>Contributing</h2>
<p>Contributions are welcome! If you find a bug or have a feature request, please open an issue on the project's GitHub page. If you'd like to contribute code, please submit a pull request with your changes.</p>
