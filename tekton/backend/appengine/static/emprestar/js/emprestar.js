app.controller("EmprestarCtrl", function($scope){
    $scope.mostrarForm = false;
    $scope.emprestars = emprestars;
    $scope.toggleShow= function () {
        $scope.mostrarForm = !$scope.mostrarForm;
    }
});

app.factory('emprestarApi', function($http){

    var url_salvar_pertence = "/emprestars/rest/save";

    var salvar_pertence = function(pertence, nome, descricao, emprestar){
        var data = {
            pertence: pertence,
            nome: nome,
            descricao: descricao,
            emprestar: emprestar
        };

        return $http.post(
            url_salvar_pertence,
            data
        );
    };

    var deletar_pertence = function(id_pertence){

    };

    return {
        salvar_pertence: salvar_pertence,
        deletar_pertence: deletar_pertence
    }
});

app.directive("emprestarform", function($http){
   return{
       restrict: "E",
       replace: true,
       templateUrl: "/static/emprestar/html/form.html",
       scope:{
         toggleshow: "&",
         elementos: "="
       },
       controller: function($scope, emprestarApi){

           $scope.salvando = false;
           $scope.salvar = function() {
               $scope.salvando = true;
               emprestarApi.salvar_pertence($scope.pertence, $scope.nome, $scope.descricao,
                   $scope.emprestar).success( function(result){
                    $scope.elementos.push(result)
               }).finally(function(){
                   $scope.salvando = false;
               });
           };
       }
   };
});