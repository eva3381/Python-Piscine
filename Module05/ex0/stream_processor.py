from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union


class DataProcessor(ABC):
    """Base class with mandatory processing methods."""

    @abstractmethod
    def process(self, data: Any) -> Any:
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def format_output(self, data: Any) -> str:
        pass


class NumericProcessor(DataProcessor):
    """Handles numeric lists and individual numbers."""

    def process(self, data: List[Union[int, float]]) -> Dict[str, float]:
        try:
            total = int(sum(data))
            count = len(data)
            avg = total / count if count > 0 else 0.0
            return {"count": float(count), "sum": total, "avg": avg}
        except (TypeError, ZeroDivisionError) as e:
            return {"count": 0.0, "sum": 0.0, "avg": 0.0, "error": str(e)}

    def validate(self, data: Any) -> bool:
        try:
            if not isinstance(data, list):
                return False
            return all(isinstance(x, (int, float)) for x in data)
        except Exception:
            return False

    def format_output(self, data: Dict[str, Any]) -> str:
        if "error" in data:
            return f"Numeric Error: {data['error']}"
        return (f"Processed {int(data['count'])} numeric values, "
                f"sum={data['sum']}, avg={data['avg']}")


class TextProcessor(DataProcessor):
    """Handles string data for character and word counting."""

    def process(self, data: str) -> Dict[str, int]:
        try:
            return {"chars": len(data), "words": len(data.split())}
        except Exception as e:
            return {"chars": 0, "words": 0, "error": str(e)}

    def validate(self, data: Any) -> bool:
        return isinstance(data, str)

    def format_output(self, data: Dict[str, Any]) -> str:
        if "error" in data:
            return f"Text Error: {data['error']}"
        return (f"Processed text: {data['chars']} characters, "
                f"{data['words']} words")


class LogProcessor(DataProcessor):
    """Parses log entries and generates alerts."""

    def process(self, data: str) -> Dict[str, str]:
        try:
            parts = data.split(":")
            level = parts[0].strip()
            msg = data.split(": ", 1)[1] if ": " in data else data
            return {"level": level, "message": msg}
        except Exception as e:
            return {"level": "UNKNOWN", "message": str(e), "error": "True"}

    def validate(self, data: Any) -> bool:
        return isinstance(data, str) and ":" in data

    def format_output(self, data: Dict[str, str]) -> str:
        try:
            tag = "[ALERT]" if data.get("level") == "ERROR" else "[INFO]"
            return (f"{tag} {data.get('level')} "
                    f"level detected: {data.get('message')}")
        except Exception:
            return "Log formatting failed"


def main() -> None:
    """Demonstrates polymorphism as required by the evaluation sheet."""
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    np = NumericProcessor()
    tp = TextProcessor()
    lp = LogProcessor()

    try:
        print("Initializing Numeric Processor...")
        d_n = [1, 2, 3, 4, 5]
        print(f"Processing data: {d_n}")
        if np.validate(d_n):
            print("Validation: Numeric data verified")
            print(f"Output: {np.format_output(np.process(d_n))}\n")
    except Exception as e:
        print(f"Numeric step failed: {e}")

    try:
        print("Initializing Text Processor...")
        d_t = "Hello Nexus World"
        print(f"Processing data: \"{d_t}\"")
        if tp.validate(d_t):
            print("Validation: Text data verified")
            print(f"Output: {tp.format_output(tp.process(d_t))}\n")
    except Exception as e:
        print(f"Text step failed: {e}")

    try:
        print("Initializing Log Processor...")
        d_l = "ERROR: Connection timeout"
        print(f"Processing data: \"{d_l}\"")
        if lp.validate(d_l):
            print("Validation: Log entry verified")
            print(f"Output: {lp.format_output(lp.process(d_l))}")
    except Exception as e:
        print(f"Log step failed: {e}")

    print("\n=== Polymorphic Processing Demo ===")
    try:
        procs: List[DataProcessor] = [np, tp, lp]
        mixed: List[Any] = [[1, 2, 3], "Nexus Stream", "INFO: System ready"]
        for i, (p, d) in enumerate(zip(procs, mixed), 1):
            processed_data = p.process(d)
            print(f"Result {i}: {p.format_output(processed_data)}")
    except Exception as e:
        print(f"Demo failed: {e}")

    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
