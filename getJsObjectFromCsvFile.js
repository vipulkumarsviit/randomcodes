function getJsObjectFromCsvFile(files) {
            $scope.startingTime = new Date().getTime();
            if (files) {
                $scope.uploadingImage = true;

                if (files) {
                    var r = new FileReader();
                    r.onload = function (e) {
                        var pattern = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
                        var contents = e.target.result;
                        var lines = contents.split("\n");
                        var result = [];
                        var headers = lines[0].split(",");
                        for (var i = 1; i < lines.length; i++) {
                            var obj = {};
                            var currentline = lines[i].split(",");
                            for (var j = 0; j < headers.length; j++) {
                                obj[headers[j]] = currentline[j];
                            }
                            if (pattern.test(obj.email))
                                ;

                            result.push(obj);

                        }

                        var finalList = result.filter(function (res) {
                            return pattern.test(res.email)
                        });
                        $scope.endingTime = new Date().getTime();
                        console.log("Time Taken : ", $scope.endingTime - $scope.startingTime);

                    };

                    r.readAsText(files);
                }
            }
        }
