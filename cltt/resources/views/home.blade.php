



@include(errors.commonerror)
<div class="contents">
  <div class="contents_heading">
    여기부터 컨텐츠
  </div>
  <div class="contents_body">

    <table class="table table_contents">
      <thead>
        <th class="table-head">title</th>
        <th class="table-head">url</th>
        <th class="table-head">num</th>
      </thead>
      <tbody>
        @foreach ($contents as $content)
          <tr>
            <td class="table-text">
              <div>{{$content->title}}</div>
              <div>{{$content->url}}</div>
              <div>{{$content->num}}</div>
            </td>
          </tr>
        @endforeach
      </tbody>
    </table>

  </div>
</div>
