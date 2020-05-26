FROM traefik:v2.0
RUN mkdir -p /etc/traefik/


COPY ./compose/production/traefik/certificate.crt /etc/traefik/
COPY ./compose/production/traefik/cert.key /etc/traefik/
RUN chmod 600 /etc/traefik/certificate.crt
RUN chmod 600 /etc/traefik/cert.key

COPY ./compose/production/traefik/traefik.yml /etc/traefik
