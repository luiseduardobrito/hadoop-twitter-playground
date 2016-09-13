mc855-2s2016-unicamp
====================

Simple project for Twitter trend monitoring for São Paulo 2016 mayor elections.

*Authors*
- Luis Brito <luiseduardobrito.github.com>

*Installation*

Clone the repository using git then install its requirements:
```sh
cd mc855-2s2016/
pip install
```

*Running the report*

To start the crawler reporter:
```sh
./run-crawler <term> [candidates.json]
```

The start the streaming reporter:
```sh
# The streamer will remain listening until wait_for_count tweets arrives with the supplied term.
./run-streamer <term> <wait_for_count> [candidates.json]
```

*Roadmap*

- Streamer: continuously report based on input tweets updating the terminal screen.
- Streamer: set max timeout to wait before generating reports