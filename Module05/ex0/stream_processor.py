from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union


class DataProcessor(ABC):
    """Abstract base class for data processing units."""

    @abstractmethod
    def process(self, data: Any) -> Any:
        """Execute core data transformation."""
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Check if data is valid for processing."""
        pass

    @abstractmethod
    def format_output(self, data: Any) -> str:
        """Return a formatted string representation of the result."""
        pass


class NumericProcessor(DataProcessor):
    """Processor for list of numbers."""

    def process(self, data: List[Union[int, float]]) -> Dict[str, float]:
        """Calculate count, sum, and average from a list of numbers."""
        try:
            total: float = float(sum(data))
            count: int = len(data)
            avg: float = total / count if count > 0 else 0.0
            return {"count": float(count), "sum": total, "avg": avg}
        except Exception as e:
            return {"count": 0.0, "sum": 0.0, "avg": 0.0, "error": str(e)}

    def validate(self, data: Any) -> bool:
        """Validate that input is a list of numeric values."""
        try:
            if not isinstance(data, list):
                return False
            return all(isinstance(x, (int, float)) for x in data)
        except Exception:
            return False

    def format_output(self, data: Dict[str, float]) -> str:
        """Format numeric processing results."""
        if "error" in data:
            return f"Numeric Error: {data['error']}"
        return (f"Processed {int(data['count'])} numeric values, "
                f"sum={data['sum']}, avg={data['avg']}")


class TextProcessor(DataProcessor):
    """Processor for string text."""

    def process(self, data: str) -> Dict[str, int]:
        """Count characters and words in a string."""
        try:
            return {"chars": len(data), "words": len(data.split())}
        except Exception as e:
            return {"chars": 0, "words": 0, "error": str(e)}

    def validate(self, data: Any) -> bool:
        """Validate that input is a string."""
        try:
            return isinstance(data, str)
        except Exception:
            return False

    def format_output(self, data: Dict[str, int]) -> str:
        """Format text processing results."""
        if "error" in data:
            return f"Text Error: {data['error']}"
        return (f"Processed text: {data['chars']} characters, "
                f"{data['words']} words")


class LogProcessor(DataProcessor):
    """Processor for log entries."""

    def process(self, data: str) -> Dict[str, str]:
        """Extract level and message from log string."""
        try:
            level: str = data.split(":")[0]
            msg: str = data.split(": ")[1] if ": " in data else data
            return {"level": level, "message": msg}
        except Exception as e:
            return {"level": "UNKNOWN", "message": str(e), "error": "True"}

    def validate(self, data: Any) -> bool:
        """Validate log format (string with colon)."""
        try:
            return isinstance(data, str) and ":" in data
        except Exception:
            return False

    def format_output(self, data: Dict[str, str]) -> str:
        """Format log processing results."""
        try:
            tag: str = "[ALERT]" if data.get("level") == "ERROR" else "[INFO]"
            return f"{tag} {data.get('level')} level detected: {data.get('message')}"
        except Exception:
            return "Log formatting failed"


def main() -> None:
    """Execute the data processor foundation demo."""
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    np: NumericProcessor = NumericProcessor()
    tp: TextProcessor = TextProcessor()
    lp: LogProcessor = LogProcessor()

    try:
        print("Initializing Numeric Processor...")
        d_n: List[int] = [1, 2, 3, 4, 5]
        print(f"Processing data: {d_n}")
        if np.validate(d_n):
            print("Validation: Numeric data verified")
            print(f"Output: {np.format_output(np.process(d_n))}")
    except Exception as e:
        print(f"Numeric step failed: {e}")

    try:
        print("Initializing Text Processor...")
        d_t: str = "Hello Nexus World"
        print(f"Processing data: \"{d_t}\"")
        if tp.validate(d_t):
            print("Validation: Text data verified")
            print(f"Output: {tp.format_output(tp.process(d_t))}")
    except Exception as e:
        print(f"Text step failed: {e}")

    try:
        print("Initializing Log Processor...")
        d_l: str = "ERROR: Connection timeout"
        print(f"Processing data: \"{d_l}\"")
        if lp.validate(d_l):
            print("Validation: Log entry verified")
            print(f"Output: {lp.format_output(lp.process(d_l))}")
    except Exception as e:
        print(f"Log step failed: {e}")

    print("=== Polymorphic Processing Demo ===")
    try:
        procs: List[DataProcessor] = [np, tp, lp]
        mixed: List[Any] = [[1, 2, 3], "Nexus Stream", "INFO: System ready"]
        for i, (p, d) in enumerate(zip(procs, mixed), 1):
            processed_data = p.process(d)
            print(f"Result {i}: {p.format_output(processed_data)}")
    except Exception as e:
        print(f"Demo failed: {e}")

    print("Foundation systems online.\nNexus ready for advanced streams.")


if __name__ == "__main__":
    main()
