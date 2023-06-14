# fetch-data
In this script, we simulate fetching data from a server with the fetch_data function. This function waits a random amount of seconds (between 1 and 5) to simulate a server response delay. We then create 10 of these tasks and run them concurrently using asyncio's gather function.
