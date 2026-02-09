import base64
import hashlib
import os
from dataclasses import dataclass

import streamlit as st
from PIL import Image

from config import (
    ALARM_CARD_TITLE_KO,
    ALARM_MAIN_FORMAT_KO,
    ALARM_SUB_FORMAT_KO,
    BRAND_SUBTITLE_KO,
    BRAND_TITLE_KO,
    CCTV2_OVERRIDE_DESCRIPTION_KO,
    CCTV2_OVERRIDE_LEVEL,
    CCTV2_OVERRIDE_SCORE,
    CCTV_VIEW_TITLE_KO,
    DEFAULT_CCTV_IMAGE_PATHS_REL,
    DEFAULT_IMAGE_CANDIDATES_REL,
    DEFAULT_REPORT_TEMPLATE_KO,
    DESCRIPTION_TITLE_KO,
    LEVEL_LABELS_KO,
    PAGE_TITLE_KO,
    PIA_LOGO_DARK_REL_PATH,
    REPORT_TITLE_KO,
    REPORT_TWO_COLUMNS_HTML_KO,
    RISK_LEVEL_DESCRIPTIONS_KO,
    VLM_DESCRIPTION_TITLE_KO,
)


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_IMAGE_CANDIDATES = [os.path.join(BASE_DIR, rel_path) for rel_path in DEFAULT_IMAGE_CANDIDATES_REL]
DEFAULT_CCTV_IMAGE_PATHS = {
    cctv_id: os.path.join(BASE_DIR, rel_path)
    for cctv_id, rel_path in DEFAULT_CCTV_IMAGE_PATHS_REL.items()
}

SYNC_ITEM_HEIGHT = 320
IMAGE_DISPLAY_HEIGHT = 240

PIA_LOGO_DARK_PATH = os.path.join(BASE_DIR, PIA_LOGO_DARK_REL_PATH)

ROBOT_SVG = """
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" height="64">
  <rect x="14" y="16" width="36" height="36" rx="8" fill="#1f2937"/>
  <circle cx="26" cy="32" r="4" fill="#60a5fa"/>
  <circle cx="38" cy="32" r="4" fill="#60a5fa"/>
  <rect x="24" y="41" width="16" height="4" rx="2" fill="#93c5fd"/>
  <rect x="9" y="26" width="5" height="12" rx="2" fill="#4b5563"/>
  <rect x="50" y="26" width="5" height="12" rx="2" fill="#4b5563"/>
  <rect x="28" y="8" width="8" height="8" rx="2" fill="#1f2937"/>
  <circle cx="32" cy="8" r="2.5" fill="#f59e0b"/>
</svg>
"""


@dataclass
class MockResult:
    alarm_level: str
    risk_score: int
    description: str
    report_markdown: str


def _first_existing_path(paths: list[str]) -> str | None:
    for path in paths:
        if os.path.exists(path):
            return path
    return None


def _get_file_as_base64(path: str | None) -> str | None:
    if not path or not os.path.exists(path):
        return None
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()


def _get_robot_as_base64() -> str:
    return base64.b64encode(ROBOT_SVG.encode("utf-8")).decode()


def _risk_from_image_name(image_name: str) -> tuple[str, int]:
    digest = hashlib.sha256(image_name.encode("utf-8")).hexdigest()
    score = 45 + (int(digest[:8], 16) % 51)

    if score >= 75:
        return "High", score
    if score >= 60:
        return "Medium", score
    return "Low", score


def _to_korean_level(level: str) -> str:
    return LEVEL_LABELS_KO.get(level, level)

def _build_mock_result(image_name: str) -> MockResult:
    level, score = _risk_from_image_name(image_name)

    report_markdown = DEFAULT_REPORT_TEMPLATE_KO
    return MockResult(
        alarm_level=level,
        risk_score=score,
        description=RISK_LEVEL_DESCRIPTIONS_KO[level],
        report_markdown=report_markdown,
    )


def _load_cctv_images() -> dict[str, tuple[Image.Image, str]] | None:
    fallback_path = _first_existing_path(DEFAULT_IMAGE_CANDIDATES)
    if fallback_path is None:
        return None

    loaded: dict[str, tuple[Image.Image, str]] = {}
    for cctv_id, image_path in DEFAULT_CCTV_IMAGE_PATHS.items():
        selected_path = image_path if os.path.exists(image_path) else fallback_path
        loaded[cctv_id] = (Image.open(selected_path).convert("RGB"), os.path.basename(selected_path))
    return loaded


