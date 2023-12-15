<img width="250" src="extras/images/bitcoin-logo.png" alt="Bitcoin Logo">

# Bitcoin Proof of Work Sample

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
Difficulty bits: 25
Target: 3450873173395281893717377931138512726225554486085193277581262111899648
Success with nonce: 16659493
Hash is: 00000003f5c7a6abafd59697b8d5ce1f196196e99adaeb00885d274925833445
Hash int is: 106763483141386349073813431350758629195147764529015996425106295567429
Processing time: 00:00:11
```

If you want real Bitcoin difficulty number, set `use_bitcoin_difficulty` to `True` (it will take hours or days to find).

## License

[MIT](http://opensource.org/licenses/MIT)

Copyright (c) 2023, Paulo Coutinho
