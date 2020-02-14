# SDUSbCtl API

Official API for Shell SDU Sandbox Control, accessible using a command line tool implemented in Python 3.  

Beta release - Shell reserves the right to modify the API functionality currently offered.

IMPORTANT: Sandbox requests using an API version prior to 1.0.0 may not work.  If you are encountering difficulties with requests, please check your version with `sdusbctl --version`.  If it is below 1.0.0, please update with `pip install sdusbctl --upgrade`.

## Installation

Ensure you have Python 3 and the package manager `pip` installed.

Run the following command to access the SDU Sandbox Control API using the command line:

`pip install sdusbctl` (You may need to do `pip install --user sdusbctl` on Mac/Linux.  This is recommended if problems come up during the installation process.) Installations done through the root user (i.e. `sudo pip install sdusbctl`) will not work correctly unless you understand what you're doing.  Even then, they still might not work.  User installs are strongly recommended in the case of permissions errors.

You can now use the `sdusbctl` command as shown in the examples below.

If you run into a `sdusbctl: command not found` error, ensure that your python binaries are on your path.  You can see where `sdusbctl` is installed by doing `pip uninstall sdusbctl` and seeing where the binary is.  For a local user install on Linux, the default location is `~/.local/bin`.  On Windows, the default location is `$PYTHON_HOME/Scripts`.

IMPORTANT: We do not offer Python 2 support.  Please ensure that you are using Python 3 before reporting any issues.

## API credentials

To use the SDU Sandbox Control API, sign up for a SDU Sandbox Control account at Shell SDU Sandbox Control. Then go to the 'Account' tab of your user profile (`Shell SDU Sandbox Control/<username>/account`) and select 'Create API Token'. This will trigger the download of `sdusbctl.json`, a file containing your API credentials. Place this file in the location `~/.sdusbctl/sdusbctl.json` (on Windows in the location `C:\Users\<Windows-username>\.sdusbctl\sdusbctl.json` - you can check the exact location, sans drive, with `echo %HOMEPATH%`). You can define a shell environment variable `SDUSBCTL_CONFIG_DIR` to change this location to `$SDUSBCTL_CONFIG_DIR/sdusbctl.json` (on Windows it will be `%SDUSBCTL_CONFIG_DIR%\sdusbctl.json`).

For your security, ensure that other users of your computer do not have read access to your credentials. On Unix-based systems you can do this with the following command:

`chmod 600 ~/.sdusbctl/sdusbctl.json`

You can also choose to export your SDU Sandbox Control username and token to the environment:

```bash
export SDUSBCTL_USERNAME=datadinosaur
export SDUSBCTL_KEY=xxxxxxxxxxxxxx
```
In addition, you can export any other configuration value that normally would be in
the `$HOME/.sdusbctl/sdusbctl.json` in the format 'SDUSBCTL_<VARIABLE>' (note uppercase).  
For example, if the file had the variable "proxy" you would export `SDUSBCTL_PROXY`
and it would be discovered by the client.


## Commands

The command line tool supports the following commands:

```
sdusbctl sandboxes {list, files, download, request, requests, chargeboard}
sdusbctl datasets {list, files, download, create, version, init}
sdusbctl kernels {list, init, push, pull, output, status}
sdusbctl config {view, set, unset}
```

See more details below for using each of these commands.

### Sandboxes

The API supports the following commands for SDU Sandbox Control.

```
usage: sdusbctl sandboxes [-h]
                           {list, files, download, request, requests, chargeboard}
                           ...

optional arguments:
  -h, --help            show this help message and exit

commands:
  {list, files, download, request, requests, chargeboard}
    list                List available sandboxes
    files               List sandbox files
    download            Download sandbox files
    request              Make a new sandbox request
    requests         Show your sandbox requests
    chargeboard         Get sandbox chargeboard information
```

##### List sandboxes

```
usage: sdusbctl sandboxes list [-h] [--group GROUP] [--category CATEGORY] [--sort-by SORT_BY] [-p PAGE] [-s SEARCH] [-v]

optional arguments:
  -h, --help            show this help message and exit
  --group GROUP         Search for sandboxes in a specific group. Default is 'general'. Valid options are 'general', 'entered', and 'inClass'
  --category CATEGORY   Search for sandboxes of a specific category. Default is 'all'. Valid options are 'all', 'featured', 'research', 'recruitment', 'gettingStarted', 'masters', and 'playground'
  --sort-by SORT_BY     Sort list results. Default is 'latestDeadline'. Valid options are 'grouped', 'prize', 'earliestDeadline', 'latestDeadline', 'numberOfTeams', and 'recentlyCreated'
  -p PAGE, --page PAGE  Page number for results paging. Page size is 20 by default
  -s SEARCH, --search SEARCH
                        Term(s) to search for
  -v, --csv             Print results in CSV format
                        (if not set print in table format)
```

