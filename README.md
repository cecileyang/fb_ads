## Workflow
This repo currently can do the following:
- Create fb ad campaign
- Search advertising target, ex. geo location, interest, etc
- Create ads set
- Call stability.ai and generate images using text prompt
- Upload generated image to fb library
- Create ad creative using uploaded image
- Create AD!

Run the following command to get the above done:
`python access.py`


## What you'll need
- facebook business sdk. The current version is v15, can be downloaded and installed from https://github.com/cecileyang/facebook_business_python_sdk_v15.git
- Facebook developer getting started guide: https://developers.facebook.com/docs/marketing-apis/get-started
- Manually create a fb page. https://www.facebook.com/help/104002523024878 (Need page id + page link for `create_ad_creative` to run)
- Stability ai, register account + getting its API key. https://stability.ai/