import getpass, os, io, warnings
from IPython.display import display
from PIL import Image
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation

def generate_image_by_prompt(prompt, file_name, seed=34567, steps=30):
    # NB: host url is not prepended with \"https\" nor does it have a trailing slash.
    os.environ['STABILITY_HOST'] = 'grpc.stability.ai:443'

    # To get your API key, visit https://beta.dreamstudio.ai/membership
    os.environ['STABILITY_KEY'] = 'xxxx'

    stability_api = client.StabilityInference(
        key=os.environ['STABILITY_KEY'], 
        verbose=True,
    )

    answers = stability_api.generate(
        prompt=prompt,
        seed=seed, # if provided, specifying a random seed makes results deterministic
        steps=steps, # defaults to 50 if not specified
    )

    # iterating over the generator produces the api response
    for resp in answers:
        for artifact in resp.artifacts:
            if artifact.finish_reason == generation.FILTER:
                warnings.warn(
                    "Your request activated the API's safety filters and could not be processed."
                    "Please modify the prompt and try again.")
            if artifact.type == generation.ARTIFACT_IMAGE:
                img = Image.open(io.BytesIO(artifact.binary))
                img.save(file_name)