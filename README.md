# 2024-HeXA-최마진

# 키워드 추출 및 자동 검색

이 라이브러리는 PDF 파일의 텍스트 중 키워드를 추출, 위키피디아에서 검색하여 그 결과를 제공하는 기능을 수행합니다.

공부를 하면서 모르는 단어가 있거나 단어 의미 정리 과제를 해야하는 등의 상황에서 일일이 단어를 검색하는 것이 귀찮았고, 그런 단어들은 주로 문장의 키워드가 된다는 것에서 착안하여 이 프로젝트를 진행했습니다.

KeyBERT를 이용하여 키워드를 추출하고, 이를 위키피디아에 검색하여 결과를 갖고 오는 방식을 채택했습니다.

# 주요 함수

1. pdf2txt(pdf_path, start_page=None, end_page=None)
   pdf 파일에서 텍스트를 추출하고 마침표를 기준으로 split하여 이를 list로 반환합니다. PyPDF2 라이
   브러리를 활용했습니다. 시작 페이지와 끝 페이지를 각각 start_page와 end_page에 정수로 제공해줄
   수 있습니다.

2. ext_keyword(text_list, setting)
   KeyBERT를 활용하여 키워드를 추출합니다. 문자열이 요소인 list를 text_list에, KeyBERT의 설정값
   을 dictionary 자료형으로 setting에 입력받습니다.

   *KeyBERT 설정 등은 다음 자료 참조: https://github.com/MaartenGr/KeyBERT