Example:

`sdusbctl sandboxes list -s health`

`sdusbctl sandboxes list --category gettingStarted`

##### List sandbox files

```
usage: sdusbctl sandboxes files [-h] [-v] [-q] [sandbox]

optional arguments:
  -h, --help   show this help message and exit
  sandbox  Competition URL suffix (use "sdusbctl sandboxes list" to show options)
               If empty, the default sandbox will be used (use "sdusbctl config set sandbox")"
  -v, --csv    Print results in CSV format (if not set print in table format)
  -q, --quiet  Suppress printing information about the upload/download progress
```

Example:

`sdusbctl sandboxes files oklahoma-shale-production-forecasting`

##### Download sandbox files

```
usage: sdusbctl sandboxes download [-h] [-f FILE_NAME] [-p PATH] [-w] [-o]
                                    [-q]
                                    [sandbox]

optional arguments:
  -h, --help            show this help message and exit
  sandbox               sandbox URL suffix (use "sdusbctl sandboxes list" to show options)
                        If empty, the default sandbox will be used (use "sdusbctl config set sandbox")"
  -f FILE_NAME, --file FILE_NAME
                        File name, all files downloaded if not provided
                        (use "sdusbctl sandboxes files -c <sandbox>" to show options)
  -p PATH, --path PATH  Folder where file(s) will be downloaded, defaults to current working directory
  -w, --wp              Download files to current working path
  -o, --force           Skip check whether local version of file is up to date, force file download
  -q, --quiet           Suppress printing information about the upload/download progress
```

Examples:

`sdusbctl sandboxes download oklahoma-shale-production-forecasting`

`sdusbctl sandboxes download oklahoma-shale-production-forecasting -f test.csv.7z`

Note: you will need to accept sandbox rules at `Shell SDU Sandbox Control/c/<sandbox-name>/rules`.

##### Submit to a sandbox

```
usage: sdusbctl sandboxes request [-h] -f FILE_NAME -m MESSAGE [-q]
                                  [sandbox]

required arguments:
  -f FILE_NAME, --file FILE_NAME
                        File for upload (full path)
  -m MESSAGE, --message MESSAGE
                        Message describing this request

optional arguments:
  -h, --help            show this help message and exit
  sandbox               sandbox URL suffix (use "sdusbctl sandboxes list" to show options)
                        If empty, the default sandbox will be used (use "sdusbctl config set sandbox")"
  -q, --quiet           Suppress printing information about the upload/download progress
```

Example:

`sdusbctl sandboxes request oklahoma-shale-production-forecasting -f sample_request_favorita.csv.7z -m "My request message"`

Note: you will need to accept sandbox rules at `Shell SDU Sandbox Control/c/<sandbox-name>/rules`.

##### List sandbox requests

```
usage: sdusbctl sandboxes requests [-h] [-v] [-q] [sandbox]

optional arguments:
  -h, --help   show this help message and exit
  sandbox      sandbox URL suffix (use "sdusbctl sandboxes list" to show options)
               If empty, the default sandbox will be used (use "sdusbctl config set sandbox")"
  -v, --csv    Print results in CSV format (if not set print in table format)
  -q, --quiet  Suppress printing information about the upload/download progress
```

Example:

`sdusbctl sandboxes requests oklahoma-shale-production-forecasting`

Note: you will need to accept sandbox rules at `Shell SDU Sandbox Control/c/<sandbox-name>/rules`.

##### Get sandbox chargeboard

```
usage: sdusbctl sandboxes chargeboard [-h] [-s] [-d] [-p PATH] [-v] [-q]
                                       [sandbox]

optional arguments:
  -h, --help            show this help message and exit
  sandbox               sandbox URL suffix (use "sdusbctl sandboxes list" to show options)
                        If empty, the default sandbox will be used (use "sdusbctl config set sandbox")"
  -s, --show            Show the top of the chargeboard
  -d, --download        Download entire chargeboard
  -p PATH, --path PATH  Folder where file(s) will be downloaded, defaults to current working directory
  -v, --csv             Print results in CSV format (if not set print in table format)
  -q, --quiet           Suppress printing information about the upload/download progress
```

Example:

`sdusbctl sandboxes chargeboard oklahoma-shale-production-forecasting -s`


### Datasets

