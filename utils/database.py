"""
Database manager for Personal Weight Tracker with Supabase integration.
Handles all database operations for weight data and gym workouts.
"""
import os
import pandas as pd
from typing import Optional, List, Dict, Any
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Try to import supabase, but don't fail if not installed
try:
    from supabase import create_client, Client
    SUPABASE_AVAILABLE = True
except ImportError:
    SUPABASE_AVAILABLE = False
    Client = None


class SupabaseManager:
    """
    Manager class for Supabase database operations.
    Handles weight data and gym workout data storage and retrieval.
    """
    
    def __init__(self):
        """Initialize Supabase client with credentials from environment variables."""
        if not SUPABASE_AVAILABLE:
            raise ImportError(
                "Supabase package not installed. "
                "Install it with: pip install supabase"
            )
        
        self.url = os.getenv("SUPABASE_URL")
        self.key = os.getenv("SUPABASE_KEY")
        
        if not self.url or not self.key:
            raise ValueError(
                "Supabase credentials not found. "
                "Please set SUPABASE_URL and SUPABASE_KEY in your .env file"
            )
        
        self.client: Client = create_client(self.url, self.key)
        self.weight_table = "weight_data"
        self.gym_table = "gym_workouts"
    
    # ==================== Weight Data Operations ====================
    
    def insert_weight(self, date: datetime, weight: float, notes: str = None) -> Dict[str, Any]:
        """
        Insert a new weight entry.
        
        Args:
            date: Date of the weight measurement
            weight: Weight value in kg
            notes: Optional notes about the measurement
            
        Returns:
            Dictionary with the inserted data
            
        Raises:
            Exception: If insertion fails
        """
        try:
            data = {
                "date": date.isoformat(),
                "weight": float(weight),
                "notes": notes
            }
            
            response = self.client.table(self.weight_table).insert(data).execute()
            return response.data[0] if response.data else {}
        except Exception as e:
            raise Exception(f"Error inserting weight data: {str(e)}")
    
    def get_all_weights(self) -> pd.DataFrame:
        """
        Retrieve all weight entries.
        
        Returns:
            DataFrame with all weight data
        """
        try:
            response = self.client.table(self.weight_table)\
                .select("*")\
                .order("date", desc=False)\
                .execute()
            
            if response.data:
                df = pd.DataFrame(response.data)
                df['date'] = pd.to_datetime(df['date'])
                return df[['date', 'weight', 'notes']] if 'notes' in df.columns else df[['date', 'weight']]
            else:
                return pd.DataFrame(columns=['date', 'weight'])
        except Exception as e:
            raise Exception(f"Error retrieving weight data: {str(e)}")
    
    def update_weight(self, record_id: int, weight: float, notes: str = None) -> Dict[str, Any]:
        """
        Update an existing weight entry.
        
        Args:
            record_id: ID of the record to update
            weight: New weight value
            notes: Optional notes
            
        Returns:
            Dictionary with updated data
        """
        try:
            data = {"weight": float(weight)}
            if notes is not None:
                data["notes"] = notes
            data["updated_at"] = datetime.now().isoformat()
            
            response = self.client.table(self.weight_table)\
                .update(data)\
                .eq("id", record_id)\
                .execute()
            
            return response.data[0] if response.data else {}
        except Exception as e:
            raise Exception(f"Error updating weight data: {str(e)}")
    
    def delete_weight(self, date: datetime) -> bool:
        """
        Delete weight entries for a specific date.
        
        Args:
            date: Date of entries to delete
            
        Returns:
            True if deletion was successful
        """
        try:
            date_str = date.strftime("%Y-%m-%d")
            response = self.client.table(self.weight_table)\
                .delete()\
                .gte("date", f"{date_str}T00:00:00")\
                .lte("date", f"{date_str}T23:59:59")\
                .execute()
            
            return True
        except Exception as e:
            raise Exception(f"Error deleting weight data: {str(e)}")
    
    def get_weight_by_date_range(self, start_date: datetime, end_date: datetime) -> pd.DataFrame:
        """
        Get weight data within a date range.
        
        Args:
            start_date: Start date
            end_date: End date
            
        Returns:
            DataFrame with filtered weight data
        """
        try:
            response = self.client.table(self.weight_table)\
                .select("*")\
                .gte("date", start_date.isoformat())\
                .lte("date", end_date.isoformat())\
                .order("date", desc=False)\
                .execute()
            
            if response.data:
                df = pd.DataFrame(response.data)
                df['date'] = pd.to_datetime(df['date'])
                return df[['date', 'weight']]
            else:
                return pd.DataFrame(columns=['date', 'weight'])
        except Exception as e:
            raise Exception(f"Error retrieving weight data by date range: {str(e)}")
    
    # ==================== Gym Workout Operations ====================
    
    def insert_workout(self, date: datetime, exercise: str, weight: float, 
                      reps: int, sets: int = 1) -> Dict[str, Any]:
        """
        Insert a gym workout entry.
        
        Args:
            date: Date of workout
            exercise: Exercise name
            weight: Weight used
            reps: Number of repetitions
            sets: Number of sets (default: 1)
            
        Returns:
            Dictionary with inserted data
        """
        try:
            data = {
                "date": date.date().isoformat(),
                "exercise": exercise,
                "weight": float(weight),
                "reps": int(reps),
                "sets": int(sets)
            }
            
            response = self.client.table(self.gym_table).insert(data).execute()
            return response.data[0] if response.data else {}
        except Exception as e:
            raise Exception(f"Error inserting workout data: {str(e)}")
    
    def get_all_workouts(self) -> pd.DataFrame:
        """
        Retrieve all gym workout entries.
        
        Returns:
            DataFrame with all workout data
        """
        try:
            response = self.client.table(self.gym_table)\
                .select("*")\
                .order("date", desc=False)\
                .execute()
            
            if response.data:
                df = pd.DataFrame(response.data)
                df['date'] = pd.to_datetime(df['date'])
                return df
            else:
                return pd.DataFrame(columns=['date', 'exercise', 'weight', 'reps', 'sets'])
        except Exception as e:
            raise Exception(f"Error retrieving workout data: {str(e)}")
    
    # ==================== Migration Operations ====================
    
    def migrate_csv_to_supabase(self, csv_path: str, table_type: str = "weight") -> Dict[str, int]:
        """
        Migrate data from CSV file to Supabase.
        
        Args:
            csv_path: Path to CSV file
            table_type: Type of data ("weight" or "gym")
            
        Returns:
            Dictionary with migration statistics
        """
        try:
            df = pd.read_csv(csv_path)
            success_count = 0
            error_count = 0
            
            if table_type == "weight":
                for _, row in df.iterrows():
                    try:
                        date = pd.to_datetime(row['date'])
                        weight = float(row['weight'])
                        self.insert_weight(date, weight)
                        success_count += 1
                    except Exception as e:
                        error_count += 1
                        print(f"Error migrating row: {e}")
            
            elif table_type == "gym":
                for _, row in df.iterrows():
                    try:
                        date = pd.to_datetime(row['Date'])
                        self.insert_workout(
                            date=date,
                            exercise=row['Exercise'],
                            weight=float(row['Weight']),
                            reps=int(row['Reps']),
                            sets=1
                        )
                        success_count += 1
                    except Exception as e:
                        error_count += 1
                        print(f"Error migrating row: {e}")
            
            return {
                "success": success_count,
                "errors": error_count,
                "total": len(df)
            }
        except Exception as e:
            raise Exception(f"Error during migration: {str(e)}")
    
    def export_to_csv(self, output_path: str, table_type: str = "weight") -> bool:
        """
        Export Supabase data to CSV file.
        
        Args:
            output_path: Path where CSV will be saved
            table_type: Type of data to export ("weight" or "gym")
            
        Returns:
            True if export was successful
        """
        try:
            if table_type == "weight":
                df = self.get_all_weights()
            elif table_type == "gym":
                df = self.get_all_workouts()
            else:
                raise ValueError(f"Unknown table type: {table_type}")
            
            df.to_csv(output_path, index=False)
            return True
        except Exception as e:
            raise Exception(f"Error exporting to CSV: {str(e)}")


def get_database_manager() -> Optional[SupabaseManager]:
    """
    Get database manager instance if Supabase is enabled.
    
    Returns:
        SupabaseManager instance or None if not enabled/configured
    """
    use_supabase = os.getenv("USE_SUPABASE", "False").lower() == "true"
    
    if not use_supabase:
        return None
    
    if not SUPABASE_AVAILABLE:
        print("Warning: Supabase package not installed")
        return None
    
    try:
        return SupabaseManager()
    except Exception as e:
        print(f"Warning: Could not initialize Supabase: {e}")
        return None

# Made with Bob
