<template>
  <div id='nav'>
    <!--<G2 :data = "item.line.data" type="line" :paddingAuto="true" id="line_img"></G2>-->
    <div class="img">
      <div id="line_img">
         <G2 :data = "item.line.data" type="line" :paddingAuto="false"></G2>
    </div>
      <div id="round_img">
        <G2 :data = "item.round.data" type="pie" :paddingAuto="false"></G2>
      </div>
      <div class="table">
      <Table :columns="columns" :data="dataList"></Table>
    </div>
    </div>
  </div>
</template>


<script src='@/controller/host/host_img.js'></script>
<style>
  #nav {
    width: 100%;
    height: 100%;
    /*background-color: #DDDDFF;*/
    /*background-color： ;*/
    position: relative;
    overflow: scroll;
  }
  #line_img {
    /*float: left;*/
    width: 580px;
    height: 300px;
    background-color: #fff;
    display: inline-block;
    margin: 10px;
    left: 73px;
    position: absolute
  }
  #round_img {
    width: 580px;
    height: 300px;
    background-color: #fff;
    display: inline-block;
    margin: 10px;
    right: 60px;
    position: absolute
  }
  #canvas_1{
    height: 300px;
    width: 500px;
  }
  .ivu-table-wrapper{
    /*position: absolute;
    bottom: 30%;*/
    margin: 0 80px;
    /*width: 1000px;*/
  }
  .img{
    position: relative;
  }
  .table{
    position: absolute;
    top: 339px
  }
</style>
