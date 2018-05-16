from youtube_dl.utils import DateRange

# general
MAX_ATTEMPT = 5

# urls
HD_THUMB_URL_FRMT = 'http://i.ytimg.com/vi/{0}/hqdefault.jpg'

# temporary directories names
ROOT_TEMP_DIR = 'temp'
VIDEO_TEMP_DIR = 'video'
IMAGE_TEMP_DIR = 'image'

# ytdl output format
YTDL_OUTP_FRMT = "%(id)s.%(ext)s"
# result output format
RES_OUTP_FRMT = "{0} [{1}].{2}"

# ytdl default options
YTDL_OPTS = {
    'usenetrc': False,
    'username': None,
    'password': None,
    'twofactor': None,
    'videopassword': None,
    'ap_mso': None,
    'ap_username': None,
    'ap_password': None,
    'quiet': False,
    'no_warnings': False,
    'forceurl': False,
    'forcetitle': False,
    'forceid': False,
    'forcethumbnail': False,
    'forcedescription': False,
    'forceduration': False,
    'forcefilename': False,
    'forceformat': False,
    'forcejson': False,
    'dump_single_json': False,
    'simulate': False,
    'skip_download': False,
    'format': None,
    'listformats': None,
    'outtmpl': '%(title)s-%(id)s.%(ext)s',
    'autonumber_size': None,
    'autonumber_start': 1,
    'restrictfilenames': False,
    'ignoreerrors': False,
    'force_generic_extractor': False,
    'ratelimit': None,
    'nooverwrites': False,
    'retries': 10,
    'fragment_retries': 10,
    'skip_unavailable_fragments': True,
    'keep_fragments': False,
    'buffersize': 1024,
    'noresizebuffer': False,
    'http_chunk_size': None,
    'continuedl': True,
    'noprogress': False,
    'progress_with_newline': False,
    'playliststart': 1,
    'playlistend': None,
    'playlistreverse': None,
    'playlistrandom': None,
    'noplaylist': False,
    'logtostderr': False,
    'consoletitle': False,
    'nopart': False,
    'updatetime': True,
    'writedescription': False,
    'writeannotations': False,
    'writeinfojson': False,
    'writethumbnail': False,
    'write_all_thumbnails': False,
    'writesubtitles': False,
    'writeautomaticsub': False,
    'allsubtitles': False,
    'listsubtitles': False,
    'subtitlesformat': 'best',
    'subtitleslangs': [],
    'matchtitle': None,
    'rejecttitle': None,
    'max_downloads': None,
    'prefer_free_formats': False,
    'verbose':False,
    'dump_intermediate_pages': False,
    'write_pages': False,
    'test': False,
    'keepvideo': False,
    'min_filesize': None,
    'max_filesize': None,
    'min_views': None,
    'max_views': None,
    'daterange': DateRange('00010101', '99991231'),
    'cachedir': None,
    'youtube_print_sig_code': False,
    'age_limit': None,
    'download_archive': None,
    'cookiefile': None,
    'nocheckcertificate': False,
    'prefer_insecure': None,
    'proxy': None,
    'socket_timeout': None,
    'bidi_workaround': None,
    'debug_printtraffic': False,
    'prefer_ffmpeg': None,
    'include_ads': None,
    'default_search': None,
    'youtube_include_dash_manifest': True,
    'encoding': None, # or utf-8
    'extract_flat': False,
    'mark_watched': False,
    'merge_output_format': None,
    'postprocessors': [],
    'fixup': u'detect_or_warn',
    'source_address': None,
    'call_home': False,
    'sleep_interval': None,
    'max_sleep_interval': None,
    'external_downloader': None,
    'list_thumbnails': False,
    'playlist_items': None,
    'xattr_set_filesize': None,
    'match_filter': None,
    'no_color': False,
    'ffmpeg_location': None,
    'hls_prefer_native': None,
    'hls_use_mpegts': None,
    'external_downloader_args': None,
    'postprocessor_args': None,
    'cn_verification_proxy': None,
    'geo_verification_proxy': None,
    'config_location': None,
    'geo_bypass': True,
    'geo_bypass_country': None,
    'geo_bypass_ip_block': None,
    # just for deprecation check
    'autonumber': None,
    'usetitle': None,
}
