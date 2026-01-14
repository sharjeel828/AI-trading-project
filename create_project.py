import os
import sys

def create_project(project_name):
    if os.path.exists(project_name):
        print(f"Error: Directory '{project_name}' already exists.")
        return

    os.makedirs(project_name)
    os.makedirs(os.path.join(project_name, 'storage'))
    os.makedirs(os.path.join(project_name, 'storage', 'logs'))
    os.makedirs(os.path.join(project_name, 'storage', 'db'))
    os.makedirs(os.path.join(project_name, 'strategies'))

    # Create ExampleStrategy
    strategy_dir = os.path.join(project_name, 'strategies', 'ExampleStrategy')
    os.makedirs(strategy_dir)
    with open(os.path.join(strategy_dir, '__init__.py'), 'w') as f:
        f.write("from jesse.strategies import Strategy, cached\n\n")
        f.write("class ExampleStrategy(Strategy):\n")
        f.write("    def should_long(self) -> bool:\n")
        f.write("        return False\n\n")
        f.write("    def should_short(self) -> bool:\n")
        f.write("        return False\n\n")
        f.write("    def go_long(self):\n")
        f.write("        pass\n\n")
        f.write("    def go_short(self):\n")
        f.write("        pass\n\n")
        f.write("    def update_position(self):\n")
        f.write("        pass\n")

    # Create .env file
    env_content = """# DATABASE
POSTGRES_NAME=jesse_db
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_USERNAME=jesse_user
POSTGRES_PASSWORD=password
POSTGRES_SSLMODE=disable

# REDIS
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_PASSWORD=

# APP
# The path to the project directory
# 
APP_PORT=9000
APP_HOST=0.0.0.0
PASSWORD=password
"""
    with open(os.path.join(project_name, '.env'), 'w') as f:
        f.write(env_content)

    print(f"Project '{project_name}' created successfully.")
    print(f"cd {project_name}")
    print("jesse run")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python create_project.py <project_name>")
    else:
        create_project(sys.argv[1])
