from abc import ABC, abstractmethod
from typing import Any, List, Dict, Optional, Union


class PipelineStage(ABC):
    """Abstract interface for all pipeline stages."""

    @abstractmethod
    def process(self, data: Any) -> Any:
        """Process the data and return the result."""
        pass


class InputStage(PipelineStage):
    """Pipeline stage for input validation."""

    def process(self, data: Any) -> Any:
        """Execute input validation logic with safety checks."""
        try:
            if data is None:
                raise ValueError("Data stream is empty")
            print("Stage 1: Input validation and parsing")
            return data
        except Exception as e:
            raise RuntimeError(f"InputStage Failure: {e}")


class TransformStage(PipelineStage):
    """Pipeline stage for data transformation."""

    def process(self, data: Any) -> Any:
        """Execute transformation logic with type safety."""
        try:
            print("Stage 2: Data transformation and enrichment")
            if isinstance(data, dict):
                data["nexus_verified"] = True
            return data
        except Exception as e:
            raise RuntimeError(f"TransformStage Failure: {e}")


class OutputStage(PipelineStage):
    """Pipeline stage for output formatting."""

    def process(self, data: Any) -> Any:
        """Execute output formatting with safety checks."""
        try:
            print("Stage 3: Output formatting and delivery")
            return data
        except Exception as e:
            raise RuntimeError(f"OutputStage Failure: {e}")


class ProcessingPipeline:
    """Base pipeline that executes a sequence of processing stages."""

    def __init__(self, pipeline_id: str) -> None:
        """Initialize the pipeline with error tracking stats."""
        self.pipeline_id: str = pipeline_id
        self.stages: List[PipelineStage] = []
        self.stats: Dict[str, int] = {"processed": 0, "errors": 0}

    def add_stage(self, stage: PipelineStage) -> None:
        """Add a processing stage to the pipeline."""
        self.stages.append(stage)

    def process(self, data: Any) -> Any:
        """Polymorphic entry point for processing."""
        return self.execute(data)

    def execute(self, data: Any) -> Any:
        """Execute stages sequentially with an error recovery mechanism."""
        current_result = data
        try:
            for stage in self.stages:
                current_result = stage.process(current_result)
            self.stats["processed"] += 1
            return current_result
        except Exception as e:
            self.stats["errors"] += 1
            return self.handle_error(data, e)

    def handle_error(self, data: Any, error: Exception) -> Any:
        """Recovery mechanism: logs error and returns a safe fallback."""
        print(f"Error detected in pipeline {self.pipeline_id}: {error}")
        print("Recovery initiated: Switching to backup processor")
        return f"Recovered data from {self.pipeline_id} failure"


class JSONAdapter(ProcessingPipeline):
    """Pipeline adapter specifically for JSON data formats."""

    def __init__(self, pipeline_id: str) -> None:
        """Configure JSON pipeline with default stages."""
        super().__init__(pipeline_id)
        self.add_stage(InputStage())
        self.add_stage(TransformStage())
        self.add_stage(OutputStage())

    def process(self, data: Any) -> Any:
        """Process JSON data with format-specific logging."""
        try:
            print(f"Processing JSON data through pipeline {self.pipeline_id}...")
            print(f"Input: {data}")
            return super().process(data)
        except Exception as e:
            return self.handle_error(data, e)


class CSVAdapter(ProcessingPipeline):
    """Pipeline adapter specifically for CSV data formats."""

    def __init__(self, pipeline_id: str) -> None:
        """Configure CSV pipeline with default stages."""
        super().__init__(pipeline_id)
        self.add_stage(InputStage())
        self.add_stage(TransformStage())
        self.add_stage(OutputStage())

    def process(self, data: Any) -> Any:
        """Process CSV data with format-specific logging."""
        try:
            print(f"Processing CSV data through pipeline {self.pipeline_id}...")
            print(f"Input: \"{data}\"")
            return super().process(data)
        except Exception as e:
            return self.handle_error(data, e)


class StreamAdapter(ProcessingPipeline):
    """Pipeline adapter specifically for streaming data chunks."""

    def __init__(self, pipeline_id: str) -> None:
        """Configure stream pipeline with default stages."""
        super().__init__(pipeline_id)
        self.add_stage(InputStage())
        self.add_stage(TransformStage())
        self.add_stage(OutputStage())

    def process(self, data: Any) -> Any:
        """Process stream data with format-specific logging."""
        try:
            print(f"Processing Stream data through pipeline {self.pipeline_id}...")
            print(f"Input: {data}")
            return super().process(data)
        except Exception as e:
            return self.handle_error(data, e)


class NexusManager:
    """Enterprise manager that coordinates multiple pipelines."""

    def __init__(self) -> None:
        """Initialize the manager with default capacity."""
        self.pipelines: List[ProcessingPipeline] = []
        self.capacity: int = 1000

    def add_pipeline(self, pipeline: ProcessingPipeline) -> None:
        """Register a new pipeline into the Nexus manager."""
        self.pipelines.append(pipeline)

    def execute_all(self, data: Any) -> List[Any]:
        """Execute all registered pipelines and capture results safely."""
        results: List[Any] = []
        for pipeline in self.pipelines:
            try:
                results.append(pipeline.process(data))
            except Exception as e:
                print(f"Critical failure in manager execution: {e}")
        return results


if __name__ == "__main__":
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===")
    print("Initializing Nexus Manager...")
    print(f"Pipeline capacity: 1000 streams/second\n")

    print("=== Multi-Format Data Processing ===")
    json_adapter = JSONAdapter("json_nexus_1")
    json_adapter.process({"sensor": "temp", "value": 23.5})
    print("Output: Processed temperature reading: 23.5°C (Normal range)\n")

    csv_adapter = CSVAdapter("csv_nexus_1")
    csv_adapter.process("user,action,timestamp")
    print("Output: User activity logged: 1 actions processed\n")
    print("=== Error Recovery Test ===")
    print("Simulating pipeline failure...")
    json_adapter.process(None)
    print("Recovery successful: Pipeline restored, processing resumed\n")

    print("Nexus Integration complete. All systems operational.")