import pymongo
from datetime import datetime, timedelta
import random
import time
from faker import Faker
import json


class MongoDataGenerator:
    def __init__(self, connection_string):
        self.client = pymongo.MongoClient(connection_string)
        self.db = self.client['atlas_charts_poc']
        self.fake = Faker()

    def generate_sales_data(self, num_records=1000):
        """Generate realistic sales data for visualization"""
        sales_collection = self.db['sales_data']

        # Clear existing data
        sales_collection.delete_many({})

        products = [
            {'name': 'Laptop Pro', 'category': 'Electronics', 'base_price': 1200},
            {'name': 'Smartphone X', 'category': 'Electronics', 'base_price': 800},
            {'name': 'Wireless Headphones', 'category': 'Electronics', 'base_price': 150},
            {'name': 'Coffee Maker', 'category': 'Appliances', 'base_price': 80},
            {'name': 'Desk Chair', 'category': 'Furniture', 'base_price': 200},
            {'name': 'Running Shoes', 'category': 'Sports', 'base_price': 120},
            {'name': 'Backpack', 'category': 'Accessories', 'base_price': 60},
            {'name': 'Tablet', 'category': 'Electronics', 'base_price': 300},
            {'name': 'Bluetooth Speaker', 'category': 'Electronics', 'base_price': 50},
            {'name': 'Fitness Tracker', 'category': 'Sports', 'base_price': 180}
        ]

        regions = ['North America', 'Europe', 'Asia Pacific', 'Latin America', 'Middle East & Africa']
        sales_reps = ['Alice Johnson', 'Bob Smith', 'Carol Davis', 'David Wilson', 'Eva Martinez', 'Frank Chen']

        sales_records = []
        start_date = datetime.now() - timedelta(days=90)

        for i in range(num_records):
            product = random.choice(products)
            sale_date = start_date + timedelta(days=random.randint(0, 90))

            # Add some seasonality - higher sales in recent weeks
            days_from_start = (sale_date - start_date).days
            seasonal_multiplier = 1 + (days_from_start / 90) * 0.5

            quantity = random.randint(1, 10)
            unit_price = product['base_price'] * random.uniform(0.8, 1.2)  # Price variation
            total_amount = unit_price * quantity * seasonal_multiplier

            record = {
                'sale_id': f'SALE_{i + 1:06d}',
                'product_name': product['name'],
                'category': product['category'],
                'quantity': quantity,
                'unit_price': round(unit_price, 2),
                'total_amount': round(total_amount, 2),
                'sale_date': sale_date,
                'region': random.choice(regions),
                'sales_rep': random.choice(sales_reps),
                'customer_type': random.choice(['Enterprise', 'SMB', 'Individual']),
                'payment_method': random.choice(['Credit Card', 'Bank Transfer', 'PayPal', 'Cash']),
                'discount_percent': random.choice([0, 5, 10, 15, 20]),
                'created_at': datetime.now()
            }

            sales_records.append(record)

        # Insert records in batches
        batch_size = 100
        for i in range(0, len(sales_records), batch_size):
            batch = sales_records[i:i + batch_size]
            sales_collection.insert_many(batch)
            print(f"Inserted batch {i // batch_size + 1}/{(len(sales_records) // batch_size) + 1}")

        print(f"✅ Generated {len(sales_records)} sales records")
        return sales_collection

    def generate_user_activity_data(self, num_records=500):
        """Generate user activity data for web analytics"""
        activity_collection = self.db['user_activity']

        # Clear existing data
        activity_collection.delete_many({})

        pages = ['/home', '/products', '/about', '/contact', '/checkout', '/profile', '/search', '/blog']
        devices = ['Desktop', 'Mobile', 'Tablet']
        browsers = ['Chrome', 'Firefox', 'Safari', 'Edge']
        countries = ['USA', 'Canada', 'UK', 'Germany', 'France', 'Japan', 'Australia', 'Brazil']

        activity_records = []
        start_date = datetime.now() - timedelta(days=30)

        for i in range(num_records):
            session_start = start_date + timedelta(days=random.randint(0, 30),
                                                   hours=random.randint(0, 23),
                                                   minutes=random.randint(0, 59))

            record = {
                'session_id': f'SESSION_{i + 1:06d}',
                'user_id': f'USER_{random.randint(1, 100):04d}',
                'page_visited': random.choice(pages),
                'device_type': random.choice(devices),
                'browser': random.choice(browsers),
                'country': random.choice(countries),
                'session_duration': random.randint(30, 1800),  # 30 seconds to 30 minutes
                'page_views': random.randint(1, 20),
                'bounce_rate': random.choice([True, False]),
                'conversion': random.choice([True, False]) if random.random() < 0.1 else False,
                'timestamp': session_start,
                'created_at': datetime.now()
            }

            activity_records.append(record)

        activity_collection.insert_many(activity_records)
        print(f"✅ Generated {len(activity_records)} user activity records")
        return activity_collection

    def generate_realtime_data(self, duration_minutes=5):
        """Generate real-time data for live chart updates"""
        realtime_collection = self.db['realtime_metrics']

        print(f"🔄 Generating real-time data for {duration_minutes} minutes...")
        print("This will continuously add new data points. Press Ctrl+C to stop.")

        metrics = ['CPU Usage', 'Memory Usage', 'Network Traffic', 'Disk I/O', 'Response Time']
        servers = ['Server-01', 'Server-02', 'Server-03', 'Server-04', 'Server-05']

        end_time = datetime.now() + timedelta(minutes=duration_minutes)

        try:
            while datetime.now() < end_time:
                batch = []
                for server in servers:
                    for metric in metrics:
                        # Generate realistic values based on metric type
                        if metric == 'CPU Usage':
                            value = random.uniform(10, 90)
                        elif metric == 'Memory Usage':
                            value = random.uniform(20, 85)
                        elif metric == 'Network Traffic':
                            value = random.uniform(1, 100)
                        elif metric == 'Disk I/O':
                            value = random.uniform(0, 50)
                        else:  # Response Time
                            value = random.uniform(50, 500)

                        record = {
                            'timestamp': datetime.now(),
                            'server': server,
                            'metric': metric,
                            'value': round(value, 2),
                            'status': 'normal' if value < 80 else 'warning' if value < 95 else 'critical'
                        }
                        batch.append(record)

                realtime_collection.insert_many(batch)
                print(f"📊 Added {len(batch)} real-time data points at {datetime.now().strftime('%H:%M:%S')}")
                time.sleep(10)  # Add data every 10 seconds

        except KeyboardInterrupt:
            print("\n🛑 Real-time data generation stopped.")

    def create_indexes(self):
        """Create indexes for better chart performance"""
        print("📈 Creating indexes for optimal chart performance...")

        # Sales data indexes
        self.db.sales_data.create_index([('sale_date', 1)])
        self.db.sales_data.create_index([('category', 1)])
        self.db.sales_data.create_index([('region', 1)])
        self.db.sales_data.create_index([('sales_rep', 1)])

        # User activity indexes
        self.db.user_activity.create_index([('timestamp', 1)])
        self.db.user_activity.create_index([('device_type', 1)])
        self.db.user_activity.create_index([('country', 1)])

        # Real-time metrics indexes
        self.db.realtime_metrics.create_index([('timestamp', 1)])
        self.db.realtime_metrics.create_index([('server', 1)])
        self.db.realtime_metrics.create_index([('metric', 1)])

        print("✅ Indexes created successfully")

    def show_data_summary(self):
        """Display summary of generated data"""
        print("\n📊 DATA SUMMARY:")
        print("=" * 50)

        collections = ['sales_data', 'user_activity', 'realtime_metrics']
        for collection_name in collections:
            collection = self.db[collection_name]
            count = collection.count_documents({})
            if count > 0:
                latest = collection.find_one(sort=[('created_at', -1)])
                print(f"{collection_name}: {count} documents")
                if latest:
                    print(f"  Latest entry: {latest.get('created_at', 'N/A')}")

        print("\n🎯 Ready for Atlas Charts visualization!")
        print("Next steps:")
        print("1. Go to MongoDB Atlas Dashboard")
        print("2. Navigate to Charts section")
        print("3. Create charts using the 'atlas_charts_poc' database")
        print("4. Use collections: sales_data, user_activity, realtime_metrics")


