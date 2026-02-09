"""Text and template configuration for the Streamlit dashboard."""

# --- Path config (project-relative) ---
ASSETS_ROOT_DIR = "assets"
LOGO_ASSETS_DIR = "assets/logo"

DEFAULT_IMAGE_CANDIDATES_REL = [
    "assets/case1.png",
    "assets/logo/289.jpg",
    "assets/logo/batch_test_sample.png",
]

DEFAULT_CCTV_IMAGE_PATHS_REL = {
    "CCTV1": "assets/case1.png",
    "CCTV2": "assets/case2.png",
    "CCTV3": "assets/case3.png",
    "CCTV4": "assets/case4.png",
}

PIA_LOGO_DARK_REL_PATH = "assets/logo/pia-logo-white.png"

# --- English ---
PAGE_TITLE = "DTRO Safety Dashboard"
BRAND_TITLE = "PIA-SPACE Safety Dashboard"
BRAND_SUBTITLE = "PIA SPACE - CCTV-Based Safety Description Report"

ALARM_CARD_TITLE = "Alarm"
ALARM_MAIN_FORMAT = "{icon} {level} Risk"
ALARM_SUB_FORMAT = "Risk Score: {score} / 100"

DESCRIPTION_TITLE = "Description"
CCTV_VIEW_TITLE = "CCTV View"
VLM_DESCRIPTION_TITLE = "VLM Description"

REPORT_TITLE = "# 🚨 CCTV1 Safety Risk Assessment Report"
REPORT_TWO_COLUMNS_HTML = """
<div class="report-layout">
  <div class="report-row">
    <div class="report-card">
      <h4>🔍 Summary</h4>
      <ul>
        <li>Forklift operating in a warehouse aisle with pedestrians working in close proximity, indicating insufficient separation between personnel and equipment.</li>
      </ul>
    </div>
    <div class="report-card">
      <h4>⚠️ Risk Level</h4>
      <ul>
        <li><strong>{alarm_level}</strong></li>
        <li>Risk Score: <strong>{risk_score} / 100</strong></li>
      </ul>
    </div>
  </div>
  <div class="report-row">
    <div class="report-card">
      <h4>👀 Observation</h4>
      <ul>
        <li>A forklift is actively transporting palletized goods within a warehouse rack aisle</li>
        <li>Multiple workers and pedestrians are present in the same aisle during forklift operation</li>
        <li>Personnel are positioned very close to the forklift's travel path</li>
        <li>Work activities such as box handling are occurring simultaneously with vehicle movement</li>
        <li>Clear separation between pedestrian walkways and forklift operating routes is not observed</li>
      </ul>
    </div>
    <div class="report-card">
      <h4>✅ Recommended Actions</h4>
      <ol>
        <li><strong>Immediately restrict pedestrian access</strong> to forklift operating aisles during active transport</li>
        <li><strong>Implement physical separation</strong> (floor markings, cones, barriers) between pedestrian and equipment routes</li>
        <li>Assign a <strong>spotter or traffic controller</strong> when forklift operations occur in shared spaces</li>
        <li>Reinforce safety procedures regarding <strong>forklift blind spots, stopping distance, and turning radius</strong></li>
      </ol>
    </div>
  </div>
  <div class="report-row">
    <div class="report-card">
      <h4>📘 Safety Guideline Reference</h4>
      <p class="report-quote">Forklift operation and pedestrian traffic separation guidelines</p>
    </div>
    <div class="report-card">
      <h4>🖼️ Visual Indicators</h4>
      <ul>
        <li><strong>Highlighted Object:</strong> Forklift-pedestrian interaction zone</li>
        <li><strong>Highlight Style:</strong> 🔴 Red danger zone overlay</li>
      </ul>
    </div>
  </div>
</div>
"""

