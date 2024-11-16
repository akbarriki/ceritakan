import pandas as pd
import requests, json
from bs4 import BeautifulSoup as bs
from datetime import datetime as dt

# url = "https://x.com/i/api/graphql/MJpyQGqgklrVl_0X9gNy3A/SearchTimeline?variables=%7B%22rawQuery%22%3A%22pingin%20mati%20aja%22%2C%22count%22%3A20%2C%22cursor%22%3A%22DAADDAABCgABGb8Qj0aWEX8KAAIXdmbluVtwAAAIAAIAAAACCAADAAAAAggABAAAACAKAAUZvx8HVsB1MAoABhm_HwdWuvbwAAA%22%2C%22querySource%22%3A%22typed_query%22%2C%22product%22%3A%22Latest%22%7D&features=%7B%22rweb_tipjar_consumption_enabled%22%3Atrue%2C%22responsive_web_graphql_exclude_directive_enabled%22%3Atrue%2C%22verified_phone_label_enabled%22%3Afalse%2C%22creator_subscriptions_tweet_preview_api_enabled%22%3Atrue%2C%22responsive_web_graphql_timeline_navigation_enabled%22%3Atrue%2C%22responsive_web_graphql_skip_user_profile_image_extensions_enabled%22%3Afalse%2C%22communities_web_enable_tweet_community_results_fetch%22%3Atrue%2C%22c9s_tweet_anatomy_moderator_badge_enabled%22%3Atrue%2C%22articles_preview_enabled%22%3Atrue%2C%22responsive_web_edit_tweet_api_enabled%22%3Atrue%2C%22graphql_is_translatable_rweb_tweet_is_translatable_enabled%22%3Atrue%2C%22view_counts_everywhere_api_enabled%22%3Atrue%2C%22longform_notetweets_consumption_enabled%22%3Atrue%2C%22responsive_web_twitter_article_tweet_consumption_enabled%22%3Atrue%2C%22tweet_awards_web_tipping_enabled%22%3Afalse%2C%22creator_subscriptions_quote_tweet_preview_enabled%22%3Afalse%2C%22freedom_of_speech_not_reach_fetch_enabled%22%3Atrue%2C%22standardized_nudges_misinfo%22%3Atrue%2C%22tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled%22%3Atrue%2C%22rweb_video_timestamps_enabled%22%3Atrue%2C%22longform_notetweets_rich_text_read_enabled%22%3Atrue%2C%22longform_notetweets_inline_media_enabled%22%3Atrue%2C%22responsive_web_enhance_cards_enabled%22%3Afalse%7D"
# url = "https://x.com/i/api/graphql/MJpyQGqgklrVl_0X9gNy3A/SearchTimeline?variables=%7B%22rawQuery%22%3A%22capek%20nyerah%20mati%22%2C%22count%22%3A20%2C%22cursor%22%3A%22DAADDAABCgABGb8SzXnaURYKAAIX_aC1yZtwBwAIAAIAAAACCAADAAAAAAgABAAAAAkKAAUZwJgyiUAnEAoABhnAmDKJPnlgAAA%22%2C%22querySource%22%3A%22typed_query%22%2C%22product%22%3A%22Latest%22%7D&features=%7B%22rweb_tipjar_consumption_enabled%22%3Atrue%2C%22responsive_web_graphql_exclude_directive_enabled%22%3Atrue%2C%22verified_phone_label_enabled%22%3Afalse%2C%22creator_subscriptions_tweet_preview_api_enabled%22%3Atrue%2C%22responsive_web_graphql_timeline_navigation_enabled%22%3Atrue%2C%22responsive_web_graphql_skip_user_profile_image_extensions_enabled%22%3Afalse%2C%22communities_web_enable_tweet_community_results_fetch%22%3Atrue%2C%22c9s_tweet_anatomy_moderator_badge_enabled%22%3Atrue%2C%22articles_preview_enabled%22%3Atrue%2C%22responsive_web_edit_tweet_api_enabled%22%3Atrue%2C%22graphql_is_translatable_rweb_tweet_is_translatable_enabled%22%3Atrue%2C%22view_counts_everywhere_api_enabled%22%3Atrue%2C%22longform_notetweets_consumption_enabled%22%3Atrue%2C%22responsive_web_twitter_article_tweet_consumption_enabled%22%3Atrue%2C%22tweet_awards_web_tipping_enabled%22%3Afalse%2C%22creator_subscriptions_quote_tweet_preview_enabled%22%3Afalse%2C%22freedom_of_speech_not_reach_fetch_enabled%22%3Atrue%2C%22standardized_nudges_misinfo%22%3Atrue%2C%22tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled%22%3Atrue%2C%22rweb_video_timestamps_enabled%22%3Atrue%2C%22longform_notetweets_rich_text_read_enabled%22%3Atrue%2C%22longform_notetweets_inline_media_enabled%22%3Atrue%2C%22responsive_web_enhance_cards_enabled%22%3Afalse%7D"
# user


