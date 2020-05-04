from enum import IntEnum


class EventType(IntEnum):
    view_conversion = 1
    click_conversion = 2
    server_to_server_conversion = 3
    upvote = 10
    downvote = 11
    downvote_uninteresting = 12
    downvote_misleading = 13
    downvote_offensive = 14
    downvote_repetitive = 15
    downvote_other = 16
    close_ad = 17
    like = 20
    share = 21
    comment = 22
    comment_reply = 101
    comment_upvote = 102
    comment_downvote = 103
    visible = 30
    hover = 31
    expand_div = 32
    viewable_impression = 40
    share_on_facebook = 50
    share_on_twitter = 51
    share_on_pinterest = 52
    share_on_reddit = 53
    share_on_email = 54
    video_start = 70
    video_first_quartile = 71
    video_mid_point = 72
    video_third_quartile = 73
    video_complete = 74
    video_mute = 75
    video_unmute = 76
    video_pause = 77
    video_rewind = 78
    video_resume = 79
    video_full_screen = 80
    video_exit_full_screen = 81
    video_expand = 82
    video_collapse = 83
    video_accept_invitation_linear = 84
    video_close_linear = 85
    video_skip = 86
    video_progress = 87
    video_zero_seconds_viewed = 400
    video_ones_seconds_viewed = 401
    video_two_seconds_viewed = 402
    video_three_seconds_viewed = 403
    video_four_seconds_viewed = 404
    video_five_seconds_viewed = 405
    video_six_seconds_viewed = 406
    video_seven_seconds_viewed = 407
    video_eight_seconds_viewed = 408
    video_nNine_seconds_viewed = 409
    video_ten_seconds_viewed = 410
    video_fifteen_seconds_viewed = 415
    video_twenty_seconds_viewed = 420
    video_twenty_five_seconds_viewed = 425
    video_thirty_seconds_viewed = 430


class RateType(IntEnum):
    flat = 1
    cpm = 2
    cpc = 3
    cpa_view = 4
    cpa_click = 5
    cpa_view_and_click = 6
