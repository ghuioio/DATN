from twarc.client2 import Twarc2

# Your bearer token here
t = Twarc2(bearer_token="AAAAAAAAAAAAAAAAAAAAACcSnAEAAAAApgB%2BCROzbjX%2FeRDngRTO0Z3Y0KA%3D1ftJISHlgpEBaT5am4K3oGOzAxs6zmJeItgkLIqM6zD5QJxunk")

user_ids = [12, 2244994945, 4503599627370241] # @jack, @twitterdev, @overflow64

# Iterate over our target users
for user_id in user_ids:

    # Iterate over pages of followers
    for i, follower_page in enumerate(t.followers(user_id)):

         # Do something with the follower_page here
         print(f"Fetched a page of {len(follower_page['data'])} followers for {user_id}")

         if i == 1: # Only retrieve the first two pages (enumerate starts from 0)
               break