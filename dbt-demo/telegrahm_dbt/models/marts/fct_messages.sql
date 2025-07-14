{{
  config(
    materialized='table',
    schema='telegram_marts'
  )
}}

SELECT
    s.message_id,
    s.channel_name,
    s.date,
    s.message_timestamp,
    s.message_text,
    s.sender_id,
    s.has_media,
    s.media_type,
    s.media_path,
    s.message_length,
    c.channel_url,
    d.year,
    d.month,
    d.day
FROM {{ ref('stg_telegram_messages') }} s
LEFT JOIN {{ ref('dim_channels') }} c ON s.channel_name = c.channel_name
LEFT JOIN {{ ref('dim_dates') }} d ON s.date = d.date