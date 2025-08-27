#!/bin/bash

# Charger les variables d'environnement
if [ -f .env ]; then
    export $(grep -v '^#' .env | xargs)
fi

echo "🧹 Cleaning data from database..."

# Nettoyer les données tout en gardant la structure
psql -h localhost -U $DB_USER -d $DB_NAME << 'EOF'
-- Désactiver temporairement les contraintes de clés étrangères
SET session_replication_role = replica;

-- Vider les tables (en gardant la structure)
TRUNCATE TABLE user_subscriptions RESTART IDENTITY CASCADE;
TRUNCATE TABLE attempts RESTART IDENTITY CASCADE;
TRUNCATE TABLE answers RESTART IDENTITY CASCADE;
TRUNCATE TABLE questions RESTART IDENTITY CASCADE;
TRUNCATE TABLE sub_themes RESTART IDENTITY CASCADE;
TRUNCATE TABLE sub_categories RESTART IDENTITY CASCADE;
TRUNCATE TABLE categories RESTART IDENTITY CASCADE;
TRUNCATE TABLE user_settings RESTART IDENTITY CASCADE;
TRUNCATE TABLE streaks RESTART IDENTITY CASCADE;
TRUNCATE TABLE progress RESTART IDENTITY CASCADE;

-- Garder les users si tu veux, ou les vider aussi :
-- TRUNCATE TABLE users RESTART IDENTITY CASCADE;

-- Réactiver les contraintes
SET session_replication_role = DEFAULT;

-- Vérifier que c'est vide
SELECT 
    table_name as "Table",
    0 as "Rows (should be 0)"
FROM information_schema.tables 
WHERE table_schema = 'public' 
AND table_type = 'BASE TABLE'
AND table_name NOT IN ('alembic_version')
ORDER BY table_name;
EOF

echo "✅ Data cleaned! Structure preserved."
