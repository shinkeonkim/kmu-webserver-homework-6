# 과제 6 - Request 객체 실습

## 제출 내용

제출자: 20191564 김신건
Github (1점) : https://github.com/shinkeonkim/kmu-webserver-homework-6

### a. 제출 화면 1 – request 객체 실습 GET 실행화면(2점)

<img width="452" alt="image" src="https://github.com/user-attachments/assets/36607e53-9df8-4a15-bde1-9c2e53c40fbe" />

### b. 제출 화면 2 – request 객체 실습 POST 실행화면 (2점)

<img width="426" alt="image" src="https://github.com/user-attachments/assets/1de95ee0-fddf-496d-8a75-facd27711bda" />

### c. 제출 화면 3 – 파일 업로드 실행화면 (2점)

<img width="364" alt="image" src="https://github.com/user-attachments/assets/66ebd678-c865-4980-aed5-6c6d67044682" />

### d. 코드 완성 (13점)
#### d.1. request_info.html (10점)

항목별 내용
1.	method
2.	path
3.	full_url
4.	client_ip
5.	user_agent
6.	get_data
7.	post_data
8.	is_logged_in
9.	user
10.	session_value

전체 코드

```html
<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<title>Request 실습</title>
</head>
<body>
<h2>🔍 request 객체 실습</h2>
<p><strong>요청 방식:</strong> {{ method }} </p>
<p><strong>요청 경로:</strong> {{ path }}</p>
<p><strong>전체 URL:</strong> {{ full_url }}</p>
<p><strong>클라이언트 IP:</strong> {{ client_ip }}</p>
<p><strong>User-Agent:</strong> {{ user_agent }}</p>

<hr>
<h3>🧾 GET 요청 정보</h3>
<pre>{{ get_data }}</pre>

<h3>🧾 POST 요청 정보</h3>
<pre>{{ post_data }}</pre>

<hr>
<h3>🙍 사용자 정보</h3>
<p>로그인 여부: {{ is_logged_in }}</p>
{% if is_logged_in %}
    <p>사용자: {{ user }}</p>
{% else %}
    <p>익명 사용자입니다.</p>
{% endif %}

<hr>
<h3>📦 세션 데이터</h3>
<p>session['demo']: {{ session_value }}</p>

<hr>
<h3>📤 요청 테스트</h3>
<form method="get">
    <input type="text" name="search" placeholder="GET 요청 파라미터">
    <button type="submit">GET 전송</button>
</form>

<form method="post">
    {% csrf_token %}
    <input type="text" name="message" placeholder="POST 요청 내용">
    <button type="submit">POST 전송</button>
</form>
</body>
</html>
```


#### d.2. 4단계 템플릿 (upload_file.html) (1점)

항목별 내용
1.	uploaded_file_url

전체코드
```html
<h2>📤 파일 업로드</h2>
<form method="post" enctype="multipart/form-data">
    {% csrf_token %}
    <label>제목:</label><br>
    <input type="text" name="title"><br><br>
    <label>파일 선택:</label><br>
    <input type="file" name="file"><br><br>
    <button type="submit">업로드</button>
</form>

{% if uploaded_file_url %}
    <h3>업로드 결과</h3>
    <p><strong>제목:</strong> {{ title }}</p>
    <p><a href="{{ uploaded_file_url }}">업로드된 파일 보기</a></p>
{% endif %}
```

#### d.3. 5단계 뷰 만들기 (views.py) (2점)

항목별 내용
1.	request.FILES
2.	request.POST.get

전체 코드
```python
from django.shortcuts import render
from .models import UploadedFile

def file_upload_view(request):
    uploaded_file_url = None
    title = None

    if request.method == 'POST' and request.FILES.get('file'):
        file = request.FILES['file']
        title = request.POST.get('title', '')
        uploaded = UploadedFile.objects.create(title=title, file=file)
        uploaded_file_url = uploaded.file.url

    return render(request, 'request_test/upload_file.html', {
        'uploaded_file_url': uploaded_file_url,
        'title': title,
    })

```



