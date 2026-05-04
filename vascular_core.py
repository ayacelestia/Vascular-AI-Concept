class VascularOptimizer:
    """
    Vascular-AI: Tissue Viability and Vascularization Analyzer
    """
    def __init__(self, tissue_type, thickness):
        self.tissue_type = tissue_type
        self.thickness = thickness
        self.DIFFUSION_LIMIT = 200  # MicroMeter (µm)

    def analyze_viability(self):
        """Analyzes if cells can reach oxygen."""
        print(f"--- Analyzing {self.tissue_type} ---")
        
        # Status check based on 200 micron rule
        status = "SAFE" if self.thickness <= self.DIFFUSION_LIMIT else "CRITICAL"
        oxygen_penetration = min(100, (self.DIFFUSION_LIMIT / self.thickness) * 100)
        
        return {
            "Status": status,
            "Oxygen Penetration": f"%{oxygen_penetration:.1f}",
            "Required Vascular Depth": max(0, self.thickness - self.DIFFUSION_LIMIT)
        }

# Starts Simulation
# Example: A thick liver tissue block
model = VascularOptimizer(tissue_type="Liver Tissue Block", thickness=450)
results = model.analyze_viability()

for key, value in results.items():
    print(f"{key}: {value}")