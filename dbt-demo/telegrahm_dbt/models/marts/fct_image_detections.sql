 WITH staged_detections AS (
      SELECT
          message_id,
          detected_object_class,
          confidence_score,
          detection_time
      FROM {{ source('raw_data', 'stg_image_detections') }}
  )
  SELECT
      message_id,
      detected_object_class,
      ROUND(confidence_score::NUMERIC, 2) AS confidence_score,
      detection_time
  FROM staged_detections
  WHERE confidence_score >= 0.5  -- Filter for confident detections
  