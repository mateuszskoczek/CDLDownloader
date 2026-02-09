<p align="center"><img src=".gitea/readme/icon.png"/></p>

<h1 align="center">CDL Downloader</h1>

<h3 align="center"><b>Automation script for downloading medical test results files from <a href="ewyniki.cdl.pl">ewyniki.cdl.pl</a></b></h3>

<p align="center">CDL Downloader makes use of Selenium test software to automatically fill patient data textboxes and download PDF files.</p>

---

## Features

- Download medical test results files from <a href="ewyniki.cdl.pl">ewyniki.cdl.pl</a> automatically.
- Headless mode - can be used entirely without graphical interface
- Return basic information after download in JSON format, such as failure/success status and tests results as html table

## Installation

Download latest package version from <a href="https://repos.mateuszskoczek.com/MateuszSkoczek/CDLDownloader/releases">Releases</a> tab, unpack, install requirements and you good to go

**Requirements**

- Chrome Driver installed
- Python installed
- PIP packages:
    - `selenium`
    - `webdriver-manager`
    - `argparse`

You can also use `requirements.txt` file to install PIP dependencies

```
pip install -r requirements.txt
```

## Usage

```
python cdl_downloader <pesel> <barcode> [additional_options]
```

**Additional options:**

- `--headless` - headless mode
- `--path <path>` - set download path

**Execution:**

1. Script starts browser
2. Goes to <a href="https://ewyniki.cdl.pl/kl322-n/index.php?page=logowanie&barcodeLogin=true">ewyniki.cdl.pl barcode login page</a>
3. Fills PESEL and barcode textbox and submit
4. Waits either for error message (and then stops and returns error) or download button
5. Gathers info about test results
6. Creates dedicated download directory
7. Downloads file

**Returned data:**

In case of failure:

```
{
    "success": false
}
```

In case of success:

```
{
    "success": true,
    "id": "e1ce9235-9c36-4b7a-b245-e2f1c3d3b1c0",
    "fileName": "TEST_FILE.pdf",
    "formattedDate": "2026.01.31",
    "resultTableHTML": "<table>...</table>"
}
```

With `--path /mnt/example/download_dir/` file will be saved under `/mnt/example/download_dir/e1ce9235-9c36-4b7a-b245-e2f1c3d3b1c0/TEST_FILE.pdf`

## Attribution

You can copy this repository and create your own version of the app freely. However, it would be nice if you included URL to this repository in the description to your repository or in README file.

**Other sources:**

- Icon by <a href="icons8.com">Icons8</a>