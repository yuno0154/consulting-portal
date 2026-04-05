# 성취평가제 점검단 통합 포털 - 사양서

## 1. 프로젝트 개요

- **프로젝트명**: 2026학년도 성취평가제 점검단 통합 포털
- **유형**: 랜딩 페이지 / 포털 사이트
- **핵심 기능**: 점검단 구성원 안내, 외부 리소스(패들렛, 드라이브, 성취기준 검색)へのクイックアクセス
- **목표 사용자**: 사곡고등학교 성취평가 종합점검단 구성원

---

## 2. URLs (Provided)

| 서비스 | URL |
|--------|-----|
| 성취평가 종합점검단 (균형편성) | https://docs.google.com/spreadsheets/d/1UljogUTq1RETDI3BF3uIDl1A_u_CVomz/edit |
| 성취기준 검색 (Streamlit) | https://sgh-streamslit-achive-base-eval-hfghb.streamlit.app/ |
| 패들렛 - 중학교 | https://padlet.com/sgh/2604072 |
| 패들렛 - 고등학교 | https://padlet.com/sgh/2604071 |
| 구글 드라이브 | https://drive.google.com/drive/folders/1UljogUTq1RETDI3BF3uIDl1A_u_CVomz |

---

## 3. 디자인 가이드

### 색상 팔레트
- **Primary**: `#1a365d` (Deep Navy)
- **Secondary**: `#2c5282` (Medium Blue)
- **Accent**: `#ed8936` (Warm Orange)
- **Background**: `#f7fafc` (Off-white)
- **Card Background**: `#ffffff`
- **Text Primary**: `#1a202c`
- **Text Secondary**: `#4a5568`
- **Border**: `#e2e8f0`

### 타이포그래피
- **Heading Font**: 'Noto Sans KR', sans-serif (weight: 700)
- **Body Font**: 'Noto Sans KR', sans-serif (weight: 400)
- **English/Numbers**: 'Inter', sans-serif

### 공간 시스템
- Base unit: 8px
- Card padding: 24px (3 units)
- Section gap: 64px (8 units)
- Card gap: 24px (3 units)
- Border radius: 12px

### 모션
- Hover transitions: 200ms ease-out
- Card hover: translateY(-4px) + subtle shadow
- Link hover: color transition + underline

---

## 4. 레이아웃 구조

```
┌─────────────────────────────────────────────────────┐
│  Header: 로고/타이틀 + 연도 배지                      │
├─────────────────────────────────────────────────────┤
│  Hero Section: 환영 메시지 + 점검단 소개              │
├─────────────────────────────────────────────────────┤
│  Quick Access Cards (2x2 Grid)                      │
│  ┌──────────────┐  ┌──────────────┐                 │
│  │ 점검단 편성   │  │ 성취기준 검색 │                 │
│  └──────────────┘  └──────────────┘                 │
│  ┌──────────────┐  ┌──────────────┐                 │
│  │ 중학교 자료   │  │ 고등학교 자료 │                 │
│  └──────────────┘  └──────────────┘                 │
├─────────────────────────────────────────────────────┤
│  Google Drive Banner CTA                            │
├─────────────────────────────────────────────────────┤
│  Footer: 학교명 + copyright                          │
└─────────────────────────────────────────────────────┘
```

### 반응형 전략
- Desktop: 2-column card grid
- Tablet (< 900px): 2-column maintained
- Mobile (< 600px): 1-column stack

---

## 5. 컴포넌트

### Header
- 로고/아이콘 (🎓 이모지 사용)
- 타이틀: "2026학년도 성취평가제 점검단"
- 연도 배지: "2026"

### Hero Section
- 메인 메시지: "성취평가제 점검단 포털에 오신 것을 환영합니다"
- 서브 메시지: 점검단 목적 안내
- 배경: subtle gradient overlay

### Quick Access Card
- 아이콘 (SVG 또는 이모지)
- 타이틀
- 설명 텍스트
- "바로가기" 버튼
- States: default, hover (elevated shadow + slight lift)

### Drive CTA Banner
- Drive 아이콘
- "필요한 파일은 구글 드라이브에서 확인하세요"
- 버튼: "드라이브 열기"

### Footer
- "사곡고등학교"
- "© 2026"

---

## 6. 트위aks / 기능

- 외부 링크 새 탭에서 열기 (`target="_blank"`)
- 카드 호버 시 시각적 피드백
- 부드러운 스크롤
- 파비콘: 🎓

---

## 7. 기술 선택

- **순수 HTML + CSS + Vanilla JS** (단일 파일 또는 분리)
- 외부 폰트: Google Fonts (Noto Sans KR, Inter)
- 아이콘: 내장 SVG 또는 이모지
- 배포: 정적 파일 (Netlify, GitHub Pages 등 호환)
