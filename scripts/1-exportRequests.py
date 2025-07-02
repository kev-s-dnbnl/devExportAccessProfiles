import sailpoint
import sailpoint.v3
from sailpoint.configuration import Configuration
from sailpoint.v3.api import AccessProfilesApi
import pandas as pd
import urllib3

# Kevin lasted edited on 7-2-2025
# Note: remove SB vs prod- SSL warnings (optional, as it's obv not recommended for prod)
urllib3.disable_warnings()
#

configuration = Configuration()
with sailpoint.v3.ApiClient(configuration) as api_client:
    api_instance = AccessProfilesApi(api_client)

    limit = 250
    offset = 0
    all_profiles = []

    while True:
        response = api_instance.list_access_profiles(limit=limit, offset=offset)
        profiles = [profile.to_dict() for profile in response]
        all_profiles.extend(profiles)

        if len(profiles) < limit:
            break

        offset += limit

df = pd.DataFrame(all_profiles)
df.to_csv("access_profiles.csv", index=False)
print("Access profiles written to access_profiles.csv")