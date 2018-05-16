import constants
import httplib
import logging
import os

import pafy

from downloader.ytdl import YtdlMedia
from util import convert_to_mp3
from util import generate_video_title
from util import get_local_audios
from util import json_url_open


YOUTUBE_API_URL = 'https://content.googleapis.com/youtube/v3'
YOUTUBE_PLAYLIST_API_URL = YOUTUBE_API_URL + '/playlists?part=snippet&key={0}&id={1}'
YOUTUBE_PLAYLIST_ITEMS_API_URL = YOUTUBE_API_URL + '/playlistItems?part=id,contentDetails,snippet&key={0}&playlistId={1}&pageToken={2}'
YOUTUBE_PLAYLIST_NEXT_PAGE = '&pageToken={0}'
YOUTUBE_WATCH_URL = 'https://www.youtube.com/watch?v={0}'

# response variables
CHANNEL_TITLE 		= 'channelTitle'
CONTENT_DETAILS 	= 'contentDetails'
ID 					= 'id'
ITEMS 				= 'items'
NEXT_PAGE_TOKEN 	= 'nextPageToken'
PAGE_INFO 			= 'pageInfo'
RESULTS_PER_PAGE 	= 'resultsPerPage'
SNIPPET 			= 'snippet'
TITLE 				= 'title'
TOTAL_RESULTS 		= 'totalResults'
VIDEO_ID 			= 'videoId'


def get_playlist_info(api_key, playlist_id):
    logging.info('Retrieving information about playlist with id = %s', playlist_id)

    try:
        url = YOUTUBE_PLAYLIST_API_URL.format(api_key, playlist_id)

        json_response = json_url_open(url)

        logging.debug('Retrieving playlist info')

        if json_response.get(PAGE_INFO).get(TOTAL_RESULTS) > 0:
            json_info = json_response.get(ITEMS)[0]

            json_snippet = json_info.get(SNIPPET)
            playlist_title = json_snippet.get(TITLE).encode('UTF-8')
            channel_title = json_snippet.get(CHANNEL_TITLE).encode('UTF-8')

            description = 'Playlist name - {0}, channel title - {1}'.format(playlist_title, channel_title)

            return description
        else:
            logging.info('No playlist was found with specified id = %s', playlist_id)
            raise Exception('Playlist info could not be retrieved. '
                            'Check if playlist id is correct or it has public access')

    except Exception as ex:
        logging.error('An exception raised while retrieving information about playlist')
        raise ex


def get_videos_from_playlist(api_key, playlist_id):
    logging.info('Retrieving videos from playlist with id = %s', playlist_id)

    videos = []
    try:
        done = False
        next_page_token = ''
        page = 0
        while not done:
            url = YOUTUBE_PLAYLIST_ITEMS_API_URL.format(api_key, playlist_id, next_page_token)

            json_response = json_url_open(url)

            results_per_page = json_response.get(PAGE_INFO).get(RESULTS_PER_PAGE)
            total_results = json_response.get(PAGE_INFO).get(TOTAL_RESULTS)

            if total_results is None or total_results == 0:
                logging.info('No videos in this playlits, id = %s', playlist_id)

            total_pages = total_results / results_per_page
            if total_results % results_per_page > 0:
                total_pages += 1

            page += 1

            logging.info('Processing page %d of %d', page, total_pages)

            json_videos = json_response.get(ITEMS)

            for json_video in json_videos:
                videos.append(json_video)

            next_page_token = json_response.get(NEXT_PAGE_TOKEN)

            if next_page_token is None:
                done = True

    except Exception as ex:
        logging.error('An exception raised while retrieving videos from playlist')
        raise ex

    logging.info('Done with retrieving videos from playlist')

    return videos


def synchronize_audios(videos, working_dir):
    logging.info('Synchronizing all videos from youtube playlist with local playlist')

    audios_to_download = []

    try:
        local_audios = get_local_audios(working_dir)

        logging.debug('Local audios = %d, cloud videos = %d', len(local_audios), len(videos))

        for cloud_video in videos:
            audio_title = unicode(cloud_video.get(SNIPPET).get(TITLE))
            content_details_json = cloud_video.get(CONTENT_DETAILS)
            audio_id = content_details_json.get(VIDEO_ID)

            audio_title_full = generate_video_title(audio_title, audio_id)
            if audio_title_full not in local_audios:
                audios_to_download.append(cloud_video)

        logging.info('Files to download - %s', len(audios_to_download))

    except Exception as ex:
        logging.error('An error occurred while synchronizing audios')
        raise ex

    return audios_to_download


def get_playlist_videos_url(videos_as_json):
    logging.info('Retrieving videos urls from json response')

    urls = []

    try:
        for video in videos_as_json:

            content_details_json = video.get(CONTENT_DETAILS)

            video_url = content_details_json.get(VIDEO_ID)

            if video_url is not None:
                urls.append({VIDEO_ID: video_url})

    except Exception as ex:
        logging.error('An error occurred while retrieving videos url from response')
        raise ex

    return urls


def get_single_video_urls(video_url):
    logging.info('Preparing video url')

    url = [
        {VIDEO_ID: video_url}
    ]

    return url


def download_data_from_video(video_id, root):

    temp_dir = os.path.join(root, constants.ROOT_TEMP_DIR)

    try:
        url = YOUTUBE_WATCH_URL.format(video_id)
        logging.debug('Working with url: %s', url)

        video = YtdlMedia(url, temp_dir)

        logging.info('Video title: %s', video.title)
        logging.debug('Downloading video for url: %s', url)

        video.download_audio()

        video.download_thumb()

    except Exception as ex:
        logging.error('An error occurred while downloading audios from videos')
        raise ex

    return video.title


def save_mp3(urls, working_dir, album=None, track_number=0):
    logging.info('Downloading and converting files to mp3, working directory - "%s"', os.path.abspath(working_dir))

    for url in urls:
        track_number += 1
        title = download_data_from_video(url[VIDEO_ID], working_dir)
        convert_to_mp3(title, url[VIDEO_ID], working_dir, album, track_number)

    logging.info('Finished downloading and converting audio from all videos, downloaded videos = %d', len(urls))