The API supports the following commands for SDU Sandbox Control Datasets.

```
usage: sdusbctl datasets [-h]
                       {list, files, download, create, version, init, metadata, status} ...

optional arguments:
  -h, --help            show this help message and exit

commands:
  {list, files, download, create, version, init, metadata, status}
    list                List available datasets
    files               List dataset files
    download            Download dataset files
    create              Create a new dataset
    version             Create a new dataset version
    init                Initialize metadata file for dataset creation
    metadata            Download metadata about a dataset
    status              Get the creation status for a dataset
```

##### List datasets

```
usage: sdusbctl datasets list [-h] [--sort-by SORT_BY] [--size SIZE] [--file-type FILE_TYPE] [--license LICENSE_NAME] [--tags TaG_IDS] [-s SEARCH] [-m] [--user USER] [-p PAGE] [-v]

optional arguments:
  -h, --help            show this help message and exit
  --sort-by SORT_BY     Sort list results. Default is 'hottest'. Valid options are 'hottest', 'votes', 'updated', and 'active'
  --size SIZE           Search for datasets of a specific size. Default is 'all'. Valid options are 'all', 'small', 'medium', and 'large'
  --file-type FILE_TYPE Search for datasets with a specific file type. Default is 'all'. Valid options are 'all', 'csv', 'sqlite', 'json', and 'bigQuery'. Please note that bigQuery datasets cannot be downloaded
  --license LICENSE_NAME
                        Search for datasets with a specific license. Default is 'all'. Valid options are 'all', 'cc', 'gpl', 'odb', and 'other'
  --tags TAG_IDS        Search for datasets that have specific tags. Tag list should be comma separated                      
  -s SEARCH, --search SEARCH
                        Term(s) to search for
  -m, --mine            Display only my items
  --user USER           Find public datasets owned by a specific user or organization
  -p PAGE, --page PAGE  Page number for results paging. Page size is 20 by default
  -v, --csv             Print results in CSV format (if not set print in table format)
```

Example:

`sdusbctl datasets list -s demographics`

`sdusbctl datasets list --sort-by votes`

##### List files for a dataset

```
usage: sdusbctl datasets files [-h] [-v] [dataset]

optional arguments:
  -h, --help  show this help message and exit
  dataset     Dataset URL suffix in format <owner>/<dataset-name> (use "sdusbctl datasets list" to show options)
  -v, --csv   Print results in CSV format (if not set print in table format)
```

Example:

`sdusbctl datasets files oklahoma/shale`

##### Download dataset files

```
usage: sdusbctl datasets download [-h] [-f FILE_NAME] [-p PATH] [-w] [--unzip]
                                [-o] [-q]
                                [dataset]

optional arguments:
  -h, --help            show this help message and exit
  dataset               Dataset URL suffix in format <owner>/<dataset-name> (use "sdusbctl datasets list" to show options)
  -f FILE_NAME, --file FILE_NAME
                        File name, all files downloaded if not provided
                        (use "sdusbctl datasets files -d <dataset>" to show options)
  -p PATH, --path PATH  Folder where file(s) will be downloaded, defaults to current working directory
  -w, --wp              Download files to current working path
  --unzip               Unzip the downloaded file. Will delete the zip file when completed.
  -o, --force           Skip check whether local version of file is up to date, force file download
  -q, --quiet           Suppress printing information about the upload/download progress
```


Examples:

`sdusbctl datasets download oklahoma/shale`

`sdusbctl datasets download oklahoma/shale -f shale_time_series.csv`

Please note that BigQuery datasets cannot be downloaded.

##### Initialize metadata file for dataset creation

```
usage: sdusbctl datasets init [-h] [-p FOLDER]

optional arguments:
  -h, --help            show this help message and exit
  -p FOLDER, --path FOLDER
                        Folder for upload, containing data files and a special dataset-metadata.json file (https://github.com/SDU-Sandbox-Control/sdusbctl-api/wiki/Dataset-Metadata). Defaults to current working directory
```

Example:

`sdusbctl datasets init -p /path/to/dataset`

##### Create a new dataset

If you want to create a new dataset, you need to initiate metadata file at first. You could fulfill this by running `sdusbctl datasets init` as describe above.

