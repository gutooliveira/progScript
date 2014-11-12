app.factory('emprestarApi', function($http){

    var url_salvar_pertence = "/emprestars/rest/save";
    var url_deletar_pertence = "/emprestars/rest/delete";

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
        return $http.post(
            url_deletar_pertence,
            {emprestar_id: id_pertence}
        );
    };

    return {
        salvar_pertence: salvar_pertence,
        deletar_pertence: deletar_pertence
    }
});

app.controller("EmprestarCtrl", function($scope, emprestarApi){
    $scope.mostrarForm = false;
    $scope.deletando = false;
    $scope.emprestars = emprestars;
    $scope.toggleShow= function () {
        $scope.mostrarForm = !$scope.mostrarForm;
    };

    $scope.deletar = function(pertence){
       pertence.deletando = true;
       emprestarApi.deletar_pertence(pertence.id).success( function(result){
           for(var i = 0; i < $scope.emprestars.length; ++i){
                if(result.id == $scope.emprestars[i].id){
                    $scope.emprestars.splice(i, 1);
                    break;
                }
           }
       }).finally(function(){
           $scope.deletando = false;
       });
    };
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