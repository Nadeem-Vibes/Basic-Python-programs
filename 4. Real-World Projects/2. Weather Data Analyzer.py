"""
Real-World Project 2: Weather Data Analyzer
============================================

A comprehensive weather data analysis application that demonstrates:
- API integration (simulated with sample data)
- Data processing and statistics
- Visualization concepts
- Working with CSV files
- Command-line arguments
- Logging

Features:
1. Load weather data from CSV
2. Calculate statistics (avg, min, max, trends)
3. Filter data by date range
4. Generate reports
5. Export analysis results

Note: This uses simulated weather data. In production, you would
connect to a real weather API like OpenWeatherMap or WeatherAPI.
"""

import csv
import logging
from datetime import datetime, timedelta
from pathlib import Path
from typing import List, Dict, Optional
from dataclasses import dataclass
import statistics

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


@dataclass
class WeatherData:
    """Represents a single weather reading"""
    date: str
    temperature_high: float
    temperature_low: float
    humidity: int
    precipitation: float
    wind_speed: float
    condition: str
    
    @property
    def temperature_avg(self) -> float:
        return (self.temperature_high + self.temperature_low) / 2
    
    def to_dict(self) -> Dict:
        return {
            'date': self.date,
            'temp_high': self.temperature_high,
            'temp_low': self.temperature_low,
            'temp_avg': self.temperature_avg,
            'humidity': self.humidity,
            'precipitation': self.precipitation,
            'wind_speed': self.wind_speed,
            'condition': self.condition
        }


