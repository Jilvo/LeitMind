#!/bin/bash

# Charger les variables d'environnement depuis le fichier .env
if [ -f .env ]; then
    export $(grep -v '^#' .env | xargs)
else
    echo "❌ Fichier .env non trouvé !"
    exit 1
fi

# Vérifier que les variables nécessaires sont définies
if [ -z "$DB_NAME" ] || [ -z "$DB_USER" ]; then
    echo "❌ Variables DB_NAME et DB_USER doivent être définies dans .env"
    exit 1
fi

echo "🚀 Quick database reset..."
echo "📋 Database: $DB_NAME"
echo "👤 User: $DB_USER"

# Drop database
echo "Dropping database..."
psql -h localhost -U $DB_USER -d postgres -c "DROP DATABASE IF EXISTS $DB_NAME;"

# Create database
echo "Creating database..."
psql -h localhost -U $DB_USER -d postgres -c "CREATE DATABASE $DB_NAME;"

# Apply migrations
echo "Applying migrations..."
cd backend/ && poetry run alembic upgrade head

echo "✅ Done!"