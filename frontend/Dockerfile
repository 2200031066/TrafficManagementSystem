FROM node:18-alpine AS builder

WORKDIR /app
COPY package*.json ./

RUN npm ci
COPY . .

RUN npm run build
FROM nginx:alpine

# Copy built files from builder
COPY --from=builder /app/build /usr/share/nginx/html
# Copy custom nginx configuration
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expose port
EXPOSE 80
# Start nginx
CMD ["nginx", "-g", "daemon off;"]
