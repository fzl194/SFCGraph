---
id: UNC@20.15.2@MMLCommand@LST SYSMAPFIXEDFC
type: MMLCommand
name: LST SYSMAPFIXEDFC（查询VLR整系统Map固定速率流控）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SYSMAPFIXEDFC
command_category: 查询类
applicable_nf:
- SMSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 信令传输管理
- SMSF管理
- Vlr Map固定速率流控
status: active
---

# LST SYSMAPFIXEDFC（查询VLR整系统Map固定速率流控）

## 功能

**适用NF：SMSF**

此命令用于查询VLR整系统Map固定速率流控参数。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [VLR整系统Map固定速率流控（SYSMAPFIXEDFC）](configobject/UNC/20.15.2/SYSMAPFIXEDFC.md)

## 使用实例

查询VLR整系统Map固定速率流控，可以用如下命令：

```
%%LST SYSMAPFIXEDFC:;%% 
RETCODE = 0  操作成功  
操作结果如下 ------------              
                          流控功能开关  =  ON 
       Update Location 速率门限(个/秒)  =  500        
               Purge Ms速率门限(个/秒)  =  500              
                    MO 速率门限(个/秒)  =  500              
                    MT 速率门限(个/秒)  =  500                  
                        流控响应原因值  =  NULL
(结果个数 = 1)  
---    结束
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询VLR整系统Map固定速率流控-(LST-SYSMAPFIXEDFC-)_19522769.md`
