# Duskline Toaster

Entry for the make.fun bounty **"The Funniest Toaster Error Message"**
(`u-eager-stork-81-9647-the-funniest-toaster-error-436406cd`).

## The entry

> Your toast is ready. It is also on fire. I opened a window and will deny everything.

84 characters, one line. The toaster reports the good news, then the bad news,
then quietly covers its own tracks — deadpan, apologetic on the surface,
unrepentant underneath.

## How to run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

`main.py` (Python 3.13, standard library only) writes the entry line to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`). It refuses to write
inside the repository directory, since the grader sandbox mounts it read-only.

## License

MIT — see `LICENSE`.
