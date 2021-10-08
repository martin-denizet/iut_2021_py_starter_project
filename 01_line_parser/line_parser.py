def parse_line(line):
    """

    :param line:
    :return:
    :rtype: dict[str,Any]
    """

    return dict(
        remote_ip='',
        time='',
        request='',
        response=0,
        bytes=0,
        referrer='',
        user_agent=''
    )
