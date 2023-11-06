import psutil
import os

# Function to get system statistics
def get_system_stats():
    stats = {
        'cpu_percentage': psutil.cpu_percent(interval=1),
        'memory_percentage': psutil.virtual_memory().percent,
        'disk_usage': psutil.disk_usage('/').percent
    }
    return stats

# Function to check system health
def check_system_health():
    stats = get_system_stats()

    print(f"CPU Usage: {stats['cpu_percentage']}%")
    print(f"Memory Usage: {stats['memory_percentage']}%")
    print(f"Disk Usage: {stats['disk_usage']}%")

    # You can add more logic to send alerts if any of the stats are above a certain threshold
    # e.g., if stats['cpu_percentage'] > 80: alert()

# Main execution
if __name__ == "__main__":
    check_system_health()