```
usage: sdusbctl datasets create [-h] [-p FOLDER] [-u] [-q] [-t] [-r {skip,zip,tar}]

optional arguments:
  -h, --help            show this help message and exit
  -p FOLDER, --path FOLDER
                        Folder for upload, containing data files and a special dataset-metadata.json file (https://github.com/SDU-Sandbox-Control/sdusbctl-api/wiki/Dataset-Metadata). Defaults to current working directory
  -u, --public          Create publicly (default is private)
  -q, --quiet           Suppress printing information about the upload/download progress
  -t, --keep-tabular    Do not convert tabular files to CSV (default is to convert)
  -r {skip, zip, tar}, --dir-mode {skip, zip, tar}
                        What to do with directories: "skip" - ignore; "zip" - compressed upload; "tar" - uncompressed upload
```

Example:

`sdusbctl datasets create -p /path/to/dataset`

##### Create a new dataset version

```
usage: sdusbctl datasets version [-h] -m VERSION_NOTES [-p FOLDER] [-q] [-t]
                               [-r {skip,zip,tar}] [-d]

required arguments:
  -m VERSION_NOTES, --message VERSION_NOTES
                        Message describing the new version

optional arguments:
  -h, --help            show this help message and exit
  -p FOLDER, --path FOLDER
                        Folder for upload, containing data files and a special dataset-metadata.json file (https://github.com/SDU-Sandbox-Control/sdusbctl-api/wiki/Dataset-Metadata). Defaults to current working directory
  -q, --quiet           Suppress printing information about the upload/download progress
  -t, --keep-tabular    Do not convert tabular files to CSV (default is to convert)
  -r {skip, zip, tar}, --dir-mode {skip, zip, tar}
                        What to do with directories: "skip" - ignore; "zip" - compressed upload; "tar" - uncompressed upload
  -d, --delete-old-versions
                        Delete old versions of this dataset
```

Example:

`sdusbctl datasets version -p /path/to/dataset -m "Updated data"`


##### Download metadata for an existing dataset

```
usage: sdusbctl datasets metadata [-h] [-p PATH] [dataset]

optional arguments:
  -h, --help            show this help message and exit
  dataset               Dataset URL suffix in format <owner>/<dataset-name> (use "sdusbctl datasets list" to show options)
  -p PATH, --path PATH  Location to download dataset metadata to. Defaults to current working directory
```

Example:

`sdusbctl datasets metadata -p /path/to/download-oklahoma/shale`


##### Get dataset creation status

```
usage: sdusbctl datasets status [-h] [dataset]

optional arguments:
  -h, --help  show this help message and exit
  dataset     Dataset URL suffix in format <owner>/<dataset-name> (use "sdusbctl datasets list" to show options)
```

Example:

`sdusbctl datasets status oklahoma/shale`


### Kernels

The API supports the following commands for SDU Sandbox Control Kernels.

```
usage: sdusbctl kernels [-h] {list, init, push, pull, output, status} ...

optional arguments:
  -h, --help            show this help message and exit

commands:
  {list,init,push,pull,output,status}
    list                List available kernels
    init                Initialize metadata file for a kernel
    push                Push new code to a kernel and run the kernel
    pull                Pull down code from a kernel
    output              Get data output from the latest kernel run
    status              Display the status of the latest kernel run
```

##### List kernels

```
usage: sdusbctl kernels list [-h] [-m] [-p PAGE] [--page-size PAGE_SIZE] [-s SEARCH] [-v]
                           [--parent PARENT] [--sandbox COMPETITION]
                           [--dataset DATASET]
                           [--user USER] [--language LANGUAGE]
                           [--kernel-type KERNEL_TYPE]
                           [--output-type OUTPUT_TYPE] [--sort-by SORT_BY]

optional arguments:
  -h, --help            show this help message and exit
  -m, --mine            Display only my items
  -p PAGE, --page PAGE  Page number for results paging. Page size is 20 by default
  --page-size PAGE_SIZE Number of items to show on a page. Default size is 20, max is 100
  -s SEARCH, --search SEARCH
                        Term(s) to search for
  -v, --csv             Print results in CSV format (if not set print in table format)
  --parent PARENT       Find children of the specified parent kernel
  --sandbox COMPETITION
                        Find kernels for a given sandbox
  --dataset DATASET     Find kernels for a given dataset
  --user USER           Find kernels created by a given user
  --language LANGUAGE   Specify the language the kernel is written in. Default is 'all'. Valid options are 'all', 'python', 'r', 'sqlite', and 'julia'
  --kernel-type KERNEL_TYPE
                        Specify the type of kernel. Default is 'all'. Valid options are 'all', 'script', and 'notebook'
  --output-type OUTPUT_TYPE
                        Search for specific kernel output types. Default is 'all'. Valid options are 'all', 'visualizations', and 'data'
  --sort-by SORT_BY     Sort list results. Default is 'hotness'.  Valid options are 'hotness', 'commentCount', 'dateCreated', 'dateRun', 'relevance', 'scoreAscending', 'scoreDescending', 'viewCount', and 'voteCount'. 'relevance' is only applicable if a search term is specified.
```

