
## IP Freely
#### by Owen Milota
This is a Python script that scans a given subnet for online hosts.

## Installation
Clone the repository and run `ipfreely`.py
```bash
cd ip-freely-RandomHuman2020
python3 ipfreely.py <subnet>
```
replace <subnet> with the subnet you wish to use in the 192.168.0.0/24 format.

## Requirements
- Git
- Python 3
- the ping3 Python library

## Usage
Give the script a subnet in the 0.0.0.0/0 format as an argument, and it will scan that subnet for devices.
If you're running this script on Windows, it will need Administrator permission as pings require admin rights for whatever reason.

If you wish to check if a list of ports is up, provide the -p flag with a comma seperated list of ports.

Example: `python3 ./ipfreely.py -p 80,443,500,1234 192.168.0.3/32`

## Screenshots
<img width="535" height="149" alt="image" src="https://github.com/user-attachments/assets/ac5eb047-f933-495c-9e6d-560bf74dd91e" />

<img width="541" height="126" alt="image" src="https://github.com/user-attachments/assets/36f3e259-a214-494d-9329-8c8ccecf0184" />

<img width="653" height="172" alt="image" src="https://github.com/user-attachments/assets/3c3310ee-c501-426f-af8d-a27d627a9318" />


## Contributing
If you wish to contribute code to this project, fork the repo, make your changes, and make a pull request.

## Licensing
This project is licensed under the BSD Zero Clause License.

See LICENSE.md for more info.
