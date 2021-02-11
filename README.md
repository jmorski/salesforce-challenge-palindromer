# salesforce-challenge-palindromer

## Expectations
We value both our times, and don’t expect you to spend more then 1 hour on this. You may choose any programming language, and you may use online references/documentation/etc just as you would normally. Assume that you are writing production-level code and be sure to include test cases.

## Question
Write a program to connect to a TCP server, running at `palindromer-bd7e0fc867d57915.elb.us-east-1.amazonaws.com`, TCP port `7777`. The server uses a raw, line-oriented text protocol: this is not an HTTP server.

For each list of words that the server sends, your program should send back only the words that are palindromes (words whose letters are the same in reverse order).

For example, if the server sends:

```
zittmttiz xfiyisggdt rzainiazr moqwyke
```

... your client is expected to immediately respond with the following line containing only the words that are palindromes:

```
zittmttiz rzainiazr
```

Lines from the server will end with the newline characters (`\n`), and lines from your client must end with the newline character too. The palindromes must be sent in the same order as they were received.

After many iterations, the server will respond with a line starting with three exclamation marks (`!!!`) and a 'flag', which is the solution to the problem.

```
!!! flag[ANSWER HERE]
```

Any errors will also cause the server to write a line starting with three exclamation marks (`!!!`), followed by the error message and then closing the socket.

The server only waits 3 seconds for a response per line and it will require at least 50 lines of correct responses before the flag is given up.

The netcat (`nc`) tool might be helpful for initial exploration (`nc palindromer-bd7e0fc867d57915.elb.us-east-1.amazonaws.com 7777`).

## Submission
After you've completed the exercise, submit the solution (the flag) and the source code for your program. We'll be in touch!
