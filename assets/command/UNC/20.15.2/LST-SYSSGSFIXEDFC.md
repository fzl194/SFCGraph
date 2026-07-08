---
id: UNC@20.15.2@MMLCommand@LST SYSSGSFIXEDFC
type: MMLCommand
name: LST SYSSGSFIXEDFC（查询VLR整系统Sgs固定速率流控）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SYSSGSFIXEDFC
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
- Vlr Sgs固定速率流控
status: active
---

# LST SYSSGSFIXEDFC（查询VLR整系统Sgs固定速率流控）

## 功能

**适用NF：SMSF**

此命令用于查询VLR整系统Sgs固定速率流控参数。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/SYSSGSFIXEDFC]] · VLR整系统Sgs固定速率流控（SYSSGSFIXEDFC）

## 使用实例

查询VLR整系统Sgs固定速率流控参数，可以用如下命令：

```
%%LST SYSSGSFIXEDFC:;%%
RETCODE = 0  操作成功  
操作结果如下 ------------              
                                             流控功能开关  =   ON
                   Location Update Request速率门限(个/秒)  =  2000       
                         Detach Indication速率门限(个/秒)  =  2000                  
                                    Paging速率门限(个/秒)  =  2000
 
(结果个数 = 1)  
---    结束
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询VLR整系统Sgs固定速率流控-(LST-SYSSGSFIXEDFC-)_69082810.md`