def main():
    CONNECTION_STRING = "mongodb+srv://mongoadmin:<password>@pocs.wktu1.mongodb.net/"

    try:
        generator = MongoDataGenerator(CONNECTION_STRING)

        print("🚀 Starting MongoDB Atlas Charts POC Data Generation")
        print("=" * 60)

        # Test connection
        generator.client.admin.command('ping')
        print("✅ Connected to MongoDB Atlas successfully!")

        # Generate different types of data
        print("\n1. Generating sales data...")
        generator.generate_sales_data(1000)

        print("\n2. Generating user activity data...")
        generator.generate_user_activity_data(500)

        print("\n3. Creating performance indexes...")
        generator.create_indexes()

        print("\n4. Data generation complete!")
        generator.show_data_summary()

        # Ask user if they want to generate real-time data
        print("\n" + "=" * 60)
        choice = input("Would you like to generate real-time data for live charts? (y/n): ").lower()

        if choice == 'y':
            duration = input("Enter duration in minutes (default 5): ").strip()
            duration = int(duration) if duration.isdigit() else 5
            generator.generate_realtime_data(duration)
            generator.show_data_summary()

    except Exception as e:
        print(f"❌ Error: {str(e)}")
        print("Please check your connection string and internet connection.")


if __name__ == "__main__":
    main()