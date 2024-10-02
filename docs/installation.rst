Installation
============

Installing Python
-----------------

You can choose to install Python from the official website or use the Anaconda distribution, which comes with many data science packages pre-installed. We will not discuss the benefits of using Anaconda here, but encourage you to do your own research.

This application is written in the Python programming language.

Standard Python
~~~~~~~~~~~~~~~

**Step 1: Download Python**

1. Visit the official Python website: https://www.python.org/downloads/
2. Download the latest version of Python for your operating system.
3. Follow the installation instructions for your operating system:
   - **Windows**: Run the installer and make sure to select **"Add Python to PATH"** before proceeding.
   - **macOS**: Install the downloaded package. You may also use `brew install python` if you have Homebrew installed.
   - **Linux**: Most Linux distributions come with Python pre-installed. You can update Python via your package manager.

**Step 2: Verify Python Installation**

After installation, verify that Python is installed correctly by running the following command in your terminal:

.. code-block:: bash

    python --version

Anaconda
~~~~~~~~

Anaconda is a popular distribution that comes with Python and many data science packages pre-installed.

**Step 1: Download Anaconda**

1. Visit the official Anaconda website: https://www.anaconda.com/download/
2. Download the distribution for your operating system.
3. Follow the installation instructions for your operating system:
   - **Windows**:
     - Run the `.exe` file.
     - Follow the prompts to install Anaconda.
     - Make sure to select the option to add Anaconda to your system's PATH environment variable (optional).
   - **macOS**:
     - Run the `.pkg` installer.
     - Follow the on-screen instructions to complete the installation.
   - **Linux**:
     - Open a terminal in the directory where you downloaded the `.sh` file.
     - Run the following command to install Anaconda:

            bash Anaconda3-<version>-Linux-x86_64.sh

**Step 2: Verify the Anaconda Installation**

After installation, open your terminal and run the following command to verify the installation:

.. code-block:: bash

    conda --version


Creating a virtual environment
------------------------------

Virtual environments allow you to manage dependencies for different projects independently.

Standard Python
~~~~~~~~~~~~~~~

**Step 1: Create a Virtual Environment**

To create a virtual environment:

1. Navigate to the directory where you want to create the virtual environment.
2. Run the following command:

.. code-block:: bash

    python -m venv myenv

Replace `myenv` with your desired virtual environment name.

**Step 3: Activate the Virtual Environment**

- **Windows**:

.. code-block:: bash

    myenv\Scripts\activate

- **macOS/Linux**:

.. code-block:: bash

    source myenv/bin/activate

You should now see the virtual environment's name in your terminal prompt.

Anaconda
~~~~~~~~

**Step 1: Create a Conda Environment**

1. To create a new Conda environment, use the following command:

.. code-block:: bash

    conda create --name myenv

Replace `myenv` with the name you want to give your environment, e.g., `phenopackets_venv`.

2. Conda will ask for confirmation. Press `y` and hit Enter.

**Step 2: Activate the Conda Environment**

Activate the environment using:

.. code-block:: bash

    conda activate myenv

You should see the environment name in your terminal prompt. E.g., on Windows:

.. code-block:: bash

    (myenv) PS C:\Users\YourName>


Installing Git
--------------

Git is a tool to manage source code repositories. You can download Git from the official website: https://git-scm.com/downloads

**Windows**
There are a few ways to install Git on Windows. The most official build is available for download on the Git website. Just go to https://git-scm.com/download/win and the download will start automatically. Note that this is a project called Git for Windows, which is separate from Git itself; for more information on it, go to https://gitforwindows.org.

To get an automated installation you can use the Git Chocolatey package. Note that the Chocolatey package is community maintained.

**Linux**
If you want to install the basic Git tools on Linux via a binary installer, you can generally do so through the package management tool that comes with your distribution. If you’re on Fedora (or any closely-related RPM-based distribution, such as RHEL or CentOS), you can use dnf:

.. code-block:: bash

    $ sudo dnf install git-all

If you’re on a Debian-based distribution, such as Ubuntu, try apt:

.. code-block:: bash

    $ sudo apt install git-all

For more options, there are instructions for installing on several different Unix distributions on the Git website, at https://git-scm.com/download/linux.

**macOS**
There are several ways to install Git on macOS. The easiest is probably to install the Xcode Command Line Tools. On Mavericks (10.9) or above you can do this simply by trying to run git from the Terminal the very first time.

.. code-block:: bash

    $ git --version

If you don’t have it installed already, it will prompt you to install it.

If you want a more up to date version, you can also install it via a binary installer. A macOS Git installer is maintained and available for download at the Git website, at https://git-scm.com/download/mac.

For more information visit https://git-scm.com/book/en/v2/Getting-Started-Installing-Git


Installing Java
---------------

For Phenopacket validation this library uses `phenopacket-tools`, which in turn is written in Java. In order for the library to work, you need to have Java installed on your system.

**Step 1: Download the JRE**

1. Visit the Oracle Java website: https://www.oracle.com/java/technologies/javase-jre8-downloads.html
2. Download the JRE for your operating system:
   - **Windows**: `.exe` file.
   - **macOS**: `.dmg` file.
   - **Linux**: `.tar.gz` or through a package manager.

**Step 2: Install the JRE**

- **Windows**:
  - Run the `.exe` installer and follow the prompts.
- **macOS**:
  - Run the `.dmg` file and follow the instructions.
- **Linux**:
  - **Option 1**: Extract the `.tar.gz` and move it to `/opt`.
  - **Option 2**: Install OpenJRE via the package manager:
    .. code-block:: bash

        sudo apt install openjdk-<version>-jre   # Ubuntu
        sudo dnf install java-<version>-openjdk  # Fedora


**Step 3: Verify Installation**

After installation, verify the JRE is working by running:

.. code-block:: bash

    java -version


**Step 4: Setting Up Environment Variables**

To ensure Java runs correctly, you may need to set the `JAVA_HOME` environment variable and add Java to the system `PATH`.

- **Windows**:
    1. Open **Environment Variables** in System Properties.
    2. Under **System variables**, click **New**:
       - **Variable name**: `JAVA_HOME`
       - **Variable value**: Path to JRE installation (e.g., `C:\Program Files\Java\jre<version>`).
    3. Edit the **Path** variable and add the JRE `bin` folder (e.g., `C:\Program Files\Java\jre<version>\bin`).
    4. Restart the terminal to apply changes.

- **macOS/Linux**:
    1. Open a terminal and edit your shell profile (e.g., `~/.bash_profile` or `~/.bashrc`):

    .. code-block:: bash

       export JAVA_HOME=/path/to/jre
       export PATH=$JAVA_HOME/bin:$PATH

    2. Apply changes:

    .. code-block:: bash

        source ~/.bash_profile  # or source ~/.bashrc

Installing the Phenopacket Mapper
---------------------------------

[WIP] Local installation
~~~~~~~~~~~~~~~~~~~~~~~~

Since the Phenopacket Mapper is not yet available on PyPI, you can install it locally by following these steps:

**Step 1: Clone the Repository**

1. Open your terminal.

2. Clone the repository using the following command:

.. code-block:: bash

    git clone https://github.com/BIH-CEI/phenopacket_mapper

3. Navigate to the cloned repository:

.. code-block:: bash

    cd phenopacket_mapper

**Step 2: Install the Phenopacket Mapper**

Run the following command to install the Phenopacket Mapper:

.. code-block:: bash

    pip install .


Using `pip`
~~~~~~~~~~~

To install the `phenopacket_mapper` library, simply run:

.. code-block:: bash

    pip install phenopacket_mapper
