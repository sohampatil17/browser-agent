from multion.client import MultiOn


client = MultiOn(
    api_key="c83946ed56e447548cad35d6d2eaa9bc" # defaults to os.getenv("MULTION_API_KEY")
)

response = client.browse(
    cmd="Find me a list of all the companies in Y Combinator's S24 batch",
    url="https://google.com",
    local=True,
)

# Print the response message
print(response.message)
