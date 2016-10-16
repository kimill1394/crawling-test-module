<?php


use App\Content;
use Illuminate\http\Request;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| This file is where you may define all of the routes that are handled
| by your application. Just tell Laravel the URIs it should respond
| to using a Closure or controller method. Build something great!
|
*/

Route::get('/', function () {
    $comments = Content::orderBy('num', 'asc')->get();

    return view('home', ['contents' => $comments]);
});


Route::post('/task', function (Request $request) {
    //
    $validator = Validator::make($request->all(), [
      'name' => 'required|max:255',
    ]);

    if ($validator->fails()) {
      return redirect('/')
              ->withInput()
              ->withErrors($validator);
    }

    $task = new Task;
    $task->name = $request->name;
    $task->save();

    return redirect('/');

});

Route::post('/update', function () {

  // 파이썬 실행해서 반환받은 객체로...

  return redirect('/executemodule');

  // return 불린반환해서 update.php가 성공(몇개 갱신) 혹은 실패를 띄울 수 있게
});
