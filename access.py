from facebook_business.adobjects.ad import Ad
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.adcreative import AdCreative
from facebook_business.adobjects.adimage import AdImage
from facebook_business.adobjects.adset import AdSet
from facebook_business.adobjects.campaign import Campaign
from facebook_business.adobjects.targetingsearch import TargetingSearch
from facebook_business.api import FacebookAdsApi

# Business settings - Accounts - Ad accounts - ID
ACCOUNT_ID = 'act_16digitNumber'

def get_credentials():
# App Dashboard - side bar - Marketing API - Tools - Get Access Token
  access_token = 'xxxx'
  app_secret = 'xxxx'
  app_id = 'xxxx'
  return app_id, app_secret, access_token

def connect_to_ad_account(app_id, app_secret, access_token):
  FacebookAdsApi.init(app_id, app_secret, access_token)
  return AdAccount(ACCOUNT_ID)

def create_campaign(ad_account):
  fields = []
  params = {
    'name': 'BeautyCampaign',
    'objective': 'LINK_CLICKS',
    'status': 'PAUSED',
    'special_ad_categories': [],
  }
  campaign = ad_account.create_campaign(
    fields=fields,
    params=params,
  )
  print(campaign, 'type= ', type(campaign), campaign[Campaign.Field.id])
  return campaign

def search_target():
  search_params = {
    'q': 'US',
    'type': 'adgeolocation',
    'location_types': ['country'], # city(menlo), region(california), country(US)
  }
  targets = TargetingSearch().search(params=search_params)
  print(targets)
  return targets

def create_ads_set(ad_account, campaign_id):
  # budget unit is cent
  fields = []
  params = {
    'name': 'BeautyAdSetCode',
    'campaign_id': campaign_id,
    'daily_budget': 200,
    'billing_event': 'IMPRESSIONS',
    'optimization_goal': 'REACH',
    'bid_amount': 200,
    'targeting': {
      'geo_locations': {'countries': ['US']}
    },
    'status': 'PAUSED'
  }
  adset = ad_account.create_ad_set(fields=fields, params=params)
  print(adset)
  return adset

def upload_image(ad_account):
  fields = []
  params = {
    'filename': 'path_to_local_file_including_extension'
  }
  image = ad_account.create_ad_image(fields=fields, params=params)
  print('image = ', image, ',image_hash = ', image[AdImage.Field.hash])
  return image

def create_ad_creative(ad_account, image_hash):
  fields = []
  params = {
    'name': 'KraveBeautyFirstCodeNameTest',
    'object_story_spec': {
      'page_id': 'xxxx', # created manually
      'link_data': {
        'image_hash': image_hash,
        'link': 'xxxx' # page link 
      }
    }
  }
  ad_creative = ad_account.create_ad_creative(fields=fields,params=params)
  print(ad_creative)
  return ad_creative

def create_ad(ad_account, creative, adset_id):
  fields = []
  params = {
    'name': 'KraveBeautyAd',
    'adset_id': adset_id,
    'creative': {'creative_id': creative[AdCreative.Field.id]},
    'status': 'PAUSED'
  }
  ad = ad_account.create_ad(fields=fields, params=params)
  print(ad)
  return ad

def main():
  app_id, app_secret, access_token = get_credentials()

  print('='*30, 'ad_account', '='*30)
  ad_account = connect_to_ad_account(app_id, app_secret, access_token)

  print(ad_account)
  print('='*30, 'campaign', '='*30)
  campaign = create_campaign(ad_account)

  print('='*30, 'search_target', '='*30)
  search_target()

  print('='*30, 'ads_set', '='*30)
  ads_set = create_ads_set(ad_account, campaign[Campaign.Field.id])

  print('='*30, 'upload_image', '='*30)
  image = upload_image(ad_account)

  print('='*30, 'ad_creative', '='*30)
  creative = create_ad_creative(ad_account, image[AdImage.Field.hash])

  print('='*30, 'ad', '='*30)
  create_ad(ad_account, creative, ads_set[AdSet.Field.id])


if __name__ == '__main__':
  main()