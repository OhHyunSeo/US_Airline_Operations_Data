# 🛫 US Airline Operations Data Analysis

[![Python Version](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)

## 🔍 소개

이 프로젝트는 미국 항공사 운항 데이터를 기반으로 지연 원인을 분석하고  
지연 최적화, 항공기 기령 분석 등 다양한 관점에서 데이터를 탐색하는 데이터 분석 프로젝트입니다.

---

## 📊 주요 기능

- ✈️ 항공 지연 최적화 분석
- 🛬 항공기 기령(Plane Age) 기반의 운항 특성 분석
- 🧼 데이터 병합 및 전처리 처리 (`new_data.py`)
- 🧪 한국어 텍스트 분석 실험용 `konlpy_test.py` 포함 (실험적)

---

## 📁 프로젝트 구조

```
📁 US_Airline_Operations_Data-master/
│
├── delay_optimization.py     # 항공 지연 최소화를 위한 최적화 분석
├── konlpy_test.py            # 한국어 형태소 분석 테스트용 (KoNLPy)
├── new_data.py               # 새로운 항공 데이터 통합 및 전처리
├── plane_age.py              # 항공기 기령 분석
└── __pycache__/              # 파이썬 캐시 파일
    └── konlpy.cpython-311.pyc
```

---

## 🚀 실행 방법

### 1. 환경 설정

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt  # 필요 시 수동 생성
```

### 2. 실행 예시

```bash
python delay_optimization.py     # 지연 최적화 분석 실행
python plane_age.py              # 항공기 기령 분석 실행
python new_data.py               # 데이터 병합 및 전처리
```

---

## 📈 분석 예시

- 지연 시간 최소화 모델 구현
- 항공기 기령이 지연에 미치는 영향 분석
- 다중 연도 항공 운항 데이터 통합 및 탐색

---

## 🧑‍💻 기여 방법

1. 이 레포지토리를 포크하세요.
2. 새 브랜치를 생성하세요: `git checkout -b feature/기능명`
3. 변경사항을 커밋하세요: `git commit -m "Add 기능"`
4. 브랜치에 푸시하세요: `git push origin feature/기능명`
5. Pull Request를 생성하세요.

---

## 📄 라이선스

이 프로젝트는 MIT 라이선스를 따릅니다.
