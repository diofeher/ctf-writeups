(function init() {
  let game;
  let mouseX = 0, mouseY = 0;
  let id = 0, xp = 0, yp = 0, alive = 1;
  let dead = 0;
  let nkillers = -1;

  const socket = io.connect('http://ec2-54-194-213-165.eu-west-1.compute.amazonaws.com:5005');

  // roomId Id of the room in which the game is running on the server.
  class Game {
    constructor(roomId) {
      this.roomId = roomId;

      this.pointsId = [];
      this.pointsX = [];
      this.pointsY = [];

      this.followerID = [];
      this.followerX = [];
      this.followerY = [];
      this.followerSize = [];
      this.followerSrc = [];
      this.followerState = [];
    }

    getPointsId() { return this.pointsId; }
    setPointsId(iter, val) { this.pointsId[iter] = val; }
    setPointsId_(val) { this.pointsId = val; }
    addPointsId(val) { this.pointsId.push(val); }

    getPointsX() { return this.pointsX; }
    setPointsX(iter, val) { this.pointsX[iter] = val; }
    setPointsX_(val) { this.pointsX = val; }
    addPointsX(val) { this.pointsX.push(val); }

    getPointsY() { return this.pointsY; }
    setPointsY(iter, val) { this.pointsY[iter] = val; }
    setPointsY_(val) { this.pointsY = val; }
    addPointsY(val) { this.pointsY.push(val); }

    getFollowerID() { return this.followerID; }
    setFollowerID(iter, val) { this.followerID[iter] = val; }
    setFollowerID_(val) { this.followerID = val; }
    addFollowerID(val) { this.followerID.push(val); }

    getFollowerX() { return this.followerX; }
    setFollowerX(iter, val) { this.followerX[iter] = val; }
    setFollowerX_(val) { this.followerX = val; }
    addFollowerX(val) { this.followerX.push(val); }

    getFollowerY() { return this.followerY; }
    setFollowerY(iter, val) { this.followerY[iter] = val; }
    setFollowerY_(val) { this.followerY = val; }
    addFollowerY(val) { this.followerY.push(val); }

    getFollowerSize() { return this.followerSize; }
    setFollowerSize(iter, val) { this.followerSize[iter] = val; }
    setFollowerSize_(val) { this.followerSize = val; }
    addFollowerSize(val) { this.followerSize.push(val); }

    getFollowerSrc() { return this.followerSrc; }
    setFollowerSrc(iter, val) { this.followerSrc[iter] = val; }
    setFollowerSrc_(val) { this.followerSrc = val; }
    addFollowerSrc(val) { this.followerSrc.push(val); }

    getFollowerState() { return this.followerState; }
    setFollowerState(iter, val) { this.followerState[iter] = val; }
    setFollowerState_(val) { this.followerState = val; }
    addFollowerState(val) { this.followerState.push(val); }


    InitMap(points) {
      for (var i = 0; i < points.length; i++) {
        if (points[i]) {
          DrawPointCanvas(points[i][1], points[i][2], "#aaaaaa");
          this.pointsId.push(points[i][0]);
          this.pointsX.push(points[i][1]);
          this.pointsY.push(points[i][2]);
        }
      }
    }

    UpdateMap() {
      socket.emit('getUpdatesMap', {
        room: this.getRoomId(),
      });
    }

    DeletePoint(idP, idF) {
      socket.emit('DeletePoint', {
        room: this.getRoomId(),
        idP: idP,
        idF: idF
      });
    }

    KillAction(index, idS, idD, xS, yS, xD, yD) {
      socket.emit('KillAction', {
        room: this.getRoomId(),
        index: index,
        idS: idS,
        idD: idD,
        xS: xS,
        yS: yS,
        xD: xD,
        yD: yD
      });
    }

    InitKillers(killers) {
      for (var i = 0; i < killers.length; i++) {
        killers[i][1] = parseFloat(killers[i][1]);
        killers[i][2] = parseFloat(killers[i][2]);
        killers[i][5] = 1;
      }
      nkillers = killers.length;
      for (var i = 0; i < killers.length; i++) {
        $("#toBeZoomedOut").prepend('<img id="follower_' + killers[i][0] +
          '" src="' + killers[i][4] + '" class="follower" style="top:' + (killers[i][2] - (killers[i][3] / 2)) +
          'px;left:' + (killers[i][1] - (killers[i][3] / 2)) + 'px;width:' + killers[i][3] + 'px;height:' + killers[i][3] + 'px">');
      }
      for (var i = 0; i < killers.length; i++) {
        game.addFollowerID(killers[i][0]);
        game.addFollowerX(killers[i][1]);
        game.addFollowerY(killers[i][2]);
        game.addFollowerSize(killers[i][3]);
        game.addFollowerSrc(killers[i][4]);
        game.addFollowerState(killers[i][5]);
      }
    }

    ReviveKillers() {
      socket.emit('ReviveKillers', {
        room: this.getRoomId()
      });
    }

    getFlag() {
      socket.emit('getFlag', {
        room: this.getRoomId()
      });
    }



    // Remove the menu from DOM, display the gameboard and greet the player.
    displayGame() {
      $('body').css('width', '6366px');
      $('body').css('height', '10000px');
      $('.form').hide();
      $('link').remove();
      $('#game_body').show();
      //      this.createGameBoard();
    }

    getRoomId() {
      return this.roomId;
    }

  }

  // Create a new game. Emit newGame event.
  $('#new').on('click', () => {
    socket.emit('createGame', {});
  });

  // New Game created by current client. Update the UI and create new Game var.
  socket.on('newGame', (data) => {
    game = new Game(data.room);//console.log("New game created");
    game.InitMap(data.points);//console.log("InitMap performed");
    game.InitKillers(data.killers);//console.log("InitKillers performed");
    game.displayGame();
    var loop1 = setInterval(function () {
      if (dead > 0) game.ReviveKillers();
    }, 2000);
    if (game.getFollowerState()[0] == 1) { xp = game.getFollowerX()[0]; yp = game.getFollowerY()[0]; }
  });

  /**
	 * End the game on any err event. 
	 */
  socket.on('err', (data) => {
    alert(data.message);
  });



  function DrawPointCanvas(centerX = -1, centerY = -1, color) {
    var canvas = document.getElementById('myCanvas');
    var context = canvas.getContext('2d');
    var radius = 4;
    context.beginPath();
    context.arc(centerX, centerY, radius, 0, 2 * Math.PI, false);
    context.fillStyle = "#" + color;
    context.fill();
    context.lineWidth = 1;
    context.strokeStyle = '#0003';
    context.stroke();
  }

  function ClearPointCanvas(centerX = -1, centerY = -1) {
    var canvas = document.getElementById('myCanvas');
    var context = canvas.getContext('2d');
    var radius = 4;
    context.globalCompositeOperation = 'destination-out'
    context.arc(centerX, centerY, radius + 1, 0, Math.PI * 2, false);
    context.fill();
  }

  socket.on('updateMap', (data) => {
    console.log(data);
    var arr = Object.keys(points);
    arr.forEach(function (key) {
      result.push(points[key]);
    });
    for (var i = 0; i < arr.length; i++) {
      DrawPointCanvas(result[i][1], result[i][2], result[i][3]);
    }
  });

  socket.on('PointDeleted', (data) => {
    console.log(data);
    result = parseInt(data);
    //          if(result>0)return result;
    //    else return 0;

  });

  socket.on('KillActionPerformed', (data) => {
    dead++;
    game.setFollowerSize(data.index, data.size);
    if (dead == (nkillers - 1)) game.getFlag();
    //	result=parseFloat(data);
    //	    if(result>0)return result;
    //    else return 0;

  });



  function sortFunction(a, b) {
    if (a[0] === b[0]) {
      return 0;
    }
    else {
      return (a[0] < b[0]) ? -1 : 1;
    }
  }

  socket.on('ReviveKillersPerformed', (data) => {
    revived = data.revived;
    for (var i = 0; i < revived.length; i++) {
      dead--;
      $("#follower_" + revived[i][0]).css({ top: (revived[i][2] - (revived[i][3] / 2)), left: (revived[i][1] - (revived[i][3] / 2)), width: revived[i][3], height: revived[i][3] });
      if (revived[i][0] == 0) $("#revive").hide();
      pos = game.getFollowerID().indexOf(revived[i][0]);
      if (pos != -1) {
        game.setFollowerID(pos, revived[i][0]);
        game.setFollowerX(pos, revived[i][1]);
        game.setFollowerY(pos, revived[i][2]);
        game.setFollowerSize(pos, revived[i][3]);
        game.setFollowerSrc(pos, revived[i][4]);
        game.setFollowerState(pos, 1);
      }
      $("#follower_" + revived[i][0]).show();
    }
  });

  socket.on('getFlagPerformed', (data) => {
    $("#flag").text(data.flag);
  });


  $(document).mousemove(function (e) {
    mouseX = e.pageX;
    mouseY = e.pageY;
  });

  $("#progressController").change(function () {
    var val = parseInt($(this).val()) / 100;
    $('#toBeZoomedOut').css({ 'transform': 'scale(' + val + ')', '-webkit-transform': 'scale(' + val + ')', '-moz-transform': 'scale(' + val + ')', '-o-transform': 'scale(' + val + ')', '-ms-transform': 'scale(' + val + ')' });
  });

  $("#zm").click(function () {
    var val = parseInt($("#progressController").val()) - 1;
    $("#progressController").val(val);
    $("#progressController").trigger("change");
  });

  $("#zp").click(function () {
    var val = parseInt($("#progressController").val()) + 1;
    $("#progressController").val(val);
    $("#progressController").trigger("change");
  });

  $("html, body").animate({ scrollTop: "0px" }, 1);
  $("html, body").animate({ scrollLeft: "0px" }, 1);
  $("#start").attr("disabled", "disabled");
  $("#progressController").val(0.15 * 100); $("#progressController").trigger("change");

  $("#intro").click(function (e) {
    $("html, body").animate({ scrollTop: "0px" }, 1);
    $("html, body").animate({ scrollLeft: "0px" }, 1);
    $("#progressController").val(0.2 * 100); $("#progressController").trigger("change");
    $("#intro").attr("disabled", "disabled");
    $("#skipintro").attr("disabled", "disabled");
    $("#start").attr("disabled", "disabled");
    $("html, body").animate({ scrollTop: "1800px" }, 10000);
    $('#toBeZoomedOut').delay(10000).queue(function (next) {
      sl = ((6366 - $(window).width()) / 2) + "px";
      st = (10000 - ($(window).height() / 2)) + "px";
      $("html, body").animate({ scrollTop: st, scrollLeft: sl }, 2000);
      $({ someValue: 0.2 * 100 }).animate({ someValue: 1 * 100 }, {
        duration: 2000,
        step: function () {
          $("#progressController").val(this.someValue); $("#progressController").trigger("change");
        }
      });
      next();
    });
    $('#toBeZoomedOut').delay(1).queue(function (next) {
      $("#intro").removeAttr("disabled");
      $("#skipintro").removeAttr("disabled");
      $("#start").removeAttr("disabled");
      next();
    });
  });

  $("#skipintro").click(function (e) {
    $("#progressController").val(1 * 100); $("#progressController").trigger("change");
    sl = ((6366 - $(window).width()) / 2) + "px";
    st = (10000 - ($(window).height() / 2)) + "px";
    $("html, body").animate({ scrollTop: st, scrollLeft: sl }, 1);
    $("#start").removeAttr("disabled");
  });


  $("#start").click(function (e) {
    var loop = setInterval(function () {
      var follower = $("#follower_" + id);
      for (var i = 0; i < game.getFollowerID().length; i++) {
        $("#follower_" + game.getFollowerID()[i]).css('zIndex', game.getFollowerSize()[i]);
      }
      if (game.getFollowerState()[0] == 1) {
        tmpRx = (mouseX - xp);
        tmpRy = (mouseY - yp);
        tmpRt = Math.sqrt(Math.pow(tmpRx, 2) + Math.pow(tmpRy, 2));
        tmpx = (mouseX - xp) / 50;
        tmpy = (mouseY - yp) / 50;
        tmpt = Math.sqrt(Math.pow(tmpx, 2) + Math.pow(tmpy, 2));
        if (tmpRt > (game.getFollowerSize()[id] / 2)) {
          addedX = (tmpx / tmpt) * 100 / (game.getFollowerSize()[id]);
          addedY = (tmpy / tmpt) * 100 / (game.getFollowerSize()[id]);
          xp += addedX;
          yp += addedY;
        } else {
          xp += tmpx;
          yp += tmpy;
        }
        game.setFollowerX(id, xp); game.setFollowerY(id, yp);
      }
      var removed = [];
      for (var i = 0; i < game.getPointsId().length; i++) {
        for (var j = 0; j < game.getFollowerID().length; j++) {
          if (Math.sqrt(Math.pow(Math.abs(game.getFollowerX()[j] - game.getPointsX()[i]), 2) + Math.pow(Math.abs(game.getFollowerY()[j] - game.getPointsY()[i]), 2)) < game.getFollowerSize()[j] / 2 && game.getFollowerSize()[j] < 100) {
            ClearPointCanvas(game.getPointsX()[i], game.getPointsY()[i]);
            game.getFollowerSize()[j] = DeletePoint(game.getPointsId()[i], game.getFollowerID()[j]);
            if (j == 0) {
              $("#score").text(game.getFollowerSize()[j]);
              if (dead == (nkillers - 1)) game.getFlag();
            }
            removed.push(i);
          }
        }
      }

      if (game.getFollowerState()[0] == 1) follower.css({ left: (xp - (game.getFollowerSize()[id] / 2)), top: (yp - (game.getFollowerSize()[id] / 2)), width: game.getFollowerSize()[id], height: game.getFollowerSize()[id] });

      for (var i = 0; i < game.getFollowerID().length; i++) {
        if (game.getFollowerState()[i] != 0) {
          for (var j = 0; j < game.getFollowerID().length; j++) {
            if (i != j && game.getFollowerState()[j] != 0) {
              if (Math.sqrt(Math.pow(Math.abs(game.getFollowerX()[i] - game.getFollowerX()[j]), 2) + Math.pow(Math.abs(game.getFollowerY()[i] - game.getFollowerY()[j]), 2))
                < game.getFollowerSize()[i] / 2 && game.getFollowerSize()[i] > game.getFollowerSize()[j]) {
                $("#follower_" + game.getFollowerID()[j]).hide();
                if (j == 0) $("#revive").show();
                game.setFollowerState(j, 0);
                game.KillAction(i, game.getFollowerID()[i], game.getFollowerID()[j],
                  game.getFollowerX()[i], game.getFollowerY()[i], game.getFollowerX()[j], game.getFollowerY()[j]);
                if (i == 0) {
                  $("#score").text(game.getFollowerSize()[i]);
                  if (dead == (nkillers - 1)) game.getFlag();
                }
              }
            }
          }
        }
      }

      var limiteMapXMin = 0, limiteMapYMin = 0, limiteMapXMax = 6366, limiteMapYMax = 10000;
      for (var i = 0; i < game.getFollowerID().length; i++) {
        if (game.getFollowerState()[i] != 0 && game.getFollowerID()[i] != 0) {
          var distMinFollow = 10000000000;
          var distMinSkip = 10000000000;
          var nSkip = 0, nFollow = 0;
          var followed = i;
          var skiped = i;
          var evil = 122, power = 1;
          if (game.getFollowerSize()[i] < game.getFollowerSize()[0]) {
            console.log(i, 'eh menor do q ', 0)
          }
          if (game.getFollowerState()[i] != 0) {
            tmp = Math.sqrt(Math.pow(Math.abs(game.getFollowerX()[i] - game.getFollowerX()[0]), 2) + Math.pow(Math.abs(game.getFollowerY()[i] - game.getFollowerY()[0]), 2));
            if (tmp < distMinFollow && game.getFollowerSize()[i] < game.getFollowerSize()[0]) { distMinFollow = tmp; followed = 0; nFollow++; }
            if (tmp < distMinSkip && game.getFollowerSize()[i] > game.getFollowerSize()[0]) { distMinSkip = tmp; skiped = 0; nSkip++; }
          }
          var angleFollow = Math.atan2(game.getFollowerY()[followed] - game.getFollowerY()[i], game.getFollowerX()[followed] - game.getFollowerX()[i]);
          var angleSkip = Math.atan2(game.getFollowerY()[i] - game.getFollowerY()[skiped], game.getFollowerX()[i] - game.getFollowerX()[skiped]);
          if (game.getFollowerID()[i] == evil) power = (100 / 150) * 2 * 30; else power = 1;
          if ((distMinSkip < game.getFollowerSize()[skiped] || nFollow == 0) && game.getFollowerX()[i] > limiteMapXMin && game.getFollowerX()[i] < limiteMapXMax && game.getFollowerY()[i] > limiteMapYMin && game.getFollowerY()[i] < limiteMapYMax) {
            game.setFollowerX(i, game.getFollowerX()[i] + parseFloat(Math.cos(angleSkip) * 150 * power / (game.getFollowerSize()[i])));
            game.setFollowerY(i, game.getFollowerY()[i] + parseFloat(Math.sin(angleSkip) * 150 * power / (game.getFollowerSize()[i])));
          } else if (game.getFollowerX()[i] > limiteMapXMin && game.getFollowerX()[i] < limiteMapXMax && game.getFollowerY()[i] > limiteMapYMin && game.getFollowerY()[i] < limiteMapYMax) {
            game.setFollowerX(i, game.getFollowerX()[i] + parseFloat(Math.cos(angleFollow) * 150 * power / (game.getFollowerSize()[i])));
            game.setFollowerY(i, game.getFollowerY()[i] + parseFloat(Math.sin(angleFollow) * 150 * power / (game.getFollowerSize()[i])));
          } else {
            if (game.getFollowerX()[i] <= limiteMapXMin) game.setFollowerX(i, limiteMapXMin + 1);
            if (game.getFollowerX()[i] >= limiteMapXMax) game.setFollowerX(i, limiteMapXMax - 1);
            if (game.getFollowerY()[i] <= limiteMapYMin) game.setFollowerY(i, limiteMapYMin + 1);
            if (game.getFollowerY()[i] >= limiteMapYMax) game.setFollowerY(i, limiteMapYMax - 1);
          }
          $("#follower_" + game.getFollowerID()[i]).css({ left: (game.getFollowerX()[i] - (game.getFollowerSize()[i] / 2)), top: (game.getFollowerY()[i] - (game.getFollowerSize()[i] / 2)), width: game.getFollowerSize()[i], height: game.getFollowerSize()[i] });
        }
      }
    }, 100);

  });


}());
