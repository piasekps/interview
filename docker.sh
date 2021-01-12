#!/usr/bin/env bash

containers="api"

help=$(cat <<-EOF
Usage: $0 [options]

Containers:
    up                              run environment
    build                           build environment
    list                            list containers
    ssh <container_name>            log in to container (available containers: $containers)
    run <container_name> <command>  run command in a container (available containers: $containers)
    rebuild                         rebuild all containers
    rebuild <container_name>        rebuild single container (available containers: $containers)
    destroy                         stop and remove containers, networks, images, and volumes

Tests:
    ipdb                            allow to use ipdb (run all containers and attach to api container)
    pytests [options]               run python tests

Utils:
    shell                           Run ipython console with loaded models and created session under "db_session" variable
EOF
)

case "$1" in
    up|build)
        docker-compose up
        ;;
    list)
        docker-compose ps
        ;;
    ssh)
        docker-compose run --rm $2 bash
        ;;
    run)
        docker-compose run --rm $2 $3
        ;;
    ipdb)
        docker-compose up -d db
        docker-compose run --rm --service-ports api
        ;;
    pytests)
        docker-compose run -e API_ENV=tests --rm api pytest -s ${@:2}
        ;;
    coverage)
        docker-compose run -e API_ENV=tests --rm api pytest --cov=api
        ;;
    rebuild)
        if [ -z "$2" ]
            then
                docker-compose build
            else
                docker-compose build $2
        fi
        ;;
    destroy)
        docker-compose down
        ;;
    shell)
        docker-compose exec api ipython -i -c "\
        from core.db.session import Session; \
        from organisations.models import Organisation; \
        from users.models import User; \
        db_session = Session();"
        ;;
    --help)
        echo "$help"
        ;;
    *)
        echo -e "Unknown parameter $1!\n\nUse $0 --help to list all available commands."
        ;;
esac
