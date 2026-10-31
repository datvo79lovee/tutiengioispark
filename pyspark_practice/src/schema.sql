
CREATE DATABASE IF NOT EXISTS github_data;
USE github_data;

-- 1. Users
CREATE TABLE IF NOT EXISTS github_users (
    id BIGINT PRIMARY KEY,
    login VARCHAR(255),
    gravatar_id VARCHAR(255),
    avatar_url TEXT,
    api_url TEXT,
    html_url TEXT,
    user_type VARCHAR(50),
    site_admin BOOLEAN
);

-- 2. Organizations
CREATE TABLE IF NOT EXISTS github_organizations (
    id BIGINT PRIMARY KEY,
    login VARCHAR(255),
    gravatar_id VARCHAR(255),
    avatar_url TEXT,
    api_url TEXT
);

-- 3. Repositories
CREATE TABLE IF NOT EXISTS github_repositories (
    id BIGINT PRIMARY KEY,
    name VARCHAR(255),
    full_name VARCHAR(512),
    owner_id BIGINT,
    owner_type VARCHAR(50),
    description TEXT,
    api_url TEXT,
    html_url TEXT,
    clone_url TEXT,
    language VARCHAR(100),
    is_fork BOOLEAN,
    is_private BOOLEAN,
    is_public BOOLEAN,
    default_branch VARCHAR(255),
    repo_size INT,
    stargazers_count INT,
    watchers_count INT,
    forks_count INT,
    open_issues_count INT,
    created_at DATETIME,
    updated_at DATETIME,
    pushed_at DATETIME
);

-- 4. Events
CREATE TABLE IF NOT EXISTS github_events (
    id BIGINT PRIMARY KEY,
    event_type VARCHAR(100),
    actor_id BIGINT,
    repo_id BIGINT,
    org_id BIGINT,
    is_public BOOLEAN,
    created_at DATETIME,

    FOREIGN KEY (actor_id)
        REFERENCES github_users(id),

    FOREIGN KEY (repo_id)
        REFERENCES github_repositories(id),

    FOREIGN KEY (org_id)
        REFERENCES github_organizations(id)
);

-- 5. Fork Events
CREATE TABLE IF NOT EXISTS github_fork_events (
    event_id BIGINT PRIMARY KEY,
    forkee_id BIGINT NOT NULL,

    FOREIGN KEY (event_id)
        REFERENCES github_events(id),

    FOREIGN KEY (forkee_id)
        REFERENCES github_repositories(id)
);
