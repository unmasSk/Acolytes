# Technical Stack

## Application Framework
- **Framework:** Ruby on Rails 7.1.2
- **Runtime:** Ruby 3.2.0
- **Server:** Puma 6.4

## Database System
- **Primary Database:** PostgreSQL 15.4
- **Caching Layer:** Redis 7.2
- **Search Engine:** Elasticsearch 8.10

## JavaScript Framework
- **Frontend Framework:** Vue.js 3.3.8
- **Build Tool:** Vite 4.5
- **State Management:** Pinia 2.1

## Import Strategy
- **Module System:** importmaps
- **Package Manager:** npm 10.2
- **Bundling:** Rails Asset Pipeline + Vite

## CSS Framework
- **Framework:** Tailwind CSS 3.3.6
- **Components:** Headless UI 1.7
- **Icons:** Heroicons 2.0

## UI Component Library
- **Library:** Custom Vue components built on Headless UI
- **Design System:** Internal design tokens
- **Accessibility:** WCAG 2.1 AA compliant

## Fonts Provider
- **Primary:** Google Fonts (Inter, JetBrains Mono)
- **Fallback:** System font stack
- **Loading:** Font Display Swap

## Icon Library
- **Primary:** Heroicons 2.0
- **Custom Icons:** SVG sprite system
- **Format:** Inline SVG with Vue components

## Application Hosting
- **Platform:** Heroku Professional
- **CDN:** Cloudflare
- **SSL:** Automated Let's Encrypt

## Database Hosting
- **Service:** Heroku Postgres Standard-2
- **Backup:** Heroku PG Backups (daily)
- **Monitoring:** Heroku Postgres Insights

## Asset Hosting
- **Service:** AWS S3 + CloudFront
- **Image Processing:** Active Storage + ImageMagick
- **File Upload:** Direct S3 upload with presigned URLs

## Deployment Solution
- **Platform:** Heroku with GitHub integration
- **Pipeline:** GitHub Actions → Staging → Production
- **Rollback:** Heroku rollback capability

## Code Repository
- **URL:** https://github.com/taskflow-team/taskflow-app
- **Branching:** GitFlow with main, develop, and feature branches
- **CI/CD:** GitHub Actions with automated testing

## Development Tools
- **Code Editor:** VS Code with Ruby/Vue extensions
- **Database Client:** TablePlus
- **API Testing:** Postman/Insomnia
- **Version Control:** Git with conventional commits

## Monitoring & Analytics
- **Application Monitoring:** New Relic
- **Error Tracking:** Sentry
- **Analytics:** Google Analytics 4
- **Uptime Monitoring:** Pingdom

## Authentication & Security
- **Authentication:** Devise with JWT tokens
- **Authorization:** Pundit policies
- **Security Headers:** Secure Headers gem
- **Rate Limiting:** Rack::Attack

## Testing Framework
- **Backend Testing:** RSpec with Factory Bot
- **Frontend Testing:** Vitest + Vue Test Utils
- **E2E Testing:** Cypress
- **Coverage:** SimpleCov (>90% target)