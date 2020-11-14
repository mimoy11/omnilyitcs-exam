# Stage 1, based on Nginx, to have only the compiled app, ready for production with Nginx
FROM nginx:1.17-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.dev.conf /etc/nginx/conf.d

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