def _inject_css() -> None:
    css = """
<style>
  [data-testid="stAppViewContainer"] {
    background: #0A0A1A;
    color: #FFFFFF;
  }
  [data-testid="stHeader"] {
    background: #0A0A1A;
  }
  [data-testid="stSidebar"] {
    background: #1E1E3F;
    color: #FFFFFF;
  }
  [data-testid="stVerticalBlockBorderWrapper"] {
    background: #1E1E3F;
    border: 1px solid rgba(255, 255, 255, 0.15);
  }
  [data-testid="stMarkdownContainer"] p,
  [data-testid="stMarkdownContainer"] li,
  [data-testid="stMarkdownContainer"] h1,
  [data-testid="stMarkdownContainer"] h2,
  [data-testid="stMarkdownContainer"] h3,
  [data-testid="stMarkdownContainer"] h4,
  [data-testid="stMarkdownContainer"] h5,
  [data-testid="stMarkdownContainer"] h6,
  [data-testid="stMarkdownContainer"] strong,
  [data-testid="stMarkdownContainer"] blockquote,
  [data-testid="stCaptionContainer"] {
    color: #FFFFFF !important;
  }
  [data-testid="stImage"] img {
    border-radius: 10px;
    height: __IMAGE_DISPLAY_HEIGHT__px;
    object-fit: cover;
  }
  .brand-wrap {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 14px 18px;
    border-radius: 14px;
    background: #1E1E3F;
    border: 1px solid rgba(255, 255, 255, 0.2);
    margin-bottom: 16px;
  }
  .brand-title {
    margin: 0;
    font-size: 28px;
    font-weight: 800;
    color: #FFFFFF;
  }
  .brand-sub {
    margin: 4px 0 0;
    color: rgba(255, 255, 255, 0.85);
    font-size: 14px;
  }
  .brand-logos {
    display: flex;
    align-items: center;
    gap: 12px;
  }
  .brand-logos img {
    max-height: 84px;
    width: auto;
  }
  .card-title {
    margin: 0 0 10px;
    font-size: 20px;
    font-weight: 700;
    color: #FFFFFF;
  }
  .cctv-item-title {
    margin: 10px 0 8px;
    font-size: 18px;
    font-weight: 700;
    color: #FFFFFF;
  }
  .section-sep {
    margin: 10px 0;
    border-top: 1px solid rgba(255, 255, 255, 0.22);
  }
  .alarm-box {
    border-radius: 12px;
    padding: 6px 10px;
    color: #ffffff;
    font-weight: 700;
    font-size: 14px;
    line-height: 1.2;
    box-sizing: border-box;
    width: 100%;
    margin-bottom: 10px;
  }
  .alarm-main {
    margin: 0;
    font-size: 15px;
    font-weight: 800;
  }
  .alarm-sub {
    margin: 1px 0 0;
    font-size: 12px;
    opacity: 0.95;
  }
  .alarm-high {
    background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%);
  }
  .alarm-medium {
    background: linear-gradient(135deg, #f59e0b 0%, #ea580c 100%);
  }
  .alarm-low {
    background: linear-gradient(135deg, #10b981 0%, #059669 100%);
  }
  .desc-box {
    border-radius: 12px;
    padding: 12px 14px;
    background: linear-gradient(135deg, #1e293b 0%, #334155 100%);
    border: 1px solid rgba(255, 255, 255, 0.25);
    margin-top: 6px;
  }
  .desc-head {
    display: flex;
    align-items: center;
    gap: 10px;
    margin-bottom: 8px;
  }
  .desc-head img {
    width: 36px;
    height: 36px;
  }
  .desc-head span {
    font-size: 18px;
    font-weight: 700;
    color: #dbeafe;
  }
  .desc-text {
    color: #f8fafc;
    line-height: 1.7;
    font-size: 15px;
  }
  .report-card {
    border-radius: 12px;
    padding: 12px 14px;
    background: linear-gradient(135deg, #18243d 0%, #223559 100%);
    border: 1px solid rgba(255, 255, 255, 0.2);
    box-sizing: border-box;
    width: 100%;
    height: 100%;
    min-width: 0;
    overflow-wrap: anywhere;
    word-break: break-word;
    margin-bottom: 10px;
  }
  .report-layout {
    width: 100%;
    max-width: 100%;
    box-sizing: border-box;
  }
  .report-row {
    display: grid;
    grid-template-columns: minmax(0, 1fr) minmax(0, 1fr);
    gap: 10px;
    align-items: stretch;
    margin-bottom: 10px;
  }
  .report-card h4 {
    margin: 0 0 8px;
    font-size: 18px;
    font-weight: 800;
    color: #ffffff;
  }
  .report-card p,
  .report-card li {
    margin: 0;
    color: #f8fafc;
    line-height: 1.55;
    font-size: 14px;
  }
  .report-card ul,
  .report-card ol {
    margin: 0;
    padding-left: 18px;
  }
  .report-quote {
    margin: 0;
    padding-left: 10px;
    border-left: 3px solid #93c5fd;
  }
</style>
    """.replace("__IMAGE_DISPLAY_HEIGHT__", str(IMAGE_DISPLAY_HEIGHT))
    st.markdown(
        css,
        unsafe_allow_html=True,
    )


