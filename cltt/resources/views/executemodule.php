

<?php


$crawling_tag = array();

$crawling_tag['serial_number'] = 1;
$crawling_tag['url'] = "http://news.naver.com/main/list.nhn?mode=LS2D&mid=shm&sid1=105&sid2=226";
$crawling_tag['major_tag'] = "ul > li > dl";
$crawling_tag['minor_tag'] = "div[id=articleBodyContents]";

$crawling_tag['serial_number'] = 2;
$crawling_tag['url'] = "http://www.ittoday.co.kr/news/articleList.html?sc_section_code=S1N11&amp;view_type=sm";
$crawling_tag['major_tag'] = "td[class=ArtList_Title]";
$crawling_tag['minor_tag'] = "td[class=view_r]";

$crawling_tag['serial_number'] = 3;
$crawling_tag['url'] = "http://blog.naver.com/PostList.nhn?blogId=smashhit&from=postList&categoryNo=17";
$crawling_tag['major_tag'] = "div[class='se_doc_viewer se_body_wrap se_theme_transparent ']";
$crawling_tag['minor_tag'] = "div[class=se_post_function]";

array_push($crawling_tag_arr,$crawling_tag);





function content_data_input(){
  global $crawling_tag_arr;


  for($i = 0 ; $i < count($crawling_tag_arr) ; $i++){
    $reverse_array = array();

    $total_parameter = "/Users/Lee/Desktop/Python/crawling_module_ver_1.py {$crawling_tag_arr[$i]['serial_number']} \"{$crawling_tag_arr[$i]['url']}\" \"{$crawling_tag_arr[$i]['major_tag']}\" \"{$crawling_tag_arr[$i]['minor_tag']}\"";

    $command = escapeshellcmd($total_parameter);
    $output_array = json_decode(exec($command), true);

    $serial_number = $i + 1;

    $query = "select url from content_db where content_number = (select max(content_number) from content_db group by serial_number having serial_number = :serial_number)";
    $stmt = $pdo->prepare($query);
    $stmt ->bindParam(":serial_number",$serial_number, PDO::PARAM_INT);
    /* 이거 무슨 방법이 있댔는데.. 교수님 수업 참고!*/
    $stmt ->execute();

    $result = $stmt->fetch(PDO::FETCH_ASSOC);

    foreach($output_array as $dict_array){
      if($result['url'] != $dict_array['url']){
        array_unshift($reverse_array,$dict_array);
      }else{
        break;
      }
    }


    foreach($reverse_array as $result_array){
      $content = new Content;
      $content->title = $result_array->title;
      $content->url = $result_array->url;
      $content->num = $result_array->serial_number;
      $content->save();
    }

  }

}






content_data_input();


?>
