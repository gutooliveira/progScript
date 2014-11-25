app.factory('emprestarApi', function($http){

    var url_salvar_pertence = "/emprestars/rest/save";
    var url_deletar_pertence = "/emprestars/rest/delete";
    var url_editar_pertence = "/emprestars/rest/edit";

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

    var editar_pertence = function(id, pertence, nome, descricao){
        var data = {
            emprestar_id: id,
            pertence: pertence,
            nome: nome,
            descricao: descricao
        };

        return $http.post(
            url_editar_pertence,
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
        deletar_pertence: deletar_pertence,
        editar_pertence: editar_pertence
    }
});

app.controller("EmprestarCtrl", function($scope, emprestarApi){
    $scope.mostrarForm = false;
    $scope.deletando = false;
    $scope.emprestars = emprestars;
    $scope.editando = false;
    $scope.salvando = false;
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

    $scope.enable_editar = function(){
        $scope.editando = true;
    };

    $scope.disable_editar = function(){
        $scope.editando = false;
    };

    $scope.editar = function(emprestar) {
        $scope.salvando = true;
        emprestarApi.editar_pertence(emprestar.id, emprestar.pertence, emprestar.nome, emprestar.descricao).success( function(result){

        }).finally(function(){
            $scope.salvando = false;
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
                if($scope.nome == undefined)
                    $scope.nome_error = true;
                else
                    $scope.nome_error = false;

                if($scope.pertence == undefined)
                    $scope.pertence_error = true;
                else
                    $scope.pertence_error = false;

                if($scope.descricao == undefined)
                    $scope.descricao_error = true;
                else
                    $scope.descricao_error = false;

                if($scope.emprestar == undefined)
                    $scope.emprestar_error = true;
                else
                    $scope.emprestar_error = false;

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