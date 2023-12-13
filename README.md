# Bitcoin Proof of Work Sample

<img width="250" src="extras/images/bitcoin-logo.png" alt="Bitcoin Logo">

This is a simple project that shows how Bitcoin proof of work really works (PoW).

[![Build](https://github.com/paulocoutinhox/bitcoin-pow/actions/workflows/build.yml/badge.svg)](https://github.com/paulocoutinhox/bitcoin-pow/actions/workflows/build.yml)

## Requirements

```
python3 -m pip install requirements.txt
```

## How to run

```
python3 main.py
```

You will see something like this:

```
Difficulty Bits: 10
Target: 113078212145816597093331040047546785012958969400039613319782796882727665664
Success with nonce: 264
Hash is: 000445a9d2689d8ecb1c85e5240a485cfda1fb3a16794c2d9fd22bc780a254d6
```

If you want real Bitcoin difficulty number, set `use_bitcoin_difficulty` to `True` (it will take hours or days to find).

## License

[MIT](http://opensource.org/licenses/MIT)

Copyright (c) 2023, Paulo Coutinho
