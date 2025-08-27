#!/bin/bash

# Charger les variables d'environnement
if [ -f .env ]; then
    export $(grep -v '^#' .env | xargs)
fi

DB_TEST_NAME="leitmind_test"
echo "🧪 Resetting test database..."

# Drop et recréer la DB de test
echo "🗑️  Dropping and recreating test database..."
psql -h localhost -U $DB_USER -d postgres << EOF
DROP DATABASE IF EXISTS $DB_TEST_NAME;
CREATE DATABASE $DB_TEST_NAME;
EOF

# Appliquer les migrations
echo "📦 Applying migrations..."
export POSTGRES_DB_URL="postgresql://$DB_USER@localhost/$DB_TEST_NAME"
cd backend/ && poetry run alembic upgrade head

# Insérer des données de test
echo "🌱 Seeding test data..."
cd .. && python scripts/seed_test_data.py

echo "✅ Test database ready!"