class WeatherAnalyzer:
    """Main weather analysis application"""
    
    def __init__(self):
        self.data: List[WeatherData] = []
        self.location = "Unknown"
    
    def load_from_csv(self, filepath: str) -> bool:
        """Load weather data from CSV file"""
        try:
            path = Path(filepath)
            if not path.exists():
                logger.warning(f"File not found: {filepath}")
                return False
            
            with open(path, 'r') as f:
                reader = csv.DictReader(f)
                self.data = []
                for row in reader:
                    weather = WeatherData(
                        date=row['date'],
                        temperature_high=float(row['temp_high']),
                        temperature_low=float(row['temp_low']),
                        humidity=int(row['humidity']),
                        precipitation=float(row['precipitation']),
                        wind_speed=float(row['wind_speed']),
                        condition=row['condition']
                    )
                    self.data.append(weather)
            
            self.location = path.stem.replace('_', ' ').title()
            logger.info(f"Loaded {len(self.data)} records from {filepath}")
            return True
            
        except Exception as e:
            logger.error(f"Error loading CSV: {e}")
            return False
    
    def generate_sample_data(self, days: int = 30) -> None:
        """Generate sample weather data for demonstration"""
        logger.info(f"Generating {days} days of sample data...")
        
        conditions = ['Sunny', 'Cloudy', 'Rainy', 'Partly Cloudy', 'Stormy']
        base_date = datetime.now()
        
        self.data = []
        for i in range(days):
            date = (base_date - timedelta(days=days-i)).strftime("%Y-%m-%d")
            
            # Simulate realistic weather patterns
            import random
            temp_high = round(random.uniform(15, 35), 1)
            temp_low = round(temp_high - random.uniform(5, 15), 1)
            humidity = random.randint(30, 95)
            precipitation = round(random.uniform(0, 50), 1) if random.random() < 0.3 else 0
            wind_speed = round(random.uniform(0, 30), 1)
            condition = random.choice(conditions)
            
            weather = WeatherData(
                date=date,
                temperature_high=temp_high,
                temperature_low=temp_low,
                humidity=humidity,
                precipitation=precipitation,
                wind_speed=wind_speed,
                condition=condition
            )
            self.data.append(weather)
        
        self.location = "Sample City"
        logger.info(f"Generated {len(self.data)} sample records")
    
    def get_statistics(self) -> Dict:
        """Calculate comprehensive statistics"""
        if not self.data:
            return {}
        
        temps_high = [d.temperature_high for d in self.data]
        temps_low = [d.temperature_low for d in self.data]
        temps_avg = [d.temperature_avg for d in self.data]
        humidities = [d.humidity for d in self.data]
        precipitations = [d.precipitation for d in self.data]
        wind_speeds = [d.wind_speed for d in self.data]
        
        # Count conditions
        conditions_count = {}
        for d in self.data:
            conditions_count[d.condition] = conditions_count.get(d.condition, 0) + 1
        
        # Rainy days
        rainy_days = sum(1 for d in self.data if d.precipitation > 0)
        
        stats = {
            'location': self.location,
            'total_days': len(self.data),
            'date_range': {
                'start': self.data[0].date,
                'end': self.data[-1].date
            },
            'temperature': {
                'high': {
                    'max': max(temps_high),
                    'min': min(temps_high),
                    'avg': round(statistics.mean(temps_high), 2),
                    'median': round(statistics.median(temps_high), 2)
                },
                'low': {
                    'max': max(temps_low),
                    'min': min(temps_low),
                    'avg': round(statistics.mean(temps_low), 2),
                    'median': round(statistics.median(temps_low), 2)
                },
                'average': {
                    'overall': round(statistics.mean(temps_avg), 2),
                    'std_dev': round(statistics.stdev(temps_avg), 2) if len(temps_avg) > 1 else 0
                }
            },
            'humidity': {
                'avg': round(statistics.mean(humidities), 2),
                'max': max(humidities),
                'min': min(humidities)
            },
            'precipitation': {
                'total': round(sum(precipitations), 2),
                'avg': round(statistics.mean(precipitations), 2),
                'rainy_days': rainy_days,
                'dry_days': len(self.data) - rainy_days
            },
            'wind': {
                'avg': round(statistics.mean(wind_speeds), 2),
                'max': max(wind_speeds)
            },
            'conditions': conditions_count
        }
        
        return stats
    
    def filter_by_date_range(self, start_date: str, end_date: str) -> List[WeatherData]:
        """Filter data by date range"""
        try:
            start = datetime.strptime(start_date, "%Y-%m-%d")
            end = datetime.strptime(end_date, "%Y-%m-%d")
            
            filtered = [
                d for d in self.data
                if start <= datetime.strptime(d.date, "%Y-%m-%d") <= end
            ]
            
            logger.info(f"Filtered to {len(filtered)} records")
            return filtered
            
        except Exception as e:
            logger.error(f"Error filtering dates: {e}")
            return []
    
    def find_extremes(self) -> Dict:
        """Find extreme weather days"""
        if not self.data:
            return {}
        
        hottest = max(self.data, key=lambda x: x.temperature_high)
        coldest = min(self.data, key=lambda x: x.temperature_low)
        wettest = max(self.data, key=lambda x: x.precipitation)
        windiest = max(self.data, key=lambda x: x.wind_speed)
        most_humid = max(self.data, key=lambda x: x.humidity)
        
        return {
            'hottest_day': hottest.to_dict(),
            'coldest_day': coldest.to_dict(),
            'wettest_day': wettest.to_dict(),
            'windiest_day': windiest.to_dict(),
            'most_humid_day': most_humid.to_dict()
        }
    
    def get_trend_analysis(self) -> Dict:
        """Analyze weather trends"""
        if len(self.data) < 7:
            return {'message': 'Not enough data for trend analysis'}
        
        # Compare first half vs second half
        mid = len(self.data) // 2
        first_half = self.data[:mid]
        second_half = self.data[mid:]
        
        first_avg_temp = statistics.mean([d.temperature_avg for d in first_half])
        second_avg_temp = statistics.mean([d.temperature_avg for d in second_half])
        
        first_avg_precip = statistics.mean([d.precipitation for d in first_half])
        second_avg_precip = statistics.mean([d.precipitation for d in second_half])
        
        temp_trend = "warming" if second_avg_temp > first_avg_temp else "cooling"
        precip_trend = "increasing" if second_avg_precip > first_avg_precip else "decreasing"
        
        return {
            'temperature_trend': temp_trend,
            'temp_change': round(second_avg_temp - first_avg_temp, 2),
            'precipitation_trend': precip_trend,
            'precip_change': round(second_avg_precip - first_avg_precip, 2),
            'first_half_avg_temp': round(first_avg_temp, 2),
            'second_half_avg_temp': round(second_avg_temp, 2)
        }
    
    def export_to_csv(self, filepath: str) -> bool:
        """Export analysis results to CSV"""
        try:
            with open(filepath, 'w', newline='') as f:
                writer = csv.DictWriter(f, fieldnames=[
                    'date', 'temp_high', 'temp_low', 'temp_avg', 
                    'humidity', 'precipitation', 'wind_speed', 'condition'
                ])
                writer.writeheader()
                for weather in self.data:
                    writer.writerow(weather.to_dict())
            
            logger.info(f"Exported data to {filepath}")
            return True
            
        except Exception as e:
            logger.error(f"Error exporting CSV: {e}")
            return False
    
    def print_report(self) -> None:
        """Print formatted weather report"""
        stats = self.get_statistics()
        extremes = self.find_extremes()
        trends = self.get_trend_analysis()
        
        print("\n" + "=" * 60)
        print(f"WEATHER ANALYSIS REPORT - {stats.get('location', 'Unknown')}")
        print("=" * 60)
        
        print(f"\n📅 Period: {stats['date_range']['start']} to {stats['date_range']['end']}")
        print(f"📊 Total Days Analyzed: {stats['total_days']}")
        
        print("\n🌡️  TEMPERATURE SUMMARY")
        print(f"   Highest: {stats['temperature']['high']['max']}°C")
        print(f"   Lowest: {stats['temperature']['low']['min']}°C")
        print(f"   Average High: {stats['temperature']['high']['avg']}°C")
        print(f"   Average Low: {stats['temperature']['low']['avg']}°C")
        print(f"   Overall Average: {stats['temperature']['average']['overall']}°C")
        
        print("\n💧 PRECIPITATION")
        print(f"   Total: {stats['precipitation']['total']} mm")
        print(f"   Rainy Days: {stats['precipitation']['rainy_days']}")
        print(f"   Dry Days: {stats['precipitation']['dry_days']}")
        
        print("\n💨 WIND")
        print(f"   Average Speed: {stats['wind']['avg']} km/h")
        print(f"   Maximum Speed: {stats['wind']['max']} km/h")
        
        print("\n💧 HUMIDITY")
        print(f"   Average: {stats['humidity']['avg']}%")
        print(f"   Range: {stats['humidity']['min']}% - {stats['humidity']['max']}%")
        
        print("\n☁️  WEATHER CONDITIONS")
        for condition, count in sorted(stats['conditions'].items(), key=lambda x: -x[1]):
            percentage = count / stats['total_days'] * 100
            print(f"   {condition}: {count} days ({percentage:.1f}%)")
        
        print("\n📈 EXTREME DAYS")
        print(f"   Hottest: {extremes['hottest_day']['date']} ({extremes['hottest_day']['temp_high']}°C)")
        print(f"   Coldest: {extremes['coldest_day']['date']} ({extremes['coldest_day']['temp_low']}°C)")
        print(f"   Wettest: {extremes['wettest_day']['date']} ({extremes['wettest_day']['precipitation']} mm)")
        
        if 'message' not in trends:
            print("\n📊 TRENDS")
            print(f"   Temperature: {trends['temperature_trend']} ({trends['temp_change']:+.2f}°C)")
            print(f"   Precipitation: {trends['precipitation_trend']} ({trends['precip_change']:+.2f} mm)")