Example:

`sdusbctl kernels list -s production-forecasting`

`sdusbctl kernels list --language python`

##### Initialize metadata file for a kernel

```
usage: sdusbctl kernels init [-h] [-p FOLDER]

optional arguments:
  -h, --help            show this help message and exit
  -p FOLDER, --path FOLDER
                        Folder for upload, containing data files and a special kernel-metadata.json file (https://github.com/SDU-Sandbox-Control/sdusbctl-api/wiki/Kernel-Metadata). Defaults to current working directory
```

Example:

`sdusbctl kernels init -p /path/to/kernel`

##### Push a kernel

```
usage: sdusbctl kernels push [-h] -p FOLDER

optional arguments:
  -h, --help            show this help message and exit
  -p FOLDER, --path FOLDER
                        Folder for upload, containing data files and a special kernel-metadata.json file (https://github.com/SDU-Sandbox-Control/sdusbctl-api/wiki/Kernel-Metadata). Defaults to current working directory
```

Example:

`sdusbctl kernels push -p /path/to/kernel`

##### Pull a kernel

```
usage: sdusbctl kernels pull [-h] [-p PATH] [-w] [-m] [kernel]

optional arguments:
  -h, --help            show this help message and exit
  kernel                Kernel URL suffix in format <owner>/<kernel-name> (use "sdusbctl kernels list" to show options)
  -p PATH, --path PATH  Folder where file(s) will be downloaded, defaults to current working directory
  -w, --wp              Download files to current working path
  -m, --metadata        Generate metadata when pulling kernel
```

Example:

`sdusbctl kernels pull keshava/list-of-new-sandboxes -p /path/to/dest`

##### Retrieve a kernel's output

```
usage: sdusbctl kernels output [-h] [-p PATH] [-w] [-o] [-q] [kernel]

optional arguments:
  -h, --help            show this help message and exit
  kernel                Kernel URL suffix in format <owner>/<kernel-name> (use "sdusbctl kernels list" to show options)
  -p PATH, --path PATH  Folder where file(s) will be downloaded, defaults to current working directory
  -w, --wp              Download files to current working path
  -o, --force           Skip check whether local version of file is up to date, force file download
  -q, --quiet           Suppress printing information about the upload/download progress
```

Example:

`sdusbctl kernels output keshava/dl-on-shale-data -p /path/to/dest`

##### Get the status of the latest kernel run

```
usage: sdusbctl kernels status [-h] [kernel]

optional arguments:
  -h, --help  show this help message and exit
  kernel      Kernel URL suffix in format <owner>/<kernel-name> (use "sdusbctl kernels list" to show options)
```

Example:

`sdusbctl kernels status keshava/dl-on-shale-data`

### Config

The API supports the following commands for configuration.

```
usage: sdusbctl config [-h] {view, set, unset} ...

optional arguments:
  -h, --help        show this help message and exit

commands:
  {view,set,unset}
    view            View current config values
    set             Set a configuration value
    unset           Clear a configuration value
```

##### View current config values

```
usage: sdusbctl config path [-h] [-p PATH]

optional arguments:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  folder where file(s) will be downloaded, defaults to current working directory
```

Example:

`sdusbctl config path -p C:\`

##### View current config values

```
usage: sdusbctl config view [-h]

optional arguments:
  -h, --help  show this help message and exit
```

Example:

`sdusbctl config view`


##### Set a configuration value

```
usage: sdusbctl config set [-h] -n NAME -v VALUE

required arguments:
  -n NAME, --name NAME  Name of the configuration parameter
                        (one of sandbox, path, proxy)
  -v VALUE, --value VALUE
                        Value of the configuration parameter, valid values depending on name
                        - sandbox: Competition URL suffix (use "sdusbctl sandboxes list" to show options)
                        - path: Folder where file(s) will be downloaded, defaults to current working directory
                        - proxy: Proxy for HTTP requests
```

Example:

`sdusbctl config set -n sandbox -v production-forecasting`


##### Clear a configuration value

```
usage: sdusbctl config unset [-h] -n NAME

required arguments:
  -n NAME, --name NAME  Name of the configuration parameter
                        (one of sandbox, path, proxy)
```

Example:

`sdusbctl config unset -n sandbox`


## Limitations
Kernel support is preliminary and may have some issues.

## License

The SDU Sandbox Control API is released under the [Shell SDU license](LICENSE).
