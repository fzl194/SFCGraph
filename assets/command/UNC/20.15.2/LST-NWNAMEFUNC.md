---
id: UNC@20.15.2@MMLCommand@LST NWNAMEFUNC
type: MMLCommand
name: LST NWNAMEFUNC（查询运营商名称信息功能）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NWNAMEFUNC
command_category: 查询类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- 归属网络运营商管理
- 运营商名称信息功能管理
status: active
---

# LST NWNAMEFUNC（查询运营商名称信息功能）

## 功能

**适用NF：MME**

本命令用于查询运营商名称信息下发功能。该命令对应的业务功能暂未实现。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NWNAMEFUNC]] · 运营商名称信息功能（NWNAMEFUNC）

## 使用实例

查询运营商名称信息下发功能，可以用如下命令：

```
%%LST NWNAMEFUNC:;%%
RETCODE = 0  操作成功  
操作结果如下 ------------              
    使用HSS网元标识不发送运营商名称开关  =  ON
使用HSS主机名或域名不发送运营商名称开关  =  OFF
         NB-IoT用户不发送运营商名称开关  =  OFF
       5G到4G业务流程发送运营商名称开关  =  OFF
 
(结果个数 = 1)  
---    结束
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-NWNAMEFUNC.md`
