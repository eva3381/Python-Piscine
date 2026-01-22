from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union


class DataProcessor(ABC):
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
    def process(self, data: List[Union[int, float]]) -> Dict[str, float]:
        total: float = float(sum(data))
        count: int = len(data)
        avg: float = total / count if count > 0 else 0.0
        return {"count": float(count), "sum": total, "avg": avg}

    def validate(self, data: Any) -> bool:
        if not isinstance(data, list):
            return False
        return all(isinstance(x, (int, float)) for x in data)

    def format_output(self, data: Dict[str, float]) -> str:
        return (f"Processed {int(data['count'])} numeric values, "
                f"sum={data['sum']}, avg={data['avg']}")


class TextProcessor(DataProcessor):
    def process(self, data: str) -> Dict[str, int]:
        return {"chars": len(data), "words": len(data.split())}

    def validate(self, data: Any) -> bool:
        return isinstance(data, str)

    def format_output(self, data: Dict[str, int]) -> str:
        return (f"Processed text: {data['chars']} characters, "
                f"{data['words']} words")


class LogProcessor(DataProcessor):
    def process(self, data: str) -> Dict[str, str]:
        level: str = data.split(":")[0]
        msg: str = data.split(": ")[1] if ": " in data else data
        return {"level": level, "message": msg}

    def validate(self, data: Any) -> bool:
        return isinstance(data, str) and ":" in data

    def format_output(self, data: Dict[str, str]) -> str:
        tag: str = "[ALERT]" if data["level"] == "ERROR" else "[INFO]"
        return f"{tag} {data['level']} level detected: {data['message']}"


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    np: NumericProcessor = NumericProcessor()
    tp: TextProcessor = TextProcessor()
    lp: LogProcessor = LogProcessor()

    print("Initializing Numeric Processor...")
    d_n: List[int] = [1, 2, 3, 4, 5]
    print(f"Processing data: {d_n}")
    if np.validate(d_n):
        print("Validation: Numeric data verified")
        print(f"Output: {np.format_output(np.process(d_n))}")

    print("Initializing Text Processor...")
    d_t: str = "Hello Nexus World"
    print(f"Processing data: \"{d_t}\"")
    if tp.validate(d_t):
        print("Validation: Text data verified")
        print(f"Output: {tp.format_output(tp.process(d_t))}")

    print("Initializing Log Processor...")
    d_l: str = "ERROR: Connection timeout"
    print(f"Processing data: \"{d_l}\"")
    if lp.validate(d_l):
        print("Validation: Log entry verified")
        print(f"Output: {lp.format_output(lp.process(d_l))}")

    print("=== Polymorphic Processing Demo ===")
    procs: List[DataProcessor] = [np, tp, lp]
    mixed: List[Any] = [[1, 2, 3], "Nexus Stream", "INFO: System ready"]
    for i, (p, d) in enumerate(zip(procs, mixed), 1):
        print(f"Result {i}: {p.format_output(p.process(d))}")
    print("Foundation systems online.\nNexus ready for advanced streams.")


if __name__ == "__main__":
    main()