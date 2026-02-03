from abc import ABC, abstractmethod
from typing import Any, List


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

    def process_batch(self, batch: List[Any]) -> str:
        """Calculates average temperature filtering specific temp readings."""
        try:
            items = [x for x in batch if "temp:" in str(x)]
            temps = [float(item.split(":")[1]) for item in items]
            if not temps:
                nums = [float(str(x).split(":")[1]) if ":" in str(x)
                        else float(x) for x in batch]
                avg = sum(nums) / len(nums) if nums else 0.0
                return f"{len(nums)} readings processed, avg temp: {avg:.1f}°C"

            avg_val = sum(temps) / len(temps)
            return (f"{len(batch)} readings processed, "
                    f"avg temp: {avg_val:.1f}°C")
        except Exception as e:
            return f"Sensor error: {e}"


class TransactionStream(DataStream):
    """Stream specialized for financial operations."""

    def process_batch(self, batch: List[str]) -> str:
        """Parses transactions and calculates net flow."""
        try:
            net: int = 0
            for item in batch:
                op, val = item.split(":")
                amount = int(val)
                net += amount if op.lower() == "sell" else -amount
            res: str = f"+{net}" if net > 0 else str(net)
            return f"{len(batch)} operations, net flow: {res} units"
        except Exception as e:
            return f"Transaction error: {e}"


class EventStream(DataStream):
    """Stream specialized for system logs and event strings."""

    def process_batch(self, batch: List[str]) -> str:
        """Counts error occurrences in system events."""
        errs = sum(1 for e in batch if "error" in str(e).lower())
        err_word = "error" if errs == 1 else "errors"
        return f"{len(batch)} events, {errs} {err_word} detected"


class StreamProcessor:
    """Orchestrator for unified stream processing."""

    def process(self, streams: List[DataStream],
                batches: List[List[Any]]) -> List[str]:
        """Processes streams and prints real-time status."""
        results = []
        for s, b in zip(streams, batches):
            if isinstance(s, SensorStream):
                print("Initializing Sensor Stream...")
                name, t, label = "Sensor", "Environmental Data", "sensor"
            elif isinstance(s, TransactionStream):
                print("Initializing Transaction Stream...")
                name, t, lbl = "Transaction", "Financial Data", "transaction"
                label = lbl
            else:
                print("Initializing Event Stream...")
                name, t, label = "Event", "System Events", "event"

            print(f"Stream ID: {s.stream_id}, Type: {t}")
            batch_str = str(b).replace("'", "")
            print(f"Processing {label} batch: {batch_str}")

            res = s.process_batch(b)
            print(f"{name} analysis: {res}\n")
            results.append(res)
        return results


def main() -> None:
    """Main execution entry point with dynamic summary generation."""
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    streams: List[DataStream] = [
        SensorStream("SENSOR_001"),
        TransactionStream("TRANS_001"),
        EventStream("EVENT_001")
    ]

    data: List[List[Any]] = [
        ["temp:22.5", "humidity:65", "pressure:1013"],
        ["buy:100", "sell:250", "buy:25"],
        ["login", "error", "logout"]
    ]

    proc = StreamProcessor()
    results = proc.process(streams, data)

    print("=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...\n")
    print("Batch 1 Results:")

    [print(f"- Sensor data: {r.split(',')[0]}")
     for r in results if "readings" in r]
    [print(f"- Transaction data: {r.split(',')[0]}")
     for r in results if "operations" in r]
    [print(f"- Event data: {r.split(',')[0]}")
     for r in results if "events" in r]

    alerts = [x for x in data[0] if "temp:" in str(x)
              and float(x.split(":")[1]) > 30]
    big_tx = [x for x in data[1] if ":" in str(x)
              and int(x.split(":")[1]) > 150]

    print("\nStream filtering active: High-priority data only")
    f_res = (f"Filtered results: {len(alerts)} critical sensor alerts, "
             f"{len(big_tx)} large transaction\n")
    print(f_res)
    print("All streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
