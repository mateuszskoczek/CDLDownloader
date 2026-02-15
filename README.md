<p align="center"><img src=".gitea/readme/icon.png"/></p>

<h1 align="center">CDL Downloader</h1>

<h3 align="center"><b>Automation script for downloading medical test results files from <a href="ewyniki.cdl.pl">ewyniki.cdl.pl</a></b></h3>

<p align="center">CDL Downloader makes use of Selenium test software to automatically fill patient data textboxes and download PDF files.</p>

---

## Informations

> [!Important]
> **For Github users:**
>
> This is only mirror repository. All changes are first uploaded to the repository <a href="https://repos.mateuszskoczek.com/MateuszSkoczek/CDLDownloader">here</a>. Releases are also published on original repository. However, Github repository handles issues and pull requests for better accessibility.

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

With `--path /mnt/example/download_dir/` file will be saved as `/mnt/example/download_dir/e1ce9235-9c36-4b7a-b245-e2f1c3d3b1c0/TEST_FILE.pdf`

## Attribution and contribution

This project is open source on MIT License, so you can just copy and upload again to your repository. But according to the license, you must include information about the original author. You can find license <a href="https://repos.mateuszskoczek.com/MateuszSkoczek/CDLDownloader/src/branch/main/LICENSE">here</a>.

However, the preferred way to contribute would be to propose improvements in a pull request, through issues, or through other means of communication as project is still maintained.

**Other sources:**

- Icon by <a href="icons8.com">Icons8</a>