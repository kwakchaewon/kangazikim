package com.example.team11_project_front.MyPage;

import android.content.Intent;
import android.content.SharedPreferences;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ListView;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.widget.AppCompatButton;

import com.example.team11_project_front.API.petlistApi;
import com.example.team11_project_front.API.pictureApi;
import com.example.team11_project_front.API.refreshApi;
import com.example.team11_project_front.ChangeHospitalActivity;
import com.example.team11_project_front.Data.MypostlistResponse;
import com.example.team11_project_front.Data.PetInfo;
import com.example.team11_project_front.Data.PetlistResponse;
import com.example.team11_project_front.Data.PictureResponse;
import com.example.team11_project_front.Data.PostedList;
import com.example.team11_project_front.Data.RefreshRequest;
import com.example.team11_project_front.Data.RefreshResponse;
import com.example.team11_project_front.MainActivity;
import com.example.team11_project_front.QnA.ArticleActivity;
import com.example.team11_project_front.R;
import com.example.team11_project_front.RetrofitClient;

import java.util.ArrayList;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class PostedActivity extends AppCompatActivity {

    ArrayList<PostedList> list;
    ListView listView;

    private ArrayList<PostedList> postInfos;

    private RetrofitClient retrofitClient;
    private com.example.team11_project_front.API.mypostlistApi mypostlistApi;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_posted);
        retrofitClient = RetrofitClient.getInstance();
        mypostlistApi = RetrofitClient.getRetrofitMypostlistInterface();
        listView = (ListView) findViewById(R.id.postedList);

        mypostlistApi.getMypostlistResponse("Bearer " + getPreferenceString("acessToken")).enqueue(new Callback<ArrayList<MypostlistResponse>>() {
            @Override
            public void onResponse(Call<ArrayList<MypostlistResponse>> call, Response<ArrayList<MypostlistResponse>> response) {
                Log.d("retrofit", "Data fetch success");
                if (response.code() == 401) {
                    RefreshRequest refreshRequest = new RefreshRequest(getPreferenceString("refreshToken"));
                    refreshApi refreshApi = RetrofitClient.getRefreshInterface();
                    refreshApi.getRefreshResponse(refreshRequest).enqueue(new Callback<RefreshResponse>() {
                        @Override
                        public void onResponse(Call<RefreshResponse> call, Response<RefreshResponse> response) {
                            if(response.isSuccessful() && response.body() != null){
                                setPreference("acessToken", response.body().getAccessToken());
                                Toast.makeText(PostedActivity.this, "토큰이 만료되어 갱신하였습니다. 다시 시도해주세요.", Toast.LENGTH_LONG).show();
                            }else{
                                Toast.makeText(PostedActivity.this, "토큰 갱신에 실패하였습니다. 관리자에게 문의해주세요.", Toast.LENGTH_LONG).show();
                            }
                        }

                        @Override
                        public void onFailure(Call<RefreshResponse> call, Throwable t) {
                            Toast.makeText(PostedActivity.this, "토큰 갱신에 실패하였습니다. 관리자에게 문의해주세요.", Toast.LENGTH_LONG).show();
                        }
                    });
                } else if (response.isSuccessful() && response.body() != null && response.body().size() > 0) {
                    ArrayList<MypostlistResponse> mypostlistResponses = response.body();
                    // PetlistResponse 객체를 PetInfo 객체로 변환하여 리스트에 추가

                    postInfos = new ArrayList<>();
                    listView.setAdapter(null);
                    for (MypostlistResponse mypostlistResponse : mypostlistResponses) {
                            String id = mypostlistResponse.getId();
                            String title = mypostlistResponse.getTitle();
                            String contents = mypostlistResponse.getContents();
                            String created_at = mypostlistResponse.getCreated_at();
                            String updated_at = mypostlistResponse.getUpdated_at();
                            String pictureid = mypostlistResponse.getPictureid();
                            PostedList postInfo = new PostedList(id, title,contents,created_at,updated_at,pictureid);
                            postInfos.add(postInfo);
                    }
                    PostedAdapter adapter = new PostedAdapter(PostedActivity.this, postInfos);
                    listView.setAdapter(adapter);
                    adapter.notifyDataSetChanged();
                }
            }

            public void onFailure(Call<ArrayList<MypostlistResponse>> call, Throwable t) {
                Log.e("postedActivity", t.getMessage());
                Toast.makeText(PostedActivity.this, "동물 정보를 제대로 가져오지 못 했습니다.", Toast.LENGTH_LONG).show();
            }
        });


        //뒤로가기 버튼 클릭 시 다시 마이페이지로 돌아감
        AppCompatButton btn = (AppCompatButton) findViewById(R.id.backbtn);
        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                finish();

            }
        });

    }
    public void onResume() {
        super.onResume();

        listView.setOnItemClickListener(new AdapterView.OnItemClickListener() {
            @Override
            public void onItemClick(AdapterView parent, View v, int position, long id) {
                Intent intent = new Intent(PostedActivity.this, ArticleActivity.class);
                /* putExtra의 첫 값은 식별 태그, 뒤에는 다음 화면에 넘길 값 */
                intent.putExtra("qId", postInfos.get(position).getId());
                intent.putExtra("title", postInfos.get(position).getTitle());
                intent.putExtra("writer", getPreferenceString("first_name"));
                intent.putExtra("date", postInfos.get(position).getCreated_at());
                intent.putExtra("contents", postInfos.get(position).getContents());
                intent.putExtra("photo", postInfos.get(position).getPictureid());
                startActivity(intent);
            }
        });


    }

    public String getPreferenceString(String key) {
        SharedPreferences pref = getSharedPreferences("DATA_STORE", MODE_PRIVATE);
        return pref.getString(key, "");
    }

    public void setPreference(String key, String value){
        SharedPreferences pref = getSharedPreferences("DATA_STORE", MODE_PRIVATE);
        SharedPreferences.Editor editor = pref.edit();
        editor.putString(key, value);
        editor.apply();
    }
}