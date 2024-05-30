FROM fluent/fluentd:v1.16-debian-arm64-1

USER root

RUN apt-get update && apt-get install -y --no-install-recommends \
    sudo build-essential ruby-dev \
    && gem install fluent-plugin-elasticsearch \
    && gem sources --clear-all \
    && apt-get remove --purge -y build-essential ruby-dev \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* \
    /home/fluent/.gem/ruby/2.3.0/cache/*.gem

USER fluent
