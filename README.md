# LeetCode redirector

Using LeetCode api, takes a problem id (number) or path and redirects to `https://leetcode.com/problems/$problem`.

`leetcode` command expects a path or problem id and spawns a firefox tab with the problem.

Example command: `leetcode 42`.

`leetcode-server` command starts a server (by default listening on localhost on port 8080) and expects requests in the form `/$problem-number'.

For example, after starting the server, try opening 'localhost:8080/42` in your browser.

In takes optional port argument to change the port.

Example command: `leetcode-server 9999`.

# Dependencies

Python 3, curl, firefox command in PATH.

# License

MIT.