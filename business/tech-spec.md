```markdown
# Technical Specification for saas-localize

## Stack
- **Language**: Python (3.11+)
- **Framework**: FastAPI (for API), Django (for admin panel)
- **Runtime**: Docker containers orchestrated by Kubernetes
- **Database**: PostgreSQL (with PostGIS extension for geospatial features)
- **Message Broker**: RabbitMQ for async task processing
- **Search**: Elasticsearch for full-text search capabilities
- **Translation Engines**: Integration with Google Translate API, DeepL, and AWS Translate

## Hosting
- **Free-Tier-First**: AWS Free Tier (EC2, RDS, S3, Lambda)
- **Specific Platforms**:
  - **Development**: AWS Lightsail (for simplicity and cost-effectiveness)
  - **Staging**: AWS EKS (Elastic Kubernetes Service)
  - **Production**: AWS EKS with multi-AZ deployment for high availability

## Data Model
### Tables/Collections
1. **Projects**
   - `project_id` (UUID, primary key)
   - `name` (String)
   - `description` (Text)
   - `created_at` (Timestamp)
   - `updated_at` (Timestamp)

2. **Translations**
   - `translation_id` (UUID, primary key)
   - `project_id` (UUID, foreign key)
   - `source_language` (String)
   - `target_language` (String)
   - `source_text` (Text)
   - `translated_text` (Text)
   - `status` (String, enum: 'pending', 'in_progress', 'completed', 'failed')
   - `created_at` (Timestamp)
   - `updated_at` (Timestamp)

3. **Users**
   - `user_id` (UUID, primary key)
   - `email` (String, unique)
   - `password_hash` (String)
   - `created_at` (Timestamp)
   - `updated_at` (Timestamp)

4. **API_Keys**
   - `api_key_id` (UUID, primary key)
   - `user_id` (UUID, foreign key)
   - `key` (String, unique)
   - `created_at` (Timestamp)
   - `expires_at` (Timestamp)

## API Surface
1. **POST /api/projects**
   - **Purpose**: Create a new project.

2. **GET /api/projects**
   - **Purpose**: List all projects for the authenticated user.

3. **GET /api/projects/{project_id}**
   - **Purpose**: Retrieve details of a specific project.

4. **POST /api/projects/{project_id}/translations**
   - **Purpose**: Submit a new translation job.

5. **GET /api/projects/{project_id}/translations**
   - **Purpose**: List all translations for a specific project.

6. **GET /api/projects/{project_id}/translations/{translation_id}**
   - **Purpose**: Retrieve the status and result of a specific translation job.

7. **POST /api/users**
   - **Purpose**: Register a new user.

8. **POST /api/users/login**
   - **Purpose**: Authenticate a user and generate an API key.

9. **GET /api/users/me**
   - **Purpose**: Retrieve the details of the authenticated user.

10. **DELETE /api/users/me**
    - **Purpose**: Delete the authenticated user's account.

## Security Model
- **Authentication**: JWT (JSON Web Tokens) for API authentication.
- **Secrets**: Use AWS Secrets Manager to store sensitive information like database credentials and API keys.
- **IAM**: Implement role-based access control (RBAC) to manage permissions for different user roles (e.g., admin, project manager, translator).

## Observability
- **Logs**: Use AWS CloudWatch for centralized logging.
- **Metrics**: Implement Prometheus for monitoring and alerting.
- **Traces**: Use AWS X-Ray for distributed tracing to monitor the performance and health of the application.

## Build/CI
- **CI/CD Pipeline**: Use GitHub Actions for continuous integration and deployment.
- **Build Tools**: Docker for containerization, Kubernetes for orchestration.
- **Testing**: Implement unit tests, integration tests, and end-to-end tests using pytest.
- **Deployment**: Automated deployment to AWS EKS using GitHub Actions and Helm charts.
```