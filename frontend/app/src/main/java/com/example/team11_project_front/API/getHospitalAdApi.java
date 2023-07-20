package com.example.team11_project_front.API;

import com.example.team11_project_front.Data.HospitalAdResponse;
import com.example.team11_project_front.Data.HospitalResponse;

import java.util.List;

import retrofit2.Call;
import retrofit2.http.GET;
import retrofit2.http.Header;

public interface getHospitalAdApi {
    //@통신 방식("통신 API명")
    @GET("/accounts/api/hospital-ad/")
    Call<HospitalAdResponse> getHospitalResponse(@Header("Authorization") String auth);
}