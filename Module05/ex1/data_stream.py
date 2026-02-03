from abc import ABC, abstractmethod
from typing import Any, List, Union, Dict


class DataStream(ABC):
    """Abstract base class representing a generic data stream in the Nexus."""

    def __init__(self, stream_id: str) -> None:
        """Initialize the stream with a unique identifier."""
        self.stream_id: str = stream_id

    @abstractmethod
    def process_batch(self, batch: List[Any]) -> str:
        """Process a batch of data and return a summary string."""
        pass


class SensorStream(DataStream):
    """Stream specialized for environmental sensor numerical data."""

    def process_batch(self, batch: List[float]) -> str:
        """Calculates average temperature with safety checks for empty or invalid data."""
        try:
            if not batch:
                return "Sensor analysis: No readings to process"
            
            avg: float = sum(batch) / len(batch)
            return f"Sensor analysis: {len(batch)} readings processed, avg temp: {avg:.1f}°C"
        except (TypeError, ZeroDivisionError) as e:
            return f"Sensor error: Failed to calculate metrics ({e})"


class TransactionStream(DataStream):
    """Stream specialized for financial operations in 'action:value' format."""

    def process_batch(self, batch: List[str]) -> str:
        """Parses transaction strings and calculates net flow with format validation."""
        try:
            net: int = 0
            for item in batch:
                op, val = item.split(":")
                amount = int(val)
                net += amount if op.lower() == "sell" else -amount
            
            res: str = f"+{net}" if net > 0 else str(net)
            return f"Transaction analysis: {len(batch)} operations, net flow: {res} units"
        except (ValueError, AttributeError, IndexError) as e:
            return f"Transaction error: Malformed data detected ({e})"


class EventStream(DataStream):
    """Stream specialized for system logs and event strings."""

    def process_batch(self, batch: List[str]) -> str:
        """Counts error occurrences in system events."""
        try:
            errs: int = sum(1 for e in batch if isinstance(e, str) and "error" in e.lower())
            return f"Event analysis: {len(batch)} events, {errs} errors detected"
        except Exception as e:
            return f"Event error: Could not analyze logs ({e})"


class StreamProcessor:
    """Orchestrator that processes multiple streams through a unified interface."""

    def process(self, streams: List[DataStream], batches: List[List[Any]]) -> None:
        """Iterates through streams and batches, providing high-level error isolation."""
        for s, b in zip(streams, batches):
            try:
                t: str = "Environmental Data" if isinstance(s, SensorStream) else \
                         "Financial Data" if isinstance(s, TransactionStream) else \
                         "System Events"
                
                print(f"Stream ID: {s.stream_id}, Type: {t}")
                print(f"Processing batch: {b}")
                
                result = s.process_batch(b)
                print(result)
            except Exception as e:
                print(f"Critical failure processing stream {s.stream_id}: {e}")
            print("-" * 30)


def main() -> None:
    """Main execution entry point for Polymorphic Stream System testing."""
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")
    
    streams: List[DataStream] = [
        SensorStream("SENSOR_001"),
        TransactionStream("TRANS_001"),
        EventStream("EVENT_001"),
        TransactionStream("TRANS_ERROR_TEST")
    ]
    
    data: List[List[Any]] = [
        [22.5, 23.1, 21.9],
        ["buy:100", "sell:150"],
        ["login", "ERROR: db fail"],
        ["corrupt_data", "sell:abc"]
    ]
    
    proc: StreamProcessor = StreamProcessor()
    proc.process(streams, data)
    
    print("\n=== Polymorphic Stream Processing Summary ===")
    print("Nexus throughput optimal. Error isolation active.")


if __name__ == "__main__":
    main()