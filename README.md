# RandomWords

French dictionary word sampler in Python 3.

**Developer:** Hamdy Abou El Anein  
**Contact:** info@daylightlinux.ch  
**License:** GNU GPL v3 (see LICENSE).

Pick four distinct words from the bundled `listfr.txt`, or supply your own UTF-8 dictionary. The original version is preserved on the [old branch](https://github.com/hamdyaea/RandomWords/tree/old).

```sh
python3 randwords.py --name Alice
python3 randwords.py --name Alice --count 6 --dictionary ./listfr.txt
python3 -m unittest discover -s tests -v
```

Dictionary entries are stripped and deduplicated; requesting more distinct words than the dictionary contains is an error.
