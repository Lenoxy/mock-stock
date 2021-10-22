# requires ng build
FROM nginx:1.17.1-alpine
COPY nginx.conf /etc/nginx/nginx.conf
COPY /home/mock-stock/mock-stock/dist/mockstock /usr/share/nginx/html
