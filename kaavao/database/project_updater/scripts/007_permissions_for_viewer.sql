GRANT USAGE ON SCHEMA SCHEMANAME TO kaavao_viewer;
GRANT SELECT ON ALL TABLES IN SCHEMA SCHEMANAME TO kaavao_viewer;
ALTER DEFAULT PRIVILEGES IN SCHEMA SCHEMANAME
    GRANT SELECT ON TABLES TO kaavao_viewer;
