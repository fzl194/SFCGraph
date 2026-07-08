---
id: UNC@20.15.2@MMLCommand@LST GTPUPARA
type: MMLCommand
name: LST GTPUPARA（查询GTP-U协议参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: GTPUPARA
command_category: 查询类
applicable_nf:
- SGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 数据转发管理
- GTP-U
- GTP-U协议参数管理
status: active
---

# LST GTPUPARA（查询GTP-U协议参数）

## 功能

**适用网元：SGSN**

该命令用于查询GTP-U用户面协议参数。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [GTP-U协议参数（GTPUPARA）](configobject/UNC/20.15.2/GTPUPARA.md)

## 使用实例

查询GTP-U协议参数：

LST GTPUPARA:;

```
%%LST GTPUPARA:;%%
RETCODE = 0  操作成功。

输出结果如下
------------
          GTPU 上游接口发送Echo信令  =  关闭
           GTPU下游接口发送Echo信令  =  关闭
           GTPU路径Echo探测发送间隔  =  239
GTPU路径的Echo探测的T3 Response时长  =  7
   GTPU路径的Echo探测的消息发送次数  =  2
                       发送私有信息  =  关闭
                             企业号  =  2011
                           私有信息  =  usn
          检查GTP扩展头类型个数上限  =  10
          检查GTP扩展头类型长度上限  =  100
          检查GTP扩展头列表个数上限  =  100
                路径数过载门限（%）  =  85
                路径数过载恢复（%）  =  80
                路径数拥塞门限（%）  =  95
                路径数拥塞恢复（%）  =  90
         GTPU信令面报文校验功能开关  =  打开
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询GTP-U协议参数(LST-GTPUPARA)_72345445.md`