DEFAULT_REPORT_TEMPLATE = """## 🚨 CCTV1 Safety Risk Assessment Report
### 🔍 Summary
- Forklift operating in a warehouse aisle with pedestrians working in close proximity, indicating insufficient separation between personnel and equipment.
---
### ⚠️ Risk Level
- **High**  
- Risk Score: **82 / 100**
---
### 👀 Observation
- A forklift is actively transporting palletized goods within a warehouse rack aisle
- Multiple workers and pedestrians are present in the same aisle during forklift operation
- Personnel are positioned very close to the forklift’s travel path
- Work activities such as box handling are occurring simultaneously with vehicle movement
- Clear separation between pedestrian walkways and forklift operating routes is not observed
---
### ✅ Recommended Actions
1. **Immediately restrict pedestrian access** to forklift operating aisles during active transport
2. **Implement physical separation** (floor markings, cones, barriers) between pedestrian and equipment routes
3. Assign a **spotter or traffic controller** when forklift operations occur in shared spaces
4. Reinforce safety procedures regarding **forklift blind spots, stopping distance, and turning radius**
---
### 📘 Safety Guideline Reference
> Forklift operation and pedestrian traffic separation guidelines
---
### 🖼️ Visual Indicators
- **Highlighted Object:** Forklift–pedestrian interaction zone  
- **Highlight Style:** 🔴 Red danger zone overlay

"""

RISK_LEVEL_DESCRIPTIONS = {
    "High": (
        # "The scene indicates insufficient separation between personnel and equipment in the work area, "
        # "with a high likelihood of missing protective gear. Immediate on-site inspection is required."
"A forklift is operating in a warehouse aisle with pedestrians working in close proximity. Insufficient separation between pedestrian and equipment traffic creates a high risk of collision, particularly due to forklift blind spots and sudden movement."
    ),
    "Medium": (
        "Some risk signs are observed. It is not at the level of requiring an immediate stop, "
        "but sufficient distance between personnel and equipment appears necessary. "
        "Please quickly verify close-proximity operations and PPE compliance."
    ),
    "Low": (
        "Clear high-risk indicators are limited. Maintain the current state, "
        "but continue monitoring compliance with basic safety rules."
    ),
}

CCTV2_OVERRIDE_LEVEL = "Medium"
CCTV2_OVERRIDE_SCORE = 68
CCTV2_OVERRIDE_DESCRIPTION = (
    "Some risk signs are observed. It is not at the level of requiring an immediate stop, "
    "but sufficient distance between personnel and equipment appears necessary. "
    "Please quickly verify compliance with safe separation distances between nearby workers and equipment, "
    "as well as PPE usage."
)

# --- Korean --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- --- ---
# --- Korean ---
PAGE_TITLE_KO = "DTRO 안전 대시보드"
BRAND_TITLE_KO = "PIA-SPACE 안전 대시보드"
BRAND_SUBTITLE_KO = "PIA SPACE - CCTV 기반 안전 설명 보고서"

ALARM_CARD_TITLE_KO = "알림"
ALARM_MAIN_FORMAT_KO = "{icon} {level_ko} 위험"
ALARM_SUB_FORMAT_KO = "위험 점수: {score} / 100"

DESCRIPTION_TITLE_KO = "설명"
CCTV_VIEW_TITLE_KO = "CCTV 화면"
VLM_DESCRIPTION_TITLE_KO = "VLM 설명"

REPORT_TITLE_KO = "# 🚨 CCTV1 안전 위험 평가 보고서"
REPORT_TWO_COLUMNS_HTML_KO = """
<div class="report-layout">
  <div class="report-row">
    <div class="report-card">
      <h4>🔍 요약</h4>
      <ul>
        <li>지게차 작업 구역에서 안전모를 착용하지 않은 인원이 다수 확인되었습니다.</li>
      </ul>
    </div>
    <div class="report-card">
      <h4>⚠️ 위험 수준</h4>
      <ul>
        <li><strong>{alarm_level_ko}</strong></li>
        <li>위험 점수: <strong>{risk_score} / 100</strong></li>
      </ul>
    </div>
  </div>
  <div class="report-row">
    <div class="report-card">
      <h4>👀 관찰 내용</h4>
      <ul>
        <li>지게차 작업 구역에 3명의 인원이 있습니다</li>
        <li>모든 인원이 필수 안전모를 착용하지 않았습니다</li>
        <li>지게차 작업이 진행 중이어서 두부 손상 위험이 증가합니다</li>
      </ul>
    </div>
    <div class="report-card">
      <h4>✅ 권고 조치</h4>
      <ol>
        <li><strong>즉시 안전모 착용 의무화</strong>를 시행합니다</li>
        <li>PPE 준수 확인 전까지 <strong>지게차 작업을 중단</strong>합니다</li>
        <li>해당 구역 전 인원을 대상으로 <strong>의무 안전 브리핑</strong>을 실시합니다</li>
      </ol>
    </div>
  </div>
  <div class="report-row">
    <div class="report-card">
      <h4>📘 안전 지침 참고</h4>
      <p class="report-quote">물류 취급 구역 PPE 지침</p>
    </div>
    <div class="report-card">
      <h4>🖼️ 시각적 지표</h4>
      <ul>
        <li><strong>강조 대상:</strong> 보호장비 미착용 인원</li>
        <li><strong>강조 방식:</strong> 🔴 빨간 바운딩 / 오버레이</li>
      </ul>
    </div>
  </div>
</div>
"""

