(function(angular) {
    'use strict';
  var myApp = angular.module('MyApp', []);

  myApp.controller('MyCtrl', ['$scope', '$http', function($scope, $http) {
        $scope.house = {};
        $scope.house.OverallQual = 7;
        $scope.house.YearBuilt = 2003;
        $scope.house.YearRemodAdd = 2003;
        $scope.house.LotArea = 8450;
        $scope.house.LotFrontage = 65;
        $scope.house.GrLivArea = 1710;
        $scope.house.stFlrSF = 856;
        $scope.house.ndFlrSF = 854
        $scope.house.FullBath = 2;
        $scope.house.GarageCars = 2;
        $scope.house.Fireplaces = 0;
        $scope.price = 0;

        $scope.search = function () {
           $http.get('/api/predict', { params: $scope.house }).then(function(response) {
                console.log(response.data);
                $scope.price = response.data;
            }, function(failure) {
                console.log("failed :(", failure);
            });
        }
  $(document).ready(function(){

      $(window).scroll(function(){

          if($(document).scrollTop() > 0) {
              var newPos = $(document).scrollTop() + 0 ;
              $('.mPrice').css( {top:newPos});
          }

          else {
              $('.mPrice').css( {top:0});
          }
      })
  })
  }]);

})(window.angular);
