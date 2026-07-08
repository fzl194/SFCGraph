---
id: UNC@20.15.2@MMLCommand@LST MMESGSFIXEDFC
type: MMLCommand
name: LST MMESGSFIXEDFC（查询VLR局向Sgs固定速率流控）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: MMESGSFIXEDFC
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

# LST MMESGSFIXEDFC（查询VLR局向Sgs固定速率流控）

## 功能

**适用NF：SMSF**

此命令用于查询VLR局向Sgs固定速率流控参数。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MMEIDX | MME索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定一个MME实体，在全局范围内唯一。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为0~1999<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [VLR局向Sgs固定速率流控（MMESGSFIXEDFC）](configobject/UNC/20.15.2/MMESGSFIXEDFC.md)

## 使用实例

查询已经配置的所有的VLR局向Sgs固定速率流控参数。

```
%%LST MMESGSFIXEDFC:;%%
RETCODE = 0  操作成功  
操作结果如下 ------------              
                                            MME索引   =  1 
              Location Update Request速率门限(个/秒)  =  2000       
                    Detach Indication速率门限(个/秒)  =  2000                  
                               Paging速率门限(个/秒)  =  2000

(结果个数 = 1)  
---    结束
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询VLR局向Sgs固定速率流控-(LST-MMESGSFIXEDFC)_19522765.md`
