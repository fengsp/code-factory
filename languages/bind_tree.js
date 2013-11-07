/*
 * sdbinds javascript logic
 * using ztree
 * http://www.ztree.me/
 */
// global variables
var sdbindAdded = false;
var curDraggedSD = null;
var fsp_tmp = 10004;
var isSameParent=0;

// speeddial bind sample data

var sdbinds = [
    {
        id: 0,
        name: 'default',   // strategy name
        preset: 0,
        isParent:true,
        open: true
    },
    {
        id: 10000,
        name: 'fsp',
        preset: 0,
        pId: 0,
        isParent:true,
        open: true
    },
    {
        id: 10003,
        name: 'fsptest',
        preset: 0,
        pId: 10000,
        open: true
    }
];

/* sync with server side
 * update the server sdbinds
 * POSTED data schema
 * data = {
 *     'action': ('add'|'rm'|'move'),
 *     'id': speeddial_ids,
 *     'left:': left_ids,
 *     'parent': parent_ids
 * }
 */
function updateSDBind(action, sdIds, leftIds, parentIds)
{
    fsp_tmp++;
    var demo = {
        'action': action,
        'id': sdIds,
        'left': leftIds,
        'parent': parentIds
    };
    console.log(demo)
    return fsp_tmp;
}

//判断是否同级同父
function isSlevelSparent(treeNodes){
    isSameParent=0;
    for(var i=0;i<treeNodes.length-1;i++){
        if(treeNodes[i].getParentNode().id!=treeNodes[i+1].getParentNode().id){isSameParent++}
    }
}

//获取选中节点个数
function calcNodeNum(event, treeId, treeNode){
    var zTree = $.fn.zTree.getZTreeObj(treeId);

    var nodes = zTree.getSelectedNodes();
    isSlevelSparent(nodes);
};

// convert dom to TreeElement
function dom2Tree(e, treeId, treeNode){
    var parentNode;
    var sdId;
    if (curDraggedSD==null) return;
    if (treeNode == null) return;
    if (curDraggedSD.isParent && treeNode.getParentNode() != null) return;
    
    var zTree = $.fn.zTree.getZTreeObj(treeId);
    if(treeNode != null && treeNode.isParent){
        parentNode = treeNode;
        if(treeNode.children && treeNode.children.length > 0) {
            sdId = updateSDBind('add', curDraggedSD.id, treeNode.children[treeNode.children.length-1].id, parentNode.id);
        } else {
            sdId = updateSDBind('add', curDraggedSD.id, 0, parentNode.id);
        }
    }else if(treeNode != null && !treeNode.isParent){
        parentNode = treeNode.getParentNode();
        sdId = updateSDBind('add', curDraggedSD.id, treeNode.id, parentNode.id);
    }
    nodes = zTree.addNodes(parentNode, {id: sdId, name: curDraggedSD.name, preset: 0, isParent: curDraggedSD.isParent, open: true});
    if(treeNode.isParent){
        zTree.moveNode(treeNode, nodes[0], "inner");
    }else if(!treeNode.isParent){
        zTree.moveNode(treeNode, nodes[0], "next");
    }
    sdbindAdded = true;
    curDraggedSD = null;
    zTree.selectNode(nodes[0]);
}; 

//不许在根节点前后加节点, 不取把文件夹加入非根节点以下
function beforeDrop(treeId, treeNodes, targetNode, moveType){
    if((moveType == "prev" || moveType == "next") &&targetNode.id==0){
        return false;
    }
    for(var i = 0, node; node = treeNodes[i++];) {
        if (node.isParent && targetNode.getParentNode() != null) return false;
    }
};

//不许拖动根节点
function beforeDrag(treeId, treeNodes){
    if(treeNodes[0].id == 0){
        return false;
    } else if(isSameParent!=0) {
        return false;
    } else {
        return true;
    }
}  

function dropTree2Dom(e, treeId, treeNodes, targetNode, moveType){
    var zTree = $.fn.zTree.getZTreeObj(treeId);
    var selectedNodes = zTree.getSelectedNodes();
    if (selectedNodes.length < 1) return;
    var treeAreaWStart=$("#sdbind").offset().left;
    var treeAreaWEnd=$("#sdbind").offset().left+$("#sdbind").width();
    var treeAreaHStart=$("#sdbind").offset().top;
    var treeAreaHEnd=$("#sdbind").offset().top+$("#sdbind").height();
    var action = 'move';
    var sdIds, leftIds, parentIds;
    
    var prevId=selectedNodes[0].getPreNode()?selectedNodes[0].getPreNode().id:"0";
    var dadId=selectedNodes[0].getParentNode()?selectedNodes[0].getParentNode().id:"0";
    
    if(selectedNodes.length > 0) {
        sdIds = selectedNodes[0].id;
        leftIds = prevId;
        parentIds = dadId;
        for(var i = 1; i < selectedNodes.length; i++) {
            sdIds = sdIds + "," + selectedNodes[i].id;
            leftIds = leftIds + "," + selectedNodes[i-1].id;
            parentIds = parentIds + "," + dadId;
        }
    }
    
    if(e.pageY<treeAreaHStart||e.pageY>treeAreaHEnd+50||e.pageX<treeAreaWStart||e.pageX>treeAreaWEnd){
        for(var i=0;i<selectedNodes.length;i++){zTree.removeNode(selectedNodes[i])}
        action = 'del';
    }
    updateSDBind(action, sdIds, leftIds, parentIds);
};   

// ztree_settings
var treeSetting = {
    edit: {
        enable: true,
        showRemoveBtn: false,
        showRenameBtn: false
    },
    data: {
        keep: {
            leaf: true,
            parent: true
        },
        simpleData: {
            enable: true,
            idKey: "id",
            pidKey: "pId",
            rootPid: 0,
        }
    },
    view: {
        nameIsHTML: true,
        showTitle: false,
        selectedMulti: true
    },
    callback: {
        onMouseUp: dom2Tree,
        beforeDrag:beforeDrag,//约束顶级节点
        beforeDrop:beforeDrop,//约束顶级节点
        onDrop:dropTree2Dom,
        onMouseDown:calcNodeNum
    }
};

// init speeddial tree
$(document).ready(function() {
    var sdTree = $.fn.zTree.init($('#sdtree'), treeSetting, sdbinds);
    $(".sd_drag").draggable({ 
        revert: function() {
            if (sdbindAdded == false)
                return true;
        },
        helper: function() {
            var helper_val = $(this).children("td:nth-child(1)").text() + '&nbsp;&nbsp;&nbsp;&nbsp;';
            helper_val += $(this).children("td:nth-child(2)").text() + '&nbsp;&nbsp;&nbsp;&nbsp;';
            helper_val += $(this).children("td:nth-child(3)").text() + '&nbsp;&nbsp;&nbsp;&nbsp;';
            helper_val += $(this).children("td:nth-child(5)").text(); 
            return $("<div class=\"sd_helper\"></div>").append(helper_val);
        },
        start: function( event, ui ) {
            sdbindAdded = false;
            var sdId = $(this).children("td:nth-child(1)").text();
            var sdName = $(this).children("td:nth-child(2)").text();
            var sdIsParent = $(this).children("td:nth-child(3)").text() == '文件夹' ? true : false;
            curDraggedSD = {'id': sdId, 'name': sdName, 'isParent': sdIsParent};
        },
        cursorAt: {
            top: -7,
            left: -7 
        }
    });
});
