Project Name
1. Task Manager

Tech stack
Frontend (UI):

React (JavaScript) → for a modern, interactive dashboard

TailwindCSS or Material UI → for styling

Backend (API):

Python with FastAPI (fast, async, modern)

These expose APIs like /tasks, /projects, /users that your React frontend will call

Database:

Or MongoDB (document-based, flexible if you don’t want strict schemas)


AI Integration Plan
Code or Feature Generation


Frontend Components → React components such as task cards, dashboards, modals, and form elements.

Backend Routes & Controllers → REST API endpoints (e.g., /tasks, /projects, /users) along with request/response validation.

Data Models & Schemas → Database models for tasks, users, and projects (e.g., MongoDB schemas or SQLAlchemy models in Python).

Utility Functions → Common helpers like date formatters, status filters, or notification triggers.

Testing Support

I will use AI to assist in generating unit and integration tests to improve code reliability and coverage. Specifically, AI will:

Unit Tests → Suggest test cases for individual functions, models, and React components (e.g., checking task creation, validation errors, or edge cases).

Integration Tests → Generate test suites that simulate real API workflows, such as creating a task, updating it, and verifying it appears correctly on the dashboard.

Test Data Generation → Provide mock data (sample users, projects, and tasks) for testing scenarios.

Coverage Expansion → Recommend missing test cases by analyzing code paths and highlighting untested logic.

Schema-Aware or API-Aware Generation

I will use AI to accelerate development by generating functions, routes, and queries directly informed by the project’s database schema or OpenAPI specification. With this context, AI can:

Schema-Aware Code → Generate Python models (e.g., SQLAlchemy or Pydantic) or MongoDB schemas by referencing task, user, and project structures.

API-Aware Endpoints → Scaffold REST API routes and request/response handlers that strictly follow the defined OpenAPI spec, ensuring consistency between backend and frontend.

Client Functions → Create React hooks or service functions (e.g., getTasks(), createTask()) automatically typed from the API spec for safer data fetching.

Validation & Serialization → Generate input validators, serializers, and response models aligned with the schema.

Error Handling → Suggest error cases and responses that match both schema constraints and API contracts.

In-Editor/PR Review Tooling (CodeRabbit)

I will use CodeRabbit as my AI-powered assistant for code reviews and collaboration. CodeRabbit integrates directly into the development workflow and GitHub, making it ideal for maintaining high-quality code in the web dashboard project.

Code Reviews in PRs → CodeRabbit will automatically review pull requests, leaving inline comments on potential bugs, security concerns, or performance bottlenecks.

Style & Best Practices → It will flag violations of coding conventions (e.g., Python PEP8, React component patterns) and recommend improvements to maintain consistency.

Commit Message Generation → Based on the changes in a PR, CodeRabbit will generate clear, structured commit messages aligned with conventional commit standards.

Refactoring Suggestions → It will propose cleaner and more efficient alternatives for complex or repetitive logic.

Faster Collaboration → By providing automated first-pass reviews, CodeRabbit will reduce the workload for human reviewers and accelerate the merge process.

Prompting Strategy

To maximize the value of AI during development, I will rely on structured, context-rich prompts. These prompts will include the goal, the context (e.g., schema, code snippet, or spec), and the expected output format.

Sample Prompts

For Code/Feature Generation

“Generate a FastAPI route for /tasks that supports GET (list tasks) and POST (create a new task). Use Pydantic models for request/response validation and include error handling for missing fields.”

For Testing Support

“Write unit tests in pytest for the create_task function. Cover normal cases, missing required fields, and invalid data types. Use mock data for the database layer.”


