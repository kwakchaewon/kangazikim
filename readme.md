## 🐶 서비스 소개
반려동물 헬스케어 플랫폼 **강아지킴** ([소개영상](https://www.youtube.com/watch?v=77HRdebU-Z0&feature=youtu.be)) 입니다.
<br/>
AI 피부 진단, 온라인 상담, 이력관리, 수의사 연결 등의 서비스를 제공합니다.
<br/>
<br/>
![11조  3기 11조 소개 이미지](https://github.com/kwakchaewon/kangazikim/assets/74225015/7326aa89-8b94-48a3-91bc-d6f2388c371d)

### 🦮 반려인

1. 반려견의 피부 질환 의심부위를 찍고 업로드한다.<br/>
2. 진단 결과를 AI가 판단해 알려준다.<br/>
    2-1. AI가 예상한 질환에 대한 ChatGPT의 설명을 볼 수 있다.<br/>
3. 추가적인 상담이 필요한 경우 Q&A 게시판에 질문을 올린다. <br/>
    3-1. 질문이 작성되면 자동으로 질문에 대한 ChatGPT 답변이 작성된다.<br/>
    3-2. 추가적으로 작성된 수의사의 답변을 확인한다.<br/>
4. 수의사 정보란의 상담 버튼을 클릭해 전화를 통해 상담하거나 예약한다<br/>

### 🏥 수의사

1. 회원가입 시 추가적으로 수의사 관련 정보를 입력한다.
2. Q&A 게시판에 올라오는 질문에 대한 답변을 작성한다.
3. 답변 개수이 많을수록 메인 페이지 광고에 더 많이 노출된다.
<br/>

## 🛠  사용기술

### **Frontend**
- Android Studio (Java)

### **Backend**
- Django Rest Framework (Python)

### **Infra**
- Server: AWS EC2(uwsg & Nginx)
- DB: AWS RDS (MYSQL)
- Storage: AWS S3
<br/>

## ✍️ 담당 업무
1. DB 설계 및 구현
2. AWS 서버 배포:  EC2 (uWSGI, Nginx), RDS (MYSQL), S3 기반
3. Django RestFramework 기반 API 구현<br/>
   3-1. Django Rest auth, jwt 토큰 기반 로그인, 회원가입 구현<br/>
   3-2. Pydenticon 기본 프로필 이미지 적용<br/>
   3-3. Chat gpt api 자동 답변 기능 최적화: 쓰레딩 모듈 적용, 지연시간 10초 감소<br/>
   3-4. Question, Answer, Pet, Hostpital CRUD API 구현<br/>
4. 관리자 페이지 커스터마이징
<br/>

<!--
## 😊 Members
곽채원, 김민수, 박예은, 류홍규, 박지환, 이윤열, 이태훈
<br/>
<br/>
-->
## 🖥 산출물

### ✅ 서비스 아키텍쳐

![전체 아키텍처](https://github.com/AIVLE-School-Third-Big-Project/Team11-Project/assets/76936390/13626f8b-9a5f-4337-9477-b857a13bda9c)
<!--
- **Frontend**는 **Android Studio**를 사용하여 **Android APP**을 구현.
- **Frontend**에서 **Backend**로의 통신은 **Retrofit2**로 구현.
- **Backend**는 **Django REST Framwork** 를 사용하여 **REST API**를 구현.<br/>
- **Backend 서버**의 경우 **AWS EC2**를 사용하고, DB와 Storage를 **RDS**와 **S3**로 분리.
- DB는 **MySQL**을 사용했고, API 서버는 **NGINX**로 배포.
-->

### ✅ ERD 
![ERD](https://github.com/AIVLE-School-Third-Big-Project/Team11-Project/assets/76936390/b04ee526-a2e9-48a4-86de-5c6ad67e061d)

### ✅ 서비스 플로우 
![서비스 플로우](https://github.com/AIVLE-School-Third-Big-Project/Team11-Project/assets/76936390/4c5aac06-ddcb-4ef2-bc6b-1dc822403556)

### ✅ UI/UX 설계
![UI/UX 설계](https://github.com/AIVLE-School-Third-Big-Project/Team11-Project/assets/30362867/62fc0f89-6c0c-4285-867f-97055b0bc3c4)

<!--
### ✅ API 명세서
API에 대한 내용들은 Notion에 API 명세서를 작성하여 관리했습니다.
-->
<br/>


## 💻 상세 개발 내역
### ✅ 로그인/회원가입
- Django REST Auth, 를 활용하여 기본적인 회원가입, 로그인, 로그아웃 등을 구현
- AbstractUser을 상속받아 필요 필드 추가 (profile_img, is_vet)
- property 추가: 프로필 사진 없을 시 pydenticon 적용

✔️ **JWT Token**
로그인할 때에는 `AccessToken` 과 `RefreshToken` 발급

✔️ **기타 User 관련 API**
- 회원가입 시 Email 중복 확인, 비밀번호를 잊었을 때 Email을 전송하는 비밀번호 초기화 API
- 비밀번호 `SHA256` 암호화

|비밀번호 초기화 메일|비밀번호 초기화 화면|
|---|---|
|![image](https://github.com/AIVLE-School-Third-Big-Project/Team11-Project/assets/76936390/ea45c4c8-2a2a-4c51-bb27-4bf21f1f8c64)|![image](https://github.com/AIVLE-School-Third-Big-Project/Team11-Project/assets/76936390/2899f85b-1dea-4f25-b664-033b187f4f4f)|
<br/>

### ✅ Pet API
- 로그인 된 유저의 반려동물 정보 조회 및 등록하는 Pet API<br/>
- Pet 테이블은 User 와 외래키로 연결.<br/><br/>


### ✅ Hospital API
- 수의사일 경우, 병원 정보 등록하는 Hospital API<br/>
- Hospital 은 UserID와 외래키로 연결.<br/>
- 로그인 정보를 바탕으로 데이터 생성 시 자동으로 UserID를 가져옴<br/>

**✔ Hospital 광고 API**
- 메인 화면에 답변 작성이 우수한 병원 광고.<br/>
- Rank 알고리즘이 없어 ChatGPT를 제외한 병원 리스트 랜덤하게 표기 <br/><br/>


### ✅ Picture API
- 환부 사진과 그에 대한 AI 진단 결과를 등록 및 조회 Picture API<br/>
- Picture 테이블은 User 테이블, Pet 테이블과 외래키로 연결.<br/>
- 환부 사진 등록 시 PetID 를 통해 자신의 반려견을 등록 및 자신의 반려견 별로 결과를 조회<br/>
- permission_classes 로 작성자 외에 CUD 못하도록 권한 제한<br/><br/>

### ✅ Question API
- 진단 결과에 대한 추가적인 상담글을 등록하는 Question API.<br/>
- Question 테이블은 User 테이블, Picture 테이블과 외래키로 연결.<br/>
- permission_classes 로 CUD는 유저 본인만 가능하도록 권한 제한<br/>

**✔ 비동기적 gpt 답변 등록**

- Question 등록 시, 질문 내용 기반으로 Chatgpt 답변 생성 (openai_api 기반) <br/>
- threading module을 통한 최적화: 10초 이상의 자동 답변 생성 지연 시간 감소

**✔ 답변 갯수 조회**

- Serializer 집계 함수 답변 갯수를 조회<br/>

**✔ Pagenation 적용**

- PageNumberPagination 기반 기본적인 Pagenation을 적용<br/>

**✔ 검색 기능 적용**

- 제목과 내용을 기반 검색<br/><br/>


### ✅ Answer API
- 상담글에 대한 수의사와 ChatGpt의 답변을 받는 Answer API 구현<br/>
- Answer 테이블은 User, Question 테이블과 외래키로 연결.<br/>
- '질문에 대한 답변' 이라는 성격에 맞게 API path를 "question/<questionid>/answer" 로 설정<br/>
- 수의사일 경우에만 답변을 달 수 있도록 권한 제한<br/><br/>

### ✅ AWS 서버 배포
- uwsgi와 Nginx를 통해 배포
- Nginx 배포 시, AI모델이 돌아가면서 동시에 다른 API 요청이 들어오면 서버가 다운되는 문제 발생 > uwsgi 서버 부하 관련 설정을 변경
<br/><br/>

<!--
### ✅ 아키텍처, ERD, Service Flow, UI/UX 흐름도 

|아키텍처|ERD|Service Flow|UI/UX 흐름도|
|---|---|---|---|
|![architecture](https://github.com/AIVLE-School-Third-Big-Project/Team11-Project/assets/30362867/44f10a37-b3cb-4b75-b071-91c8d7165565)|![erd](https://github.com/AIVLE-School-Third-Big-Project/Team11-Project/assets/76936390/b04ee526-a2e9-48a4-86de-5c6ad67e061d)|![서비스 플로우](https://github.com/AIVLE-School-Third-Big-Project/Team11-Project/assets/76936390/4c5aac06-ddcb-4ef2-bc6b-1dc822403556)|![UI/UX](https://github.com/AIVLE-School-Third-Big-Project/Team11-Project/assets/30362867/62fc0f89-6c0c-4285-867f-97055b0bc3c4)|
<br/>
-->

### ✅ AI
- 무증상 및 6가지의 피부 질환을 포함 7 Class 분류

![ppt4](https://github.com/AIVLE-School-Third-Big-Project/Team11-Project/assets/124108688/50c97e0d-654f-4874-816f-b8a67f0dee26)


✔️ **데이터**  
[AI HUB 반려동물 피부 질환 데이터](https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=realm&dataSetSn=561)를 사용했습니다.  
~~AI HUB 데이터에서 무증상 데이터를 제공하지 않고 있어 **DALLE API**를 사용해 ***무증상 데이터를 생성***하여 학습을 진행했습니다.~~  
- 뒤늦게 반려동물 무증상 데이터가 AI HUB에 업데이트되었고 이를 6월 23일에 확인 후 해당 데이터로 학습
- 모델의 성능이 좋지 않아 데이터를 확인해본 결과, 중복되는 데이터가 여러 클래스에 들어가있고 개수를 채우기 위해 같은 이미지가 반복되는 등의 문제를 확인
- 중복되는 데이터를 삭제하고 각 피부 질환의 특질에 따라 데이터를 직접 분류하는 정제 과정을 거침


✔️ **모델**  
- pretrained InceptionV3 사용.<br>


**✔ 모델 선정과정**
- Unet

![ppt3](https://github.com/AIVLE-School-Third-Big-Project/Team11-Project/assets/124108688/bdca5b23-8c5f-4a9c-9c15-505effc30062)

- 마스킹 이미지가 작은 경우 환부로 인식하기 어려운 문제 발생<br>
- unet에서는 픽셀 주위의 local region(패치)를 입력으로 각 픽셀의 label을 예측하는데, 패치가 작아 환부에 대한 localization 성능은 향상되었으나(98.81%의 accuracy), 네트워크는 매우 작은 context만 보게 되어 context 파악 성능이 매우 떨어지는 것을 확인 <br>
(Unet의 경우 localization accuracy와 context(sementaic information) 사이는 trade off 관계)



- YOLOv5

![ppt7](https://github.com/AIVLE-School-Third-Big-Project/Team11-Project/assets/124108688/10d68a2b-7670-4d6b-b229-661c915dbe29)

마찬가지로 바운딩 박스가 작은 경우 객체 인식 자체를 잘 못하는 문제<br>
데이터 특성상 세그멘테이션 모델보다는 환부 주변 부위까지 함께 고려하는 분류 모델이 적합​하다고 판단


- 사전학습 분류모델 검토

VGG16, MobileNetV3, EfficientNet-B0, Resnet-50, InceptionV3, Inception-resnetV2모델 검토<br>
![ppt8](https://github.com/AIVLE-School-Third-Big-Project/Team11-Project/assets/124108688/32346055-04b9-4afb-a377-f5b620610f2a)

InceptionV3, Inception-resnetV2의 성능이 가장 좋은 것을 확인.<br>
모바일 환경을 고려하여 좀 더 가벼운 모델인 InceptionV3로 최종 결정<br>


**✔ 고도화 및 최적화**

- 고도화

데이터셋 정제과정을 거치다보니 줄어든 데이터를 보강하기위해 Data augmentation기법을 활용.<br>
모델 학습속도를 높이고 과적합를 방지하기 위해 213layer까지 동결하되 Batchnormalization layer는 동결하지 않았음<br>

- 최적화

기존의 313layer중 layer갯수를 줄여가면서 성능변화를 확인<br>
256layer까지는 밑단을 삭제하여도 유사한 성능을 내는 것을 확인<br>
이를 채택한 결과 기존의 Parameter기준 약 42% 경량화 (2219만-->1278만)<br>

![ppt11](https://github.com/AIVLE-School-Third-Big-Project/Team11-Project/assets/124108688/c7d81b7b-db1d-476b-be63-fbc7fa564a0a)

![ppt12](https://github.com/AIVLE-School-Third-Big-Project/Team11-Project/assets/124108688/9d5f36f7-cab1-49b1-bbef-fda07efbef42)
<br/>
<br/>

## 👀 서비스 화면

<img src="https://github.com/AIVLE-School-Third-Big-Project/Team11-Project/assets/76936390/4b99a6be-bd6e-4aab-8190-e6d3ca9404c4" width="200"/><br>
어플리케이션을 설치<br><br>
<img src="https://github.com/AIVLE-School-Third-Big-Project/Team11-Project/assets/76936390/453031bb-dfc6-40e4-bbfc-7a384078aa4a" width="200"/>&nbsp;&nbsp;
<img src="https://github.com/AIVLE-School-Third-Big-Project/Team11-Project/assets/76936390/3823bb12-4e47-4cc7-be66-c7b934c31d60" width="200"/><br>
아이콘을 눌러 실행 후 로그인 화면으로 이동<br><br>
<img src="https://github.com/AIVLE-School-Third-Big-Project/Team11-Project/assets/76936390/6831d554-d51a-408c-b547-580ba1814a9e" width="200"/>&nbsp;&nbsp;
<img src="https://github.com/AIVLE-School-Third-Big-Project/Team11-Project/assets/76936390/f68bbec1-ca2a-4ad0-9c78-f1c211e31c3d" width="200"/>&nbsp;&nbsp;
<img src="https://github.com/AIVLE-School-Third-Big-Project/Team11-Project/assets/76936390/cb6b7305-88ff-44b7-b899-0cdc5cbc0156" width="200"/><br>
회원가입 버튼 클릭 <br>
수의사 버튼 클릭 시, 병원 정보 입력 가능 <br>
약관 확인하기 문구 클릭 후 약관 확인<br><br>
<img src="https://github.com/AIVLE-School-Third-Big-Project/Team11-Project/assets/76936390/c2b0865f-a1df-4cfd-a43f-cd71d4dc6ff0" width="200"/>&nbsp;&nbsp;
<img src="https://github.com/AIVLE-School-Third-Big-Project/Team11-Project/assets/76936390/c827ef3c-9d2b-4237-8ada-5f2629fcc256" width="200"/><br>
비밀번호 초기화 클릭 시, 이메일 입력 후 위와 같은 메일 발송<br><br>
<img src="https://github.com/AIVLE-School-Third-Big-Project/Team11-Project/assets/76936390/e004ce20-450d-4ba0-b02a-9f17fa9225f3" width="200"/>&nbsp;&nbsp;
<img src="https://github.com/AIVLE-School-Third-Big-Project/Team11-Project/assets/76936390/8be44c4d-68e8-4ef6-88c5-8be4fde07b02" width="200"/>&nbsp;&nbsp;
<img src="https://github.com/AIVLE-School-Third-Big-Project/Team11-Project/assets/76936390/72ff5aee-0ddb-4725-b214-e89d2b0267d9" width="200"/><br>
로그인/회원가입 성공 시, 메인화면으로 이동<br>
답변을 많이 한 병원들 중 하나가 하단에 노출<br>
설문조사 버튼 클릭 시, 구글폼으로 이동<br>
전화상담 버튼 클릭 시, 휴대전화의 전화 화면으로 이동 및 병원 번호 다이얼 표기<br>
<img src="https://github.com/AIVLE-School-Third-Big-Project/Team11-Project/assets/76936390/456ecb12-efa8-443e-b28e-6ec6f56494cd" width="200"/>&nbsp;&nbsp;
<img src="https://github.com/AIVLE-School-Third-Big-Project/Team11-Project/assets/76936390/01d5c984-8e11-467d-9e98-ffb9a0f3095b" width="200"/>&nbsp;&nbsp;
<img src="https://github.com/AIVLE-School-Third-Big-Project/Team11-Project/assets/76936390/48c2b3cd-8f2c-4fdc-b6e1-ee0979f2198c" width="200"/><br>
메인화면에서 피부 질환 진단하기 버튼 클릭 시, 반려동물 선택 화면 <br>
사진을 촬영 또는 갤러리에서 선택 후 이미지 업로드<br>
첫번째 사진은 선택 전 화면, 두번째 사진은 사진촬영 버튼으로 넘어간 화면, <br>
세번째 사진은 사진선택 버튼으로 넘어간 화면, 마지막은 선택 후 화면<br><br>
<img src="https://github.com/AIVLE-School-Third-Big-Project/Team11-Project/assets/76936390/914a38d9-9988-425b-8b5b-f8488c078c36" width="200"/>&nbsp;&nbsp;
<img src="https://github.com/AIVLE-School-Third-Big-Project/Team11-Project/assets/76936390/77db1b3d-5f7c-4964-9262-0d9d0d958894" width="200"/>&nbsp;&nbsp;
<img src="https://github.com/AIVLE-School-Third-Big-Project/Team11-Project/assets/76936390/de1d4abe-57b2-4bc8-b883-0ba515a472ff" width="200"/>&nbsp;&nbsp;
<img src="https://github.com/AIVLE-School-Third-Big-Project/Team11-Project/assets/76936390/86b4fae0-4844-40a4-9e28-a6b4ed5b9e48" width="200"/>&nbsp;&nbsp;
<img src="https://github.com/AIVLE-School-Third-Big-Project/Team11-Project/assets/76936390/899930f3-c76e-4dbe-b37b-56e48c1c67dc" width="200"/><br>
사진을 선택한 후 사진 등록 버튼 클릭 시, 진단 결과를 보여주는 화면으로 이동 <br>
로딩 후 첫번째 사진 처럼 AI 진단 결과 표기<br>
두번째 사진처럼 설명이 도착했다고 메시지 표기<br>
이후 AI 진단 버튼 클릭 시, 진단 결과에 대한 GPT의 설명 표기 <br>
진단 결과가 나온 뒤 질문 등록 버튼 클릭 시, 마지막 사진처럼 질문을 등록할 수있는 화면 표기 <br><br>
<img src="https://github.com/AIVLE-School-Third-Big-Project/Team11-Project/assets/76936390/f22d2252-0d53-42e1-9bef-7cc96609905f" width="200"/>&nbsp;&nbsp;
<img src="https://github.com/AIVLE-School-Third-Big-Project/Team11-Project/assets/76936390/8183778f-0e24-4c42-8e94-d3f3c7165719" width="200"/>&nbsp;&nbsp;
<img src="https://github.com/AIVLE-School-Third-Big-Project/Team11-Project/assets/76936390/2c7b2f79-35d2-44f4-98cc-8206dbd01add" width="200"/>&nbsp;&nbsp;
<img src="https://github.com/AIVLE-School-Third-Big-Project/Team11-Project/assets/76936390/ca14a236-b88c-48b2-a950-220d69b08c6f" width="200"/>&nbsp;&nbsp;
<img src="https://github.com/AIVLE-School-Third-Big-Project/Team11-Project/assets/76936390/f0920683-b443-4a8d-9cf1-9ce93a1e26a1" width="200"/>&nbsp;&nbsp;<br>
질문 등록 후 메인화면<br>
하단 네비게이션의 질문게시판 버튼 클릭 시, 게시판 화면.<br>
게시물 클릭 시, 찍은 사진, AI진단결과, GPT의 설명, 질문 표기<br>
하단에 GPT 진단결과와 질문을 기반으로 답변 표기 <br>
추가적인 수의사 분들이 답변 가능<br>
게시글을 검색 기능<br><br>

<img src="https://github.com/AIVLE-School-Third-Big-Project/Team11-Project/assets/76936390/5779bca9-2236-43ff-b11d-2f87782a2374" width="200"/>&nbsp;&nbsp;
<img src="https://github.com/AIVLE-School-Third-Big-Project/Team11-Project/assets/76936390/d7f5bb1b-8f5a-4702-9910-e4778021ff9c" width="200"/>&nbsp;&nbsp;
<img src="https://github.com/AIVLE-School-Third-Big-Project/Team11-Project/assets/76936390/5aefb230-0f73-4436-ab83-ba962bd0b7bf" width="200"/>&nbsp;&nbsp;
<img src="https://github.com/AIVLE-School-Third-Big-Project/Team11-Project/assets/76936390/230b3500-9d88-4276-aaaf-e4011de83940" width="200"/>&nbsp;&nbsp;
<img src="https://github.com/AIVLE-School-Third-Big-Project/Team11-Project/assets/76936390/6f9ce39d-7506-41b9-9be6-4c8a9afcb963" width="200"/>&nbsp;&nbsp;<br>

메인화면이나 Q&A게시판에서 하단 네비게이션의 내 정보 버튼 클릭 시, 첫번째 사진과 같은 화면 이동.<br>
해당 화면의 프로필 사진 변경 버튼 클릭 시, 유저 프로필 사진 변경 가능<br>
플러스 모양을 눌러 내 반려동물을 추가<br>
세번째와 다섯번째 사진처럼 수정버튼 클릭 시, 반려동물, 병원정보 수정화면으로 이동.<br>
삭제 버튼, 로그아웃 문구, 회원탈퇴 문구 클릭 시, 확인화면으로 재확인 후 기능 수행<br><br>

<img src="https://github.com/AIVLE-School-Third-Big-Project/Team11-Project/assets/76936390/833bf7b7-de8a-428b-8df2-25f3e203a0db" width="200"/><br>
내 정보 화면에서 게시글 작성 내역 문구를 누르거나 메인화면에서 나의 질문 버튼 클릭 시, 내가 작성한 질문글 목록 표기 <br>
클릭 시, QnA게시글 화면으로 이동 후 해당 게시글 상세 표기
