SELECT DISTINCT
    channel_name,
    CASE
        WHEN channel_name = 'Chemed123' THEN 'https://t.me/Chemed123'
        WHEN channel_name = 'lobelia4cosmetics' THEN 'https://t.me/lobelia4cosmetics'
        WHEN channel_name = 'tikvahpharma' THEN 'https://t.me/tikvahpharma'
    END AS channel_url
FROM {{ ref('stg_telegram_messages') }}