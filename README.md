# 2024-HeXA-최마진

# 키워드 추출 및 자동 검색

이 라이브러리는 PDF 파일의 텍스트 중 키워드를 추출, 위키피디아에서 검색하여 그 결과를 제공하는 기능을 수행합니다.

공부를 하면서 모르는 단어가 있거나 단어 의미를 정리하는 과제가 있을 때 일일이 단어를 검색하는 것이 귀찮았고, 그런 단어들은 주로 문장의 키워드가 된다는 것에서 착안하여 이 프로젝트를 진행했습니다.

KeyBERT를 이용하여 키워드를 추출하고, 이를 위키피디아에 검색하여 결과를 갖고 오는 방식을 채택했습니다.
위키피디아에서만 검색하는 것으로 한정되어 검색했을 때 나오지 않는 단어들도 있고 원하는 것과 다른 분야의 검색 결과가 나오는 문제점을 해결하지 못했으며 향후 다른 인공지능 모델과의 연계, 다양한 검색 엔진 등의 사용을 통해 이를 보완하고 체감되는 성능과 정확도, 만족도를 높일 수 있을 것이라 예상됩니다.


# 주요 함수

1. pdf2txt(pdf_path, start_page=None, end_page=None): 
   pdf 파일에서 텍스트를 추출하고 마침표를 기준으로 split하여 이를 list로 반환합니다. PyPDF2 라이브러리를 활용했습니다. 시작 페이지와 끝 페이지를 각각 start_page와 end_page에 정수로 제공해줄 수 있습니다.

2. ext_keyword(text_list, setting): 
   KeyBERT를 활용하여 키워드를 추출합니다. 문자열이 요소인 list를 text_list에, KeyBERT의 설정값을 dictionary 자료형으로 setting에 입력받습니다.

   *KeyBERT 설정 등은 다음 자료 참조: https://github.com/MaartenGr/KeyBERT

3. PlzNoMoreKeyTerm(PDF, BERTSETTING): 
   pdf 파일 관련 dictionary PDF와 KeyBERT 세팅값 dictionary BERTSETTING을 받아 PDF에서 키워드를 추출 및 위키피디아에서 검색하여 검색 결과 dictionary와 검색에 실패한 단어 list를 dictionary로 반환합니다.
