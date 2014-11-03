app.controller("EmprestarCtrl", function($scope){
    $scope.mostrarForm = false;
    $scope.emprestars = emprestars;
    $scope.toggleShow= function () {
        $scope.mostrarForm = !$scope.mostrarForm;
    }
});

app.directive("emprestarform", function($http){
   return{
       restrict: "E",
       transclude: true,
       templateUrl: "/static/emprestar/html/form.html",
       scope:{
         toggleshow: "&",
       },
       link: function(scope, elm, attrs){

           scope.salvar = function() {
               var data = {pertence: scope.pertence, nome: scope.nome, descricao: scope.descricao, emprestar: scope.emprestar};
               $http.post("/emprestars/rest/save", data);
           };
       }
   };
});