<?php

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




// Route::get('/', function () {
//     return view('welcome');
//     // retunr "Helloooooo!";
// });




use App\Task;
use Illuminate\http\Request;


Route::get('/', function () {
    //
    $tasks = Task::orderBy('created_at', 'asc')->get();
    return view('tasks', ['tasks'=>$tasks]);
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


Route::delete('/task/{task}', function (Task $task) {
    //
    $task -> delete();
    return redirect('/');
});
