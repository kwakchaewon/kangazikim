package com.example.team11_project_front.API;

import com.example.team11_project_front.Data.ChangePetRequest;
import com.example.team11_project_front.Data.ChangePetResponse;

import retrofit2.Call;
import retrofit2.http.Body;
import retrofit2.http.Header;
import retrofit2.http.PATCH;
import retrofit2.http.PUT;
import retrofit2.http.Path;

public interface changePetApi {

    @PATCH("/accounts/api/pet/{id}/")
    Call<ChangePetResponse> getChangePetResponse (@Header("Authorization") String auth, @Path("id") String id, @Body ChangePetRequest changePetRequest);

}