def _render_brand_header() -> None:
    pia_logo = _get_file_as_base64(PIA_LOGO_DARK_PATH)

    st.markdown(
        f"""
<div class="brand-wrap">
  <div>
    <h1 class="brand-title">{BRAND_TITLE_KO}</h1>
    <p class="brand-sub">{BRAND_SUBTITLE_KO}</p>
  </div>
  <div class="brand-logos">
    {f'<img src="data:image/png;base64,{pia_logo}" alt="PIA">' if pia_logo else ""}
  </div>
</div>
        """,
        unsafe_allow_html=True,
    )


def _render_alarm(level: str, score: int, show_title: bool = True) -> None:
    if level == "High":
        css_class = "alarm-box alarm-high"
        icon = "🚨"
    elif level == "Medium":
        css_class = "alarm-box alarm-medium"
        icon = "⚠️"
    else:
        css_class = "alarm-box alarm-low"
        icon = "✅"

    level_ko = _to_korean_level(level)
    title_html = f'<p class="card-title">{ALARM_CARD_TITLE_KO}</p>' if show_title else ""
    st.markdown(
        f"""
{title_html}
<div class="{css_class}">
  <p class="alarm-main">{ALARM_MAIN_FORMAT_KO.format(icon=icon, level_ko=level_ko)}</p>
  <p class="alarm-sub">{ALARM_SUB_FORMAT_KO.format(score=score)}</p>
</div>
        """,
        unsafe_allow_html=True,
    )


def _render_description(text: str) -> None:
    robot = _get_robot_as_base64()
    st.markdown(
        f"""
<div class="desc-box">
  <div class="desc-head">
    <img src="data:image/svg+xml;base64,{robot}" alt="로봇" />
    <span>{DESCRIPTION_TITLE_KO}</span>
  </div>
  <div class="desc-text">{text}</div>
</div>
        """,
        unsafe_allow_html=True,
    )


def _render_report_two_columns(result: MockResult) -> None:
    level_ko = _to_korean_level(result.alarm_level)
    st.markdown(REPORT_TITLE_KO)
    st.markdown(
        REPORT_TWO_COLUMNS_HTML_KO.format(alarm_level_ko=level_ko, risk_score=result.risk_score),
        unsafe_allow_html=True,
    )


page_icon = "🚨"
if os.path.exists(PIA_LOGO_DARK_PATH):
    page_icon = Image.open(PIA_LOGO_DARK_PATH)

st.set_page_config(
    page_title=PAGE_TITLE_KO,
    page_icon=page_icon,
    layout="wide",
    initial_sidebar_state="collapsed",
)

_inject_css()
_render_brand_header()

cctv_images = _load_cctv_images()
if cctv_images is None:
    st.error("기본 이미지를 찾지 못했습니다. `assets/case1.png` 또는 `assets/logo`를 확인해주세요.")
    st.stop()

cctv_ids = list(DEFAULT_CCTV_IMAGE_PATHS.keys())
results = {cctv_id: _build_mock_result(f"{cctv_images[cctv_id][1]}-{cctv_id}") for cctv_id in cctv_ids}
for cctv_id in cctv_ids:
    if cctv_id == "CCTV2":
        results[cctv_id] = MockResult(
            alarm_level=CCTV2_OVERRIDE_LEVEL,
            risk_score=CCTV2_OVERRIDE_SCORE,  # 60~74 권장
            description=CCTV2_OVERRIDE_DESCRIPTION_KO,
            report_markdown=DEFAULT_REPORT_TEMPLATE_KO,
        )
    else:
        results[cctv_id] = _build_mock_result(f"{cctv_images[cctv_id][1]}-{cctv_id}")
        
col_image, col_output, col_report = st.columns([1.15, 1.1, 1.75], gap="small")

with col_image:
    with st.container(border=True):
        st.markdown(f'<p class="card-title">{CCTV_VIEW_TITLE_KO}</p>', unsafe_allow_html=True)
        for idx, cctv_id in enumerate(cctv_ids):
            with st.container(height=SYNC_ITEM_HEIGHT):
                st.markdown(f'<p class="cctv-item-title">{cctv_id}</p>', unsafe_allow_html=True)
                st.image(cctv_images[cctv_id][0], use_container_width=True)
            if idx < len(cctv_ids) - 1:
                st.markdown('<div class="section-sep"></div>', unsafe_allow_html=True)

with col_output:
    with st.container(border=True):
        st.markdown(f'<p class="card-title">{VLM_DESCRIPTION_TITLE_KO}</p>', unsafe_allow_html=True)
        for idx, cctv_id in enumerate(cctv_ids):
            result = results[cctv_id]
            with st.container(height=SYNC_ITEM_HEIGHT):
                st.markdown(f'<p class="cctv-item-title">{cctv_id}</p>', unsafe_allow_html=True)
                _render_alarm(result.alarm_level, result.risk_score, show_title=False)
                _render_description(result.description)
            if idx < len(cctv_ids) - 1:
                st.markdown('<div class="section-sep"></div>', unsafe_allow_html=True)

with col_report:
    with st.container(border=True):
        _render_report_two_columns(results[cctv_ids[0]])