def create_sample_csv(filepath: str = "sample_weather.csv") -> None:
    """Create a sample CSV file for testing"""
    analyzer = WeatherAnalyzer()
    analyzer.generate_sample_data(60)
    analyzer.export_to_csv(filepath)
    print(f"✓ Created sample data file: {filepath}")


def print_menu():
    """Display main menu"""
    print("\n" + "=" * 60)
    print("WEATHER DATA ANALYZER")
    print("=" * 60)
    print("1. Generate Sample Data")
    print("2. Load Data from CSV")
    print("3. View Statistics Report")
    print("4. Find Extreme Weather Days")
    print("5. Analyze Trends")
    print("6. Filter by Date Range")
    print("7. Export Data to CSV")
    print("8. Exit")
    print("=" * 60)


def main():
    """Main application loop"""
    analyzer = WeatherAnalyzer()
    
    while True:
        print_menu()
        choice = input("\nEnter your choice (1-8): ").strip()
        
        if choice == '1':  # Generate Sample Data
            days = int(input("Number of days (default 30): ") or "30")
            analyzer.generate_sample_data(days)
            print(f"✓ Generated {days} days of weather data")
        
        elif choice == '2':  # Load from CSV
            filepath = input("CSV filename: ").strip()
            if analyzer.load_from_csv(filepath):
                print(f"✓ Loaded data from {filepath}")
            else:
                print("✗ Failed to load data")
        
        elif choice == '3':  # View Report
            if analyzer.data:
                analyzer.print_report()
            else:
                print("No data loaded! Generate or load data first.")
        
        elif choice == '4':  # Extreme Days
            if analyzer.data:
                extremes = analyzer.find_extremes()
                print("\n📈 EXTREME WEATHER DAYS")
                print(f"   Hottest: {extremes['hottest_day']['date']} ({extremes['hottest_day']['temp_high']}°C)")
                print(f"   Coldest: {extremes['coldest_day']['date']} ({extremes['coldest_day']['temp_low']}°C)")
                print(f"   Wettest: {extremes['wettest_day']['date']} ({extremes['wettest_day']['precipitation']} mm)")
                print(f"   Windiest: {extremes['windiest_day']['date']} ({extremes['windiest_day']['wind_speed']} km/h)")
            else:
                print("No data loaded!")
        
        elif choice == '5':  # Trend Analysis
            if analyzer.data:
                trends = analyzer.get_trend_analysis()
                if 'message' in trends:
                    print(trends['message'])
                else:
                    print("\n📊 TREND ANALYSIS")
                    print(f"   Temperature Trend: {trends['temperature_trend']} ({trends['temp_change']:+.2f}°C)")
                    print(f"   Precipitation Trend: {trends['precipitation_trend']} ({trends['precip_change']:+.2f} mm)")
            else:
                print("No data loaded!")
        
        elif choice == '6':  # Filter by Date
            if analyzer.data:
                start = input("Start date (YYYY-MM-DD): ").strip()
                end = input("End date (YYYY-MM-DD): ").strip()
                filtered = analyzer.filter_by_date_range(start, end)
                if filtered:
                    print(f"\n✓ Found {len(filtered)} records in range")
                    for w in filtered[:5]:  # Show first 5
                        print(f"   {w.date}: {w.temperature_low}-{w.temperature_high}°C, {w.condition}")
                else:
                    print("No records found in that range!")
            else:
                print("No data loaded!")
        
        elif choice == '7':  # Export
            if analyzer.data:
                filepath = input("Export filename: ").strip() or "export_weather.csv"
                if analyzer.export_to_csv(filepath):
                    print(f"✓ Exported to {filepath}")
            else:
                print("No data to export!")
        
        elif choice == '8':  # Exit
            print("\nThank you for using Weather Data Analyzer!")
            break
        
        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()

"""
HOW TO USE THIS PROJECT:
========================

1. Run the script: python "4. Real-World Projects/2. Weather Data Analyzer.py"

2. The app will:
   - Let you generate sample weather data
   - Load data from CSV files
   - Calculate comprehensive statistics
   - Identify extreme weather days
   - Analyze trends over time
   - Export results

3. Skills demonstrated:
   ✓ CSV file handling
   ✓ Data classes
   ✓ Statistics calculations
   ✓ Date/time operations
   ✓ Logging
   ✓ Type hints
   ✓ Error handling
   ✓ Data visualization concepts

EXTENSION IDEAS:
================
- Connect to real weather API (OpenWeatherMap, WeatherAPI)
- Add data visualization with matplotlib
- Create interactive dashboard
- Add forecasting capabilities
- Support multiple locations
- Add database storage
"""