def CollectTweetsFromUser(username, last_tweets=5):
    url_userid = f"https://x.com/i/api/graphql/BQ6xjFU6Mgm-WhEP3OiT9w/UserByScreenName?variables=%7B%22screen_name%22%3A%22{username}%22%7D&features=%7B%22hidden_profile_subscriptions_enabled%22%3Atrue%2C%22rweb_tipjar_consumption_enabled%22%3Atrue%2C%22responsive_web_graphql_exclude_directive_enabled%22%3Atrue%2C%22verified_phone_label_enabled%22%3Afalse%2C%22subscriptions_verification_info_is_identity_verified_enabled%22%3Atrue%2C%22subscriptions_verification_info_verified_since_enabled%22%3Atrue%2C%22highlights_tweets_tab_ui_enabled%22%3Atrue%2C%22responsive_web_twitter_article_notes_tab_enabled%22%3Atrue%2C%22subscriptions_feature_can_gift_premium%22%3Atrue%2C%22creator_subscriptions_tweet_preview_api_enabled%22%3Atrue%2C%22responsive_web_graphql_skip_user_profile_image_extensions_enabled%22%3Afalse%2C%22responsive_web_graphql_timeline_navigation_enabled%22%3Atrue%7D&fieldToggles=%7B%22withAuxiliaryUserLabels%22%3Afalse%7D"
    
    headers_userid  = {
        'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
        'Content-Type': 'application/json',
        'Cookie': 'guest_id=172973070495866289; night_mode=2; guest_id_marketing=v1%3A172973070495866289; guest_id_ads=v1%3A172973070495866289; g_state={"i_l":0}; kdt=EOB28raiE5vT5RlHpd6OTTfvxrIwGm4rX8Y1HsLf; auth_token=2375dfef2276800e3c58fe17fac6d753b684e283; ct0=12d129958b50216e10333ad4446283b5fff9976337e930ee3f329eb1b821980035e7990eeb8305f0269a7ebb541d5852f1ea25fb68c3f7c3fdaa212b74c438d234c434dddf7842ee30194d97d9133007; twid=u%3D975916602465009664; des_opt_in=Y; _ga=GA1.2.593174452.1731156145; _ga_KEWZ1G5MB3=GS1.2.1731157342.1.0.1731157342.60.0.0; lang=en; personalization_id="v1_cb1gLOnG33Lzay1isUXyfg=="',
        'Priority': 'u=1, i',
        'Referer': f'https://x.com/{username}',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0',
        'X-Csrf-Token': '12d129958b50216e10333ad4446283b5fff9976337e930ee3f329eb1b821980035e7990eeb8305f0269a7ebb541d5852f1ea25fb68c3f7c3fdaa212b74c438d234c434dddf7842ee30194d97d9133007',
        'X-Twitter-Active-User': 'yes',
        'X-Twitter-Auth-Type': 'OAuth2Session',
        'X-Twitter-Client-Language': 'en'
    }

    headers  = {
        'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
        'Content-Type': 'application/json',
        'Cookie': 'guest_id=172973070495866289; night_mode=2; guest_id_marketing=v1%3A172973070495866289; guest_id_ads=v1%3A172973070495866289; g_state={"i_l":0}; kdt=EOB28raiE5vT5RlHpd6OTTfvxrIwGm4rX8Y1HsLf; auth_token=2375dfef2276800e3c58fe17fac6d753b684e283; ct0=12d129958b50216e10333ad4446283b5fff9976337e930ee3f329eb1b821980035e7990eeb8305f0269a7ebb541d5852f1ea25fb68c3f7c3fdaa212b74c438d234c434dddf7842ee30194d97d9133007; twid=u%3D975916602465009664; des_opt_in=Y; _ga=GA1.2.593174452.1731156145; _ga_KEWZ1G5MB3=GS1.2.1731157342.1.0.1731157342.60.0.0; lang=en; personalization_id="v1_cb1gLOnG33Lzay1isUXyfg=="',
        'Priority': 'u=1, i',
        'Referer': f'https://x.com/{username}',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36 Edg/130.0.0.0',
        'X-Client-Uuid': '0bda2303-cdd8-4f6e-9be9-ce69e58d83c9',
        'X-Csrf-Token': '12d129958b50216e10333ad4446283b5fff9976337e930ee3f329eb1b821980035e7990eeb8305f0269a7ebb541d5852f1ea25fb68c3f7c3fdaa212b74c438d234c434dddf7842ee30194d97d9133007',
        'X-Twitter-Active-User': 'yes',
        'X-Twitter-Auth-Type': 'OAuth2Session',
        'X-Twitter-Client-Language': 'en'
    }

    resp = requests.get(url_userid, headers=headers_userid)
    tweets = []
    
    if resp.status_code == 200:
        userid = json.loads(resp.text)['data']['user']['result']['rest_id']
        url = f"https://x.com/i/api/graphql/Tg82Ez_kxVaJf7OPbUdbCg/UserTweets?variables=%7B%22userId%22%3A%22{userid}%22%2C%22count%22%3A20%2C%22includePromotedContent%22%3Atrue%2C%22withQuickPromoteEligibilityTweetFields%22%3Atrue%2C%22withVoice%22%3Atrue%2C%22withV2Timeline%22%3Atrue%7D&features=%7B%22rweb_tipjar_consumption_enabled%22%3Atrue%2C%22responsive_web_graphql_exclude_directive_enabled%22%3Atrue%2C%22verified_phone_label_enabled%22%3Afalse%2C%22creator_subscriptions_tweet_preview_api_enabled%22%3Atrue%2C%22responsive_web_graphql_timeline_navigation_enabled%22%3Atrue%2C%22responsive_web_graphql_skip_user_profile_image_extensions_enabled%22%3Afalse%2C%22communities_web_enable_tweet_community_results_fetch%22%3Atrue%2C%22c9s_tweet_anatomy_moderator_badge_enabled%22%3Atrue%2C%22articles_preview_enabled%22%3Atrue%2C%22responsive_web_edit_tweet_api_enabled%22%3Atrue%2C%22graphql_is_translatable_rweb_tweet_is_translatable_enabled%22%3Atrue%2C%22view_counts_everywhere_api_enabled%22%3Atrue%2C%22longform_notetweets_consumption_enabled%22%3Atrue%2C%22responsive_web_twitter_article_tweet_consumption_enabled%22%3Atrue%2C%22tweet_awards_web_tipping_enabled%22%3Afalse%2C%22creator_subscriptions_quote_tweet_preview_enabled%22%3Afalse%2C%22freedom_of_speech_not_reach_fetch_enabled%22%3Atrue%2C%22standardized_nudges_misinfo%22%3Atrue%2C%22tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled%22%3Atrue%2C%22rweb_video_timestamps_enabled%22%3Atrue%2C%22longform_notetweets_rich_text_read_enabled%22%3Atrue%2C%22longform_notetweets_inline_media_enabled%22%3Atrue%2C%22responsive_web_enhance_cards_enabled%22%3Afalse%7D&fieldToggles=%7B%22withArticlePlainText%22%3Afalse%7D"
        resp = requests.get(url, headers=headers)
        # print(resp.status_code)
        if resp.status_code == 200:
            entries = json.loads(resp.text)['data']['user']['result']['timeline_v2']['timeline']['instructions'][1]['entries']
            for entry in entries:
                try:
                    user = entry['content']['itemContent']['tweet_results']['result']['core']['user_results']['result']['legacy']
                    user_created_at = user['created_at']
                    user_location = user['location']
                    user_name = username
                    user_device = entry['content']['itemContent']['tweet_results']['result']['source']
                    user_tweet = entry['content']['itemContent']['tweet_results']['result']['legacy']['full_text']
                    user_tweet_created_at = entry['content']['itemContent']['tweet_results']['result']['legacy']['created_at']
                    tweets.append({
                        "user_created_at": user_created_at,
                        "user_location": user_location,
                        "user_name": user_name,
                        "user_device": user_device,
                        "user_tweet": user_tweet,
                        "user_tweet_created_at": user_tweet_created_at
                    })
                    if len(tweets) == last_tweets:
                        break
                except:
                    continue
            return tweets
    return None

if __name__ == '__main__':
    username = "gakbolehspill"
    # print(username)
    tweets = CollectTweetsFromUser(username)
    print(tweets)