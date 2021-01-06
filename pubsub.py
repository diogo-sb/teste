gcloud pubsub topics create Contract-SubContract
gcloud pubsub subscriptions create SubContract \
    --topic Contract-SubContract \
    --push-endpoint \
    https://cerc-datalake-dev-01.REGION_ID.r.appspot.com/pubsub/push?token=YOUR_TOKEN \
    --ack-deadline 10