DEFAULT_REPORT_TEMPLATE_KO = """## 🚨 CCTV1 안전 위험 평가 보고서
### 🔍 요약
- 창고 랙 통로에서 지게차가 운행 중이며 보행자가 근접 작업 중이어서, 인원과 장비 간 분리가 불충분합니다.
---
### ⚠️ 위험 수준
- **높음**  
- 위험 점수: **82 / 100**
---
### 👀 관찰 내용
- 지게차가 창고 랙 통로에서 팔레트 화물을 운반하고 있습니다
- 지게차 운행 중 동일 통로에 다수의 작업자와 보행자가 함께 있습니다
- 인원이 지게차 주행 경로와 매우 근접해 있습니다
- 차량 이동과 동시에 박스 취급 등 작업이 병행되고 있습니다
- 보행자 동선과 지게차 운행 동선의 명확한 분리가 확인되지 않습니다
---
### ✅ 권고 조치
1. 지게차 운행 중 통로에 대한 **보행자 접근을 즉시 제한**합니다
2. 보행자/장비 동선 사이에 **물리적 분리 수단**(바닥 표시, 콘, 차단대)을 적용합니다
3. 공유 작업 공간에서 지게차 운행 시 **유도자(스포터) 또는 교통 통제 담당자**를 배치합니다
4. **지게차 사각지대, 제동거리, 회전 반경** 관련 안전 절차를 재강화합니다
---
### 📘 안전 지침 참고
> 지게차 운행 및 보행자 동선 분리 지침
---
### 🖼️ 시각적 지표
- **강조 대상:** 지게차-보행자 상호작용 구역  
- **강조 방식:** 🔴 적색 위험 구역 오버레이
"""

LEVEL_LABELS_KO = {
    "High": "높음",
    "Medium": "보통",
    "Low": "낮음",
}

RISK_LEVEL_DESCRIPTIONS_KO = {
    "High": (
        "지게차가 창고 통로에서 운행 중이며 보행자가 근접 작업 중입니다. "
        "보행자 동선과 장비 동선이 충분히 분리되지 않아, 지게차 사각지대와 급작스러운 이동으로 인한 충돌 위험이 높습니다."
    ),
    "Medium": (
        "일부 위험 징후가 관찰됩니다. 즉시 작업 중지 수준은 아니지만, "
        "인원과 장비 간 충분한 거리 확보가 필요합니다. "
        "근접 작업 상황과 PPE 준수 여부를 빠르게 확인해야 합니다."
    ),
    "Low": (
        "뚜렷한 고위험 징후는 제한적입니다. 현재 상태를 유지하되, "
        "기본 안전 수칙 준수 여부를 지속적으로 모니터링해야 합니다."
    ),
}

CCTV2_OVERRIDE_DESCRIPTION_KO = (
    "일부 위험 징후가 관찰됩니다. 즉시 작업 중지 수준은 아니지만, "
    "인원과 장비 간 충분한 거리 확보가 필요합니다. "
    "근접 작업 상황과 PPE 준수 여부를 빠르게 확인해야 합니다."
)
