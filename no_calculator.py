"""
Prostate Micro-Tubule & Hard Water Mineral Calculator
Evaluates age-related mineral deposition and bio-chelation dosage requirements.
"""

def calculate_prostate_load(age: int, hard_water_years: int) -> dict:
    base_calcification = min(0.85, (age - 40) * 0.018 + (hard_water_years * 0.012))
    flow_pressure_score = max(15, int((1.0 - base_calcification) * 100))
    chelator_dosage_ml = 2.0 if flow_pressure_score < 50 else 1.0

    return {
        "user_age": age,
        "hard_water_exposure_years": hard_water_years,
        "estimated_calcification_index": f"{int(base_calcification * 100)}%",
        "urinary_flow_efficiency": f"{flow_pressure_score}%",
        "recommended_daily_dropper_ml": chelator_dosage_ml
    }

if __name__ == "__main__":
    print("=" * 60)
    print("PotentStream Clinical Mineral Chelation Model (2027)")
    print("=" * 60)
    report = calculate_prostate_load(age=58, hard_water_years=22)
    for k, v in report.items():
        print(f" - {k.replace('_', ' ').title()}: {v}")
    print("=" * 60)
